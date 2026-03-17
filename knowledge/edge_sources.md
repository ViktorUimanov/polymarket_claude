# Edge Sources

Where edge has actually been found. Each source tracks success rate over time.
A source is "active" only if it has produced at least 1 win OR has strong theoretical basis.

Last reviewed: 2026-03-17 (synthesis run)

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
**Status**: ACTIVE LIVE TEST (3 trades, 0 resolved — promoted from Potential 2026-03-17)
**Description**: Markets systematically overestimate the probability of dramatic short-term political/military change (ceasefires, regime falls, diplomatic agreements). Historical base rates show ~70% probability of no dramatic change within 30–90 days in active conflicts. Markets price dramatic change at 2–4× the historical rate.
**Key fact**: Iran regime fall 2027 priced at 39.5% YES by market vs our estimate of 13% (3× overpriced). Iran ceasefire by April 30 priced at 39.5% YES vs our estimate of 11% (3.6× overpriced).
**Signal**: Any "dramatic change by X" market where: (a) no change is already well underway, (b) key actors have explicitly rejected the change, (c) market prices change at > 20%
**Best market type**: "Ceasefire by [date]", "Regime falls by [date]", "Leader resigns by [date]"
**Active trades**:
- Iran ceasefire Apr 30 NO ($200, resolves 2026-04-30, +28.5pp edge at entry)
- Iran regime fall June NO ($200, resolves 2026-06-30, +17-22pp edge at entry)
- Iran regime fall 2027 NO ($200, resolves 2026-12-31, +26.5pp edge at entry)
- Total Iran correlated exposure: $600 (6.2% bankroll — within 10% cap)
**Confirmed wins**: 0 (all trades open)
**Losses**: 0
**Success rate**: UNTESTED — first data point expected April 30, 2026
**Last updated**: 2026-03-17

### 5. Sportsbook vs Polymarket Pricing Gap on Major Sports Futures
**Status**: ACTIVE LIVE TEST (1 trade, 0 resolved)
**Description**: For major sports futures (NHL, NBA, EPL) with high Polymarket volume (> $5M), Polymarket prices lag sportsbook consensus by 4–8pp on analytics-favored teams. Sportsbooks have dedicated quant teams and sharp bettor flow that converge to more efficient prices.
**Signal**: Sportsbook consensus (3+ books) exceeds Polymarket by ≥ 5pp on the favored team AND Polymarket volume > $5M
**Best market type**: NHL Stanley Cup, NBA Finals, EPL winner futures where analytics clearly favor one team
**Active trades**: Colorado Avalanche Stanley Cup YES ($35, 21.6% Polymarket vs 25.7-27.8% sportsbooks, resolves 2026-06-30)
**Confirmed wins**: 0 (trade open)
**Losses**: 0
**Success rate**: UNTESTED
**Last updated**: 2026-03-17

## Potential Edge Sources (Untested — Proposed)

| Source | Hypothesis | Status |
|--------|-----------|--------|
| Tightening-race proportional election | Market > 75% for one party but polls show statistical tie → market overconfident | LIVE TEST — Slovenia SDS NO (2026-03-16, $100, resolves 2026-03-22). First data point available March 22. |
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
