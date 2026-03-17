# Strategies

Strategies are systematic patterns for finding edge. Each has a status, evidence base, and performance record.

**Statuses**: WINNING (>55% win rate, ≥5 trades) | TESTING (<5 trades) | UNDERPERFORMING (<45%, ≥5 trades) | RETIRING (0 wins last 5) | RETIRED

Last reviewed: 2026-03-17 (synthesis run)

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
**Status**: TESTING (2 trades open, 1 voluntary early exit — not a resolution loss)
**Hypothesis**: CME settlement prices are systematically lower than intraday highs (mean reversion near close). Markets that price binary outcomes on settlement may overestimate the probability of reaching round-number targets based on intraday data.
**Entry signal**: Large gap between intraday high and recent settlements, binary market priced off intraday data
**Current evidence**: March 9: intraday $119.94, settlement $94.65 (−21%)
**Trades**: 2 open (Oil $120 NO at 54.0¢, Oil $110 NO at 51.5¢, both resolve 2026-03-31). Oil $100 YES closed early on 2026-03-16 (Bessent tanker announcement — thesis broke, not a resolution loss). Oil $80 NO was drafted but NOT EXECUTED (market not found via API — confirmed 2026-03-17).
**Key learning from $100 exit**: Administration/Treasury price statements are tier-1 signals. The catalyst (Hormuz closure) proved unstable within 24 hours. Gap trades require stable fundamental driver for at least 2× the remaining window.
**Last updated**: 2026-03-17

---

### Short-Window Data Frequency (Musk Tweets)
**Status**: TESTING (1 resolved LOSS — 0/1 win rate, but < 5 trades, NOT retiring)
**Hypothesis**: Markets for counting discrete events (tweets, posts) over short windows can be priced using LIVE CURRENT count data when a real-time tracker is accessible. Historical pace extrapolation without live data is insufficient.
**What went wrong (2026-03-17)**: Entered at 28.5% (fair value estimated 35-40%) based on 5-day weekday pace extrapolation (45.4/day). Actual count stalled at ~248 by March 16 with 18h remaining — well below 300. Live-counter participants knew this and repriced to 7-25%.
**Revised hypothesis**: The edge is real IF: (a) live counter is accessible at entry, (b) live count supports the target bucket currently (not via historical extrapolation), (c) window is either all-weekdays OR weekend pace data is obtained separately.
**Revised entry signal**: Live counter shows running total within the target bucket OR within 1 standard deviation below lower bound with > 36h remaining.
**Required data source**: Live real-time counter (e.g., xtracker.polymarket.com or similar) confirmed accessible at entry.
**Trades**: 1 resolved LOSS (Musk 300-319 tweets, −$150, 2026-03-17). 0 resolved wins.
**Last updated**: 2026-03-17

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

## TESTING Strategies (recently promoted from Proposed)

### Geopolitical Tail Risk Discount
**Status**: TESTING (3 active trades, 0 resolved)
**Hypothesis**: During active conflicts, markets for "conflict resolution" (ceasefire, regime fall) are systematically underpriced at low probabilities, and "escalation" events are overpriced at high probabilities. The status quo has more inertia than markets price.
**Evidence needed**: 5+ geopolitical markets across multiple conflicts
**Entry signal**: "Conflict ends by X" at > 15%, regime survival at < 90% despite structural stability
**Active trades**: Iran regime fall June NO ($200, resolves 2026-06-30), Iran regime fall 2027 NO ($200, resolves 2026-12-31), Iran ceasefire April 30 NO ($200, resolves 2026-04-30). All entered at 17–29pp edge.
**Last updated**: 2026-03-17

### Sportsbook vs Polymarket Pricing Gap
**Status**: TESTING (1 active trade, 0 resolved)
**Hypothesis**: For major sports futures (NHL, NBA, EPL) with high volume, Polymarket systematically lags sportsbook consensus on favored teams by 4–8pp. The edge is on the YES side for teams the sportsbooks favor more than Polymarket does.
**Entry signal**: Sportsbook consensus (3+ books) > Polymarket price by ≥ 5pp on a team with high-volume market (> $5M)
**Required check**: Sportsbooks must agree (not one outlier); team must be analytics favorite (not just popular sentiment)
**Active trades**: Colorado Avalanche Stanley Cup YES ($35 at 21.6% vs 25.7-27.8% sportsbooks, resolves 2026-06-30)
**Last updated**: 2026-03-17

## Proposed Strategies (Not Yet Tested)

### Tournament Early-Round Favorites
**Hypothesis**: In sports tournaments (World Cup, NBA playoffs, Champions League), early-round heavy favorites are systematically underpriced because casual bettors seek upsets.
**Evidence needed**: 5+ tournament markets
**Entry signal**: Implied probability > 85% for a team vs opponent with 2:1+ record advantage

### Tightening-Race Proportional Election Edge
**Hypothesis**: When a proportional election market prices one party at 75%+ but recent polls show the race within polling-error range, the market is systematically overconfident. The edge is on the "upset" side.
**Evidence needed**: 3+ proportional elections where pre-election polls showed a tightening race
**Entry signal**: Market > 75% for one outcome but recent polling aggregate shows the race within 5pp
**Active test**: Slovenia SDS NO ($100, resolves 2026-03-22). Market at 81% YES vs statistical tie in March polls.

---

## How to Add a New Strategy

1. Observe a pattern in 1–2 winning trades
2. Write a clear hypothesis (if X, then Y edge of Zpp)
3. Set status to TESTING
4. After 5 trades: calculate win rate and update status
5. After 10 trades: decide WINNING / UNDERPERFORMING / RETIRING
