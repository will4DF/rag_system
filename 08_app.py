"""
Step 7: Streamlit UI for the RAG assistant.

Same retrieval + generation pipeline as 07_ask.py, wrapped in a web UI
so coworkers can use it without touching the terminal. Adds optional
screenshot upload — if attached, the image is sent to Gemini alongside
the retrieved docs so it can see what the user is looking at.

Setup:
  Create a .env file in this folder (see .env.example) with:
    GEMINI_API_KEY=your-key-here
  pip install -r requirements.txt

Run:
  streamlit run 08_app.py

Then share the "Network URL" streamlit prints (something like
http://192.168.x.x:8501) with coworkers on the same office network.
"""

import base64
import io
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from PIL import Image
from dotenv import load_dotenv

load_dotenv()  # picks up a local .env file if present; no-op if it doesn't exist

try:
    # Streamlit Community Cloud ships an old system sqlite3 that Chroma
    # rejects. pysqlite3-binary provides a newer one; swap it in before
    # chromadb is imported. Falls back silently if not installed (e.g.
    # running locally on Mac, where the system sqlite3 is new enough).
    import pysqlite3
    sys.modules["sqlite3"] = pysqlite3
except ImportError:
    pass

import chromadb
import requests
import streamlit as st
from sentence_transformers import SentenceTransformer

# ---------------------------------------------------------------------------
# Config (same as 07_ask.py)
# ---------------------------------------------------------------------------

DB_DIR = "chroma_db"
COLLECTION_NAME = "element451_help"
EMBED_MODEL_NAME = "BAAI/bge-small-en-v1.5"
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "
TOP_K = 10

def get_api_key() -> str | None:
    """Streamlit Cloud stores secrets in st.secrets; locally, we read from
    the environment (populated by the .env file loaded above, or a manual
    `export`). Checking st.secrets first means the exact same code and
    deployment work in both places without any branching elsewhere."""
    try:
        return st.secrets["GEMINI_API_KEY"]
    except (KeyError, FileNotFoundError):
        return os.environ.get("GEMINI_API_KEY")


API_KEY = get_api_key()
GEN_MODEL = "gemini-3.6-flash"
FALLBACK_MODEL = "gemini-3.5-flash-lite"  # separate free-tier quota pool from GEN_MODEL —
                                           # tried automatically if the primary model is rate-limited
MAX_RETRIES = 2       # per model — kept low; with a fallback model available, it's better to
                       # move on to it quickly than sit waiting on a model that's still busy
MAX_WAIT_SECONDS = 15  # cap on any single retry wait, so total time stays bounded and predictable
INITIAL_BACKOFF = 5.0


def endpoint_for(model: str) -> str:
    return f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent"

MAX_IMAGE_DIMENSION = 1600  # longest side, in pixels — plenty for Gemini to read UI text
JPEG_QUALITY = 85

DEFAULT_VIDEO_MAX_SECONDS = 90  # default cap; can be lifted per-upload via an explicit opt-out
VIDEO_MIME_TYPES = {
    "mp4": "video/mp4", "mov": "video/mov", "webm": "video/webm",
    "m4v": "video/mp4", "avi": "video/x-msvideo",
}
FILES_API_BASE = "https://generativelanguage.googleapis.com/v1beta"
FILES_API_UPLOAD = "https://generativelanguage.googleapis.com/upload/v1beta/files"
VIDEO_PROCESSING_POLL_SECONDS = 3
VIDEO_PROCESSING_TIMEOUT_SECONDS = 120

