#!/usr/bin/env python3
"""
AI-Trader market-intel + Polymarket signal feed fetcher.

Usage:
  python3 scripts/market_intel.py                  # full macro context
  python3 scripts/market_intel.py --overview        # compact summary only
  python3 scripts/market_intel.py --news macro      # news for one category
  python3 scripts/market_intel.py --news commodities
  python3 scripts/market_intel.py --signals         # polymarket signal feed
  python3 scripts/market_intel.py --all             # everything (scan mode)
"""

import argparse
import json
import sys
from datetime import datetime, timezone

import requests

BASE = "https://ai4trade.ai/api"
TIMEOUT = 10

RELEVANT_NEWS_CATS = ["macro", "commodities"]


def get(path, params=None):
    try:
        r = requests.get(f"{BASE}{path}", params=params, timeout=TIMEOUT)
        r.raise_for_status()
        return r.json()
    except requests.RequestException as e:
        print(f"[market_intel] WARNING: {path} failed: {e}", file=sys.stderr)
        return None


def fmt_overview(d):
    if not d or not d.get("available"):
        return "  [market-intel unavailable]"
    ts = d.get("last_updated_at", "")[:16].replace("T", " ")
    lines = [
        f"  Updated: {ts} UTC",
        f"  Macro:   {d['macro_verdict'].upper()} ({d['macro_bullish_count']}/{d['macro_total_count']} bullish signals)",
        f"           {d.get('macro_summary', '')}",
        f"  ETF:     {d['etf_direction'].upper()} — {d.get('etf_summary', '')}",
        f"  News:    {d['news_status'].upper()} | {d['headline_count']} headlines across {d['active_categories']} categories",
        f"  Latest:  {d.get('latest_headline', '')[:90]}",
    ]
    return "\n".join(lines)


def fmt_macro_signals(d):
    if not d or not d.get("available"):
        return "  [macro signals unavailable]"
    lines = [f"  Regime: {d['verdict'].upper()} ({d['bullish_count']}/{d['total_count']} bullish)"]
    for s in d.get("signals", []):
        icon = "▲" if s["status"] == "bullish" else ("▼" if s["status"] == "defensive" else "→")
        val = f"{s['value']:+.1f}{s.get('unit','')}" if s.get("value") is not None else ""
        lines.append(f"  {icon} {s['label']:<25} {val:<12} {s.get('explanation', '')}")
    return "\n".join(lines)


def fmt_news(d, category):
    if not d:
        return f"  [{category} news unavailable]"
    cats = d.get("categories", [])
    for cat in cats:
        if cat["category"] == category:
            items = cat.get("items", [])
            activity = cat.get("activity_level", "")
            activity_str = f", {activity.upper()}" if activity else ""
            lines = [f"  {cat['label']} ({len(items)} items{activity_str}):"]
            for it in items[:5]:
                sentiment = it.get("overall_sentiment_label", "Neutral")
                icon = "▲" if "Bullish" in sentiment else ("▼" if "Bearish" in sentiment else "→")
                lines.append(f"  {icon} {it['title'][:85]}")
                summary = it.get("summary", "")
                if summary:
                    lines.append(f"    {summary[:120]}")
            return "\n".join(lines)
    return f"  [no {category} data]"


def fmt_signals(d):
    if not d:
        return "  [polymarket signals unavailable]"
    sigs = d.get("signals", [])
    if not sigs:
        return "  [no polymarket signals in feed]"

    # Extract unique market references (token_id or content hints)
    seen = set()
    lines = [f"  {len(sigs)} polymarket signals in feed:"]
    for s in sigs:
        if s.get("agent_name") in seen:
            continue
        seen.add(s.get("agent_name"))
        token = s.get("token_id") or ""
        content = (s.get("title") or s.get("content") or "")[:80]
        side = s.get("side", "").upper() or s.get("signal_type", "")
        lines.append(f"  [{side}] {s.get('agent_name','?')}: {content}")
        if token:
            lines.append(f"         token_id: {token}")
    return "\n".join(lines)


def run_all():
    print("=" * 70)
    print("MARKET INTEL — AI-Trader Context Feed")
    print(f"Fetched: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 70)

    overview = get("/market-intel/overview")
    print("\n## Overview")
    print(fmt_overview(overview))

    macro_sigs = get("/market-intel/macro-signals")
    print("\n## Macro Regime Signals")
    print(fmt_macro_signals(macro_sigs))

    for cat in RELEVANT_NEWS_CATS:
        news = get("/market-intel/news", {"category": cat})
        print(f"\n## {cat.title()} News")
        print(fmt_news(news, cat))

    signals = get("/signals/feed", {"market": "polymarket", "limit": 20})
    print("\n## Polymarket Community Activity")
    print(fmt_signals(signals))

    print("\n" + "=" * 70)


def main():
    parser = argparse.ArgumentParser(description="AI-Trader market intel fetcher")
    parser.add_argument("--overview", action="store_true")
    parser.add_argument("--news", metavar="CATEGORY")
    parser.add_argument("--signals", action="store_true")
    parser.add_argument("--macro", action="store_true")
    parser.add_argument("--all", dest="all_", action="store_true")
    args = parser.parse_args()

    if args.all_ or not any([args.overview, args.news, args.signals, args.macro]):
        run_all()
        return

    if args.overview:
        d = get("/market-intel/overview")
        print(fmt_overview(d))

    if args.macro:
        d = get("/market-intel/macro-signals")
        print(fmt_macro_signals(d))

    if args.news:
        d = get("/market-intel/news", {"category": args.news})
        print(fmt_news(d, args.news))

    if args.signals:
        d = get("/signals/feed", {"market": "polymarket", "limit": 20})
        print(fmt_signals(d))


if __name__ == "__main__":
    main()
