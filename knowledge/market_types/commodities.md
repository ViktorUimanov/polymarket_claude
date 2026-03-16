# Commodities Markets — Knowledge Base

## Category Profile

| Attribute | Value |
|-----------|-------|
| Variance level | HIGH (geopolitical shock risk) |
| Calibration status | No data (4 open trades) |
| Max position size | 4% bankroll |
| Min edge required | 4pp (standard) |
| Current focus | WTI crude oil (Iran war premium) |

---

## Rules (Apply Before Every Commodities Bet)

### Rule 1 — Settlement Price ≠ Intraday Price (CRITICAL)
**Date learned**: 2026-03-15
**Rule**: Always research which price mechanism Polymarket uses for resolution. For WTI crude oil, Polymarket uses CME OFFICIAL SETTLEMENT price, NOT the intraday high/low.
**Why**: March 9, 2026: WTI intraday high = $119.94, but CME settlement = $94.65 (−21% gap). If you price binary targets off intraday data, you will massively overestimate the probability of hitting round-number thresholds.
**Apply when**: Any oil market (or any commodity) where the resolution says "settles at X" or "WTI settlement price."
**Settlement mechanics**: Settlement = volume-weighted average near market close. Professional sellers sell into intraday spikes, pulling settlement below intraday high.

### Rule 2 — Know Which Benchmark (WTI vs Brent)
**Date learned**: 2026-03-15
**Rule**: Polymarket oil markets typically use WTI (NYMEX). Brent trades at a premium of $4–7 typically. Do not use Brent prices to estimate WTI resolution probability.
**Apply when**: Any crude oil binary market.
**Data source**: CME Group WTI settlement history (free on CME website or Bloomberg).

### Rule 3 — Check Geopolitical Context Before Sizing
**Date learned**: 2026-03-15
**Rule**: During active geopolitical crises (Hormuz closure, OPEC+ emergency meetings, strategic reserve releases), oil markets have extreme volatility AND mean-reversion risk. Size down 25% from standard Kelly for any position opened during a crisis spike.
**Apply when**: Oil price is >25% above its 30-day average.

### Rule 4 — Monitor Resolution Date vs Geopolitical Timeline
**Rule**: For monthly binary targets (e.g., "WTI ≥ $100 before end of March"), monitor the geopolitical situation daily. A ceasefire or diplomatic breakthrough can move the price by 15–20% overnight, converting a near-certain WIN to a LOSS.
**Current risk**: Iran-US ceasefire risk exists while Hormuz remains closed.

---

## WTI Crude Oil — March 2026 Context

### Key Facts
- **Cause of surge**: US/Israel struck Iran nuclear sites Feb 28, 2026. Iran closed Strait of Hormuz (~20% global supply). WTI surged ~35% in one week.
- **Settlement price history**:
  - Mar 3: $76.31
  - Mar 6: $90.90 (biggest weekly gain in WTI futures history)
  - Mar 9: $94.65 (intraday hit $119.94)
  - Mar 10: $83.45 (−11.8% reversal)
  - Mar 11: $87.25
  - Mar 12: $95.73
  - Mar 13: $98.71

### Open Positions (as of 2026-03-15)
- Oil ≥ $100 YES at 88.8¢ ($300) — gap was $1.29 on Mar 15
- Oil ≥ $120 NO at 54.0¢ ($400) — requires 21.5% more gain from Mar 15 level

### Key Catalysts to Monitor
- Trump statements on Iran military operations
- IEA emergency stock release decision
- Saudi Arabia diplomatic outreach to Iran
- Iran nuclear talks progress
- Kharg Island port security
- OPEC+ emergency meeting call

---

## Commodity Edge Sources

| Signal | Type | Reliability |
|--------|------|------------|
| Settlement < intraday gap > 15% | NO bias on round-number targets | THEORETICAL (untested) |
| Ceasefire imminent → crash risk | Scenario risk | HIGH — monitor daily |
| IEA release announced → crash | Scenario risk | HIGH — usually −10–15% |
| Brent already > X → WTI approaching | Leading indicator | MEDIUM (5-7 day lag) |

---

## Calibration History

| Date | Market | Stated % | Outcome | Error |
|------|--------|----------|---------|-------|
| 2026-03-15 | Oil $100 YES | 91% | OPEN | — |
| 2026-03-15 | Oil $120 NO | 62% | OPEN | — |

No resolved trades yet. Update when oil markets close end of March 2026.