SYSTEM_INSTRUCTIONS = """You are a helpful assistant answering questions about the Element451 platform, using the documentation excerpts provided below.

How to use the excerpts:
- Piece together information across MULTIPLE excerpts when they're related — don't require one excerpt to fully answer the question on its own. If one excerpt describes how filters/segments work generally and another mentions a specific field or date behavior, combine them into one coherent answer.
- If the excerpts describe the general mechanism (e.g. how filters or conditions work) but not the exact specific case asked about, use reasonable inference to suggest how it likely works, based on the patterns shown — just be clear when you're inferring vs. stating something the docs say directly. Say something like "the docs describe X generally, which suggests Y" rather than presenting an inference as a directly documented fact.
- Only say you don't have enough information if the excerpts are genuinely unrelated to the question — not just because no single excerpt spells out every detail.
- Be direct and practical. Give concrete steps when possible, even partial ones, rather than declining to answer.
- Do not invent specific UI labels, button names, or menu paths that aren't mentioned anywhere in the excerpts — inference is for connecting concepts, not fabricating specifics.
- If a screenshot is provided, use it to understand what the user is trying to accomplish overall — not just literal error text. It might show the screen they're on, a partially-built workflow, a field they're stuck on, or their end goal. Ground your answer in that context rather than answering generically.
- Respond in the same language the user's question is written in. The documentation excerpts are in English regardless — if the question is in Spanish, translate the relevant content into natural, fluent Spanish for your answer (technical platform terms like "segment" or "filter" can stay in English if that's how they're normally used). Keep article titles as given, even when answering in Spanish.
- If the user explicitly asks you to switch languages (e.g. "answer in English" or "respondeme en español"), follow that instruction for the rest of the conversation, overriding the default of matching each new question's language.
- Cite which article(s) your answer draws from at the end, using the titles provided."""


# ---------------------------------------------------------------------------
# Cached resources — loaded once per server process, not per request
# ---------------------------------------------------------------------------

@st.cache_resource(show_spinner="Loading embedding model...")
def load_embed_model():
    return SentenceTransformer(EMBED_MODEL_NAME)


@st.cache_resource(show_spinner="Connecting to database...")
def load_collection():
    client = chromadb.PersistentClient(path=DB_DIR)
    return client.get_collection(COLLECTION_NAME)


# ---------------------------------------------------------------------------
# Pipeline (same logic as 07_ask.py)
# ---------------------------------------------------------------------------

def retrieve(model, collection, query: str, top_k: int = TOP_K) -> list[dict]:
    query_vec = model.encode([QUERY_PREFIX + query], normalize_embeddings=True)[0].tolist()
    results = collection.query(query_embeddings=[query_vec], n_results=top_k)

    hits = []
    for doc, meta, dist in zip(results["documents"][0], results["metadatas"][0], results["distances"][0]):
        hits.append({
            "text": doc,
            "title": meta["title"],
            "url": meta["url"],
            "collection": meta["collection"],
            "similarity": 1 - dist,
        })
    return hits


def _call_gemini(
    payload: dict,
    models: tuple[str, ...] = (GEN_MODEL, FALLBACK_MODEL),
    status_callback=None,
) -> tuple[str, str, str]:
    """POST to Gemini. Retries on 429 using Google's own retry-after time (capped so a
    single wait never balloons); if a model's quota is still exhausted after retrying,
    moves on to the next model in `models` (e.g. flash -> flash-lite, separate free-tier
    quota pools). status_callback(str), if given, is called with progress text so the UI
    can show what's happening instead of sitting on a static "thinking" message.
    Returns (answer_text, model_that_actually_answered, thought_summary — "" if none/not requested).
    Raises RuntimeError only if every model in the list fails.
    """
    def report(msg: str):
        if status_callback:
            status_callback(msg)

    last_error: Exception | None = None

    for model in models:
        backoff = INITIAL_BACKOFF
        for attempt in range(1, MAX_RETRIES + 1):
            report(f"Asking {model}..." if attempt == 1 else f"Retrying {model} (attempt {attempt}/{MAX_RETRIES})...")
            resp = requests.post(
                endpoint_for(model),
                headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
                json=payload,
                timeout=30,
            )
            if resp.status_code == 200:
                data = resp.json()
                parts = data["candidates"][0]["content"]["parts"]
                # Thought-summary parts are flagged with "thought": true when
                # thinkingConfig.includeThoughts was requested; everything else
                # is the actual answer text.
                thought_text = "".join(p.get("text", "") for p in parts if p.get("thought"))
                answer_text = "".join(p.get("text", "") for p in parts if not p.get("thought"))
                return answer_text, model, thought_text

            if resp.status_code == 429 and attempt < MAX_RETRIES:
                # Google tells us exactly how long to wait (RetryInfo.retryDelay,
                # e.g. "13s") — use that if present, but cap it: a very busy quota
                # can report long delays, and we'd rather fall back to the next
                # model quickly than sit through a minute-plus wait.
                wait_seconds = backoff
                try:
                    details = resp.json().get("error", {}).get("details", [])
                    for d in details:
                        if d.get("@type", "").endswith("RetryInfo"):
                            wait_seconds = float(d.get("retryDelay", "").rstrip("s")) + 1
                            break
                except (ValueError, AttributeError):
                    pass
                wait_seconds = min(wait_seconds, MAX_WAIT_SECONDS)
                report(f"{model} is rate-limited — waiting {wait_seconds:.0f}s before retrying...")
                time.sleep(wait_seconds)
                backoff *= 2
                continue

            if resp.status_code == 429:
                last_error = RuntimeError(f"{model} rate limit still full after retrying")
                break  # give the next model (if any) a try


            # Non-429 errors aren't fixed by trying another model — raise immediately
            raise RuntimeError(f"Generation request failed: {resp.status_code} {resp.text[:500]}")

    raise RuntimeError(
        "Gemini's free-tier rate limit is temporarily full across all available models "
        "(this app shares its quota across everyone using it). Wait about 30-60 seconds "
        "and try again."
    ) from last_error


