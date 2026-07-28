"""
Step 6 (part 1): Query the vector store directly — no LLM yet, just raw
semantic search. This lets you sanity-check that retrieval actually works
before we wire up the final answer-generation step.

Run:  python 06_search.py
Then type questions and see what chunks come back.
"""

from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer

DB_DIR = "chroma_db"
COLLECTION_NAME = "element451_help"
MODEL_NAME = "BAAI/bge-small-en-v1.5"
TOP_K = 5

# bge models require this instruction prefix on QUERIES (not documents) for
# good retrieval — without it, results skew toward generic keyword overlap
# instead of actually matching search intent.
QUERY_PREFIX = "Represent this sentence for searching relevant passages: "


def main():
    if not Path(DB_DIR).exists():
        print(f"ERROR: {DB_DIR}/ not found — run 05_build_vectorstore.py first.")
        return

    print("Loading model and database...")
    model = SentenceTransformer(MODEL_NAME)
    client = chromadb.PersistentClient(path=DB_DIR)
    collection = client.get_collection(COLLECTION_NAME)

    print(f"Ready. {collection.count()} chunks loaded. Type a question (or 'quit' to exit).\n")

    while True:
        query = input("> ").strip()
        if not query:
            continue
        if query.lower() in ("quit", "exit", "q"):
            break

        query_vec = model.encode([QUERY_PREFIX + query], normalize_embeddings=True)[0].tolist()

        results = collection.query(
            query_embeddings=[query_vec],
            n_results=TOP_K,
        )

        docs = results["documents"][0]
        metas = results["metadatas"][0]
        dists = results["distances"][0]

        print()
        for i, (doc, meta, dist) in enumerate(zip(docs, metas, dists), 1):
            similarity = 1 - dist  # cosine distance -> similarity
            print(f"[{i}] {meta['title']} ({meta['collection']}) — similarity {similarity:.2f}")
            if meta.get("section_path"):
                print(f"    Section: {meta['section_path']}")
            print(f"    {meta['url']}")
            preview = doc[:200].replace("\n", " ")
            print(f"    \"{preview}...\"")
            print()


if __name__ == "__main__":
    main()