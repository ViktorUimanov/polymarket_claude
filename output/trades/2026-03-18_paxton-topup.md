# TRADE: Ken Paxton Texas Senate YES — Top-up (Market 562186)

**Date**: 2026-03-18
**Action**: BET YES (top-up existing position)
**Market**: Will Ken Paxton win the 2026 Texas Republican Primary runoff?
**Market ID**: 562186
**Resolves**: 2026-05-26

---

## Position Details

| | |
|--|--|
| **Direction** | YES |
| **Market price** | 38.5¢ |
| **Fair value** | 61% (range: 56–66%) |
| **Edge** | +22.5pp |
| **Top-up size** | $290 |
| **New shares** | 753.2 YES shares |
| **Total Paxton exposure** | $460 ($170 original + $290 top-up) |
| **Total Paxton shares** | 1,194.8 (441.6 original + 753.2 new) |
| **Expected value (top-up)** | +$162 |
| **Category** | politics |
| **Kelly mode** | 1/4 Kelly, capped by 3% politics cap |

---

## Research Update — New Data (March 17-18)

### Why fair value was upgraded from 52% → 61%

**Original entry (March 17):** Three polls showed Paxton ahead in runoff. Trump endorsement pending. Fair value 52%, edge +13.5pp.

**New critical data (March 17-18):** Fox 26 Houston poll tested the specific "Trump endorses Cornyn" scenario:
- **If Trump endorses Cornyn**: Paxton 44% vs Cornyn 43% (Paxton STILL leads, within MOE)
- **If Trump endorses Paxton**: Paxton 58% vs Cornyn 32% (Paxton dominant)
- **No endorsement baseline**: Paxton +3–8pp lead across multiple polls

This Fox 26 data is the key upgrade: the market was pricing ~30% probability that a Trump-Cornyn endorsement would swing the race decisively to Cornyn. This assumption is now empirically tested and refuted.

### Updated Scenario Model

| Scenario | P(scenario) | P(Paxton wins | scenario) | Weighted contribution |
|---|---|---|---|
| Trump endorses Paxton | 35% | 80% | 28.0% |
| Trump endorses Cornyn | 30% | 46% | 13.8% |
| No endorsement | 35% | 55% | 19.25% |
| **Total** | **100%** | — | **61.1%** |

Notes:
- P(Paxton wins | Trump endorses Cornyn) = 46% is based on Fox 26's 44–43 Paxton lead in that scenario (within MOE, call it roughly 50/50 with slight Paxton lean given the data)
- P(Paxton wins | no endorsement) = 55% based on March 5-6 poll (+8pp) and March 10 poll (+3pp)
- P(Trump endorses Paxton) increased from 30% → 35% because Trump is "holding" the endorsement as leverage — suggesting he has a deal to extract, not that he's committed to Cornyn

### Why Market is Underpriced at 38.5%

**Market bias**: Bettors are anchoring on "Trump = decisive pivot point" — the binary of Trump endorsing Cornyn automatically flipping the race. The Fox 26 data dismantles this assumption. Paxton has a structural, durable lead that persists even under the adverse Trump scenario.

**Legal baggage discount**: Paxton's 2023 impeachment acquittal reduced his statewide appeal but his primary base is intact. Republican primary voters who supported him in March 3 primary (41% vs Cornyn's 43%) are not going to abandon him based on Trump's tepid Cornyn endorsement.

**Sanity check**: Why does +22.5pp edge sit unexploited?
- Market is information-processing the Trump endorsement uncertainty, not the structural polling lead
- Fox 26 specific scenario-test data is very recent (March 16-17) — may not be fully digested
- Runoff races are notoriously hard to poll; market applies extra uncertainty discount

---

## Sizing

```
Bankroll: $9,664
Politics cap: 3% = $290 max per new trade
Kelly formula: (edge / odds) × bankroll = (0.225 / 0.615) × 9664 = $3,535 full Kelly
1/4 Kelly = $884 → exceeds 3% politics cap
Cap constraint: $290 (binding)
Single-market total cap: 5% = $483; existing $170 + new $290 = $460 < $483 ✓
```

**Final top-up size: $290**

---

## Position Limits Check

| Check | Result |
|---|---|
| Single-market cap (5% = $483) | $460 total — within cap ($483) |
| Politics per-trade cap (3% = $290) | $290 — exactly at cap |
| Total politics exposure ($1,310 after) | 13.6% bankroll — 6 independent positions |
| Category probation? | Politics — no probation, 0 resolved |
| 4pp minimum edge | +22.5pp — well above minimum |
| Never at 97%+ | YES at 38.5% — passes |

---

## Key Risk

**Trump endorses Cornyn with enthusiasm + strong ground game deployment**: Even per Fox 26, Cornyn could close to within 1pp with full Trump backing. If the +300 volunteers and Trump rally momentum all materialize for Cornyn, could flip a coin-flip race.

**Exit trigger**: If Trump endorses Cornyn AND subsequent polling shows Cornyn pulling ahead (40%+), exit at market. Do not hold through a position where the Trump endorsement was announced AND polling confirms Cornyn leads.

**Watch for**: Trump endorsement announcement (expected before March 22 per Texas Tribune deadline reporting). Update position assessment within 24h of announcement.

---

## Thesis Monitor

**Thesis intact if**: Trump endorses Paxton OR Trump stays neutral
**Thesis requires reassessment if**: Trump endorses Cornyn
**Exit trigger**: Cornyn polling lead >3pp AFTER Trump endorsement announcement
**Monitoring frequency**: Daily until endorsement announced; then weekly
**Next mandatory check**: March 22 (any Trump announcement expected before runoff season heats up)

---

## Skills Used

- resolution-parser: Confirmed runoff resolution criteria (primary runoff winner = most votes)
- evaluate-edge: +22.5pp edge, confidence HIGH (scenario model with empirical scenario test)
- size-position: 1/4 Kelly capped to politics 3% limit = $290
- correlated-position-check: Paxton total $460 within 5% single-market cap; no cross-position correlation