REWRITE_INSTRUCTIONS = """You rewrite the latest message in a conversation into a standalone search query, for looking up documentation. Use the conversation for context, but output ONLY the rewritten query text — no explanation, no quotes, no labels.

Rules:
- If the latest message is already a clear, standalone question, return it unchanged (translated to English if it wasn't already, since the docs are in English).
- If it's a vague follow-up (e.g. "hola", "search better", "what about that"), rewrite it into a full standalone question using the conversation's topic.
- If it's a genuinely new, unrelated question, just return it as-is (don't drag in old topics).
- Keep it short — one sentence."""


def rewrite_query(history_contents: list[dict], query: str) -> str | None:
    """Turn a vague follow-up into a standalone search query using conversation context.
    Returns None on any failure so the caller can fall back to a simpler heuristic —
    this is a nice-to-have, not something that should ever break the main flow.
    """
    if not history_contents:
        return None  # nothing to rewrite against on the first message

    payload = {
        "system_instruction": {"parts": [{"text": REWRITE_INSTRUCTIONS}]},
        "contents": history_contents + [{"role": "user", "parts": [{"text": query}]}],
        "generationConfig": {"maxOutputTokens": 60},
    }
    try:
        text, _, _ = _call_gemini(payload)
        return text.strip() or None
    except Exception:
        return None


def build_turn_text(query: str, hits: list[dict], has_image: bool, has_video: bool = False) -> str:
    context_blocks = []
    for i, h in enumerate(hits, 1):
        context_blocks.append(f"[Excerpt {i}] From \"{h['title']}\" ({h['collection']}):\n{h['text']}")
    context = "\n\n".join(context_blocks)

    image_note = (
        "\nThe user has also attached a screenshot to help explain what they're trying to accomplish — "
        "use it as context for their overall goal, not just as an error message to diagnose.\n"
        if has_image else ""
    )
    video_note = (
        "\nThe user has attached a screen recording, likely narrating what they're trying to do or "
        "an issue they're running into. Use both what's shown on screen and what's said out loud as "
        "context for their overall goal.\n"
        if has_video else ""
    )

    return f"""--- DOCUMENTATION EXCERPTS ---
{context}
--- END EXCERPTS ---
{image_note}{video_note}
Question: {query}

Answer:"""


def prepare_image(raw_bytes: bytes) -> tuple[bytes, str]:
    """Downscale + re-encode any uploaded screenshot to a small JPEG.

    Full-resolution Mac/Windows screenshots are often several MB, well past
    what's needed for Gemini to read on-screen text. Rather than rejecting
    large uploads, we always normalize to something small and reliable so
    an image never silently fails to attach.
    """
    img = Image.open(io.BytesIO(raw_bytes))
    img = img.convert("RGB")  # drops alpha channel; needed for JPEG

    longest_side = max(img.size)
    if longest_side > MAX_IMAGE_DIMENSION:
        scale = MAX_IMAGE_DIMENSION / longest_side
        new_size = (round(img.width * scale), round(img.height * scale))
        img = img.resize(new_size, Image.LANCZOS)

    buf = io.BytesIO()
    img.save(buf, format="JPEG", quality=JPEG_QUALITY)
    return buf.getvalue(), "image/jpeg"


