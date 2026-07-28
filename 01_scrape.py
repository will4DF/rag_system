"""
Step 2: Scrape help.element451.com into local markdown files.

- Discovers all collections from the help center homepage
- Skips the "Feature Releases" collection (changelog, not core docs)
- Crawls every remaining collection to find article URLs
- Fetches each article, extracts title + body text, strips nav/boilerplate
- Saves one .md file per article + a manifest.json with metadata

Run:  python 01_scrape.py
Requires: pip install requests beautifulsoup4 tqdm markdownify
"""

import json
import re
import time
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as html_to_md
from tqdm import tqdm

BASE = "https://help.element451.com"
HOME = f"{BASE}/en/"
OUT_DIR = Path("output/articles")
MANIFEST_PATH = Path("output/manifest.json")
EXCLUDE_COLLECTIONS = {"feature releases"}  # lowercase match

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; RAG-ingest-bot/1.0; +internal use)"
}
REQUEST_DELAY = 0.5  # be polite to their servers


def get_soup(url: str) -> BeautifulSoup:
    resp = requests.get(url, headers=HEADERS, timeout=20)
    resp.raise_for_status()
    return BeautifulSoup(resp.text, "html.parser")


def clean_collection_name(name: str) -> str:
    """Intercom glues 'N author(s)' and 'N article(s)' counts onto the
    collection name text with no separator, e.g. 'Organizations1 author3
    articles'. Strip those trailing count segments off repeatedly."""
    while True:
        new = re.sub(r"\d+\s*(authors?|articles?)$", "", name).strip()
        if new == name:
            return name
        name = new


def is_excluded(name: str) -> bool:
    lowered = name.strip().lower()
    return any(ex in lowered for ex in EXCLUDE_COLLECTIONS)


def discover_collections() -> list[dict]:
    """Find all collection links + names from the homepage."""
    soup = get_soup(HOME)
    collections = {}
    for a in soup.select('a[href*="/collections/"]'):
        href = a.get("href")
        if not href:
            continue
        url = urljoin(BASE, href)
        # collection name is usually the link text or a nearby heading
        name = clean_collection_name(a.get_text(strip=True))
        if url not in collections and name:
            collections[url] = name
    return [{"url": u, "name": n} for u, n in collections.items()]


def get_articles_for_collection(collection_url: str, _visited: set | None = None) -> list[dict]:
    """Find all article links within a collection page, recursing into any
    nested sub-collections (e.g. 'General' contains 'Platform Information',
    'Announcements', etc. as child collections)."""
    if _visited is None:
        _visited = set()
    if collection_url in _visited:
        return []
    _visited.add(collection_url)

    soup = get_soup(collection_url)
    articles = {}

    for a in soup.select('a[href*="/articles/"]'):
        href = a.get("href")
        if not href:
            continue
        url = urljoin(BASE, href).split("#")[0]
        title = a.get_text(strip=True)
        if url not in articles and title:
            articles[url] = title

    # Recurse into nested sub-collections found on this page
    for a in soup.select('a[href*="/collections/"]'):
        href = a.get("href")
        if not href:
            continue
        sub_url = urljoin(BASE, href).split("#")[0]
        if sub_url == collection_url or sub_url in _visited:
            continue
        sub_name = clean_collection_name(a.get_text(strip=True))
        if is_excluded(sub_name):
            print(f"  [skip] nested collection excluded: {sub_name!r}")
            continue
        time.sleep(REQUEST_DELAY)
        for sub_art in get_articles_for_collection(sub_url, _visited):
            articles.setdefault(sub_art["url"], sub_art["title"])

    return [{"url": u, "title": t} for u, t in articles.items()]


END_MARKERS = [
    "Related Articles",
    "Did this answer your question",
    "The AI Platform for Higher Education",
]


