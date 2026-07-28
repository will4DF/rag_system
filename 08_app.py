"""
Step 7: Streamlit UI for the RAG assistant.

Same retrieval + generation pipeline as 07_ask.py, wrapped in a web UI
so coworkers can use it without touching the terminal. Adds optional
screenshot upload — if attached, the image is sent to Gemini alongside
the retrieved docs so it can see what the user is looking at.

Setup:
  export GEMINI_API_KEY="your-key-here"
  pip install streamlit

Run:
  streamlit run 08_app.py

Then share the "Network URL" streamlit prints (something like
http://192.168.x.x:8501) with coworkers on the same office network.
"""

import base64
import os
import time
from pathlib import Path

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

API_KEY = os.environ.get("GEMINI_API_KEY")
GEN_MODEL = "gemini-2.5-flash"
GEN_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{GEN_MODEL}:generateContent"
MAX_RETRIES = 3
INITIAL_BACKOFF = 5.0

MAX_IMAGE_MB = 4  # keep screenshots reasonably small for the API

SYSTEM_INSTRUCTIONS = """You are a helpful assistant answering questions about the Element451 platform, using the documentation excerpts provided below.

How to use the excerpts:
- Piece together information across MULTIPLE excerpts when they're related — don't require one excerpt to fully answer the question on its own. If one excerpt describes how filters/segments work generally and another mentions a specific field or date behavior, combine them into one coherent answer.
- If the excerpts describe the general mechanism (e.g. how filters or conditions work) but not the exact specific case asked about, use reasonable inference to suggest how it likely works, based on the patterns shown — just be clear when you're inferring vs. stating something the docs say directly. Say something like "the docs describe X generally, which suggests Y" rather than presenting an inference as a directly documented fact.
- Only say you don't have enough information if the excerpts are genuinely unrelated to the question — not just because no single excerpt spells out every detail.
- Be direct and practical. Give concrete steps when possible, even partial ones, rather than declining to answer.
- Do not invent specific UI labels, button names, or menu paths that aren't mentioned anywhere in the excerpts — inference is for connecting concepts, not fabricating specifics.
- If a screenshot is provided, use it to understand what the user is trying to accomplish overall — not just literal error text. It might show the screen they're on, a partially-built workflow, a field they're stuck on, or their end goal. Ground your answer in that context rather than answering generically.
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


def build_prompt(query: str, hits: list[dict], has_image: bool) -> str:
    context_blocks = []
    for i, h in enumerate(hits, 1):
        context_blocks.append(f"[Excerpt {i}] From \"{h['title']}\" ({h['collection']}):\n{h['text']}")
    context = "\n\n".join(context_blocks)

    image_note = (
        "\nThe user has also attached a screenshot to help explain what they're trying to accomplish — "
        "use it as context for their overall goal, not just as an error message to diagnose.\n"
        if has_image else ""
    )

    return f"""{SYSTEM_INSTRUCTIONS}

--- DOCUMENTATION EXCERPTS ---
{context}
--- END EXCERPTS ---
{image_note}
Question: {query}

Answer:"""


def generate_answer(prompt: str, image_bytes: bytes | None, image_mime: str | None) -> str:
    parts = [{"text": prompt}]
    if image_bytes is not None:
        parts.append({
            "inline_data": {
                "mime_type": image_mime,
                "data": base64.b64encode(image_bytes).decode("utf-8"),
            }
        })

    payload = {"contents": [{"parts": parts}]}

    backoff = INITIAL_BACKOFF
    for attempt in range(1, MAX_RETRIES + 1):
        resp = requests.post(
            GEN_ENDPOINT,
            headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        if resp.status_code == 200:
            data = resp.json()
            return data["candidates"][0]["content"]["parts"][0]["text"]

        if resp.status_code == 429 and attempt < MAX_RETRIES:
            time.sleep(backoff)
            backoff *= 2
            continue

        raise RuntimeError(f"Generation request failed: {resp.status_code} {resp.text[:500]}")

    raise RuntimeError("Exceeded retries — likely hit the daily quota. Try again later.")


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------

st.set_page_config(page_title="Element451 Help Assistant", page_icon="💬", layout="centered")
st.title("💬 Element451 Help Assistant")
st.caption("Ask a question about the platform, and optionally attach a screenshot for extra context.")

if not API_KEY:
    st.error(
        "GEMINI_API_KEY is not set on the server. Set it before launching:\n\n"
        '`export GEMINI_API_KEY="your-key-here"`'
    )
    st.stop()

if not Path(DB_DIR).exists():
    st.error(f"'{DB_DIR}/' not found next to this app — run the vectorstore build step first.")
    st.stop()

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
        if msg.get("sources"):
            with st.expander("Sources"):
                for title, url in msg["sources"]:
                    st.markdown(f"- [{title}]({url})")

# Screenshot uploader lives above the chat box so it's attached to the *next* message
uploaded_file = st.file_uploader(
    "Attach a screenshot to show what you're working on (optional)",
    type=["png", "jpg", "jpeg"],
    key=f"uploader_{len(st.session_state.messages)}",
)

query = st.chat_input("Ask a question...")

if query:
    image_bytes, image_mime, display_image = None, None, None
    if uploaded_file is not None:
        image_bytes = uploaded_file.getvalue()
        if len(image_bytes) > MAX_IMAGE_MB * 1024 * 1024:
            st.warning(f"Screenshot is over {MAX_IMAGE_MB}MB — try a smaller crop or lower resolution.")
            image_bytes = None
        else:
            image_mime = uploaded_file.type or "image/png"
            display_image = image_bytes

    st.session_state.messages.append({"role": "user", "content": query, "image": display_image})
    with st.chat_message("user"):
        st.markdown(query)
        if display_image:
            st.image(display_image, width=250)

    with st.chat_message("assistant"):
        with st.spinner("Searching docs and thinking..."):
            hits = retrieve(embed_model, collection, query)
            prompt = build_prompt(query, hits, has_image=image_bytes is not None)
            try:
                answer = generate_answer(prompt, image_bytes, image_mime)
            except RuntimeError as e:
                answer = f"⚠️ {e}"
                hits = []

        st.markdown(answer)

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
    })
    st.rerun()  # clears the file_uploader for the next question