def get_video_duration_seconds(raw_bytes: bytes, suffix: str) -> float | None:
    """Uses ffprobe (installed via packages.txt) to read a video's duration
    without needing to fully upload it first. Returns None if it can't be
    determined — callers should treat that as "unknown, proceed with caution"
    rather than blocking the upload outright."""
    with tempfile.NamedTemporaryFile(suffix=f".{suffix}", delete=True) as tmp:
        tmp.write(raw_bytes)
        tmp.flush()
        try:
            result = subprocess.run(
                ["ffprobe", "-v", "error", "-show_entries", "format=duration",
                 "-of", "default=noprint_wrappers=1:nokey=1", tmp.name],
                capture_output=True, text=True, timeout=30,
            )
            return float(result.stdout.strip())
        except (subprocess.SubprocessError, ValueError, FileNotFoundError):
            return None


def upload_video_and_wait(raw_bytes: bytes, mime_type: str, status_callback=None) -> str:
    """Uploads a video to Gemini's File API (required for anything past a
    trivially short clip) and polls until it's finished processing server-side.
    Returns the file_uri to reference in a generateContent request.
    Raises RuntimeError on upload failure, processing failure, or timeout.
    """
    def report(msg: str):
        if status_callback:
            status_callback(msg)

    report("Uploading video...")
    start_resp = requests.post(
        FILES_API_UPLOAD,
        headers={
            "x-goog-api-key": API_KEY,
            "X-Goog-Upload-Protocol": "resumable",
            "X-Goog-Upload-Command": "start",
            "X-Goog-Upload-Header-Content-Length": str(len(raw_bytes)),
            "X-Goog-Upload-Header-Content-Type": mime_type,
            "Content-Type": "application/json",
        },
        json={"file": {"display_name": "screen-recording"}},
        timeout=30,
    )
    if start_resp.status_code != 200:
        raise RuntimeError(f"Video upload failed to start: {start_resp.status_code} {start_resp.text[:300]}")
    upload_url = start_resp.headers.get("X-Goog-Upload-URL")
    if not upload_url:
        raise RuntimeError("Video upload failed: no upload URL returned")

    finalize_resp = requests.post(
        upload_url,
        headers={
            "Content-Length": str(len(raw_bytes)),
            "X-Goog-Upload-Offset": "0",
            "X-Goog-Upload-Command": "upload, finalize",
        },
        data=raw_bytes,
        timeout=120,
    )
    if finalize_resp.status_code != 200:
        raise RuntimeError(f"Video upload failed to finalize: {finalize_resp.status_code} {finalize_resp.text[:300]}")

    file_info = finalize_resp.json().get("file", {})
    file_name = file_info.get("name")  # e.g. "files/abc123"
    file_uri = file_info.get("uri")
    state = file_info.get("state", "PROCESSING")

    waited = 0.0
    while state == "PROCESSING" and waited < VIDEO_PROCESSING_TIMEOUT_SECONDS:
        report(f"Google is processing the video... ({int(waited)}s)")
        time.sleep(VIDEO_PROCESSING_POLL_SECONDS)
        waited += VIDEO_PROCESSING_POLL_SECONDS
        poll_resp = requests.get(
            f"{FILES_API_BASE}/{file_name}",
            headers={"x-goog-api-key": API_KEY},
            timeout=30,
        )
        if poll_resp.status_code == 200:
            file_info = poll_resp.json()
            state = file_info.get("state", "PROCESSING")
            file_uri = file_info.get("uri", file_uri)

    if state != "ACTIVE":
        raise RuntimeError(f"Video processing did not finish in time (last state: {state}). Try a shorter clip.")

    report("Video ready — asking Gemini...")
    return file_uri


def generate_answer(
    history_contents: list[dict],
    turn_text: str,
    image_bytes: bytes | None,
    image_mime: str | None,
    status_callback=None,
    models: tuple[str, ...] = (GEN_MODEL, FALLBACK_MODEL),
    video_file_uri: str | None = None,
    video_mime: str | None = None,
) -> tuple[str, str, str]:
    """history_contents: prior turns as [{"role": "user"|"model", "parts": [...]}, ...]
    turn_text / image_*: the current question (and optional screenshot) to append.
    video_file_uri: a file_uri from upload_video_and_wait(), if a video was attached.
    models: which model(s) to try, in order — defaults to flash then flash-lite fallback,
    but callers can pass a single model to force that exact one with no fallback.
    Returns (answer_text, model_that_answered, thought_summary).
    """
    current_parts = [{"text": turn_text}]
    if image_bytes is not None:
        current_parts.append({
            "inline_data": {
                "mime_type": image_mime,
                "data": base64.b64encode(image_bytes).decode("utf-8"),
            }
        })
    if video_file_uri is not None:
        current_parts.append({
            "file_data": {
                "mime_type": video_mime,
                "file_uri": video_file_uri,
            }
        })

    payload = {
        "system_instruction": {"parts": [{"text": SYSTEM_INSTRUCTIONS}]},
        "contents": history_contents + [{"role": "user", "parts": current_parts}],
        "generationConfig": {"thinkingConfig": {"includeThoughts": True}},
    }

    return _call_gemini(payload, models=models, status_callback=status_callback)


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

