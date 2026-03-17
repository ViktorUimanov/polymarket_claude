#!/usr/bin/env python3
"""
Polymarket Gamma API market and event fetcher.

Usage:
  python3 fetch_markets.py                          # top markets by volume
  python3 fetch_markets.py --search "oil"           # keyword search
  python3 fetch_markets.py --category sports        # category filter
  python3 fetch_markets.py --market-id 1467766      # specific market
  python3 fetch_markets.py --market-id 1467766 --price-only
  python3 fetch_markets.py --min-volume 5000 --limit 30
  python3 fetch_markets.py --events                 # use events endpoint (richer data)
  python3 fetch_markets.py --events --tags Sports   # events by tag
  python3 fetch_markets.py --events --sort-by volume24hr  # most active events today
  python3 fetch_markets.py --expiring-days 7        # markets expiring within N days
  python3 fetch_markets.py --offset 100             # pagination
"""

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta

import requests

GAMMA_BASE = "https://gamma-api.polymarket.com"

CATEGORY_KEYWORDS = {
    "sports": [
        "nba", "nfl", "epl", "mlb", "nhl", "tennis", "golf", "soccer",
        "football", "basketball", "baseball", "cricket", "formula", "f1",
        "champions league", "premier league", "world cup", "super bowl",
        "esports", "league of legends", "lol", "masters", "ncaa", "march madness",
    ],
    "politics": [
        "election", "president", "senate", "congress", "governor", "vote",
        "trump", "biden", "harris", "democrat", "republican", "parliament",
        "minister", "policy", "legislation", "ceasefire", "treaty",
        "netanyahu", "iran", "ukraine", "russia", "greenland",
    ],
    "commodities": [
        "oil", "wti", "brent", "gold", "silver", "natural gas", "crude",
        "barrel", "opec", "energy", "copper", "wheat", "corn",
    ],
    "crypto": [
        "bitcoin", "ethereum", "btc", "eth", "crypto", "defi", "nft",
        "solana", "cardano", "binance", "coinbase", "blockchain",
    ],
}


def fetch_events(search=None, tags=None, min_volume=0, limit=50, offset=0,
                 sort_by="volume24hr", expiring_days=None):
    """Fetch events from Gamma API events endpoint — richer than markets endpoint."""
    params = {
        "active": "true",
        "closed": "false",
        "limit": str(limit),
        "order": sort_by,
        "ascending": "false",
    }
    if offset:
        params["offset"] = str(offset)

    if expiring_days is not None:
        end_max = (datetime.now(timezone.utc) + timedelta(days=expiring_days)).isoformat()
        params["end_date_max"] = end_max

    r = requests.get(f"{GAMMA_BASE}/events", params=params, timeout=15)
    r.raise_for_status()
    events = r.json()
    if not isinstance(events, list):
        return []

    if search:
        kw = search.lower()
        events = [
            e for e in events
            if kw in e.get("title", "").lower() or kw in e.get("description", "").lower()
        ]

    if tags:
        tag_kw = tags.lower()
        events = [
            e for e in events
            if any(tag_kw in t.get("label", "").lower() for t in e.get("tags", []))
        ]

    if min_volume > 0:
        events = [e for e in events if float(e.get("volume24hr") or 0) >= min_volume]

    return events


