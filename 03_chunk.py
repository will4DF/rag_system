"""
Step 3: Chunk the cleaned articles in output/articles/ into retrieval-sized
pieces, split primarily along heading boundaries.

Strategy:
  1. Parse each article's frontmatter (title, url, collection) + body.
  2. Split the body into sections at markdown headings (any level).
  3. Track a heading "path" per section (e.g. "Creating a Campaign > Step 1").
  4. Merge consecutive small sections together up to ~TARGET_TOKENS.
  5. Split any section that's still too large into paragraph-based pieces,
     with a little overlap so context isn't abruptly cut off.
  6. Each chunk is saved with a text-prefix carrying the article title,
     collection, and section path, so the embedding + LLM always know
     what they're reading even out of context.

Output: output/chunks.jsonl (one JSON object per line) + a summary printed
to the console.

Run:  python 03_chunk.py
"""

import json
import re
from pathlib import Path

ARTICLES_DIR = Path("output/articles")
OUT_PATH = Path("output/chunks.jsonl")

TARGET_TOKENS = 450     # aim for chunks around this size
MAX_TOKENS = 700        # hard ceiling before we force-split a section
OVERLAP_WORDS = 40      # ~ words repeated between forced splits for context

HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n\n?(.*)$", re.DOTALL)


def approx_tokens(text: str) -> int:
    """Rough token estimate (~0.75 words per token) without needing a
    tokenizer dependency. Good enough for chunk-size decisions."""
    words = len(text.split())
    return int(words / 0.75)


def parse_frontmatter(raw: str) -> tuple[dict, str]:
    m = FRONTMATTER_RE.match(raw)
    if not m:
        return {}, raw
    fm_block, body = m.group(1), m.group(2)
    meta = {}
    for line in fm_block.splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            meta[key.strip()] = val.strip()
    return meta, body


def split_into_sections(body: str) -> list[dict]:
    """Split body text into sections at heading boundaries, tracking a
    breadcrumb 'path' of headings leading to each section."""
    matches = list(HEADING_RE.finditer(body))
    sections = []

    # Content before the first heading (e.g. an intro paragraph)
    if not matches or matches[0].start() > 0:
        intro_end = matches[0].start() if matches else len(body)
        intro = body[:intro_end].strip()
        if intro:
            sections.append({"path": "", "content": intro})

    stack = []  # list of (level, heading_text)
    for i, m in enumerate(matches):
        level = len(m.group(1))
        heading = m.group(2).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        content = body[start:end].strip()

        while stack and stack[-1][0] >= level:
            stack.pop()
        stack.append((level, heading))
        path = " > ".join(h for _, h in stack)

        if content:
            sections.append({"path": path, "content": content})

    return sections


def split_oversized_block(text: str, max_tokens: int) -> list[str]:
    """Split a single oversized block (e.g. a markdown table with no blank
    lines between rows, or one giant unbroken paragraph) that couldn't be
    split by the normal blank-line paragraph splitter."""
    lines = text.split("\n")

    if len(lines) == 1:
        # One giant line with no newlines at all — split by words.
        words = text.split()
        words_per_piece = max(int(max_tokens * 0.75), 20)
        return [
            " ".join(words[i:i + words_per_piece])
            for i in range(0, len(words), words_per_piece)
        ] or [text]

    # Multi-line block (typically a markdown table). If it looks like a
    # table, keep the header row (+ separator row) attached to every piece
    # so each chunk is still self-explanatory on its own.
    header_lines = []
    body_lines = lines
    if lines[0].strip().startswith("|") and len(lines) > 1:
        sep_chars = set(lines[1].replace("|", "").replace("-", "").replace(":", "").strip())
        if sep_chars == set():
            header_lines = lines[:2]
            body_lines = lines[2:]

    pieces = []
    current = list(header_lines)
    current_tokens = approx_tokens("\n".join(current)) if header_lines else 0

    for line in body_lines:
        line_tokens = approx_tokens(line)
        if current_tokens + line_tokens > max_tokens and len(current) > len(header_lines):
            pieces.append("\n".join(current))
            current = list(header_lines) + [line]
            current_tokens = approx_tokens("\n".join(current))
        else:
            current.append(line)
            current_tokens += line_tokens

    if len(current) > len(header_lines) or not header_lines:
        pieces.append("\n".join(current))

    return pieces if pieces else [text]


