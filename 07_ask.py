"""
Step 6 (part 2): The real RAG pipeline. Retrieves relevant chunks from
your local Chroma database, then sends them to Gemini to write an actual
answer — not just raw chunks.

Note: Gemini's free tier for text generation (gemini-2.5-flash) has a
fairly tight daily quota. That's fine for testing with a handful of
questions, but don't expect to run hundreds of queries a day on it.

Setup:
  export GEMINI_API_KEY="your-key-here"

Run:  python 07_ask.py
"""

import json
import os
import time
from pathlib import Path

import chromadb
import requests
from sentence_transformers import SentenceTransformer

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

SYSTEM_INSTRUCTIONS = """You are a helpful assistant answering questions about the Element451 platform, using the documentation excerpts provided below.

How to use the excerpts:
- Piece together information across MULTIPLE excerpts when they're related — don't require one excerpt to fully answer the question on its own. If one excerpt describes how filters/segments work generally and another mentions a specific field or date behavior, combine them into one coherent answer.
- If the excerpts describe the general mechanism (e.g. how filters or conditions work) but not the exact specific case asked about, use reasonable inference to suggest how it likely works, based on the patterns shown — just be clear when you're inferring vs. stating something the docs say directly. Say something like "the docs describe X generally, which suggests Y" rather than presenting an inference as a directly documented fact.
- Only say you don't have enough information if the excerpts are genuinely unrelated to the question — not just because no single excerpt spells out every detail.
- Be direct and practical. Give concrete steps when possible, even partial ones, rather than declining to answer.
- Do not invent specific UI labels, button names, or menu paths that aren't mentioned anywhere in the excerpts — inference is for connecting concepts, not fabricating specifics.
- Cite which article(s) your answer draws from at the end, using the titles provided."""


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


def build_prompt(query: str, hits: list[dict]) -> str:
    context_blocks = []
    for i, h in enumerate(hits, 1):
        context_blocks.append(f"[Excerpt {i}] From \"{h['title']}\" ({h['collection']}):\n{h['text']}")
    context = "\n\n".join(context_blocks)

    return f"""{SYSTEM_INSTRUCTIONS}

--- DOCUMENTATION EXCERPTS ---
{context}
--- END EXCERPTS ---

Question: {query}

Answer:"""


def generate_answer(prompt: str) -> str:
    payload = {"contents": [{"parts": [{"text": prompt}]}]}

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
            print(f"  [retry] rate limited, waiting {backoff:.0f}s (attempt {attempt}/{MAX_RETRIES})")
            time.sleep(backoff)
            backoff *= 2
            continue

        raise RuntimeError(f"Generation request failed: {resp.status_code} {resp.text[:500]}")

    raise RuntimeError("Exceeded retries — likely hit the daily quota. Try again later.")


def main():
    if not API_KEY:
        print("ERROR: Set the GEMINI_API_KEY environment variable first.")
        print('  export GEMINI_API_KEY="your-key-here"')
        return

    if not Path(DB_DIR).exists():
        print(f"ERROR: {DB_DIR}/ not found — run 05_build_vectorstore.py first.")
        return

    print("Loading model and database...")
    embed_model = SentenceTransformer(EMBED_MODEL_NAME)
    client = chromadb.PersistentClient(path=DB_DIR)
    collection = client.get_collection(COLLECTION_NAME)

    print(f"Ready. {collection.count()} chunks loaded. Ask a question (or 'quit' to exit).\n")

    while True:
        query = input("> ").strip()
        if not query:
            continue
        if query.lower() in ("quit", "exit", "q"):
            break

        hits = retrieve(embed_model, collection, query)
        prompt = build_prompt(query, hits)

        print("\nThinking...\n")
        try:
            answer = generate_answer(prompt)
        except RuntimeError as e:
            print(f"[Error] {e}\n")
            continue

        print(answer)
        print("\nSources:")
        seen = set()
        for h in hits:
            if h["url"] not in seen:
                print(f"  - {h['title']}: {h['url']}")
                seen.add(h["url"])
        print()


if __name__ == "__main__":
    main()