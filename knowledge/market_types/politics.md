# Politics Markets — Knowledge Base

## Category Profile

| Attribute | Value |
|-----------|-------|
| Variance level | HIGH |
| Calibration status | No data |
| Max position size | 3% bankroll |
| Min edge required | 5pp (higher due to tail risk) |
| Current positions | None |

---

## Rules (Apply Before Every Politics Bet)

### Rule 1 — Use Multiple Aggregators, Never Single Poll
**Rule**: Never base a political probability estimate on a single poll. Use aggregators:
- FiveThirtyEight / Nate Silver's Substack (US elections)
- Metaculus (geopolitical events)
- Manifold Markets (crowd wisdom)
- PredictIt / Kalshi (market-based)
**Apply when**: Any election or vote-based market.

### Rule 2 — Status Quo Has More Inertia Than Markets Price
**Rule**: Markets systematically overestimate the probability of dramatic political change in the short term (< 3 months):
- Ceasefires that "seem imminent" rarely materialize on schedule
- Regime collapses require sustained, organized opposition
- Policy reversals face significant institutional friction
**Implication**: On markets for rapid change ("ceasefire by month's end", "leader resigns by X"), lean toward NO unless change is already well underway.
**Calibration**: "Status quo" wins ~70% of the time vs market-implied ~40%.

### Rule 3 — Iran Conflict Context (Current)
**Rule**: During the ongoing Iran-US/Israel conflict, ALL geopolitical markets are affected by correlation risk:
- Oil markets → Iran news
- Iran regime stability → US military posture
- Regional escalation → multiple cascading markets
**Apply when**: Any geopolitical market in March 2026.
**Key uncertainty**: Hormuz Strait status. If reopened → massive cascading effects on oil, Middle East stability markets.

### Rule 4 — Black Swan Budgets for Geopolitics
**Rule**: For any geopolitical binary (will X happen by Y), give a minimum 3% probability to unexpected reversals regardless of how certain the situation seems. Never go above 90% or below 5% on geopolitical markets.

### Rule 5 — Resolution Criteria Often Ambiguous for Politics
**Rule**: Before betting any political market, read the full resolution criteria. Many geopolitical markets resolve based on specific definition of events ("official ceasefire announcement" vs "cessation of hostilities") that may differ from commonsense interpretation.
**Apply when**: Every politics/geopolitics bet. Always check how Polymarket admin resolves this type.

### Rule 6 — Proportional Elections: Tightening Polls Signal Market Overconfidence
**Date learned**: 2026-03-16 (Slovenia SDS trade)
**Rule**: In proportional parliamentary elections, a market price of 80%+ for one party to win the plurality should be questioned when recent polls show the race tightening to within polling-error range. A statistical tie in polling does not support 80%+ market confidence.
**Why**: Slovenia — market at 81% YES for SDS despite one March poll showing GS briefly ahead (24.1% GS vs 23.2% SDS, a statistical tie within MOE). In a proportional system, 3rd-party performance and late swings can flip the plurality.
**Apply when**: Any proportional election market where the leader's margin in polls is less than 5pp and the market price is above 75%.

### Rule 7 — Election Markets: 30+ Day Horizon — Model Trump Endorsement as Binary Catalyst
**Date learned**: 2026-03-17 (Paxton Texas Senate trade)
**Rule**: For US Republican primary races with a pending Trump endorsement, model the endorsement as a binary scenario. Estimate: P(Trump endorses candidate A) × P(A wins | endorsement) + P(Trump endorses B) × P(A wins | B endorsed) + P(no endorsement) × P(A wins | no endorsement). Apply specific historical win-rate data for Trump-endorsed vs non-endorsed MAGA-aligned candidates in TX GOP primaries.
**Why**: Paxton market at 38.5% despite Paxton leading in post-primary polls (45-42%) and strong MAGA alignment. The market is pricing Trump endorsement risk heavily. The three-scenario model gives 52% fair value vs 38.5% market — a 13.5pp edge.
**Apply when**: Any primary race with a high-profile pending endorsement from a dominant party figure.

