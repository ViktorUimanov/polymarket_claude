---
name: calibration-check
description: How to check historical calibration before placing a bet and adjust confidence/sizing accordingly
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Calibration Check Skill

## What Is Calibration?

When you say a market is 75% likely YES, you should win ~75% of those bets over time.
Calibration error = actual_win_rate% - average_stated_probability%

- **Positive error** (+10pp): you're winning more than expected — underconfident, can size up
- **Zero error**: perfectly calibrated
- **Negative error** (-15pp): you're winning less than expected — overconfident, reduce size and require higher edge

## Quick Check (Run Before Every Bet)

```bash
# All categories
python3 /root/workspace/polymarket/scripts/calibration.py --summary

# Specific category
python3 /root/workspace/polymarket/scripts/calibration.py --category oscars
python3 /root/workspace/polymarket/scripts/calibration.py --category sports
python3 /root/workspace/polymarket/scripts/calibration.py --category commodities

# Last 10 trades only (recency-weighted)
python3 /root/workspace/polymarket/scripts/calibration.py --category sports --last-n 10
```

## Interpreting Output

```
Category: oscars  | Trades: 3 | Win%: 0% | Avg Stated: 24% | Error: -24pp
```
→ **Severely overconfident on Oscars**. Require +10pp edge, -50% size. Max 1% bankroll.

```
Category: commodities | Trades: 5 | Win%: 80% | Avg Stated: 75% | Error: +5pp
```
→ **Well calibrated on commodities**. No adjustment needed.

## Adjustment Table

| Calibration Error | Required Min Edge | Size Adjustment |
|-------------------|-----------------|----------------|
| > +20pp | 4pp (standard) | Can size up slightly |
| +10 to +20pp | 4pp (standard) | Standard sizing |
| -10 to +10pp | 4pp (standard) | Standard sizing |
| -10 to -20pp | 6pp minimum | -25% from Kelly |
| -20 to -30pp | 8pp minimum | -50% from Kelly |
| < -30pp | 10pp minimum | Max 1% bankroll |

## Caveats

- **< 5 trades in a category**: calibration stats are noisy — use category defaults from `knowledge/market_types/<cat>.md`
- **Recency matters**: weight the last 10 trades more than all-time stats
- **Don't over-correct**: if you correct too aggressively, you create a new calibration error in the opposite direction
- **Categories are independent**: good calibration on sports doesn't help you on Oscars

## Calibration History Pattern Recognition

After 10+ trades in a category, check if there's a systematic bias:

- Always overestimate when the favorite is heavy? → You're not accounting for tail risk enough
- Always underestimate in close markets? → You're anchoring on market price too much
- Perfect calibration at 60-70% but poor at 80-90%? → You have a high-confidence overconfidence bias

Document patterns in `knowledge/market_types/<category>.md`.
