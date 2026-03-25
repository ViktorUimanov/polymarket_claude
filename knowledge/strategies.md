# Strategies

Strategies are systematic patterns for finding edge. Each has a status, evidence base, and performance record.

**Statuses**: WINNING (>55% win rate, ≥5 trades) | TESTING (<5 trades) | UNDERPERFORMING (<45%, ≥5 trades) | RETIRING (0 wins last 5) | RETIRED

Last reviewed: 2026-03-18 session2 (end-of-day fourth synthesis pass — sportsbook gap extended to Lightning (5th trade); Italy WC NO added as new injury-adjusted-squad TESTING strategy; Trump China post-exit re-entry documented as bidirectional principal statement application; proposed rules-compliance-checker skill; all strategy statuses confirmed current)

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
**Status**: TESTING (4 active NO trades + 1 indirect, 0 resolved)
**Hypothesis**: During active conflicts, markets for "conflict resolution" (ceasefire, regime fall) are systematically underpriced at low probabilities, and "escalation" events are overpriced at high probabilities. The status quo has more inertia than markets price.
**Evidence needed**: 5+ geopolitical markets across multiple conflicts
**Entry signal**: "Conflict ends by X" at > 15%, regime survival at < 90% despite structural stability
**Active trades**: Iran regime fall June NO ($200, resolves 2026-06-30), Iran regime fall 2027 NO ($200, resolves 2026-12-31), Iran ceasefire April 30 NO ($200, resolves 2026-04-30). All entered at 17–29pp edge. Also Netanyahu out by June 30 NO ($150, resolves 2026-06-30) and Israel-Saudi normalize NO ($139, resolves 2026-12-31).
**Last updated**: 2026-03-18

### Sportsbook vs Polymarket Pricing Gap
**Status**: TESTING (5 active trades, 0 resolved — extended to golf, individual awards, large-volume NBA futures, and second NHL team)
**Hypothesis**: For sports futures and individual award markets, Polymarket systematically lags sportsbook consensus. The gap is largest on thin-volume markets (<$15k) where 3–4× mispricings occur. On high-volume team futures ($5M+), gap is 4–6pp. On thin award markets/golf, gap is 10–20pp. The gap persists because Polymarket's crypto-native user base discounts sports analytics vs sportsbook quant teams.
**Entry signal (large-volume team futures, $5M+)**: Sportsbook consensus (3+ books) > Polymarket price by ≥ 5pp — 1/6 Kelly, cap 1.5% bankroll
**Entry signal (golf / mid-volume, $50k-$5M)**: Sportsbook consensus (3+ books) > Polymarket price by ≥ 5pp AND multi-book agreement — cap 2% bankroll (single-event high variance)
**Entry signal (individual awards / thin, <$15k)**: Sportsbook consensus (3+ books) > Polymarket price by ≥ 10pp — size capped at $100 for liquidity
**Required check**: Sportsbooks must agree (not one outlier); analytics must confirm the signal is not sentiment-driven
**Active trades**:
  - Colorado Avalanche Stanley Cup YES ($235 total across 3 entries at avg 21.1¢ vs 25.7-27.8% sportsbooks, resolves 2026-06-30) — third entry 2026-03-18 ($150) on persistent gap
  - Scottie Scheffler Masters YES ($190 total, avg 17.64¢ vs 22% sportsbook consensus, resolves 2026-04-13) — initial $140 + $50 top-up on Players Champ healthy confirmation
  - Kucherov Hart Trophy YES ($100 at 5.6% vs 14-18% revised sportsbooks, resolves 2026-06-30) — thin market extension; HOLD, do not top up
  - OKC Thunder NBA YES ($120 at 37.5% vs 43.3% sportsbooks, resolves 2026-07-01) — first large-volume ($5M+) extension of strategy; standing trigger ≤38%
  - Tampa Bay Lightning Cup YES ($75 at 12.3% vs 18-20% sportsbooks, resolves 2026-06-30) — second NHL team; DK +400 (20%) vs PM 12.3%; +7.7pp gap; EC leaders 40-21-4; Kucherov 106pts; correlated with Avalanche (anti-correlated outcomes — both cannot win)
**Insight from Kucherov trade**: Gap is proportionally LARGER in thin individual award markets. Sportsbooks move faster — Kucherov gap narrowed from 3.5× to 2.5× after BET99 moved from +255 to +600, signaling MacKinnon became dominant. Validate sportsbook consensus is stable before entry in thin markets.
**Insight from Avalanche third entry**: Persistent gap after 3 entries confirms structural inefficiency (thin NHL market, no sharp arbitrageurs). Top-ups justified while sportsbooks maintain 5pp+ gap.
**Insight from OKC trade**: Gap exists even in large, efficient markets. Reigning champions with best record are systematically underpriced by Polymarket crowd (regression-to-mean anchoring).
**Insight from Lightning trade**: The same NHL structural inefficiency confirmed on a second team simultaneously. The entire Polymarket NHL board compresses teams toward the mean (~6.25% = 1/16 teams). Any EC/WC leaders with elite records and 18%+ sportsbook consensus are worth evaluating. NHL total YES exposure capped at $310 (Avalanche + Lightning) — do not add further NHL YES positions without one exiting or resolving first.
**Gap magnitude confirmed across market types**: thin individual awards (<$15k): 10-20pp; mid futures ($50k-$5M): 5-8pp; large futures ($5M+): 4-6pp.
**Last updated**: 2026-03-18 session2

