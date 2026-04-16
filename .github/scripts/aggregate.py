"""Aggregate primary RSS feeds from sources.md into daily-feed.json."""
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

import feedparser
from dateutil import parser as dateparser

REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCES_FILE = REPO_ROOT / "sources.md"
OUTPUT_FILE = REPO_ROOT / "daily-feed.json"
LOOKBACK_HOURS = 36

def extract_primary_feeds(sources_md: str) -> list[str]:
    """Pull all URLs under '## Primary feeds' until the next '## ' heading."""
    lines = sources_md.splitlines()
    in_section = False
    feeds = []
    for line in lines:
        if line.startswith("## Primary feeds"):
            in_section = True
            continue
        if in_section and line.startswith("## ") and "Primary feeds" not in line:
            break
        if in_section:
            match = re.match(r"\s*-\s+(https?://\S+)", line)
            if match:
                feeds.append(match.group(1))
    return feeds

def parse_feed(url: str, cutoff: datetime) -> list[dict]:
    """Return items from this feed newer than cutoff."""
    try:
        parsed = feedparser.parse(url)
    except Exception as exc:
        print(f"[warn] failed to parse {url}: {exc}", file=sys.stderr)
        return []

    source_name = parsed.feed.get("title", url)
    items = []
    for entry in parsed.entries:
        pub_raw = entry.get("published") or entry.get("updated")
        if not pub_raw:
            continue
        try:
            pub = dateparser.parse(pub_raw)
            if pub.tzinfo is None:
                pub = pub.replace(tzinfo=timezone.utc)
        except Exception:
            continue
        if pub < cutoff:
            continue
        items.append({
            "title": entry.get("title", "").strip(),
            "source": source_name,
            "feed_url": url,
            "url": entry.get("link", ""),
            "published": pub.isoformat(),
            "summary": re.sub(r"<[^>]+>", "", entry.get("summary", ""))[:500].strip(),
        })
    return items

def main():
    sources_md = SOURCES_FILE.read_text()
    feeds = extract_primary_feeds(sources_md)
    cutoff = datetime.now(timezone.utc) - timedelta(hours=LOOKBACK_HOURS)

    all_items = []
    for feed_url in feeds:
        all_items.extend(parse_feed(feed_url, cutoff))

    # Dedupe by URL, keep newest
    by_url = {}
    for item in all_items:
        existing = by_url.get(item["url"])
        if existing is None or item["published"] > existing["published"]:
            by_url[item["url"]] = item

    items = sorted(by_url.values(), key=lambda x: x["published"], reverse=True)

    output = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "lookback_hours": LOOKBACK_HOURS,
        "feed_count": len(feeds),
        "item_count": len(items),
        "items": items,
    }
    OUTPUT_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False))
    print(f"Wrote {len(items)} items from {len(feeds)} feeds")

if __name__ == "__main__":
    main()
