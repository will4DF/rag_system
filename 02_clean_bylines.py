"""
Fix-up pass: strips the "Written by / Author / Date / Table of contents"
byline block from every .md file already sitting in output/articles/.

This does NOT re-scrape anything from the web — it just cleans the files
you already have on disk. Safe to run multiple times (it's a no-op on
files that are already clean).

Run:  python 02_clean_bylines.py
"""

import re
from pathlib import Path

ARTICLES_DIR = Path("output/articles")

MONTHS = ("January|February|March|April|May|June|July|August|"
          "September|October|November|December")

BYLINE_RE = re.compile(
    r"Written by\s*.{0,300}?Table of contents\s*\n+",
    re.DOTALL,
)

BYLINE_FALLBACK_RE = re.compile(
    rf"Written by\s*.{{0,150}}?\n+"
    rf"(?:(?:{MONTHS})\s+\d{{1,2}},\s+\d{{4}}|Updated\s+.{{0,40}}?)"
    rf"\s*\n+",
    re.DOTALL,
)


def clean_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    cleaned = BYLINE_RE.sub("", original, count=1)
    if cleaned == original:
        cleaned = BYLINE_FALLBACK_RE.sub("", original, count=1)
    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        return True
    return False


def main():
    files = sorted(ARTICLES_DIR.glob("*.md"))
    if not files:
        print(f"No .md files found in {ARTICLES_DIR}/ — check the path.")
        return

    changed = 0
    still_broken = []
    for f in files:
        if clean_file(f):
            changed += 1
        if "Written by" in f.read_text(encoding="utf-8"):
            still_broken.append(f.name)

    print(f"Checked {len(files)} files. Cleaned byline junk from {changed} of them.")
    if still_broken:
        print(f"\n{len(still_broken)} files STILL contain 'Written by' after cleanup:")
        for name in still_broken:
            print(f"  - {name}")
    else:
        print("\nAll files are clean — no 'Written by' remaining anywhere.")


if __name__ == "__main__":
    main()
