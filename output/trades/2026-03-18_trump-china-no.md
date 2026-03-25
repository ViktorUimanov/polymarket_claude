# Trade: Will Trump visit China by April 30, 2026? — BET NO

**Date**: 2026-03-18
**Market ID**: 706279
**Direction**: NO (buying NO shares)
**Entry price**: 60.5¢ (NO)
**Shares**: ~247.9 ($150 / $0.605)
**Size**: $150
**Bankroll at entry**: $9,664
**Size as % bankroll**: 1.55%

---

## Resolution Criteria

Trump must physically enter mainland China by April 30, 2026, 11:59 PM ET. Does not include Hong Kong or Taiwan. Requires actual visit — not just diplomatic contacts.

---

## Pre-Trade Reasoning

### Context: Prior Position

We held a YES position on this market (market ID 706279, entry 33.0¢, 454.5 shares, $150 size). On 2026-03-17, Trump made an on-record statement requesting China delay the visit by "a month or so." Per Rule 8 (Principal Actor Statement), we exited immediately at 48.5¢ for +$70.40 profit. The market has since corrected to 39.5% YES (60.5% NO) but may still be overpriced.

This trade is a NEW position (NO direction), not a continuation of the prior YES.

### Probability Estimation

**Base rate**: When a US president publicly announces a trip delay citing an ongoing military conflict, visit occurs within the originally scheduled window ~20-25% of the time. Base rate YES: 25%.

**Bayesian updates:**

1. Trump explicit statement March 17: "5 or 6 weeks" delay. 5 weeks = April 21, 6 weeks = April 28. Window closes April 30. Even the optimistic timeline leaves a 2-day margin. Strong bearish signal: -8pp → YES: 17%.

2. Stated reason = Iran war. Iran FM explicitly rejected ceasefire as of March 17. Both sides holding maximalist positions. The stated obstacle is not temporary or resolvable within 6 weeks. Moderate bearish signal: -3pp → YES: 14%.

3. Trump: "not ready to make a deal." Visit is substantive (deal-oriented), not symbolic. Without agreeable terms, motivation to visit is low. Weak-moderate bearish signal: -2pp → YES: 12%.

**Raw estimate: 12% YES**

**Market blend (volume $1.67M >> $50k threshold, blend at 20%)**:
0.12 × 0.8 + 0.395 × 0.2 = 0.096 + 0.079 = **17.5% YES**

**Uncertainty penalty**: Geopolitical travel schedules — moderate variance. Widen CI by 10pp.
Range: 10-30% YES. Midpoint: 20% YES.

**Final point estimate: 25% YES (75% NO)**

The research notes suggest 25-32% YES. My independent estimate converges at the conservative end of that range. Using 75% NO (25% YES) as central fair value.

**90% confidence interval: 15-35% YES (65-85% NO)**

### Edge Calculation

- Fair value: 75% NO
- Market price: 60.5% NO
- Edge: **+14.5pp** (central estimate)
- Conservative edge (fair value 68% NO): +7.5pp
- Both estimates exceed the 5pp politics minimum and 4pp universal floor.

### Applicable Rules and Strategies

**Rule 8 — Principal Statements Override Secondary Sources**: Trump's on-record "month or so" delay request is a tier-1 signal. Bessent denied it — we correctly ignored the denial when we exited YES at +$70.40. Same logic applies: Trump's own statement anchors fair value well below market price.

**Rule 2 — Status Quo Inertia**: Markets overestimate dramatic short-term change. "Leader visits adversarial nation under active military conflict they are conducting" is a dramatic departure from status quo. Status quo (no visit by April 30) wins ~70-75% of the time in comparable scenarios.

**Strategy applied**: Geopolitical Status Quo Bias (TESTING — 4 active trades, 0 resolved). This is consistent with the strategy's signal: "dramatic change by X" where key actors have explicitly deferred/rejected the change, market prices change at >15%.

This is also a follow-on from Edge Source 6 (Principal Actor Statement — confirmed WIN with +$70.40). The same statement that caused us to exit YES now supports entering NO.

### Correlation Risk Analysis

