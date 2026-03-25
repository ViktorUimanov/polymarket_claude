# Trade: Scottie Scheffler — 2026 Masters Winner YES

**Date**: 2026-03-17
**Market ID**: 568629
**Question**: Will Scottie Scheffler win the 2026 Masters Tournament?
**Direction**: YES
**Market price at entry**: 17.5¢
**Planned size**: $140
**Resolves**: 2026-04-13 (Masters April 9–12)

---

## Decision Tree

**Does YES require anything unusual?**
- YES requires Scheffler to win a 72-hole golf tournament at Augusta National. No abnormal resolution criteria.

**Resolution criteria**: Standard — whoever wins the Masters earns YES.

---

## Research Summary

**Market**: Scottie Scheffler Masters 2026 YES at 17.5¢
**Sportsbook consensus**: BetMGM +300 (25.0% implied), FanDuel +430 (18.9% implied), DraftKings +350 (22.2% implied)
**Fair value estimate**: 22–27% YES, midpoint 24.5%
**Edge**: +7.0pp (17.5% market vs 24.5% fair value)

**Bull case for Scheffler YES:**
- World #1 ranking by clear margin — dominant 2025 season (6 PGA Tour wins)
- Four consecutive top-10 finishes at Augusta National
- Defending champion / favorite status historically correlates with performance
- Augusta National suits his game: long, precise iron play, putting strength
- Consistent across multiple sportsbook lines at 22–25% implied — Polymarket at clear discount

**Bear case:**
- Golf is inherently high-variance — 80+ players, any could win
- Top-tier field: Rory McIlroy, Jon Rahm, Collin Morikawa all competitive
- Scheffler hasn't won the Masters before (no defending champion benefit from prior wins)
- Only 23 days until tournament — injury or form dip possible

**Calibration check:**
- `sports` category: 0 resolved trades, no overconfidence recorded
- `oscars/awards` overconfidence is a separate category — does NOT apply here
- Using 1/6 Kelly for medium confidence

---

## Kelly Calculation

```
Fair value: 24.5%
Market price: 17.5%
Edge: +7.0pp
Confidence: medium
Bankroll: $9,664
Full Kelly: 8.5% ($820)
1/6 Kelly: 1.4% ($140)
Max allowed (2% single-event sports): $193
```

**Position size: $140** (1.4% bankroll, within 2% single-event cap)

---

## Category Rules Applied

Per `knowledge/market_types/sports.md`:
- Rule 1: Season-long market vs single-event — this is a single tournament (4-day event). Use 2% cap.
- Rule 2: Check sportsbook signal — confirmed: multiple books at 19–25%. Polymarket at 17.5% = discount.
- Rule 13 (README): Cross-platform check done. Sportsbook gap confirmed.

---

## Risk Flags

- **Injury risk**: 23 days to tournament. If Scheffler withdraws, position goes to 0. LOW probability.
- **Form risk**: If Scheffler plays poorly in warmup events, market may drop further (opportunity to add). MONITOR.
- **High-variance event**: Even at 24.5% fair value, 75.5% chance of losing this bet. Size accordingly.

---

## Exit Plan

- **Hold to resolution** (April 13). This is a tournament bet — no mid-tournament exit mechanism on Polymarket.
- **Post-mortem**: Write immediately after resolution, regardless of outcome.
- **If Scheffler withdraws before Masters**: Seek exit at market price immediately.

---

## Expected Value

At $140 bet:
- Win (24.5% prob): profit = $140 * (1 - 0.175) / 0.175 = $140 * 4.71 = $660
- Loss (75.5% prob): lose $140
- EV = 0.245 * $660 - 0.755 * $140 = $161.70 - $105.70 = **+$56.00**
