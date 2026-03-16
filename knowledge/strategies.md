# Strategies

Strategies are systematic patterns for finding edge. Each has a status, evidence base, and performance record.

**Statuses**: WINNING (>55% win rate, ≥5 trades) | TESTING (<5 trades) | UNDERPERFORMING (<45%, ≥5 trades) | RETIRING (0 wins last 5) | RETIRED

Last reviewed: 2026-03-16

---

## TESTING Strategies

### EPL Large Points Lead
**Status**: TESTING (1 trade, unresolved)
**Hypothesis**: Teams with 9+ point leads with 9+ games remaining win the title 97–99% of the time. Market underprices this certainty due to historical Arsenal anxiety.
**Entry signal**: 9+ point lead with ≤10 games remaining, market < 95%
**Exit signal**: Lead drops to ≤5 points → review position
**Edge range**: +4–8pp on YES
**Trades**: 1 open (Arsenal EPL YES at 89.5%, fair value 93–97%)
**Last updated**: 2026-03-15

---

### Commodity Settlement Gap
**Status**: TESTING (2 trades, unresolved)
**Hypothesis**: CME settlement prices are systematically lower than intraday highs (mean reversion near close). Markets that price binary outcomes on settlement may overestimate the probability of reaching round-number targets based on intraday data.
**Entry signal**: Large gap between intraday high and recent settlements, binary market priced off intraday data
**Current evidence**: March 9: intraday $119.94, settlement $94.65 (−21%)
**Trades**: 2 open (Oil $100 YES at 88.8%, Oil $120 NO at 54%)
**Last updated**: 2026-03-15

---

### Short-Window Data Frequency (Musk Tweets)
**Status**: TESTING (1 trade, resolves 2026-03-17)
**Hypothesis**: Markets for counting discrete events (tweets, posts) over short windows can be priced using current pace extrapolation when there is reliable live data.
**Entry signal**: 5+ days of data, pace is consistent, market underestimates the bucket containing the projected total
**Data source**: Public tweet counters, official accounts
**Trades**: 1 open (Musk 300–319 YES at 28.5%, projected total ~318)
**Last updated**: 2026-03-15

---

## UNDERPERFORMING Strategies

### Awards Guild Predictor
**Status**: UNDERPERFORMING (1 trade, 0% win rate — but also only 1 trade; upgrading after 5 trades)
**Hypothesis**: SAG Ensemble win is the strongest Best Picture predictor historically (~60–65% when SAG/DGA split). Bet the SAG winner when market underprices them.
**What went wrong (2026)**: Academy diverged from ALL guild consensus. Bugonia (Yorgos Lanthimos) won despite no major guild wins. SAG + DGA + PGA + BAFTA winner all lost.
**Revised hypothesis**: Guild predictors have lower signal strength in eras of Academy voter expansion. Auteur/arthouse dark horses deserve 5–10% minimum floor.
**Entry signal**: SAG winner priced below 30% when you estimate 40%+
**Status note**: Pausing new Oscars bets until sample size > 3 and calibration improves.
**Trades**: 1 resolved LOSS (Sinners Best Picture −$200)
**Last updated**: 2026-03-16

---

## RETIRED Strategies

### Near-Certainty Lock
**Status**: RETIRED (2026-03-15)
**Was**: Bet heavily on markets at 97%+ that should resolve YES
**Why retired**: Markets at 97–100% have essentially zero edge. The 2–3 cent upside is consumed by transaction costs and the rare black swan. Maximum upside per dollar risked = $0.03. Not worth the capital allocation.
**Lesson**: Never chase markets above 95%. Edge is gone.

---

## Proposed Strategies (Not Yet Tested)

### Geopolitical Tail Risk Discount
**Hypothesis**: During active conflicts, markets for "conflict resolution" (ceasefire, regime fall) are systematically underpriced at low probabilities, and "escalation" events are overpriced at high probabilities. The status quo has more inertia than markets price.
**Evidence needed**: 5+ geopolitical markets across multiple conflicts
**Entry signal**: "Conflict ends by X" at < 5%, regime survival at > 90%

### Tournament Early-Round Favorites
**Hypothesis**: In sports tournaments (World Cup, NBA playoffs, Champions League), early-round heavy favorites are systematically underpriced because casual bettors seek upsets.
**Evidence needed**: 5+ tournament markets
**Entry signal**: Implied probability > 85% for a team vs opponent with 2:1+ record advantage

---

## How to Add a New Strategy

1. Observe a pattern in 1–2 winning trades
2. Write a clear hypothesis (if X, then Y edge of Zpp)
3. Set status to TESTING
4. After 5 trades: calculate win rate and update status
5. After 10 trades: decide WINNING / UNDERPERFORMING / RETIRING
