#!/usr/bin/env python3
"""
Kelly criterion position sizer for binary Polymarket bets.

Usage:
  python3 kelly.py --fair-value 55 --market-price 40 --confidence medium --bankroll 9650
  python3 kelly.py --edge 15 --market-price 40 --confidence medium --bankroll 9650
"""

import argparse
import sys

# Confidence-to-Kelly-fraction mapping
CONFIDENCE_FRACTIONS = {
    "high": 1 / 4,    # 1/4 Kelly
    "medium": 1 / 6,  # 1/6 Kelly
    "low": 1 / 10,    # 1/10 Kelly
}

MAX_BET_FRACTION = 0.05   # 5% hard cap
MIN_EDGE_PP = 4.0         # Minimum edge to consider betting


def kelly_bet(fair_value_pct, market_price_pct, confidence, bankroll):
    """
    Compute Kelly-optimal bet size.

    Returns a dict with action, sizing, and EV.
    """
    p = fair_value_pct / 100.0       # your win probability
    q = 1.0 - p
    mp = market_price_pct / 100.0    # cost per share
    edge_pp = fair_value_pct - market_price_pct

    if edge_pp < MIN_EDGE_PP:
        return {
            "action": "PASS",
            "reason": f"Edge {edge_pp:.1f}pp is below {MIN_EDGE_PP}pp minimum threshold",
            "edge_pp": edge_pp,
            "recommended_size": 0.0,
            "max_size": 0.0,
            "expected_value": 0.0,
        }

    if mp <= 0 or mp >= 1:
        return {
            "action": "PASS",
            "reason": f"Invalid market price {market_price_pct:.1f}% — market near resolution",
            "edge_pp": edge_pp,
            "recommended_size": 0.0,
            "max_size": 0.0,
            "expected_value": 0.0,
        }

    # Net odds: for YES bet at price mp, win (1/mp - 1) per dollar if YES, lose 1 if NO
    b = (1.0 / mp) - 1.0
    full_kelly = (b * p - q) / b

    if full_kelly <= 0:
        return {
            "action": "PASS",
            "reason": f"Negative Kelly ({full_kelly:.4f}) — stated edge doesn't survive odds math",
            "edge_pp": edge_pp,
            "recommended_size": 0.0,
            "max_size": 0.0,
            "expected_value": 0.0,
        }

    fraction = CONFIDENCE_FRACTIONS.get(confidence, 1 / 6)
    fractional_kelly = full_kelly * fraction
    max_fraction = min(fractional_kelly, MAX_BET_FRACTION)

    recommended = bankroll * max_fraction
    # Round to nearest $10 for cleanliness
    recommended = round(recommended / 10) * 10
    recommended = max(10.0, min(recommended, bankroll * MAX_BET_FRACTION))

    max_size = bankroll * MAX_BET_FRACTION

    # Expected value per dollar staked
    ev_per_dollar = p * b - q          # = p*(1/mp - 1) - q*(1) = p/mp - 1
    expected_value = ev_per_dollar * recommended

    return {
        "action": "BET",
        "edge_pp": edge_pp,
        "full_kelly_pct": full_kelly * 100,
        "fractional_kelly_pct": fractional_kelly * 100,
        "confidence_label": confidence,
        "confidence_fraction": f"1/{round(1 / fraction)}",
        "recommended_size": recommended,
        "recommended_pct": (recommended / bankroll) * 100,
        "max_size": max_size,
        "expected_value": expected_value,
        "ev_per_dollar": ev_per_dollar,
    }


def main():
    parser = argparse.ArgumentParser(description="Kelly criterion position sizer")
    parser.add_argument("--fair-value", type=float, help="Your probability estimate (0–100)")
    parser.add_argument("--market-price", type=float, required=True, help="Current market price (0–100)")
    parser.add_argument("--edge", type=float, help="Edge in pp (alternative to --fair-value)")
    parser.add_argument("--confidence", choices=["low", "medium", "high"], default="medium")
    parser.add_argument("--bankroll", type=float, default=10000.0)
    args = parser.parse_args()

    if args.fair_value is None and args.edge is None:
        print("ERROR: provide either --fair-value or --edge", file=sys.stderr)
        sys.exit(1)

    fair_value = args.fair_value if args.fair_value is not None else (args.market_price + args.edge)
    result = kelly_bet(fair_value, args.market_price, args.confidence, args.bankroll)

    print(f"\n{'=' * 52}")
    print(f"  KELLY POSITION SIZER")
    print(f"{'=' * 52}")
    print(f"  Fair value:      {fair_value:.1f}%")
    print(f"  Market price:    {args.market_price:.1f}%")
    print(f"  Edge:            {result['edge_pp']:+.1f}pp")
    print(f"  Confidence:      {args.confidence}")
    print(f"  Bankroll:        ${args.bankroll:,.2f}")
    print(f"{'─' * 52}")

    if result["action"] == "PASS":
        print(f"  ACTION:  PASS")
        print(f"  Reason:  {result['reason']}")
    else:
        full_k_dollar = args.bankroll * result["full_kelly_pct"] / 100
        print(f"  ACTION:  BET")
        print(f"  Full Kelly:      {result['full_kelly_pct']:.1f}% (${full_k_dollar:,.0f})")
        print(f"  Fractional ({result['confidence_fraction']}): {result['fractional_kelly_pct']:.1f}%")
        print(f"  ─────────────────────────────────────────────")
        print(f"  RECOMMENDED:     ${result['recommended_size']:,.0f}  ({result['recommended_pct']:.1f}% of bankroll)")
        print(f"  Max allowed:     ${result['max_size']:,.0f}  (5.0% hard cap)")
        print(f"  Expected value:  ${result['expected_value']:+,.2f}")
        print(f"  EV per $1:       ${result['ev_per_dollar']:+.4f}")

    print(f"{'=' * 52}\n")


if __name__ == "__main__":
    main()