def fetch_markets(search=None, market_id=None, min_volume=0, limit=50,
                  category=None, offset=0, expiring_days=None, max_volume=None):
    """Fetch markets from Gamma API with optional filters."""
    if market_id:
        r = requests.get(f"{GAMMA_BASE}/markets", params={"id": market_id}, timeout=15)
        r.raise_for_status()
        return r.json()

    params = {
        "active": "true",
        "closed": "false",
        "limit": str(limit),
        "order": "volumeNum",
        "ascending": "false",
    }
    if offset:
        params["offset"] = str(offset)

    r = requests.get(f"{GAMMA_BASE}/markets", params=params, timeout=15)
    r.raise_for_status()
    markets = r.json()

    # Filter future end dates only
    now = datetime.now(timezone.utc)
    filtered = []
    for m in markets:
        end = m.get("endDateIso", "")
        if end:
            try:
                end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
                if end_dt < now:
                    continue  # skip already-expired markets
            except Exception:
                pass
        filtered.append(m)
    markets = filtered

    if search:
        kw = search.lower()
        markets = [
            m for m in markets
            if kw in m.get("question", "").lower() or kw in m.get("description", "").lower()
        ]

    if category:
        keywords = CATEGORY_KEYWORDS.get(category.lower(), [category.lower()])
        markets = [
            m for m in markets
            if any(
                k in m.get("question", "").lower() or k in m.get("description", "").lower()
                for k in keywords
            )
        ]

    if min_volume > 0:
        markets = [m for m in markets if float(m.get("volumeNum") or 0) >= min_volume]

    if max_volume is not None:
        markets = [m for m in markets if float(m.get("volumeNum") or 0) <= max_volume]

    if expiring_days is not None:
        deadline = now + timedelta(days=expiring_days)
        result = []
        for m in markets:
            end = m.get("endDateIso", "")
            if end:
                try:
                    end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
                    if end_dt <= deadline:
                        result.append(m)
                except Exception:
                    pass
        markets = result

    return markets


def parse_prices(m):
    """Parse YES/NO prices from a market dict."""
    try:
        prices = json.loads(m.get("outcomePrices") or "[0.5,0.5]")
        return float(prices[0]) * 100, float(prices[1]) * 100
    except Exception:
        return 50.0, 50.0


def get_flags(m):
    """Return warning flags for a market."""
    flags = []
    volume = float(m.get("volumeNum") or 0)
    if volume < 2000:
        flags.append("[LOW_LIQUIDITY]")

    end_date = m.get("endDateIso", "")
    if end_date:
        try:
            end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
            hours_left = (end_dt - datetime.now(timezone.utc)).total_seconds() / 3600
            if hours_left < 6:
                flags.append("[EXPIRES_SOON]")
            elif hours_left < 24:
                flags.append("[TIME_PRESSURE]")
            elif hours_left < 168:
                flags.append("[EXPIRING_7D]")
        except Exception:
            pass

    desc = m.get("description", "").lower()
    if any(phrase in desc for phrase in ["at discretion", "admin decision", "sole judgment"]):
        flags.append("[AMBIGUOUS_RESOLUTION]")

    return flags


def format_market(m, price_only=False):
    """Format a market for display."""
    yes_price, no_price = parse_prices(m)

    if price_only:
        return f"YES: {yes_price:.1f}%  NO: {no_price:.1f}%"

    volume = float(m.get("volumeNum") or 0)
    liquidity = float(m.get("liquidityNum") or 0)
    end_date = m.get("endDateIso", "unknown")
    flags = get_flags(m)
    flag_str = " ".join(flags)

    try:
        outcomes = json.loads(m.get("outcomes") or '["YES","NO"]')
    except Exception:
        outcomes = ["YES", "NO"]

    lines = [
        "=" * 70,
        f"ID:       {m.get('id')}",
        f"Q:        {m.get('question')}",
        f"          {outcomes[0]}: {yes_price:.1f}%  |  {outcomes[1]}: {no_price:.1f}%  {flag_str}",
        f"          Volume: ${volume:,.0f}  |  Liquidity: ${liquidity:,.0f}",
        f"          Resolves: {end_date}",
        f"          Slug: {m.get('slug', '')}",
    ]

    desc = (m.get("description") or "")[:250].strip()
    if desc:
        lines.append(f"          Resolution: {desc}{'...' if len(m.get('description','')) > 250 else ''}")

    return "\n".join(lines)