### National Team Brand Premium vs Injury-Adjusted Squad Probability
**Status**: TESTING (1 active trade, 0 resolved — first test)
**Hypothesis**: National team tournament markets price the team's historical brand (FIFA ranking, reputation) rather than the specific squad available. When 5+ key players are confirmed injured in a short-window knockout tournament, injury-adjusted probability diverges significantly from market-implied probability, creating edge on the underdog side.
**Mechanism**: Market crowd applies a historical base rate for strong nations without rebuilding probability from the actual squad. Weak national bench depth (especially for defensive positions) is systematically underweighted. In two-game knockout formats, compounded probability drops faster than linear extrapolation suggests.
**Entry signal**: 5+ confirmed absences including 1+ key playmakers + two-game-or-more knockout format + market price for strong team YES > (injury-adjusted probability + 8pp) → bet NO (underdog to qualify/advance)
**Historical base rate check**: Italy missed 2018 WC (Sweden) and 2022 WC (North Macedonia). Brand does not guarantee qualification with a depleted squad.
**Active trades**: Italy WC NO ($150 at 39c, fair value 50% NO, resolves effectively March 26, 2026)
**First data point**: March 26, 2026 (Italy vs Northern Ireland semi-final)
**Last updated**: 2026-03-18 session2

## Proposed Strategies (Not Yet Tested)

### Tournament Early-Round Favorites
**Hypothesis**: In sports tournaments (World Cup, NBA playoffs, Champions League), early-round heavy favorites are systematically underpriced because casual bettors seek upsets.
**Evidence needed**: 5+ tournament markets
**Entry signal**: Implied probability > 85% for a team vs opponent with 2:1+ record advantage

### French Two-Round Election: First-Round Lead as Edge Signal
**Status**: TESTING (1 active trade, 0 resolved)
**Hypothesis**: In French two-round municipal elections, a candidate who leads Round 1 by 10+ pp wins the runoff approximately 80-90% of the time. Polymarket prices the runoff conservatively (underweighting the structural advantages of the R1 leader), creating systematic edge on YES for the frontrunner.
**Mechanism**: French voters in Round 2 consolidate behind the bloc leader. In triangular races with a left-wing third candidate, LFI voters useful-vote for the left frontrunner (~75%) rather than their candidate, widening the effective margin.
**Entry signal**: R1 leader margin ≥ 10pp AND structural bloc majority (left or right) AND post-R1 polling shows ≥ 5pp lead in triangular race AND market prices YES < 80%
**Active trades**: Paris Mayor Grégoire YES ($200, fair value 80%, market 71.5%, +8.5pp edge, resolves 2026-03-22)
**First data point**: Paris Mayor runoff March 22, 2026
**Last updated**: 2026-03-18

### Tightening-Race Proportional Election Edge
**Status**: TESTING — first live test INCONCLUSIVE (position exited before resolution; thesis invalidated by new polling data)
**Hypothesis**: When a proportional election market prices one party at 75%+ but recent polls show the race within polling-error range, the market is systematically overconfident. The edge is on the "upset" side.
**Evidence needed**: 3+ proportional elections where pre-election polls showed a tightening race (entry AND broader polling universe must confirm tightening)
**Refined entry signal**: Market > 75% for one outcome AND 3+ independent polls show the race within 5pp — single poll tightening is NOT sufficient
**What happened (Slovenia)**: Entered SDS NO at 19¢ based on one Ipsos poll (GS 24.1% vs SDS 23.2%). Exited at break-even 2 days later when 7 of 8 subsequent polls showed SDS ahead by 2-8pp. Market at 81% was approximately correctly priced.
**Lesson**: The hypothesis is not invalidated — a single outlier poll was not a valid entry signal. Must require polling consensus before entry.
**Trades**: 1 inconclusive exit (Slovenia SDS NO, $0 P&L, 2026-03-18 — thesis invalidated, not resolved)
**Last updated**: 2026-03-18

---

## How to Add a New Strategy

1. Observe a pattern in 1–2 winning trades
2. Write a clear hypothesis (if X, then Y edge of Zpp)
3. Set status to TESTING
4. After 5 trades: calculate win rate and update status
5. After 10 trades: decide WINNING / UNDERPERFORMING / RETIRING
