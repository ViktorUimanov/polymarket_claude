#!/usr/bin/env python3
"""
Polymarket Gamma API market fetcher.

Usage:
  python3 fetch_markets.py                          # top markets by volume
  python3 fetch_markets.py --search "oil"           # keyword search
  python3 fetch_markets.py --category sports        # category filter
  python3 fetch_markets.py --market-id 1467766      # specific market
  python3 fetch_markets.py --market-id 1467766 --price-only
  python3 fetch_markets.py --min-volume 5000 --limit 30
  python3 fetch_markets.py --search "bitcoin" --json
"""

import argparse
import json
import sys
from datetime import datetime, timezone

import requests

GAMMA_BASE = "https://gamma-api.polymarket.com"

CATEGORY_KEYWORDS = {
    "sports": [
        "nba", "nfl", "epl", "mlb", "nhl", "tennis", "golf", "soccer",
        "football", "basketball", "baseball", "cricket", "formula", "f1",
        "champions league", "premier league", "world cup", "super bowl",
    ],
    "politics": [
        "election", "president", "senate", "congress", "governor", "vote",
        "trump", "biden", "harris", "democrat", "republican", "parliament",
        "minister", "policy", "legislation", "ceasefire", "treaty",
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


def fetch_markets(search=None, market_id=None, min_volume=0, limit=50, category=None):
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
    r = requests.get(f"{GAMMA_BASE}/markets", params=params, timeout=15)
    r.raise_for_status()
    markets = r.json()

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


def main():
    parser = argparse.ArgumentParser(description="Fetch Polymarket markets via Gamma API")
    parser.add_argument("--search", help="Keyword to filter markets")
    parser.add_argument("--market-id", help="Specific market ID")
    parser.add_argument("--min-volume", type=float, default=0, help="Minimum USD volume")
    parser.add_argument("--limit", type=int, default=50, help="Max markets to fetch")
    parser.add_argument("--category", help="Category: sports / politics / commodities / crypto")
    parser.add_argument("--price-only", action="store_true", help="Only show current price")
    parser.add_argument("--json", dest="json_output", action="store_true", help="Raw JSON output")
    args = parser.parse_args()

    try:
        markets = fetch_markets(
            search=args.search,
            market_id=args.market_id,
            min_volume=args.min_volume,
            limit=args.limit,
            category=args.category,
        )
    except requests.RequestException as e:
        print(f"ERROR: API request failed: {e}", file=sys.stderr)
        sys.exit(1)

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


if __name__ == "__main__":
    main()
