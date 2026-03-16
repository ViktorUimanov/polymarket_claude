#!/usr/bin/env python3
"""
Check resolution status of open Polymarket positions.

Usage:
  python3 check_resolutions.py                    # check all positions.json
  python3 check_resolutions.py --market-id <id>   # check specific market
"""

import argparse
import json
import sys
from pathlib import Path

import requests

GAMMA_BASE = "https://gamma-api.polymarket.com"
POSITIONS_FILE = Path("/root/workspace/polymarket/output/positions.json")


def check_market_resolution(market_id):
    """
    Returns: (status, market_data, note)
    status: RESOLVED_YES | RESOLVED_NO | UNRESOLVED | ERROR
    """
    try:
        r = requests.get(f"{GAMMA_BASE}/markets", params={"id": market_id}, timeout=15)
        r.raise_for_status()
        markets = r.json()
    except requests.RequestException as e:
        return "ERROR", None, str(e)

    if not markets:
        return "ERROR", None, f"Market {market_id} not found"

    m = markets[0]

    try:
        prices = json.loads(m.get("outcomePrices") or "[0.5,0.5]")
        yes_price = float(prices[0])
    except Exception:
        return "ERROR", m, "Could not parse outcomePrices"

    # Primary signal: resolved flag
    resolved = m.get("resolved", False)

    if resolved:
        if yes_price >= 0.5:
            return "RESOLVED_YES", m, None
        else:
            return "RESOLVED_NO", m, None

    # Secondary signal: price collapsed to near 0 or 1
    if yes_price >= 0.99:
        return "RESOLVED_YES", m, "Price at 1.0 (likely resolved, resolved flag not set yet)"
    if yes_price <= 0.01:
        return "RESOLVED_NO", m, "Price at 0.0 (likely resolved, resolved flag not set yet)"

    return "UNRESOLVED", m, None


def load_positions():
    if not POSITIONS_FILE.exists():
        return []
    with open(POSITIONS_FILE) as f:
        data = json.load(f)
    return data.get("positions", [])


def compute_pnl(position, status):
    """Compute P&L for a resolved position."""
    entry_price = float(position.get("entry_price", 0))
    size = float(position.get("size", 0))
    direction = position.get("direction", "YES")
    shares = size / entry_price if entry_price > 0 else 0

    if direction == "YES":
        pnl = shares - size if status == "RESOLVED_YES" else -size
    else:  # direction == "NO"
        pnl = shares - size if status == "RESOLVED_NO" else -size

    return pnl, shares


def main():
    parser = argparse.ArgumentParser(description="Check Polymarket position resolutions")
    parser.add_argument("--market-id", help="Check a specific market ID")
    args = parser.parse_args()

    if args.market_id:
        status, market, note = check_market_resolution(args.market_id)
        print(f"Market {args.market_id}: {status}")
        if note:
            print(f"  Note: {note}")
        if market:
            try:
                prices = json.loads(market.get("outcomePrices") or "[0.5,0.5]")
                print(f"  YES: {float(prices[0])*100:.1f}%  NO: {float(prices[1])*100:.1f}%")
                print(f"  Q: {market.get('question')}")
                print(f"  End date: {market.get('endDateIso')}")
            except Exception:
                pass
        return

    # Default: check all positions
    positions = load_positions()
    if not positions:
        print("No open positions found in output/positions.json")
        return

    print(f"Checking {len(positions)} open position(s)...\n")

    results = {
        "resolved_yes": [],
        "resolved_no": [],
        "unresolved": [],
        "errors": [],
    }

    for pos in positions:
        market_id = pos.get("market_id")
        question = pos.get("question", "Unknown")[:55]
        direction = pos.get("direction", "YES")
        size = float(pos.get("size", 0))

        status, market, note = check_market_resolution(market_id)
        pnl, shares = compute_pnl(pos, status) if status in ("RESOLVED_YES", "RESOLVED_NO") else (0, 0)

        if status == "RESOLVED_YES":
            print(f"  WIN  {question}")
            print(f"       Direction: {direction} | P&L: ${pnl:+.2f} | Size: ${size} | Shares: {shares:.1f}")
            if note:
                print(f"       Note: {note}")
            results["resolved_yes"].append({**pos, "pnl": pnl, "status": status})

        elif status == "RESOLVED_NO":
            pnl_sign = "WIN" if (direction == "NO") else "LOSS"
            print(f"  {pnl_sign}  {question}")
            print(f"       Direction: {direction} | P&L: ${pnl:+.2f} | Size: ${size} | Shares: {shares:.1f}")
            if note:
                print(f"       Note: {note}")
            results["resolved_no"].append({**pos, "pnl": pnl, "status": status})

        elif status == "UNRESOLVED":
            print(f"  OPEN {question}")
            results["unresolved"].append(pos)

        else:
            print(f"  ERR  {question}")
            print(f"       Error: {note}")
            results["errors"].append({**pos, "error": note})

        print()

    # Summary
    wins = [p for p in results["resolved_yes"] if p.get("direction") == "YES"] + \
           [p for p in results["resolved_no"] if p.get("direction") == "NO"]
    losses = [p for p in results["resolved_yes"] if p.get("direction") == "NO"] + \
             [p for p in results["resolved_no"] if p.get("direction") == "YES"]

    total_win_pnl = sum(p["pnl"] for p in wins)
    total_loss_pnl = sum(p["pnl"] for p in losses)
    net_pnl = total_win_pnl + total_loss_pnl

    print("=" * 60)
    print(f"Wins:       {len(wins):2d}  (+${total_win_pnl:.2f})")
    print(f"Losses:     {len(losses):2d}  (${total_loss_pnl:.2f})")
    print(f"Unresolved: {len(results['unresolved']):2d}")
    print(f"Errors:     {len(results['errors']):2d}")
    print(f"Net P&L:    ${net_pnl:+.2f}")


if __name__ == "__main__":
    main()
