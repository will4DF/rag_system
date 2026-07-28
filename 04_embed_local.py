"""
Step 4 (local version): Embed every chunk in output/chunks.jsonl using a
local sentence-transformers model. No API key, no rate limits, no waiting —
runs entirely on your machine.

Model: BAAI/bge-small-en-v1.5 — a small, fast, well-regarded model that's
a standard choice for RAG projects. ~130MB download, first run only.

Setup:
  pip install sentence-transformers

Run:  python 04_embed_local.py
"""

import json
from pathlib import Path

from sentence_transformers import SentenceTransformer
from tqdm import tqdm

CHUNKS_PATH = Path("output/chunks.jsonl")
EMBEDDINGS_PATH = Path("output/embeddings.jsonl")

MODEL_NAME = "BAAI/bge-small-en-v1.5"
BATCH_SIZE = 32

# bge models recommend prefixing documents with this for best retrieval
# quality (asymmetric embedding — queries get a different prefix later).
DOCUMENT_PREFIX = ""  # bge-small doesn't require one for documents (only queries)


def load_chunks() -> list[dict]:
    chunks = []
    with CHUNKS_PATH.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))
    return chunks


def main():
    if not CHUNKS_PATH.exists():
        print(f"ERROR: {CHUNKS_PATH} not found — run 03_chunk.py first.")
        return

    print(f"Loading model {MODEL_NAME} (first run downloads it, ~130MB)...")
    model = SentenceTransformer(MODEL_NAME)

    chunks = load_chunks()
    print(f"Embedding {len(chunks)} chunks locally...")

    texts = [DOCUMENT_PREFIX + c["embedding_text"] for c in chunks]

    embeddings = model.encode(
        texts,
        batch_size=BATCH_SIZE,
        show_progress_bar=True,
        normalize_embeddings=True,  # makes cosine similarity == dot product later
    )

    with EMBEDDINGS_PATH.open("w", encoding="utf-8") as out:
        for c, vec in zip(chunks, embeddings):
            out.write(json.dumps({
                "chunk_id": c["chunk_id"],
                "embedding": vec.tolist(),
            }) + "\n")

    print(f"Done. Embedded {len(chunks)} chunks. Saved to {EMBEDDINGS_PATH}")
    print(f"Embedding dimension: {len(embeddings[0])}")


if __name__ == "__main__":
    main()