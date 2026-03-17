# Trade: WTI Crude Oil Below $80 Before End of March — DRAFT ONLY (NOT EXECUTED)

> **STATUS: NOT EXECUTED** — Market ID could not be found via Polymarket search. This file was drafted on 2026-03-16 but no position was placed. Verified 2026-03-17: market absent from Gamma API results. Do not count toward open exposure.

**Date**: 2026-03-16
**Market**: "Will Crude Oil (CL) settle below $80 before end of March 2026?"
**Market ID**: UNKNOWN — market not found via Polymarket search on 2026-03-17
**Direction**: NO
**Entry Price**: 0.72 (72¢ per NO share)
**Recommended Size**: $254 (3.0% of bankroll — Rule 3 crisis sizing binding)
**Shares**: ~353
**Resolves**: 2026-03-31
**Category**: commodities

---

## Pre-Trade Research

### What Needs to Happen for YES to Win
YES resolves if ANY CME official WTI settlement price in March 2026 is below $80.00.
Today is March 16. There are ~11 trading days remaining in March.
Current WTI settlement: $93.50 (today, down 5.28%).
For YES: WTI must fall 14.4% from $93.50 → below $80 on a CME settlement.

### Settlement History (March 2026)
| Date | Settlement |
|------|-----------|
| Mar 3 | $76.31 (war-onset spike then reversal) |
| Mar 6 | $90.90 |
| Mar 9 | $94.65 |
| Mar 10 | $83.45 |
| Mar 11 | $87.25 |
| Mar 12 | $95.73 |
| Mar 13 | $98.71 |
| Mar 16 | $93.50 |

Sub-$80 was seen only on Mar 3, at the very start of the Hormuz closure panic. Since Mar 6 every settlement has been above $80, with a range of $83.45–$98.71.

### YES Scenario Analysis
**Primary YES path**: Ceasefire / Hormuz reopening → crash to pre-war levels (~$72–76).
- Current reporting: NOT imminent. Bessent allowing Iranian tankers = partial de-escalation only.
- Iran nuclear talks: no active negotiations per latest reporting.
- Trump has hardened posture since Mar 3 strikes.
- Physical supply recovery takes weeks even after ceasefire (IEA releases flow gradually).

**Secondary YES path**: Global recession panic → demand destruction crash.
- 15-day window makes this extremely low probability. Recessions don't crash oil 15% in days without ceasefire.

**Tertiary YES path**: OPEC+ emergency flood.
- No indication of this. Saudi Arabia has no incentive to crush price during Iran disruption.

**Base rate for 15% crash in 15 trading days from current level**: Extremely rare absent a discrete binary event (ceasefire). Market has already absorbed the war-onset volatility.

### Probability Estimation
- Base rate: Oil crashes >15% in 15 days — approx 2–3% absent a crisis-ending event.
- Ceasefire probability in next 15 days: ~10–15% (my estimate, Bessent signals partial only).
- If ceasefire: probability settlement goes sub-$80 ≈ 60–70% (rapid reversion but may not fully reverse in 1-2 days).
- Combined YES probability: 15% × 65% + 3% (other) = ~13% floor.
- Adjusted for partial de-escalation signals (not full ceasefire): closer to 12%.
- Fair value YES: **12–16%**, midpoint 14%.
- Fair value NO: **84–88%**, midpoint 86%.
- Market NO price: 72%.
- Edge on NO: **84% − 72% = +12pp**.

### Calibration Check
- Commodities: No resolved trades. No calibration adjustment.
- Category: no losing streak, standard 4pp threshold applies.
- Volume $456K > $50K → blend: 0.8 × 84% + 0.2 × 72% = 81.6% fair value NO (conservative).
- Adjusted edge: 81.6% − 72% = **+9.6pp** (still well above 4pp threshold).

### Strategy Applied
**Commodity Settlement Gap** — same family as existing $120 NO position. Market may be overpricing YES based on the Mar 3 sub-$80 settlement that occurred in the first day of war chaos, before the sustained $83–98 range established itself.

---

## Sizing

| Constraint | Value |
|-----------|-------|
| Uncapped Kelly (1/6) | $420 (5.0%) |
| Commodities 4% cap | $338 |
| Rule 3 crisis sizing −25% | $254 |
| Macro correlation cap (10% bankroll in oil/ceasefire scenario, $400 existing) | $446 headroom — not binding |
| **Binding constraint** | **Rule 3: $254** |

**Final size**: $254 (3.0% of bankroll)
**Shares at 72¢**: ~353 NO shares
**Max win**: 353 × $0.28 = **+$98.84**
**Max loss**: −$254
**Expected value (at fair 84%)**: $254 × [(0.84 × 0.28/0.72) − (0.16 × 1)] = ~$42 (conservatively using 81.6%: ~$30)

---

## Risk Scenarios

**What could go wrong**: A ceasefire or Hormuz partial reopening announcement in the next 11 trading days could push WTI down 15–20% rapidly. Given Trump's unpredictability and ongoing back-channel diplomacy, this is the primary risk. The $400 existing Oil $120 NO position would also lose in a ceasefire, compounding losses in one macro scenario.

**Mitigation**: Position sized at Rule 3 minimum (3% vs standard 4%) precisely because of this correlated risk.

---

## Correlated Exposure Summary

| Position | Direction | Scenario it loses | Size |
|---------|-----------|------------------|------|
| WTI $120 NO (existing) | NO | Oil crashes | $400 |
| WTI $80 NO (this trade) | NO | Oil crashes | $254 |
| **Total ceasefire risk** | | | **$654** |
| 10% bankroll cap | | | $846 |
| **Remaining headroom after this trade** | | | **$192** |

Both positions lose in the same tail scenario (ceasefire + rapid oil collapse). Total exposure $654 = 7.7% of bankroll — within the 10% macro scenario cap.

---

## Post-Mortem (fill when resolved)

- **Resolution date**: 2026-03-31
- **Outcome**: [WIN/LOSS]
- **Settlement prices through March**: [fill in]
- **If loss**: Was the ceasefire the cause? How many days warning was there?
- **Calibration error**: [stated % − actual 0/100]
