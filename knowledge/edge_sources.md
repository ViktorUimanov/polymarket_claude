# Edge Sources

Where edge has actually been found. Each source tracks success rate over time.
A source is "active" only if it has produced at least 1 win OR has strong theoretical basis.

Last reviewed: 2026-03-22 21:00 UTC (Paris Mayor Grégoire YES resolved WIN +$79.70 — Edge Source 7 confirmed; electoral structural framework validates as reproducible edge)

---

## Active Edge Sources

### 1. Commodity Settlement vs Intraday Price Divergence
**Status**: UNTESTED (2 open trades)
**Description**: CME WTI settlement prices are calculated near market close and are significantly lower than intraday highs during volatile sessions. Binary markets asking "did price reach X on any day" may be priced using intraday data, creating edge on the NO side for high price targets.
**Key fact**: March 9, 2026 — WTI intraday $119.94, settlement $94.65 (−21%)
**Signal**: Settlement/intraday ratio < 0.85 on a recent volatile day → NO edge on $120+ targets
**Best market type**: Monthly binary targets on crude oil (WTI specifically)
**Confirmed wins**: 0 (trades open)
**Losses**: 0
**Success rate**: UNTESTED
**Last updated**: 2026-03-15

---

### 2. Sports: Large Points Lead + Mathematical Lock
**Status**: UNTESTED (1 open trade)
**Description**: When a team has a 9+ point lead with 9 games remaining in a 38-game season, the probability of winning the title is 97–99% historically. Markets often price this at 88–93% due to historical anxiety and narrative uncertainty.
**Signal**: Lead ≥ 9 points, ≤ 10 games remaining, market < 95%
**Best market type**: EPL winner, NBA division winner, similar season-long standings
**Confirmed wins**: 0 (trade open)
**Losses**: 0
**Success rate**: UNTESTED
**Last updated**: 2026-03-15

---

### 3. Discrete Event Counting with Real-Time Data
**Status**: FIRST DATA POINT — LOSS (1 resolved loss; NOT retired — < 5 trades per protocol)
**Description**: For markets counting discrete events over a short window (tweets, posts, appearances), when reliable LIVE real-time data is available showing the running count supports the target bucket, markets may misprice the specific bucket. The key prerequisite is live data access at entry — historical extrapolation is insufficient.
**What failed (2026-03-17)**: Entered Musk 300-319 tweets at 28.5% based on 5-day weekday extrapolation (45.4/day). Did not have live counter access at entry. Actual count showed ~248 with 18h remaining (live-counter participants knew this and correctly priced at 7-25%). Error type: model_error — insufficient data quality, not wrong hypothesis.
**Revised signal**: Live counter confirms running total is within target bucket OR within striking distance with > 36h remaining AND weekend-adjusted pace still supports target.
**Revised prerequisite**: Live counter URL must be confirmed accessible BEFORE entry. If no live counter exists, DO NOT enter. If window spans a weekend, obtain historical weekend vs. weekday pace breakdown before estimating.
**Data sources**: xtracker.polymarket.com for Twitter/X markets; official APIs for other count markets
**Confirmed wins**: 0
**Losses**: 1 (Musk 300-319 tweets, −$150, 2026-03-17)
**Success rate**: 0/1 = 0% (insufficient data — NOT retired — requires 5+ trades minimum)
**Reinstatable**: Yes — edge hypothesis is still valid if live data prerequisite is met
**Last updated**: 2026-03-17 (confirmed after resolution)

---

## Retired / Failed Edge Sources

