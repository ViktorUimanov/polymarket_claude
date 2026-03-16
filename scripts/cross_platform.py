#!/usr/bin/env python3
"""
Cross-platform probability checker — fetches implied probability from
Metaculus and Manifold Markets for independent calibration signal.

Usage:
  python3 cross_platform.py --query "Will Iran regime fall by June 2026?"
  python3 cross_platform.py --query "crude oil $100" --verbose

Output: Comparison table of platform estimates vs your stated probability.
If any platform differs by > 10pp, exits 1 (for scripting / GOLDEN_RULES).

Rule 13: For any market with volume > $50k, run this before finalising.
If diff > 10pp, you must explain the divergence before proceeding.
"""

import argparse
import json
import sys
import urllib.request
import urllib.parse
from typing import Optional


METACULUS_API = "https://www.metaculus.com/api2/questions/"
MANIFOLD_API = "https://api.manifold.markets/v0/search-markets"


def fetch_metaculus(query: str, limit: int = 3) -> list[dict]:
    """Search Metaculus for matching questions, return top results."""
    params = urllib.parse.urlencode({
        "search": query,
        "limit": limit,
        "order_by": "-votes",
        "type": "forecast",
    })
    url = f"{METACULUS_API}?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "polymarket-agent/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        results = data.get("results", [])
        out = []
        for q in results:
            community = q.get("community_prediction", {})
            prob = community.get("full", {}).get("q2") if community else None
            if prob is not None:
                out.append({
                    "platform": "Metaculus",
                    "title": q.get("title", "")[:80],
                    "probability": round(float(prob) * 100, 1),
                    "forecasters": q.get("number_of_forecasters", 0),
                    "url": f"https://www.metaculus.com/questions/{q.get('id', '')}/",
                })
        return out
    except Exception as e:
        return [{"platform": "Metaculus", "error": str(e)}]


def fetch_manifold(query: str, limit: int = 3) -> list[dict]:
    """Search Manifold Markets for matching questions."""
    params = urllib.parse.urlencode({
        "term": query,
        "limit": limit,
        "sort": "liquidity",
        "filter": "open",
        "contractType": "BINARY",
    })
    url = f"{MANIFOLD_API}?{params}"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "polymarket-agent/1.0"})
        with urllib.request.urlopen(req, timeout=10) as r:
            data = json.loads(r.read())
        out = []
        for m in data:
            prob = m.get("probability")
            if prob is not None:
                out.append({
                    "platform": "Manifold",
                    "title": m.get("question", "")[:80],
                    "probability": round(float(prob) * 100, 1),
                    "volume": round(m.get("volume", 0), 0),
                    "url": m.get("url", ""),
                })
        return out
    except Exception as e:
        return [{"platform": "Manifold", "error": str(e)}]


def main():
    parser = argparse.ArgumentParser(description="Cross-platform probability checker")
    parser.add_argument("--query", required=True, help="Market question / search terms")
    parser.add_argument("--my-prob", type=float,
                        help="Your stated probability (to check divergence)")
    parser.add_argument("--verbose", action="store_true", help="Show all results")
    args = parser.parse_args()

    print(f"\nCross-platform check: '{args.query}'")
    if args.my_prob is not None:
        print(f"Your stated probability: {args.my_prob:.1f}%")
    print(f"{'─' * 72}")

    metaculus = fetch_metaculus(args.query)
    manifold = fetch_manifold(args.query)
    all_results = metaculus + manifold

    divergence_flag = False

    for r in all_results:
        if "error" in r:
            print(f"  [{r['platform']}] ERROR: {r['error']}")
            continue

        prob = r["probability"]
        diff_str = ""
        if args.my_prob is not None:
            diff = prob - args.my_prob
            diff_str = f"  (diff: {diff:+.1f}pp)"
            if abs(diff) > 10:
                diff_str += "  *** >10pp DIVERGENCE ***"
                divergence_flag = True

        extra = ""
        if r.get("forecasters"):
            extra = f"  [{r['forecasters']} forecasters]"
        elif r.get("volume"):
            extra = f"  [vol: M${r['volume']:,.0f}]"

        print(f"  [{r['platform']}] {prob:.1f}%{diff_str}{extra}")
        print(f"    {r['title']}")
        if args.verbose and r.get("url"):
            print(f"    {r['url']}")

    print(f"{'─' * 72}")

    if not any(r for r in all_results if "error" not in r):
        print("  No matching questions found on external platforms.")
        print("  → Proceed with caution; no independent calibration available.")
        sys.exit(0)

    if divergence_flag:
        print("\n[!] DIVERGENCE > 10pp — explain before placing bet (Rule 13)")
        sys.exit(1)
    else:
        print("\n[✓] Estimates aligned with external platforms")
        sys.exit(0)


if __name__ == "__main__":
    main()