### Rule 8 — Principal Statements Override Secondary Source Denials
**Date learned**: 2026-03-17 (Trump China exit trade)
**Rule**: When a principal actor (President, head of state, CEO) makes a direct statement on record that changes the thesis, update fair value immediately, even if a secondary spokesperson contradicts them.
**Why**: Trump explicitly said he asked China to delay the visit by "a month or so." Bessent denied it the same day. We correctly weighted Trump's own statement over Bessent's denial and exited at +$70.40 profit. The market continued pricing 48.5% YES despite the president's own delay request.
**Apply when**: Any position where a principal actor has spoken directly on the key variable — weight their statement at Strong (±8–15pp) to Very Strong (±15–25pp) depending on specificity.

---

## Current Geopolitical Context (March 2026)

### Iran-US/Israel Conflict
- Started: February 28, 2026 (US/Israel struck Iran nuclear sites)
- Iran response: Closed Strait of Hormuz
- US response: Naval deployments to Gulf
- Saudi position: Diplomatic outreach to Iran
- Probability of ceasefire in March 2026: Low (15–25%)
- Probability of escalation to ground war: Very low (3–8%)
- Impact on markets: Oil, gold, Iran regime fall, Israel ground offensive

### Markets to Watch
| Market | Est. Price | Our View | Notes |
|--------|-----------|----------|-------|
| Iran regime fall by March 31 | 2.5% | Correct/slightly high (~1.5%) | No organized opposition |
| Ceasefire by March 31 | ~38% | Overpriced (~20%) | Status quo inertia rule |
| Israeli ground offensive | 65.5% | Unclear — needs research | |
| Trump acquires Greenland | 9.3% | Unclear | Long-term market |

---

## Political Base Rates

| Scenario | Probability |
|----------|------------|
| Conflict ceasefire within 30 days of escalation | 15–25% |
| Regime falls within 30 days of military strike | 3–8% |
| Incumbent wins re-election (no major scandal) | 60–70% |
| Poll-ahead candidate wins election | 70–75% |
| UN Security Council action on active conflict | 20–30% |

### Rule 9 — Iran NO Positions: Size on Correlated Basis, Not Individual Edge
**Date learned**: 2026-03-17 (synthesis — from $600 correlated Iran exposure review)
**Rule**: When holding multiple NO positions on Iran-related outcomes (ceasefire, regime fall, escalation), treat the entire Iran exposure as one correlated macro scenario. The combined loss scenario is "ceasefire occurs or regime collapses" — a single event that hits all positions simultaneously. Cap total Iran direct exposure at $600 (6% bankroll) regardless of individual edges.
**Why**: All three Iran NO positions (ceasefire Apr 30, regime June, regime 2027) share the same tail risk: a sudden diplomatic resolution or regime collapse would likely affect all three simultaneously. Individual edges of +17–29pp are real but the correlation means portfolio risk is higher than independent 2% bets.
**Apply when**: Any time adding a new Iran-related NO position while already holding 2+ Iran NOs.
**Specific sub-rule**: Before adding a 4th Iran NO position, total Iran exposure must be below $400 (the regime June + 2027 NOs = $400 already). Adding ceasefire April NO brought it to $600 — at cap. No further Iran NOs until at least one resolves.

### Rule 10 — Resolution Criteria Distinguish "Regime Fall" from "Leadership Change"
**Date learned**: 2026-03-17 (from Iran regime 2027 NO trade research)
**Rule**: For "regime fall" markets, read the exact resolution criteria. Most Polymarket regime-fall markets require dissolution of core state structures (Supreme Leader office + Guardian Council + IRGC clerical authority simultaneously). A new Supreme Leader, IRGC consolidation, or government reshuffling does NOT trigger YES.
**Why**: The March 9, 2026 installation of Mojtaba Khamenei as Supreme Leader was widely reported as "succession" and "instability" — yet it did not and would not trigger resolution on regime-fall markets. The market priced this as destabilizing (YES at 39.5%) when the institutional structures remained intact.
**Apply when**: Any "regime fall", "government collapse", or "leader ousted" binary market. Always read the full resolution criteria before estimating probability.

---

## Calibration History

No resolved trades yet. First data point expected: Slovenia SDS (March 22, 2026).
