"""
Step 5: Load chunks + embeddings into a local Chroma vector database.

Joins output/chunks.jsonl (text + metadata) with output/embeddings.jsonl
(vectors) by chunk_id, and loads everything into a persistent local Chroma
database saved to disk in ./chroma_db/. No server to run — Chroma just
reads/writes files in that folder.

Setup:
  pip install chromadb

Run:  python 05_build_vectorstore.py
"""

import json
from pathlib import Path

import chromadb

CHUNKS_PATH = Path("output/chunks.jsonl")
EMBEDDINGS_PATH = Path("output/embeddings.jsonl")
DB_DIR = "chroma_db"
COLLECTION_NAME = "element451_help"


def load_jsonl(path: Path) -> list[dict]:
    items = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                items.append(json.loads(line))
    return items


def main():
    if not CHUNKS_PATH.exists():
        print(f"ERROR: {CHUNKS_PATH} not found — run 03_chunk.py first.")
        return
    if not EMBEDDINGS_PATH.exists():
        print(f"ERROR: {EMBEDDINGS_PATH} not found — run the embedding step first.")
        return

    chunks = load_jsonl(CHUNKS_PATH)
    embeddings = load_jsonl(EMBEDDINGS_PATH)

    embed_by_id = {e["chunk_id"]: e["embedding"] for e in embeddings}

    matched = [c for c in chunks if c["chunk_id"] in embed_by_id]
    missing = len(chunks) - len(matched)
    if missing:
        print(f"Warning: {missing} chunks have no matching embedding — skipping those.")

    print(f"Loading {len(matched)} chunks into Chroma...")

    client = chromadb.PersistentClient(path=DB_DIR)

    # Fresh start each run — drop and recreate the collection so re-running
    # this script after re-chunking/re-embedding doesn't leave stale data.
    try:
        client.delete_collection(COLLECTION_NAME)
    except Exception:
        pass
    collection = client.create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )

    # Chroma wants plain lists, not numpy arrays, and metadata values must
    # be str/int/float/bool (no None) — clean that up as we go.
    BATCH = 500
    for i in range(0, len(matched), BATCH):
        batch = matched[i:i + BATCH]
        collection.add(
            ids=[c["chunk_id"] for c in batch],
            embeddings=[embed_by_id[c["chunk_id"]] for c in batch],
            documents=[c["text"] for c in batch],
            metadatas=[{
                "title": c.get("title") or "",
                "url": c.get("url") or "",
                "collection": c.get("collection") or "",
                "section_path": c.get("section_path") or "",
            } for c in batch],
        )

    print(f"Done. {collection.count()} chunks loaded into Chroma at ./{DB_DIR}/")
    print(f"Collection name: {COLLECTION_NAME}")


if __name__ == "__main__":
    main()