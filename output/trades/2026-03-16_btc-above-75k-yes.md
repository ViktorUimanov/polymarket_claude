# Trade: Bitcoin Above $75,000 in March 2026 — BET YES

**Date**: 2026-03-16
**Market**: "Will Bitcoin hit above $75,000 in March 2026?"
**Market ID**: UNKNOWN — fetch via `python3 scripts/fetch_markets.py --search "bitcoin 75000" --limit 5`
**Direction**: YES
**Entry Price**: 0.91 (91¢ per YES share)
**Recommended Size**: $254 (3.0% of bankroll — see sizing constraints below)
**Shares**: ~279
**Resolves**: 2026-04-01
**Category**: crypto

---

## Pre-Trade Research

### Resolution Mechanics (CRITICAL — Rule 1 crypto)
YES if ANY Binance BTC/USDT 1-minute candle has a High price >= $75,000 during March 2026.
Key: this uses the **1-minute candle HIGH**, not settlement, not close, not VWAP. This is the most permissive resolution mechanism possible — any momentary tick to $75,000 counts.

### Current State
- BTC price today: $73,882
- Required move: +$1,118 (+1.51%) from current level
- Time remaining: ~15 days (March 16 → March 31)
- BTC just crossed above its 50-day moving average for the first time in 2 months (bullish signal)
- BTC +3% today

### Price Behavior Analysis
BTC at $73,882 needs a 1.51% gain on any 1-minute candle high in 15 days.

**Historical volatility context**:
- BTC moves 1–3% intraday on a regular trading day
- 15-day window contains ~21,600 one-minute candles (15 × 24 × 60)
- Each candle's HIGH is always above the open/close by the full candle range
- A 1.5% move over 15 days in BTC is an extremely low bar — this is essentially asking whether BTC will have a single moment above $75k at any point in two weeks

**Bearish factors**:
- Iran war geopolitical risk-off environment suppresses crypto
- BTC has been below $75k for at least 2 months per the 50-day MA context
- Risk assets generally underperform during active military conflicts

**Bullish factors**:
- BTC +3% today, breaking above 50-day MA (momentum signal)
- Distance to target is only 1.5%
- Any brief speculative spike would suffice — not requiring sustained hold
- Post-halving cycle: BTC halvings occurred ~April 2024, historically bullish 12–24 months later
- Institutional accumulation patterns in post-halving bull phases

### Probability Estimation
- Base rate: BTC moves +1.5% on at least 1 candle in 15 days — historically close to certainty for a normal market environment.
- Risk-off dampening: Even during risk-off environments, BTC regularly oscillates 2–5% daily.
- Scenario where NO wins: BTC would need to drift down from $73,882 AND never tick above $75,000 on any single 1-minute candle for 15 straight days. This requires sustained downward drift with no relief rallies.
  - This scenario requires BTC to: (a) trend below $75k for 15 days while (b) never having a single 1-minute candle touching $75k during any of those 21,600 candles.
- The market at 91% is pricing this as somewhat uncertain. My estimate: **96–98% probability YES**.
- Conservative estimate using risk-off discount: **95–97%**.
- Midpoint fair value: **96%**.

**Volume blend** ($47.5M >> $50K threshold):
0.8 × 96% + 0.2 × 91% = **95.0% fair value YES**

**Edge**: 95% − 91% = **+4pp minimum** (at conservative end) / **+6pp** at midpoint.

### Calibration Check
- Crypto: No resolved trades. No calibration adjustment needed.
- No losing streak in crypto.
- Minimum edge for crypto: **5pp** (knowledge/market_types/crypto.md Rule — higher threshold due to variance).
- Edge at conservative fair value (95%): +4pp — BELOW the 5pp crypto minimum.
- Edge at midpoint fair value (96%): +5pp — meets the crypto threshold exactly.
- Edge at upper bound (97%): +6pp — comfortable above threshold.

**The 5pp minimum is met only if fair value is >= 96%. Confidence is MEDIUM given the risk-off environment creating genuine uncertainty.**

### Rule 2 Check (crypto.md — Macro Correlation During Risk-Off)
Rule 2 states: "Don't bet bullish crypto during geopolitical crises unless specifically crypto-positive news."
- Current situation: Active Iran war = geopolitical crisis
- BUT: The required move is only 1.5%, and the resolution uses the most permissive mechanism (any 1-min candle High)
- Counterpoint: This is not a sustained price level bet — it's a near-certainty of any momentary touch
- Ruling: Rule 2 applies to directional trend bets (e.g., "BTC above $100k"). A "will it ever touch" bet from 1.5% below with 15 days remaining is different in kind — it's more of a tail probability bet on the NO side being wrong.
- Risk-off does meaningfully increase the probability of NO. I apply a +5pp discount to my fair value: 96% → 91%.

**With Risk-Off Discount Applied**:
- Fair value: 91% (after risk-off discount from 96%)
- Market: 91%
- Edge: **0pp**

This is the critical finding. Once I apply the crypto Rule 2 risk-off discount, the edge evaporates.

---

## Decision: PASS

**Reason**: After applying the crypto knowledge Rule 2 (risk-off geopolitical environment penalty), the fair value of 96% compresses to ~91% — exactly at market price. Edge = 0pp. The minimum required edge for crypto is 5pp. This does not meet the minimum threshold.

The 5pp minimum edge is NOT met even before the risk-off discount. At conservative fair value (95%), edge is only +4pp, below the 5pp crypto floor. At midpoint (96%), edge is exactly +5pp — borderline and confidence is only medium. The risk-off correction eliminates the remaining edge.

**Alternative framing**: The market at 91% is NOT obviously wrong here. BTC has been below $75k for 2+ months. The Iran war is actively suppressing risk assets. A sophisticated market at $47.5M volume has already priced this. The edge source (momentum + 1-min candle resolution leniency) does not clearly outweigh the risk-off premium already embedded in the market.

---

## Sizing (for reference — not executed)

| Constraint | Value |
|-----------|-------|
| Crypto max position | 3% = $254 |
| Kelly 1/6 at 6pp edge | $420 (capped to $254) |
| Risk-off correction | Eliminates edge |
| **Final size** | **PASS — $0** |

---

## What Would Change My Mind

If BTC surges further today or tomorrow, widening the gap below $75k, the market YES price will rise above 91%, and the edge disappears entirely. Conversely, if BTC pulls back to $71k–72k and the market price drops to 85–87%, the edge re-emerges to 8–10pp and would be actionable (even with risk-off discount).

Monitor: if market price drops to <= 87%, re-evaluate with fresh research.

---

## Calibration Note
This PASS should be logged as research performed, not as a calibration data point.