### Awards Guild Consensus Predictor
**Status**: FAILED (1 loss, strategy on probation)
**What it was**: Using SAG Ensemble winner as a Best Picture predictor. When SAG and DGA disagree, SAG historically wins ~60–65% of the time.
**What failed**: 2026 Oscars — SAG winner (Sinners) lost. DGA winner (One Battle) lost. All guild winners lost. Complete outlier year.
**Why retired from active use**: Sample size too small (1 trade) to retire permanently, but on calibration probation. Academy voter expansion has introduced more volatility than historical base rates suggest. Dark-horse auteur films (Bugonia at 2%) can win.
**Lesson extracted**: Guild predictors have lower reliability in post-expansion Academy years. Always give dark-horse auteur films a 5–8% floor regardless of market pricing.
**Reinstatable if**: Win rate improves after 5+ total Oscars trades using updated model (5–8% dark-horse floor).

---

### 4. Geopolitical Status Quo Bias
**Status**: ACTIVE LIVE TEST (4 trades, 0 resolved — extended with Israel-Saudi 2026-03-17)
**Description**: Markets systematically overestimate the probability of dramatic short-term political/military change (ceasefires, regime falls, diplomatic agreements). Historical base rates show ~70% probability of no dramatic change within 30–90 days in active conflicts. Markets price dramatic change at 2–4× the historical rate. Also applies to long-horizon normalization deals that require multi-party ratification.
**Key fact**: Iran regime fall 2027 priced at 39.5% YES by market vs our estimate of 13% (3× overpriced). Iran ceasefire by April 30 priced at 39.5% YES vs our estimate of 11% (3.6× overpriced). Israel-Saudi normalize priced at 20.5% YES vs our estimate of 9% (2.3× overpriced).
**Signal**: Any "dramatic change by X" market where: (a) no change is already well underway, (b) key actors have explicitly rejected the change, (c) market prices change at > 15%
**Best market type**: "Ceasefire by [date]", "Regime falls by [date]", "Leader resigns by [date]", "Normalize relations by [date]"
**Active trades**:
- Iran ceasefire Apr 30 NO ($200, resolves 2026-04-30, +28.5pp edge at entry)
- Iran regime fall June NO ($200, resolves 2026-06-30, +17-22pp edge at entry)
- Iran regime fall 2027 NO ($200, resolves 2026-12-31, +26.5pp edge at entry)
- Israel-Saudi normalize by 2027 NO ($139, resolves 2026-12-31, +11.5pp edge at entry)
- Total Iran correlated exposure: $600 (AT cap — no new Iran NOs)
- Israel-Saudi: inversely correlated to Iran cluster (provides partial hedge — see trade file for correlation analysis)
**Confirmed wins**: 0 (all trades open)
**Losses**: 0
**Success rate**: UNTESTED — first data point expected April 30, 2026
**Last updated**: 2026-03-18

### 5. Sportsbook vs Polymarket Pricing Gap on Sports Futures and Awards
**Status**: FIRST DATA POINT — WIN (Kucherov early exit +$578.57; 4 trades still open)
**Description**: Polymarket prices on sports futures and individual award markets lag sportsbook consensus. The gap is largest on thin-volume markets (<$15k) where fewer sharp bettors participate. Sportsbooks with dedicated quant staff converge faster on updated odds.
**Signal (high-volume futures)**: Sportsbook consensus (3+ books) exceeds Polymarket by ≥ 5pp AND Polymarket volume > $5M
**Signal (thin award markets)**: Sportsbook consensus (3+ books) exceeds Polymarket by ≥ 10pp AND Polymarket volume < $15k — size capped at $100 for liquidity
**EXIT SIGNAL (confirmed 2026-03-22)**: When Polymarket price EXCEEDS sportsbook consensus by >10pp (gap inverted), exit immediately. The original edge is gone; continuing to hold is a directional bet without structural basis.
**Best market type**: NHL/NBA team futures, EPL winner, individual awards (Hart Trophy, Norris, NBA MVP)
**Active trades**:
  - Colorado Avalanche Stanley Cup YES ($235 total, avg 21.1¢ Polymarket vs 25.7-27.8% sportsbooks, resolves 2026-06-30) — 3 entries; gap persistent despite Kadri acquisition
  - Scottie Scheffler Masters YES ($190 total, avg 17.64¢ Polymarket vs 19-25% sportsbooks, resolves 2026-04-13) — initial $140 + $50 top-up on Players Champ health confirmation
  - OKC Thunder NBA YES ($120, 37.5% Polymarket vs 43.3% sportsbooks, resolves 2026-07-01) — first large-volume ($5M+) extension; 5.8pp gap
  - Tampa Bay Lightning Cup YES ($75, 12.3% Polymarket vs 18-20% sportsbooks, resolves 2026-06-30) — Eastern Conference leaders; DK +400 (20%) vs PM 12.3%; +7.7pp gap; correlated with Avalanche (only one NHL team wins)