st.set_page_config(page_title="Element451 Help Assistant", page_icon="💬", layout="centered")
st.title("💬 Element451 Help Assistant")
st.caption("Ask a question about the platform, and optionally attach a screenshot for extra context. · Puedes preguntar en español.")

if not API_KEY:
    st.error(
        "GEMINI_API_KEY is not set. Locally, create a .env file in this folder with:\n\n"
        "`GEMINI_API_KEY=your-key-here`\n\n"
        "On Streamlit Cloud, set it under Settings → Secrets instead."
    )
    st.stop()

if not Path(DB_DIR).exists():
    st.error(f"'{DB_DIR}/' not found next to this app — run the vectorstore build step first.")
    st.stop()

with st.sidebar:
    st.subheader("Settings")
    model_choice = st.selectbox(
        "Model",
        options=["Auto (recommended)", GEN_MODEL, FALLBACK_MODEL],
        index=0,
        help=(
            f"**Auto**: tries {GEN_MODEL} first, automatically falls back to "
            f"{FALLBACK_MODEL} if it's rate-limited.\n\n"
            f"**{GEN_MODEL}**: more capable, but the free tier's limit is easier to hit.\n\n"
            f"**{FALLBACK_MODEL}**: lighter and faster, separate free-tier quota — "
            f"good if {GEN_MODEL} is busy and you don't want to wait."
        ),
    )
    if model_choice == "Auto (recommended)":
        models_to_use = (GEN_MODEL, FALLBACK_MODEL)
    else:
        models_to_use = (model_choice,)  # exactly what the user picked, no fallback

embed_model = load_embed_model()
collection = load_collection()

if "messages" not in st.session_state:
    st.session_state.messages = []  # list of {role, content, sources?}

# Replay history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("image"):
            st.image(msg["image"], width=250)
        if msg.get("video"):
            st.video(msg["video"])
        if msg.get("thoughts"):
            with st.expander("🧠 Thinking"):
                st.markdown(msg["thoughts"])
        if msg.get("model_used"):
            st.caption(f"Answered by `{msg['model_used']}`")
        if msg.get("sources"):
            with st.expander("Sources"):
                for title, url in msg["sources"]:
                    st.markdown(f"- [{title}]({url})")

# Uploaders live above the chat box so they're attached to the *next* message
st.caption(
    "⚠️ Screenshots and videos are sent to Google's Gemini API for processing, and Google keeps "
    "uploaded videos for up to 48 hours before automatic deletion. Avoid including SSNs, financial "
    "aid details, health information, or other sensitive student data — crop, blur, or avoid saying "
    "it out loud if a screen or recording shows/mentions any."
)
IMAGE_EXTENSIONS = ["png", "jpg", "jpeg"]

col_image, col_video = st.columns(2)
with col_image:
    uploaded_file = st.file_uploader(
        "Screenshot",
        type=IMAGE_EXTENSIONS,
        key=f"uploader_{len(st.session_state.messages)}",
    )
with col_video:
    uploaded_video = st.file_uploader(
        "Screen recording",
        type=list(VIDEO_MIME_TYPES.keys()),
        key=f"video_uploader_{len(st.session_state.messages)}",
    )
    allow_long_video = False
    if uploaded_video is not None:
        allow_long_video = st.checkbox(
            f"Allow longer than {DEFAULT_VIDEO_MAX_SECONDS}s (uses noticeably more of the shared quota)",
            value=False,
            key=f"allow_long_video_{len(st.session_state.messages)}",
        )

query = st.chat_input("Ask a question...")