def split_large_section(content: str, max_tokens: int, overlap_words: int) -> list[str]:
    """Split an oversized section into paragraph-based pieces, each under
    max_tokens, with a small word-overlap between consecutive pieces.
    Any single paragraph that's still too large on its own (e.g. a
    markdown table with no blank lines) gets further split by line."""
    paragraphs = [p.strip() for p in content.split("\n\n") if p.strip()]
    pieces = []
    current = []
    current_tokens = 0

    def flush_current():
        if current:
            pieces.append("\n\n".join(current))
            current.clear()

    for para in paragraphs:
        para_tokens = approx_tokens(para)

        if para_tokens > max_tokens:
            flush_current()
            current_tokens = 0
            pieces.extend(split_oversized_block(para, max_tokens))
            continue

        if current and current_tokens + para_tokens > max_tokens:
            flush_current()
            overlap_text = " ".join(pieces[-1].split()[-overlap_words:]) if pieces else ""
            current = [overlap_text] if overlap_text else []
            current_tokens = approx_tokens(overlap_text)

        current.append(para)
        current_tokens += para_tokens

    flush_current()
    return pieces if pieces else [content]


def merge_and_split_sections(sections: list[dict]) -> list[dict]:
    """Merge small consecutive sections up to TARGET_TOKENS, and split any
    section that's still too large on its own."""
    chunks = []
    buffer_path = None
    buffer_parts = []
    buffer_tokens = 0

    def flush():
        nonlocal buffer_path, buffer_parts, buffer_tokens
        if buffer_parts:
            chunks.append({"path": buffer_path, "content": "\n\n".join(buffer_parts)})
        buffer_path, buffer_parts, buffer_tokens = None, [], 0

    for sec in sections:
        sec_tokens = approx_tokens(sec["content"])
        sec_top_level = sec["path"].split(" > ")[0] if sec["path"] else None
        buffer_top_level = buffer_path.split(" > ")[0] if buffer_path else None

        if sec_tokens > MAX_TOKENS:
            flush()
            for piece in split_large_section(sec["content"], TARGET_TOKENS, OVERLAP_WORDS):
                chunks.append({"path": sec["path"], "content": piece})
            continue

        # Never merge across different top-level heading groups, even if
        # both are individually small — that would blend unrelated topics
        # into one chunk and mislabel it with only the first section's path.
        if buffer_parts and sec_top_level != buffer_top_level:
            flush()

        if buffer_tokens + sec_tokens > TARGET_TOKENS and buffer_parts:
            flush()

        if not buffer_parts:
            buffer_path = sec["path"]
        buffer_parts.append(f"### {sec['path'].split(' > ')[-1]}\n{sec['content']}" if sec["path"] else sec["content"])
        buffer_tokens += sec_tokens

    flush()
    return chunks


def chunk_article(meta: dict, body: str) -> list[dict]:
    sections = split_into_sections(body)
    raw_chunks = merge_and_split_sections(sections)

    title = meta.get("title", "")
    collection = meta.get("collection", "")
    url = meta.get("url", "")

    results = []
    for i, c in enumerate(raw_chunks):
        header_bits = [f"Article: {title}"]
        if collection:
            header_bits.append(f"Collection: {collection}")
        if c["path"]:
            header_bits.append(f"Section: {c['path']}")
        prefix = "\n".join(header_bits)

        embedding_text = f"{prefix}\n\n{c['content']}"

        results.append({
            "chunk_id": f"{Path(url).name or title}::{i}",
            "title": title,
            "url": url,
            "collection": collection,
            "section_path": c["path"],
            "text": c["content"],
            "embedding_text": embedding_text,
            "approx_tokens": approx_tokens(embedding_text),
        })
    return results


def main():
    files = sorted(ARTICLES_DIR.glob("*.md"))
    if not files:
        print(f"No .md files found in {ARTICLES_DIR}/ — check the path.")
        return

    all_chunks = []
    for f in files:
        raw = f.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        all_chunks.extend(chunk_article(meta, body))

    with OUT_PATH.open("w", encoding="utf-8") as out:
        for c in all_chunks:
            out.write(json.dumps(c, ensure_ascii=False) + "\n")

    token_counts = [c["approx_tokens"] for c in all_chunks]
    avg_tokens = sum(token_counts) / len(token_counts) if token_counts else 0
    over_max = sum(1 for t in token_counts if t > MAX_TOKENS)

    print(f"Chunked {len(files)} articles into {len(all_chunks)} chunks.")
    print(f"Average chunk size: {avg_tokens:.0f} tokens (target {TARGET_TOKENS}).")
    print(f"Chunks over the {MAX_TOKENS}-token ceiling: {over_max}")
    print(f"Saved to {OUT_PATH}")


if __name__ == "__main__":
    main()