def extract_article(url: str) -> dict | None:
    """Fetch one article page and pull out clean title + body as real
    markdown (headings, lists, bold preserved) instead of flattened text.

    Intercom's exact CSS classes aren't reliable to guess from outside, so
    instead of trusting a selector we take the main content region and trim
    at known boundary strings that mark the end of real article content
    (related-articles module, feedback widget, footer)."""
    soup = get_soup(url)

    for junk in soup(["script", "style", "nav"]):
        junk.decompose()

    title_el = soup.find("h1")
    title = title_el.get_text(strip=True) if title_el else None

    body_el = soup.find("main") or soup.find("article") or soup.body
    if not body_el:
        return None

    # Convert to markdown so headings (#, ##, ###) and lists (-) survive,
    # which the chunker relies on to split by section.
    md = html_to_md(str(body_el), heading_style="ATX")
    md = re.sub(r"\n{3,}", "\n\n", md).strip()

    # Cut off everything from the first end-marker onward
    cut_idx = len(md)
    for marker in END_MARKERS:
        idx = md.find(marker)
        if idx != -1:
            cut_idx = min(cut_idx, idx)
    md = md[:cut_idx].strip()
    md = re.sub(r"\n#{1,6}\s*$", "", md).strip()  # trailing empty heading marker

    # Drop leading breadcrumb/byline noise before the title if it repeats
    if title and title in md:
        md = md[md.find(title) + len(title):].strip()

    # Strip the "Written by / Author Name / Month Day, Year / Table of
    # contents" byline block Intercom inserts right after the title.
    # Markdown emphasis chars (*, #) may surround these lines, so allow
    # for optional non-alphanumeric junk around them.
    months = ("January|February|March|April|May|June|July|August|"
              "September|October|November|December")
    byline_re = re.compile(
        rf"^[#*\s]*Written by\s*.*?\n+[#*\s]*(?:{months})\s+\d{{1,2}},\s+\d{{4}}[#*\s]*\n?",
        re.DOTALL,
    )
    md = byline_re.sub("", md, count=1).strip()
    md = re.sub(r"^[#*\s]*Table of contents[#*\s]*\n", "", md).strip()

    return {"title": title or url, "text": md}


def slugify(text: str) -> str:
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return text[:80]


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Discovering collections...")
    collections = discover_collections()
    print(f"Raw discovered collection names: {[c['name'] for c in collections]}")
    skipped = [c["name"] for c in collections if is_excluded(c["name"])]
    collections = [c for c in collections if not is_excluded(c["name"])]
    print(f"Skipping top-level collections: {skipped}")
    print(f"Found {len(collections)} collections to crawl (Feature Releases excluded).")

    all_articles = {}
    for col in tqdm(collections, desc="Collections"):
        try:
            arts = get_articles_for_collection(col["url"])
        except requests.RequestException as e:
            print(f"  [!] Failed to load collection {col['url']}: {e}")
            continue
        for a in arts:
            a["collection"] = col["name"]
            all_articles[a["url"]] = a
        time.sleep(REQUEST_DELAY)

    print(f"Found {len(all_articles)} unique articles. Fetching content...")

    manifest = []
    for url, meta in tqdm(all_articles.items(), desc="Articles"):
        try:
            data = extract_article(url)
        except requests.RequestException as e:
            print(f"  [!] Failed to fetch {url}: {e}")
            continue
        if not data or not data["text"]:
            continue

        fname = f"{slugify(data['title'])}.md"
        fpath = OUT_DIR / fname

        frontmatter = (
            f"---\n"
            f"title: {data['title']}\n"
            f"url: {url}\n"
            f"collection: {meta['collection']}\n"
            f"---\n\n"
        )
        fpath.write_text(frontmatter + data["text"], encoding="utf-8")

        manifest.append({
            "title": data["title"],
            "url": url,
            "collection": meta["collection"],
            "file": str(fpath),
        })
        time.sleep(REQUEST_DELAY)

    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"\nDone. Saved {len(manifest)} articles to {OUT_DIR}/")
    print(f"Manifest: {MANIFEST_PATH}")


if __name__ == "__main__":
    main()