if query:
    image_bytes, image_mime, display_image = None, None, None
    if uploaded_file is not None:
        raw_bytes = uploaded_file.getvalue()
        display_image = raw_bytes  # show the original in the chat history
        try:
            image_bytes, image_mime = prepare_image(raw_bytes)
        except Exception as e:
            st.warning(f"Couldn't process that screenshot ({e}) — continuing without it.")

    video_bytes, video_mime_type, display_video = None, None, None
    video_blocked = False
    if uploaded_video is not None:
        video_raw_bytes = uploaded_video.getvalue()
        video_ext = uploaded_video.name.rsplit(".", 1)[-1].lower()
        video_mime_type = VIDEO_MIME_TYPES.get(video_ext, "video/mp4")

        duration = get_video_duration_seconds(video_raw_bytes, video_ext)
        if duration is not None and duration > DEFAULT_VIDEO_MAX_SECONDS and not allow_long_video:
            st.error(
                f"That video is about {duration:.0f}s long — over the {DEFAULT_VIDEO_MAX_SECONDS}s "
                f"default cap. Trim it, or check \"Allow videos longer than "
                f"{DEFAULT_VIDEO_MAX_SECONDS}s\" above and resend if you're sure."
            )
            video_blocked = True
        else:
            video_bytes = video_raw_bytes
            display_video = video_raw_bytes

    if not video_blocked:
        # Build history from prior turns (before this new question is appended).
        # Only text is replayed for older turns — re-sending old screenshots on every
        # request would bloat the payload and burn through the daily quota fast; the
        # model doesn't need to re-see an old image to remember what was *said* about it.
        history_contents = []
        prior_user_texts = []
        for msg in st.session_state.messages:
            role = "model" if msg["role"] == "assistant" else "user"
            history_contents.append({"role": role, "parts": [{"text": msg["content"]}]})
            if msg["role"] == "user":
                prior_user_texts.append(msg["content"])

        # The doc search only sees whatever text we hand it — a short follow-up like
        # "hola" or "search better" carries no topic signal on its own. Try an LLM
        # rewrite into a standalone search query first (handles topic drift correctly);
        # fall back to simple concatenation if that call fails or gets rate-limited.
        rewritten = rewrite_query(history_contents, query)
        if rewritten:
            search_text = rewritten
        else:
            search_text = " ".join(prior_user_texts[-2:] + [query])

        st.session_state.messages.append({"role": "user", "content": query, "image": display_image, "video": display_video})
        with st.chat_message("user"):
            st.markdown(query)
            if display_image:
                st.image(display_image, width=250)
            if display_video:
                st.video(display_video)

        with st.chat_message("assistant"):
            with st.status("Searching docs...", expanded=False) as status:
                hits = retrieve(embed_model, collection, search_text)
                turn_text = build_turn_text(query, hits, has_image=image_bytes is not None, has_video=video_bytes is not None)
                model_used = None
                thoughts = ""
                video_file_uri = None
                try:
                    if video_bytes is not None:
                        video_file_uri = upload_video_and_wait(
                            video_bytes, video_mime_type,
                            status_callback=lambda msg: status.update(label=msg),
                        )
                    answer, model_used, thoughts = generate_answer(
                        history_contents, turn_text, image_bytes, image_mime,
                        status_callback=lambda msg: status.update(label=msg),
                        models=models_to_use,
                        video_file_uri=video_file_uri,
                        video_mime=video_mime_type,
                    )
                    status.update(label="Done", state="complete")
                except RuntimeError as e:
                    answer = f"⚠️ {e}"
                    hits = []
                    status.update(label="Failed", state="error")

            st.markdown(answer)
            if thoughts:
                with st.expander("🧠 Thinking"):
                    st.markdown(thoughts)
            if model_used:
                st.caption(f"Answered by `{model_used}`" + (" — primary model was rate-limited" if model_used == FALLBACK_MODEL else ""))

            sources = []
            seen = set()
            for h in hits:
                if h["url"] not in seen:
                    sources.append((h["title"], h["url"]))
                    seen.add(h["url"])
            if sources:
                with st.expander("Sources"):
                    for title, url in sources:
                        st.markdown(f"- [{title}]({url})")

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "sources": sources,
            "thoughts": thoughts,
            "model_used": model_used,
        })
        st.rerun()  # clears the file_uploaders for the next question