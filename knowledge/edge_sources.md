# Edge Sources

Where edge has actually been found. Each source tracks success rate over time.
A source is "active" only if it has produced at least 1 win OR has strong theoretical basis.

Last reviewed: 2026-03-16

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
**Status**: UNTESTED (1 open trade resolves March 17)
**Description**: For markets counting discrete events over a short window (tweets, posts, appearances), when reliable live data is available, the current pace extrapolated gives a strong probability estimate. Markets often misprice the specific bucket.
**Signal**: 5+ days of data, consistent pace, market underweights the correct bucket by 6+ pp
**Data sources**: Tweet counters, social media APIs, official trackers
**Confirmed wins**: 0 (trade open)
**Losses**: 0
**Success rate**: UNTESTED
**Last updated**: 2026-03-15

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

## Potential Edge Sources (Untested — Proposed)

| Source | Hypothesis | Status |
|--------|-----------|--------|
| Geopolitical status quo bias | Markets overestimate probability of dramatic change (ceasefires, regime falls) | Proposed |
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
