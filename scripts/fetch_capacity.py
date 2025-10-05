#!/usr/bin/env python3
import os, sys, json, time, pathlib, re
from datetime import datetime, timezone
from urllib.parse import urljoin, urlencode
import requests
from slugify import slugify

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "docs" / "auto"
OUT_DIR.mkdir(parents=True, exist_ok=True)

BASE = os.environ.get("CAPACITY_BASE_URL", "").rstrip("/")
API_KEY = os.environ.get("CAPACITY_API_KEY", "")
ARTICLES_EP = os.environ.get("CAPACITY_ARTICLES_ENDPOINT", "/v1/kb/articles")
PAGE_SIZE = int(os.environ.get("CAPACITY_PAGE_SIZE", "100"))

def die(msg:str, code:int=2):
    print(f"[capacity] {msg}", file=sys.stderr)
    sys.exit(code)

def get_headers():
    if not API_KEY:
        die("Missing CAPACITY_API_KEY env")
    return {
        "Authorization": f"Bearer {API_KEY}",
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "yegge-docs-capacity-sync/1.0",
    }

def fetch_paginated(path:str, params:dict=None):
    """Generic paginator. Tries common patterns: ?page/limit or ?cursor/next."""
    url = urljoin(BASE + "/", path.lstrip("/"))
    headers = get_headers()
    params = dict(params or {})
    params.setdefault("limit", PAGE_SIZE)

    items = []
    cursor = None
    tries = 0

    while True:
        q = dict(params)
        if cursor:
            q["cursor"] = cursor
        full = f"{url}?{urlencode(q)}"
        tries += 1
        try:
            r = requests.get(full, headers=headers, timeout=30)
            if r.status_code >= 400:
                die(f"HTTP {r.status_code} from {full}: {r.text[:300]}")
            data = r.json()
        except Exception as e:
            die(f"Request error on {full}: {e}")

        # Try to detect where the list is:
        payload = None
        for key in ("articles","items","data","results"):
            if isinstance(data, dict) and key in data and isinstance(data[key], list):
                payload = data[key]
                break
        if payload is None and isinstance(data, list):
            payload = data
        if payload is None:
            die(f"Could not find list in response for {full}. Keys: {list(data) if isinstance(data, dict) else type(data)}")

        items.extend(payload)

        # Try common next-page indicators
        cursor = None
        if isinstance(data, dict):
            if data.get("next"):               # URL or cursor
                nxt = data["next"]
                if isinstance(nxt, str) and "http" in nxt:
                    url = nxt.split("?")[0]
                    # try to extract cursor from next, fallback to using the URL directly next loop
                    m = re.search(r"[?&](?:cursor|page_token)=([^&]+)", nxt)
                    cursor = m.group(1) if m else None
                elif isinstance(nxt, str):
                    cursor = nxt
            elif data.get("has_more") and data.get("cursor"):
                cursor = data["cursor"]

        if not cursor:
            break

        # polite rate limit
        time.sleep(0.15)

    return items

def md_escape(text:str) -> str:
    return text.replace("\r", "").strip()

def write_article_md(article:dict):
    title = article.get("title") or article.get("name") or "Untitled"
    slug  = article.get("slug") or slugify(title) or f"article-{int(time.time())}"
    updated_at = article.get("updated_at") or article.get("updatedAt") or article.get("modified") or ""
    try:
        # normalize to ISO date
        if updated_at:
            dt = datetime.fromisoformat(updated_at.replace("Z","+00:00"))
            updated_at = dt.astimezone(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    except Exception:
        updated_at = ""

    # Try common body fields
    body = (
        article.get("body_md") or
        article.get("content_md") or
        article.get("markdown") or
        article.get("body") or
        article.get("content") or
        ""
    )
    body = md_escape(body)

    # If body looks HTML, wrap in fenced block hint; otherwise assume Markdown already
    if "<" in body and ">" in body and "\n" in body and not body.strip().startswith("#"):
        body_md = f"\n\n<div class=\"kb-html\">\n{body}\n</div>\n"
    else:
        body_md = "\n\n" + body + "\n"

    front = []
    front.append(f'title: "{title.replace("\"","'")}"')
    if updated_at:
        front.append(f'last_updated: "{updated_at}"')
    # Add more front-matter fields as you like:
    # front.append(f'category: "{article.get("category","")}"')

    md = f"""---
{chr(10).join(front)}
---

# {title}

{body_md}
"""
    path = OUT_DIR / f"{slug}.md"
    path.write_text(md, encoding="utf-8")
    return path.name

def write_index(items:list):
    # Build a simple index page that links to generated articles
    lines = ["# Knowledge Base", "", "Auto-generated from Capacity at build time."]
    for a in items:
        title = a.get("title") or a.get("name") or "Untitled"
        slug  = a.get("slug") or slugify(title)
        lines.append(f"- [{title}](./{slug}.md)")
    (OUT_DIR / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

def main():
    if not BASE:
        die("Missing CAPACITY_BASE_URL env")
    print(f"[capacity] Fetching from {BASE}{ARTICLES_EP} …")
    items = fetch_paginated(ARTICLES_EP)
    if not items:
        die("No articles returned from API")

    written = []
    for it in items:
        try:
            fn = write_article_md(it)
            written.append(fn)
        except Exception as e:
            print(f"[capacity] Skipped one article: {e}", file=sys.stderr)

    write_index(items)
    print(f"[capacity] Wrote {len(written)} article files into {OUT_DIR}")

if __name__ == "__main__":
    main()