**Critical concern**: Trump's stated reason for delaying is the Iran war. The three existing Iran NO positions (ceasefire April 30, regime fall June, regime fall 2027) share a tail risk: a surprise ceasefire or diplomatic breakthrough. That SAME tail risk would remove the obstacle for Trump's China visit, potentially driving this market back toward YES.

**Assessment of correlation**:
- Iran ceasefire NO ($200) + Iran regime June NO ($200) + Iran regime 2027 NO ($200) = $600 Iran direct exposure (AT CAP per Rule 9)
- This Trump China NO adds ~$150 of functionally Iran-correlated exposure
- Total functionally Iran-correlated exposure: $750

**Partial independence justification**:
- Resolution criteria are different: requires Trump physically in China by April 30, not dependent on Iran status
- Even if ceasefire announced in week 3 (by April 7), Trump would need to (a) want to reschedule, (b) China agree to reschedule, (c) logistics completed, all before April 30 — low conditional probability
- April 30 hard deadline is a meaningful independent constraint
- Estimate: P(ceasefire by April 7) = ~10-15%, P(Trump visits China in the remaining 3 weeks | ceasefire) = ~20-30% → P(ceasefire AND visit by April 30) ≈ 2-4.5%

**Conclusion**: Partial correlation justifies size reduction from Kelly recommendation ($290-$310) to $150 (1.5% bankroll). Does NOT justify full PASS — the independence is real and the edge is substantial.

### Size Determination

| Approach | Amount |
|----------|--------|
| Kelly 1/6 (60.5% NO basis) | $310 |
| Politics 3% cap | $290 |
| Correlation discount (50% of cap) | $145 → round to $150 |
| **Final size** | **$150** |

- Kelly recommended $310 at 60.5% NO, $480 at 75% NO
- Hard cap: 3% of $9,664 = $290
- Applied correlation discount: 50% of cap = $145 → $150
- This is 1.55% of bankroll — well within limits
- Total Iran-correlated after this trade: $750 (under $900 soft limit)

**Expected value at $150 and 75% fair value NO:**
EV = $150 × (0.75 × (1/0.605 - 1) - 0.25 × 1) = $150 × (0.75 × 0.6529 - 0.25) = $150 × (0.4897 - 0.25) = $150 × 0.2397 = **+$35.96**

---

## What Could Go Wrong

**Primary risk**: Iran-US diplomatic breakthrough in the next 6 weeks that frees up Trump's schedule. If ceasefire announced by early April AND China trip is expedited, this market moves sharply to YES. Probability: ~3-5%.

**Secondary risk**: The "5-6 week" delay wording means Trump has himself telegraphed intent to visit. If all obstacles resolve faster than expected, he visits April 21-28. This is the 10-15% tail that keeps us from sizing more aggressively.

**Resolution ambiguity risk**: LOW — criteria clearly require physical presence in mainland China. No ambiguity about what counts.

---

## Open Positions in Same Category (Politics)

| Market | Direction | Size | Notes |
|--------|-----------|------|-------|
| Iran ceasefire April 30 NO | NO | $200 | Direct correlation |
| Iran regime fall June NO | NO | $200 | Direct correlation |
| Iran regime fall 2027 NO | NO | $200 | Direct correlation |
| Netanyahu June NO | NO | $150 | — |
| Paxton YES | YES | $460 | — |
| Greenland NO | NO | $193 | — |
| Israel-Saudi NO | NO | $139 | Partial inverse correlation |
| Paris Mayor YES | YES | $200 | Resolves March 22 |
| **Trump China NO (this)** | NO | $150 | Iran-correlated |

Total politics open exposure after this trade: **$1,892**

---

## Monitor / Exit Conditions

- **Exit if** Iran ceasefire is officially announced AND Trump's team confirms a China trip before April 30 — immediate exit, do not wait for confirmation.
- **Exit if** Trump himself says he will visit China before April 30 (new statement overriding the March 17 delay).
- **Hold** through routine diplomatic contacts, state department meetings, secondary source denials.
- **Target**: Resolves NO on April 30. If market drifts to 70%+ NO before resolution, consider early exit to free capital.

---

## Post-Trade Notes (to be filled after resolution)

- Resolution date: 2026-04-30
- Outcome: [PENDING]
- P&L: [PENDING]
- Calibration update: [PENDING]
- Lessons: [PENDING]
