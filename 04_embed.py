"""
Step 4: Embed every chunk in output/chunks.jsonl using Google's free
Gemini Embedding API (gemini-embedding-001).

Free-tier limits observed for Gemini Embedding 1: 100 RPM, 30K TPM, 1000 RPD.
Each chunk counts individually toward ALL of these (confirmed: one batch of
50 chunks showed up as 50/1000 on the RPD dashboard) — batching keeps you
under the per-minute limits, but does NOT let you exceed the 1000/day cap.
At volumes over ~1000 chunks, expect to need multiple daily runs. That's
normal — this script is fully resumable, so just re-run it after the quota
resets (midnight Pacific time) and it picks up where it left off.

Setup:
  export GEMINI_API_KEY="your-key-here"
  pip install requests tqdm

Run:  python 04_embed.py
"""

import json
import os
import time
from pathlib import Path

import requests
from tqdm import tqdm

CHUNKS_PATH = Path("output/chunks.jsonl")
EMBEDDINGS_PATH = Path("output/embeddings.jsonl")

API_KEY = os.environ.get("GEMINI_API_KEY")
MODEL = "gemini-embedding-001"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:batchEmbedContents"

BATCH_SIZE = 50                # ~50 chunks/call keeps well under 30K TPM
OUTPUT_DIMENSIONALITY = 768
MAX_RETRIES = 4
INITIAL_BACKOFF = 15.0
SLEEP_BETWEEN_BATCHES = 65.0   # >1 min, so only ~1 call lands per RPM window
DAILY_REQUEST_BUDGET = 950     # stop a bit before the 1000/day ceiling


def load_chunks() -> list[dict]:
    chunks = []
    with CHUNKS_PATH.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                chunks.append(json.loads(line))
    return chunks


def load_already_embedded() -> set[str]:
    if not EMBEDDINGS_PATH.exists():
        return set()
    done = set()
    with EMBEDDINGS_PATH.open(encoding="utf-8") as f:
        for line in f:
            if line.strip():
                done.add(json.loads(line)["chunk_id"])
    return done


def embed_batch(texts: list[str]) -> list[list[float]]:
    payload = {
        "requests": [
            {
                "model": f"models/{MODEL}",
                "content": {"parts": [{"text": t}]},
                "taskType": "RETRIEVAL_DOCUMENT",
                "outputDimensionality": OUTPUT_DIMENSIONALITY,
            }
            for t in texts
        ]
    }

    backoff = INITIAL_BACKOFF
    for attempt in range(1, MAX_RETRIES + 1):
        resp = requests.post(
            ENDPOINT,
            headers={"x-goog-api-key": API_KEY, "Content-Type": "application/json"},
            json=payload,
            timeout=60,
        )
        if resp.status_code == 200:
            data = resp.json()
            return [e["values"] for e in data["embeddings"]]

        if resp.status_code == 429:
            if attempt < MAX_RETRIES:
                print(f"  [retry] status 429, waiting {backoff:.0f}s (attempt {attempt}/{MAX_RETRIES})")
                time.sleep(backoff)
                backoff *= 1.7
                continue
            raise RuntimeError("DAILY_QUOTA_LIKELY_EXHAUSTED")

        if resp.status_code in (500, 502, 503) and attempt < MAX_RETRIES:
            print(f"  [retry] status {resp.status_code}, waiting {backoff:.0f}s (attempt {attempt}/{MAX_RETRIES})")
            time.sleep(backoff)
            backoff *= 1.7
            continue

        raise RuntimeError(f"Embedding request failed: {resp.status_code} {resp.text[:500]}")

    raise RuntimeError("DAILY_QUOTA_LIKELY_EXHAUSTED")


def main():
    if not API_KEY:
        print("ERROR: Set the GEMINI_API_KEY environment variable first.")
        print('  export GEMINI_API_KEY="your-key-here"')
        return

    if not CHUNKS_PATH.exists():
        print(f"ERROR: {CHUNKS_PATH} not found — run 03_chunk.py first.")
        return

    chunks = load_chunks()
    already_done = load_already_embedded()
    todo = [c for c in chunks if c["chunk_id"] not in already_done]

    print(f"Total chunks: {len(chunks)}. Already embedded: {len(already_done)}. Remaining: {len(todo)}.")
    if not todo:
        print("Nothing to do — all chunks already embedded.")
        return

    requests_used_today = 0
    completed_this_run = 0

    with EMBEDDINGS_PATH.open("a", encoding="utf-8") as out:
        pbar = tqdm(range(0, len(todo), BATCH_SIZE), desc="Embedding batches")
        for i in pbar:
            if requests_used_today + BATCH_SIZE > DAILY_REQUEST_BUDGET:
                print(f"\nApproaching daily budget ({DAILY_REQUEST_BUDGET} chunks) — stopping for today.")
                print(f"Embedded {completed_this_run} chunks this run. Re-run this script after the quota")
                print("resets (midnight Pacific time) to continue — it will pick up automatically.")
                return

            batch = todo[i:i + BATCH_SIZE]
            texts = [c["embedding_text"] for c in batch]

            try:
                vectors = embed_batch(texts)
            except RuntimeError as e:
                if "DAILY_QUOTA_LIKELY_EXHAUSTED" in str(e):
                    print(f"\nHit persistent rate limiting — likely the daily quota is exhausted.")
                    print(f"Embedded {completed_this_run} chunks this run (total so far: {len(already_done) + completed_this_run}/{len(chunks)}).")
                    print("Re-run this script after the quota resets (midnight Pacific time) to continue.")
                    return
                raise

            for c, vec in zip(batch, vectors):
                out.write(json.dumps({
                    "chunk_id": c["chunk_id"],
                    "embedding": vec,
                }) + "\n")
            out.flush()

            requests_used_today += len(batch)
            completed_this_run += len(batch)
            time.sleep(SLEEP_BETWEEN_BATCHES)

    print(f"Done. Embeddings saved to {EMBEDDINGS_PATH}")


if __name__ == "__main__":
    main()