def format_event(e):
    """Format an event with its top markets."""
    vol24 = float(e.get("volume24hr") or 0)
    vol = float(e.get("volume") or 0)
    end = e.get("endDate", "unknown")[:10]
    tags = [t.get("label", "") for t in e.get("tags", [])[:4]]
    markets = e.get("markets", [])

    lines = [
        "=" * 70,
        f"EVENT:    {e.get('title', '')}",
        f"          24h: ${vol24:,.0f}  |  Total: ${vol:,.0f}",
        f"          Ends: {end}  |  Tags: {tags}",
        f"          Slug: {e.get('slug', '')}",
    ]

    tradeable = []
    for m in markets:
        try:
            prices = json.loads(m.get("outcomePrices") or "[0.5,0.5]")
            yes = float(prices[0]) * 100
        except Exception:
            yes = 50.0
        mvol = float(m.get("volumeNum") or 0)
        # Only show markets in 5-95% range with some volume
        if 5 <= yes <= 95 and mvol >= 1000:
            tradeable.append((yes, mvol, m.get("id"), m.get("question", "")))

    if tradeable:
        lines.append("  --- Tradeable markets (5-95% YES, vol>$1k) ---")
        for yes, mvol, mid, q in sorted(tradeable, key=lambda x: -x[1]):
            lines.append(f"  [{mid}] {yes:.1f}% YES | ${mvol:,.0f} | {q[:70]}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Fetch Polymarket markets/events via Gamma API")
    parser.add_argument("--search", help="Keyword to filter")
    parser.add_argument("--market-id", help="Specific market ID")
    parser.add_argument("--min-volume", type=float, default=0, help="Minimum USD volume (24h for events, total for markets)")
    parser.add_argument("--max-volume", type=float, help="Maximum USD volume (markets only)")
    parser.add_argument("--limit", type=int, default=50, help="Max results to fetch")
    parser.add_argument("--offset", type=int, default=0, help="Pagination offset")
    parser.add_argument("--category", help="Category keyword filter: sports / politics / commodities / crypto")
    parser.add_argument("--price-only", action="store_true", help="Only show current price")
    parser.add_argument("--json", dest="json_output", action="store_true", help="Raw JSON output")
    # Events endpoint
    parser.add_argument("--events", action="store_true", help="Use events endpoint (groups related markets)")
    parser.add_argument("--tags", help="Filter events by tag label (e.g. 'Sports', 'Politics', 'NBA')")
    parser.add_argument("--sort-by", default="volumeNum", help="Sort field: volumeNum, volume24hr, endDate, startDate")
    parser.add_argument("--expiring-days", type=int, help="Only show markets/events expiring within N days")
    args = parser.parse_args()

    try:
        if args.events:
            results = fetch_events(
                search=args.search,
                tags=args.tags,
                min_volume=args.min_volume,
                limit=args.limit,
                offset=args.offset,
                sort_by=args.sort_by if args.sort_by != "volumeNum" else "volume24hr",
                expiring_days=args.expiring_days,
            )
            if not results:
                print("No events found matching criteria.")
                return
            if args.json_output:
                print(json.dumps(results, indent=2))
                return
            print(f"Found {len(results)} events:\n")
            for e in results:
                print(format_event(e))
                print()
        else:
            markets = fetch_markets(
                search=args.search,
                market_id=args.market_id,
                min_volume=args.min_volume,
                max_volume=args.max_volume,
                limit=args.limit,
                offset=args.offset,
                category=args.category,
                expiring_days=args.expiring_days,
            )
            if not markets:
                print("No markets found matching criteria.")
                return
            if args.json_output:
                print(json.dumps(markets, indent=2))
                return
            if args.market_id and args.price_only:
                print(format_market(markets[0], price_only=True))
                return
            print(f"Found {len(markets)} markets:\n")
            for m in markets:
                print(format_market(m))
                print()

    except requests.RequestException as e:
        print(f"ERROR: API request failed: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