**Gap magnitude by market size**: thin (<$15k): 10-20pp | mid ($50k-$5M): 5-8pp | large ($5M+): 4-6pp. Pattern is consistent across all market sizes — structural, not transient.
**Extension note (2026-03-17)**: Gap is proportionally LARGER in thin individual award markets. The hypothesis applies but sizing must be constrained by liquidity (≤ 1% of total pool).
**Persistent gap signal (2026-03-18)**: Avalanche gap has not closed after 3 top-up entries over 3 days. Lightning gap confirmed same pattern. Both confirm the gap is structural (thin NHL markets, no active arbitrageurs) rather than transient.
**NHL total correlated exposure**: $310 (Avalanche $235 + Lightning $75) = 3.2% bankroll. Both teams cannot win — anti-correlated outcomes. Monitor total and do not add further NHL YES positions without reducing one.
**Confirmed wins (early exits)**: 1 — Kucherov Hart Trophy exited Mar 22 at ~38¢ (entry 5.6¢), +$578.57 profit (+578.6%). Gap inverted from PM underpriced to PM overpriced by 15pp — triggered exit signal.
**Losses**: 0
**Success rate**: 1/1 early exits (100% — insufficient data; resolution outcomes pending April–July 2026)
**Last updated**: 2026-03-22 session1

### 7. Electoral Structural Framework — First-Round Leader in Incumbent Left-Majority City
**Status**: FIRST DATA POINT — WIN (Paris Mayor 2026, +$79.70)
**Description**: In French municipal two-round elections held in cities with entrenched left majorities, the first-round leader with a 10pp+ margin carries a structural advantage that Polymarket systematically underprices. The structural factors — 25-year incumbent bloc, vote consolidation from satellite left parties, historical base rate of first-round leader winning — dominate late-horizon "tightening narrative" polls. Markets price in uncertainty from MoE-tight final polls; structural analysis correctly overrides.
**Signal**: First-round leader with ≥10pp margin in a city with ≥20-year unbroken incumbent governance + satellite party voters likely to useful-vote toward the leader + Polymarket < 80% YES
**Lesson**: When hard vote counts (actual R1 results) are available, weight them more than subsequent opinion polls. A tight final poll (45.5 vs 44.5 in the Elabe March 20 survey) reflects polling noise, not a genuine paradigm shift. Structural factors dominate.
**Best market type**: French two-round municipal elections; potentially applicable to similar runoff structures (Brazilian Presidential, other two-round systems)
**Confirmed wins**: 1 — Paris Mayor Grégoire YES (+$79.70, 2026-03-22). Entry 71.5¢, resolution 100¢. FV 80%, Polymarket 71.5%, edge +8.5pp.
**Losses**: 0
**Success rate**: 1/1 (100% — first data point; expand dataset before relying heavily)
**Last updated**: 2026-03-22 21:00 UTC

---

