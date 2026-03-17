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

### Rule 5 — Administration/Treasury Statements Are Tier-1 Price Signals
**Date learned**: 2026-03-16 (WTI $100 YES early exit)
**Rule**: Explicit public statements by the Treasury Secretary or White House projecting specific commodity prices are tier-1 signals. Weight them at ±15pp or more to fair value estimates. Do not discount as posturing or noise.
**Why**: Bessent appeared on CNBC and stated US would allow Iranian oil tankers through Hormuz and projected oil "well below $80." This was an administration-level policy signal, not analyst commentary. WTI settlement fell from $98.71 to $93.50 the same day — a 5.3% one-day drop.
**Apply when**: Any open commodity position where Treasury/White House publicly comments on price trajectory or supply policy.
**Specific sub-rule**: If a Tier-1 statement moves settlement price ≥ 3% in one day, run a fresh thesis check. The gap-to-target has likely widened materially.

### Rule 6 — Gap Trades Require Stable Catalyst + Time Buffer
**Date learned**: 2026-03-16 (WTI $100 YES early exit)
**Rule**: A "gap trade" (entry thesis: "price is $X away from target, needs only Y% more") requires: (a) the fundamental catalyst causing the price spike is stable and unlikely to reverse, AND (b) there is sufficient time remaining for the gap to be closed with margin.
**Why**: Oil $100 YES was entered at 88.8% with a $1.29 gap to target and 11 days remaining. The catalyst (Hormuz closure) proved unstable — Bessent allowed tankers through within 24 hours. The gap widened from $1.29 to $6.50 overnight.
**Apply when**: Any trade where the entry thesis is primarily that a small price gap will be closed within the market window.
**Specific sub-rule**: For gap trades, require the catalyst to have a median expected duration at least 2× the market window remaining.

### Rule 7 — Exit Discipline: Take Profit When Market Price Exceeds Revised Fair Value
**Date learned**: 2026-03-17 (from Trump China exit and WTI $100 YES exit, synthesized as general rule)
**Rule**: For any position that has moved in your favor and the current market price now exceeds your REVISED fair value (after incorporating new information), exit. Do not hold waiting for full resolution if: (a) thesis has changed, AND (b) market has overshot your updated fair value.
**Why**: Trump China YES was entered at 33¢ (fair value 44-47%). After Trump's delay statement, revised fair value dropped to 38-43%. Market moved to 48.5% — exceeding revised fair value. Exiting at 48.5¢ vs fair 40% was a +8.5pp edge in our favor. Holding to expiry would have been negative EV.
**Apply when**: Any position where new information has materially changed the thesis AND the current market price now prices in MORE certainty than your revised estimate.
**Complementary rule**: Do NOT exit when market moves AGAINST you but the fundamental thesis is unchanged. Market noise is not a thesis break. Only thesis breaks and market-exceeding-revised-fair-value trigger exits.

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

### Open Positions (as of 2026-03-17)
- Oil ≥ $100 YES at 88.8¢ ($300) — CLOSED early 2026-03-16 at 72.2¢, loss −$56.10. Bessent allowed Iranian tankers; IEA supply flow began. Thesis broke.
- Oil ≥ $120 NO at 54.0¢ ($400) — open, settlement $93.50 on Mar 16. Need $120 = +28.3% from current. Thesis strong.
- Oil $110 NO at 51.5¢ ($200) — open 2026-03-16, settlement $93.50. Need $110 = +17.6% from current. Thesis strong.

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
| 2026-03-15 | Oil $100 YES | 91% | CLOSED EARLY (thesis break, not resolution) | N/A |
| 2026-03-15 | Oil $120 NO | 62% | OPEN (resolves 2026-03-31) | — |
| 2026-03-16 | Oil $110 NO | 83% | OPEN (resolves 2026-03-31) | — |

No resolved trades yet. Early exit on $100 YES does not count as calibration data (voluntary exit on thesis change, not market resolution). Update when oil markets close end of March 2026.
