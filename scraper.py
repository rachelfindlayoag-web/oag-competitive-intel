import os
import re
import time
import sqlite3
from datetime import datetime, timezone
from urllib.parse import quote_plus

import feedparser
import requests
from bs4 import BeautifulSoup

DB_PATH = os.environ.get("DB_PATH", os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.db"))
TWITTER_BEARER_TOKEN = os.environ.get("TWITTER_BEARER_TOKEN", "")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/124.0.0.0 Safari/537.36"
    )
}

# ── Company definitions ─────────────────────────────────────────────────────
# Each company has:
#   name_variants  – strings that count as "this article is about us" when in title
#   news_queries   – Google News search strings (use quotes for exact phrases)
#   rss_feeds      – official blog / press-release RSS feeds
#   twitter_query  – Twitter/X search query (only used if TWITTER_BEARER_TOKEN is set)

COMPANIES = {
    "Cirium": {
        "name_variants": ["cirium"],
        "news_queries": [
            '"Cirium" launch OR launches OR releases OR announces OR unveils',
            '"Cirium" partnership OR partner OR deal OR contract OR client OR wins',
            '"Cirium" appoints OR acquires OR acquisition OR expands OR funding OR investment',
            '"Cirium" report OR forecast OR data OR index OR analysis OR insight',
        ],
        "rss_feeds": [
            "https://www.cirium.com/thoughtworks/feed/",
        ],
        "twitter_query": 'from:cirium_aero -is:retweet',
    },
    "RateGain": {
        "name_variants": ["rategain", "rate gain"],
        "news_queries": [
            '"RateGain" launch OR launches OR releases OR announces OR unveils OR new',
            '"RateGain" partnership OR partner OR deal OR contract OR integration OR client',
            '"RateGain" appoints OR acquires OR acquisition OR expands OR funding OR revenue',
            '"RateGain" report OR data OR survey OR study OR insight OR trend',
        ],
        "rss_feeds": [
            "https://rategain.com/blog/feed/",
            "https://rategain.com/press-releases/feed/",
        ],
        "twitter_query": 'from:RateGain -is:retweet',
    },
    "Aggregate Intelligence": {
        "name_variants": ["aggregate intelligence", "aggregate.ai", "aggregateintelligence"],
        "news_queries": [
            '"Aggregate Intelligence" airline OR aviation OR travel',
            '"Aggregate Intelligence" pricing OR revenue OR data',
            '"Aggregate Intelligence" launch OR partner OR announces OR acquires',
        ],
        "rss_feeds": [],
        "twitter_query": '"Aggregate Intelligence" airline OR travel -is:retweet',
    },
    "3Victors": {
        "name_variants": ["3victors", "3 victors"],
        "news_queries": [
            '"3Victors" launch OR releases OR announces OR new OR unveils',
            '"3Victors" partnership OR deal OR contract OR client OR integration',
            '"3Victors" appoints OR acquires OR expands OR funding',
            '"3Victors" data OR pricing OR insight OR report',
        ],
        "rss_feeds": [],
        "twitter_query": 'from:3Victors -is:retweet',
    },
}

# ── Category classification ─────────────────────────────────────────────────
# Rules checked in order — first match wins.
# Research & Data is first to prevent "releases annual review" hitting Product Launch.

def classify(title: str, source_type: str = "news") -> str:
    t = title.lower()

    # 0. Unambiguous signals — checked before Research so strong verbs aren't
    #    swallowed by generic keywords like "data" or "analysis"
    if any(kw in t for kw in [
        "acquires", "acquisition", "merger", "merges with",
        "appoints", "appointed", "hires", "joins as", "named as", "named to",
        " ceo ", " cto ", " coo ", "chief executive",
    ]):
        return "Company Update"
    if any(kw in t for kw in ["unveils", "unveiled"]):
        return "Product Launch"

    # 1. Research & Data — checked before Product Launch
    if any(kw in t for kw in [
        "report", "annual review", "monthly review", "quarterly review",
        "data", "dataset", "study", "research", "survey", "whitepaper",
        "white paper", "index", "forecast", "analysis", "findings",
        "statistics", "trend", "outlook", "benchmark", "ranking",
        "insight", "how ", "why ", "what ", "guide to",
        "understanding ", "the state of", "impact of", "future of",
    ]):
        return "Research & Data"

    # 2. Partnership & Client Win — specific phrases first, broader terms after
    if any(kw in t for kw in [
        "partners with", "partnership with", "collaboration with",
        "deal with", "contract with", "agreement with", "signs deal",
        "selected by", "chooses ", "adopts ", "wins contract",
        "awarded ", "airline selects", "hotel selects", "teams up with",
        "integrates with", "integration with",
    ]):
        return "Partnership & Client Win"
    if any(kw in t for kw in ["partner", "partnership", "collaboration"]):
        return "Partnership & Client Win"

    # 3. Company Update — financials, funding, expansions (M&A/appointments already caught above)
    if any(kw in t for kw in [
        "vice president", "raises ", " funding", "series a", "series b", "series c",
        " ipo ", "expands into", "opens office", "annual results", "quarterly results",
    ]):
        return "Company Update"

    # 4. Product Launch — "launches/launch" as a verb, or clear product-noun patterns
    if any(kw in t for kw in [
        "launches ", " launch ", "launch of", "launches its",
        "unveils new", "unveils its", "unveiled new",
        "introduces new", "introduces its",
        "new platform", "new solution", "new tool", "new product",
        "new feature", "new module", "new service", "new dashboard",
        "now available", "general availability", "goes live",
    ]):
        return "Product Launch"

    # Blog posts that don't fit above are usually thought-leadership
    if source_type == "blog":
        return "Research & Data"

    return "Press Coverage"