### 6. Principal Actor Statement — Thesis-Change Rapid Exit (and Bidirectional Re-Entry)
**Status**: FIRST DATA POINT — WIN (1 realized gain; < 5 trades — TESTING)
**Description**: When a principal actor (President, head of state, key decision-maker) makes a direct, on-record statement that invalidates the entry thesis, exit immediately even if market has not fully repriced. The market will lag the news, creating a temporary sell window at a better price than fair value. ADDITIONALLY: after exiting, immediately re-evaluate the reverse direction — the same statement may open a new opposite-direction entry if the market still misprices the revised fair value.
**Key mechanics**: (a) Principal statement carries stronger weight than secondary spokesperson denial, (b) Exit while the market is still processing — do NOT wait for confirmation, (c) Lock realized gain before the market corrects to the new fair value, (d) After exit, run fresh probability estimate with new information — if revised fair value differs from new market price by >= minimum edge, enter opposite direction.
**What confirmed it (2026-03-17)**: Trump explicitly said he asked China to delay the visit by "a month or so." Fair value dropped from 44-47% to 38-43%. Market was still at 48.5% (above our new fair value). Exited entire 454.5-share position at 48.5¢ vs entry 33.0¢. Net: +$70.40.
**What extended it (2026-03-18)**: Market corrected from 48.5% to 39.5% YES but remained above revised fair value of 25-32% YES. Entered NO at 60.5c with +14.5pp edge. The Trump delay statement was a two-sided signal — it both forced an exit AND opened a new entry.
**Signal**: Principal actor makes an explicit, direct statement on the key variable AND (a) market price remains above revised fair value by ≥ 5pp [for exit] OR (b) market price, after partial repricing, remains mispriced vs revised fair value by >= minimum edge threshold [for new entry].
**Confirmed wins**: 1 (Trump China YES exit, +$70.40, 2026-03-17)
**Losses**: 0
**Open applications**: 1 (Trump China NO, $150, entered 2026-03-18, resolves April 30)
**Success rate**: 1/1 (100% — insufficient data, 1 trade)
**Key trade files**: `output/trades/2026-03-17_trump-china-exit.md` + `output/trades/2026-03-18_trump-china-no.md`
**Last updated**: 2026-03-18 session2

---

## Potential Edge Sources (Untested — Proposed)

| Source | Hypothesis | Status |
|--------|-----------|--------|
| Tightening-race proportional election | Market > 75% for one party but polls show statistical tie → market overconfident | INCONCLUSIVE — Slovenia SDS NO exited break-even 2026-03-18. Thesis invalidated by broader polling universe (7/8 polls showed SDS +2-8pp lead). Entry error: relied on single outlier poll. Revised entry condition: requires 3+ independent polls confirming tightening. Not a negative data point for the hypothesis — it is a lesson about entry quality. Re-test with better entry criteria. |
| National team brand premium vs injury-adjusted probability | Polymarket prices national teams at their historical brand strength; when 5+ starters are injured in a knockout format, injury-adjusted probability diverges significantly from market-implied | TESTING — Italy WC NO ($150, Mar 18). Italy brand 61% YES; injury-adjusted 44% YES (7 absences including Verratti); +11pp edge on NO at 39c. Resolves effectively March 26 (Italy semi-final). |
| Tournament upset correction | Early-round heavy favorites underpriced by casual bettors | Proposed |
| Thin market inefficiency | Markets with < $5k volume hold stale prices for hours | Proposed — requires real-time monitoring |
| Interest rate near-certainty | Fed meetings with 99%+ consensus: no edge worth taking | Confirmed — don't bet |

---

## How to Update This File

When a trade resolves as a WIN:
1. Find the relevant edge source
2. Increment confirmed_wins
3. Recalculate success_rate = wins / (wins + losses)
4. Add a brief note about what confirmed the edge

When a trade resolves as a LOSS:
1. Find the relevant edge source
2. Increment losses
3. Add note about what failed
4. If success_rate < 30% with ≥ 5 trades: consider retiring the source

When discovering a new potential edge:
1. Add to "Potential Edge Sources" table
2. Write a brief hypothesis
3. Move to "Active" only after finding 1+ confirmed example