def is_relevant(company: str, title: str) -> bool:
    """Return True only if the title is actually about this company."""
    title_lower = title.lower()
    variants = COMPANIES[company]["name_variants"]
    return any(v in title_lower for v in variants)


# ── Database helpers ────────────────────────────────────────────────────────

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def save_item(company, title, url, summary, source_type, published_at, category):
    if not title or not title.strip():
        return
    conn = get_db()
    try:
        conn.execute(
            """INSERT OR IGNORE INTO items
               (company, title, url, summary, source_type, published_at, category)
               VALUES (?,?,?,?,?,?,?)""",
            (
                company,
                title.strip()[:500],
                url,
                (summary or "").strip()[:2000],
                source_type,
                published_at,
                category,
            ),
        )
        conn.commit()
    except Exception as e:
        print(f"  [DB] Error: {e}")
    finally:
        conn.close()


def normalise_date(entry) -> str:
    if hasattr(entry, "published_parsed") and entry.published_parsed:
        try:
            return datetime(*entry.published_parsed[:6], tzinfo=timezone.utc).isoformat()
        except Exception:
            pass
    return datetime.now(timezone.utc).isoformat()


# ── Scrapers ────────────────────────────────────────────────────────────────

def fetch_google_news(company: str, queries: list):
    print(f"  [News] {company}")
    for query in queries:
        url = (
            "https://news.google.com/rss/search"
            f"?q={quote_plus(query)}&hl=en-US&gl=US&ceid=US:en"
        )
        try:
            feed = feedparser.parse(url)
            for entry in feed.entries[:10]:
                title = entry.get("title", "")
                if not is_relevant(company, title):
                    continue  # skip articles where company isn't the subject
                summary = BeautifulSoup(
                    entry.get("summary", ""), "html.parser"
                ).get_text(" ", strip=True)[:500]
                save_item(
                    company=company,
                    title=title,
                    url=entry.get("link", ""),
                    summary=summary,
                    source_type="news",
                    published_at=normalise_date(entry),
                    category=classify(title, "news"),
                )
        except Exception as e:
            print(f"  [News] Error for '{query}': {e}")
        time.sleep(1)


def fetch_rss_feeds(company: str, feeds: list):
    if not feeds:
        return
    print(f"  [RSS]  {company}")
    for feed_url in feeds:
        try:
            feed = feedparser.parse(feed_url)
            for entry in feed.entries[:10]:
                title = entry.get("title", "")
                summary = BeautifulSoup(
                    entry.get("summary", ""), "html.parser"
                ).get_text(" ", strip=True)[:500]
                # RSS feeds are from the company's own blog — always relevant
                save_item(
                    company=company,
                    title=title,
                    url=entry.get("link", ""),
                    summary=summary,
                    source_type="blog",
                    published_at=normalise_date(entry),
                    category=classify(title, "blog"),
                )
        except Exception as e:
            print(f"  [RSS]  Error for {feed_url}: {e}")
        time.sleep(1)


def fetch_twitter(company: str, query: str):
    if not TWITTER_BEARER_TOKEN:
        return
    print(f"  [X]    {company}")
    try:
        url = (
            "https://api.twitter.com/2/tweets/search/recent"
            f"?query={quote_plus(query)}&max_results=10"
            "&tweet.fields=created_at,text,author_id"
            "&expansions=author_id&user.fields=username"
        )
        resp = requests.get(
            url,
            headers={"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"},
            timeout=15,
        )
        if resp.status_code != 200:
            print(f"  [X]    API error {resp.status_code}")
            return
        data = resp.json()
        users = {u["id"]: u["username"] for u in data.get("includes", {}).get("users", [])}
        for tweet in data.get("data", []):
            username = users.get(tweet.get("author_id", ""), "twitter")
            text = tweet["text"]
            save_item(
                company=company,
                title=text[:150] + ("…" if len(text) > 150 else ""),
                url=f"https://twitter.com/{username}/status/{tweet['id']}",
                summary=text,
                source_type="twitter",
                published_at=tweet.get("created_at", datetime.now(timezone.utc).isoformat()),
                category=classify(text),
            )
    except Exception as e:
        print(f"  [X]    Error: {e}")


# ── Main entry point ────────────────────────────────────────────────────────

def run_all_scrapers():
    print(f"\n{'='*55}")
    print(f"  Scrape started  {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print(f"{'='*55}")
    for company, cfg in COMPANIES.items():
        print(f"\n[{company}]")
        fetch_google_news(company, cfg["news_queries"])
        fetch_rss_feeds(company, cfg["rss_feeds"])
        if cfg.get("twitter_query"):
            fetch_twitter(company, cfg["twitter_query"])
    print(f"\n  Done.\n")
