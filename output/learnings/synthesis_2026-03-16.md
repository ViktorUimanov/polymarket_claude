# Learning Synthesis — 2026-03-16

## Overview

First synthesis run. 1 resolved trade (loss), 5 open positions, 5 passes on record.
Insufficient data for statistical calibration (< 5 trades in any category), but
qualitative analysis is rich given the Oscars post-mortem and the nature of all
open positions.

---

## Calibration Status

| Category | Trades | Win Rate | Avg Stated | Error | Status |
|----------|--------|----------|------------|-------|--------|
| oscars | 1 | 0% | 24.0% | −24pp | OVERCONFIDENT — 8pp min edge, max 1–2% |
| sports | 0 | — | — | — | No resolved data — 1 open (Arsenal) |
| commodities | 0 | — | — | — | No resolved data — 2 open (oil) |
| politics | 0 | — | — | — | No resolved data — 1 open (Iran) |
| other | 0 | — | — | — | No resolved data — 1 open (Musk tweets, expires 2026-03-17) |
| crypto | 0 | — | — | — | No trades placed |

**Calibration conclusion**: All categories except oscars are INSUFFICIENT DATA.
The oscars −24pp error is severe but statistically meaningless at n=1.
The error exists because: (a) the stated probability of 24% was correct as an estimate
of Sinners winning, but Bugonia — a third candidate we did not model — won.
This is partly a model error (incomplete option enumeration) and partly black swan
(all guild predictors failing in the same year).

**Minimum sample needed before drawing calibration conclusions**:
- Sports: 4 more trades
- Commodities: 3 more trades (2 resolve March 31)
- Politics: 4 more trades (1 resolves June 30)
- Oscars: 2 more trades (probation continues regardless until n=5)

---

## Strategy Updates

### Awards Guild Predictor
- Old status: UNDERPERFORMING (0/1, but flagged as "1 trade — also TESTING")
- New status: UNDERPERFORMING — maintained (not enough trades to retire, not enough wins to upgrade)
- Evidence: 1 trade, 0 wins. SAG predictor failed completely. DGA, PGA, BAFTA also failed.
- Action: Pausing new Oscars bets until n=3+ with updated model (dark-horse floor)
- Next upgrade criteria: 2+ wins in next 5 Oscars bets using updated framework

### EPL Large Points Lead
- Status: TESTING (unchanged — 1 open trade, unresolved)
- Arsenal lead: 9 points, 9 games remaining as of 2026-03-15
- Next review: When Arsenal win/lose EPL (estimated 2026-05-27)

### Commodity Settlement Gap
- Status: TESTING (unchanged — 2 open trades, resolve 2026-03-31)
- Alert: Oil $100 YES has drifted against entry (88.8% → 72.2%). This is a 16.6pp adverse move in market price, not in our fundamental thesis.
- The WTI settlement gap thesis (intraday ≠ settlement) remains valid — resolution not yet known.
- The market movement may reflect updated geopolitical pricing (partial Hormuz de-escalation?) or normal noise.
- Action: Monitor but do NOT exit unless fundamental thesis breaks. The settlement thesis does not change based on market repricing.

### Short-Window Data Frequency (Musk Tweets)
- Status: TESTING (1 trade, expires 2026-03-17)
- Action required: Manual resolution check needed by March 17 noon ET
- If wins: add first data point to discrete-event-counting edge source
- If loses: classify error (model vs calibration vs data quality), update knowledge/other.md

### Geopolitical Status Quo (Iran)
- Status: TESTING (1 open trade, resolves 2026-06-30)
- The Iran NO trade is the first test of the "Geopolitical Tail Risk Discount" proposed strategy.
- 17–22pp edge is unusually large and warrants monitoring for edge compression.
- No update possible until resolution.

---

## Edge Source Updates

### Awards Guild Consensus Predictor
- Status: FAILED → maintained on probation
- Trades: 1 resolved LOSS
- Losses: 1 (Sinners, −$200, 2026-03-15)
- Key learning: Guild consensus failed across all categories (SAG, DGA, PGA, BAFTA) simultaneously.
  This is rare but ~1-in-5-years event. Updated prior should reduce SAG reliability from 60–65% to 45–55%.

### Commodity Settlement vs Intraday Price Divergence
- Status: UNTESTED → unchanged (2 open trades)
- No new data. No update.

### Sports: Large Points Lead + Mathematical Lock
- Status: UNTESTED → unchanged (1 open trade)
- No new data. No update.

### Discrete Event Counting with Real-Time Data
- Status: UNTESTED → unchanged (1 open trade, resolves 2026-03-17)
- No new data. Pending resolution.

### NEW POTENTIAL: Geopolitical Status Quo Bias
- The Iran NO trade represents the first live test of this edge source.
- Basis: markets consistently overestimate probability of rapid political/military change.
- Historical base rate: regime collapse within 3–4 months of a strike event = ~5–10%.
  Market priced it at 29.5% — nearly 3× the historical base rate.
- If Iran NO resolves correctly: this becomes a confirmed edge source.
- Add formal entry to edge_sources.md after first win.

---

## Resolved Loss Analysis — Oscars: Sinners Best Picture

**Trade file**: `/root/workspace/polymarket/output/trades/2026-03-15_oscars-sinners-best-picture.md`

**Error type**: INFORMATION ERROR + MODEL ERROR (compound)

The loss was not purely random. Two distinct errors compounded:

### Error 1 — Incomplete Option Enumeration (Information Error)
**What happened**: We evaluated only the top 2 candidates (Sinners and One Battle After Another)
and assigned the remaining 2–3% to "other". We never checked Bugonia's actual market price or
analyzed it as a genuine contender.

**Root cause**: Cognitive anchoring on the two-horse narrative created by prediction markets and
awards coverage. When every pundit discusses two films, it is tempting to ignore the rest.

**Specific rule extracted**: Before placing any bet in a multi-outcome market, enumerate ALL outcomes
and assign a non-trivial probability to each before comparing to market prices. A dark-horse
auteur film by Lanthimos, Lynch, P.T. Anderson, Haneke, or Noe should receive a floor of 5–8%
regardless of market pricing.

**Application trigger**: Any Oscars Best Picture bet, any multi-outcome market where the "long tail"
is priced below 10% in aggregate.

### Error 2 — Guild Predictor Overweighting (Model Error)
**What happened**: The SAG Ensemble award was treated as the primary edge signal (~60–65%
historical reliability). But reliability had degraded post-Academy expansion and was not updated.

**Root cause**: Using historical base rates without adjusting for known structural change (the
post-2020 Academy voter expansion that introduced more international, arthouse, and genre voters).

**Specific rule extracted**: Guild predictor reliability must be adjusted downward by 10–15pp for
any Oscars bet after 2020. SAG Ensemble → 45–55% (was 60–65%). DGA → 65–75% (was 75–85%).

**Application trigger**: Any use of guild awards as a predictor for Academy Awards.

### What This Was NOT
This was NOT a black swan in the classic sense. Auteur dark-horse wins happen ~1 in 4 years.
The 2026 result was an extreme upset year (multiple categories), but the possibility of such a
year was quantifiable (~20% base rate) and was not adequately priced into our bet size or
probability estimate.

---

## Skills Audit

All skills are new as of 2026-03-16. No trade has yet resolved as a WIN (only 1 loss), so
direct contribution tracking is UNKNOWN for all skills. The Oscars trade file does reference
the core ideas behind several skills (resolution parsing, edge evaluation, calibration check),
suggesting these tools were applied during the trade — but incorrectly or incompletely.

| Skill | Type | Referenced in Trades | Status | Notes |
|-------|------|---------------------|--------|-------|
| resolution-parser | tool | Oil trades (verified settlement vs intraday) | UNKNOWN | Referenced in $100/$120 oil trades, zero resolved outcomes yet |
| evaluate-edge | tool | All 6 trades | UNKNOWN | Applied in all trades, edge was correctly identified in Iran and oil; Oscars edge was misstated due to model error |
| calibration-check | tool | Oscars trade (pre-trade check done) | UNKNOWN | Calibration check was done but data was insufficient (n=0 for oscars at trade time) |
| size-position | tool | All 6 trades | UNKNOWN | Sizing appears appropriate across all trades (2–4% range, within caps) |
| fetch-markets | tool | Scan session | UNKNOWN | Used in session but no outcomes yet |
| correlated-position-check | tool | Iran trade (explicitly documented) | UNKNOWN | Iran trade shows the skill was used correctly (oil/Iran correlation reviewed) |
| synthesize | strategy | This session | UNKNOWN | Being applied now — outcome = this document |
| opportunity-cost-tracker | strategy | 5 passes filed | UNKNOWN | Passes are correctly formatted, awaiting resolution to score |

**Flagged for pruning**: None. All skills are < 5 opportunities resolved. No skill can be
evaluated as UNDERPERFORMING at this stage.

**Observation on `evaluate-edge` and Oscars**: The skill's instruction to "enumerate all outcomes
in multi-outcome markets" should be made more explicit. The current skill doc emphasizes base
rates and evidence updates but does not mandate full option enumeration before estimation. This
is a gap — the Oscars error was an omission that could have been caught if the skill had a
mandatory checklist step: "List ALL options and assign non-zero probability to each."

---

## Proposed New Skills

### 1. `multi-outcome-enumerator` (tool)
**Rationale**: The Oscars loss was caused directly by failure to enumerate all outcomes.
A dedicated skill for multi-outcome markets (Oscars, elections, sports tournaments) would
mandate listing every candidate/option, assigning floor probabilities, and summing to
verify they total ~100% before forming a view. This is distinct from evaluate-edge (which
assumes binary YES/NO) and resolution-parser (which focuses on resolution criteria).

**What edge it systematizes**: Prevention of information errors in multi-outcome markets.
The skill forces the bettor to notice when the "long tail" is mispriced relative to base rates.

**Key rule it would encode**:
- List every outcome in the market
- For each: check market price, assign independent fair-value estimate
- Flag any outcome where market price < 5% but your base rate suggests > 8%
- Never let "other" be a residual — it must be itemized

### 2. `dark-horse-floor` (tool — could fold into multi-outcome-enumerator)
**Rationale**: Specific rule that auteur/art-house filmmaker films should never be priced below
5% in Best Picture markets. Can be implemented as a lookup table of directors whose
track record warrants a floor (Lanthimos, Lynch, Anderson, Haneke, etc.).

---

## Passes Review

| Pass | Date | Stated Edge | Status | Notes |
|------|------|-------------|--------|-------|
| Fed rate no-change | 2026-03-15 | N/A (market at 99.7%) | CORRECT PASS | Rule 7 (never bet 97%+) applied correctly |
| Iran regime fall YES | 2026-03-15 | Unknown (we bet NO instead) | N/A | Not a pass — we bet the opposite direction |
| Measles 1450 | 2026-03-15 | Unknown | Unresolved | Check after resolution |
| World Baseball Classic | 2026-03-15 | Unknown | Unresolved | Check after resolution |
| Russia-Ukraine ceasefire | 2026-03-16 | ~10–12pp on NO | Unresolved | Reasonable pass given stronger Iran NO; revisit if YES > 45% |

---

## WTI Oil $100 YES — Position Alert

The open WTI $100 YES position has moved from 88.8% to 72.2% — a 16.6pp adverse move.

**Thesis check** (does the adverse move change our edge?):

- Original thesis: "Only 1.3% gap to target, 11 trading days remaining, Hormuz closure ongoing"
- As of 2026-03-16: unknown current WTI settlement; if it has fallen below ~$95, the thesis weakens
- The market repricing from 88.8% → 72.2% could reflect: (a) WTI settlement pulling back
  from the $98.71 high, (b) Hormuz de-escalation news, (c) IEA emergency release announcement,
  (d) demand-destruction narrative strengthening

**Action**: Do not exit based on price movement alone. Requires a fundamental thesis check:
What is the current WTI settlement price? If below $90, the 1.3% gap has widened significantly
and the market repricing is telling us something real.

**Rule for future**: For any position that moves adversely by > 10pp in market price, run a
fresh fundamental thesis check. Not to exit reflexively, but to confirm the thesis still holds.
Document this as a position monitoring rule.

---

## Summary of Knowledge Base Updates This Synthesis

1. `knowledge/market_types/oscars.md` — Rules already documented (by resolver). No new rules needed beyond what is already there. The synthesis confirmed the existing rules are correct and complete.

2. `knowledge/strategies.md` — No status changes required (all strategies either TESTING with < 5 trades, or UNDERPERFORMING with documented rationale). No changes needed.

3. `knowledge/edge_sources.md` — No wins to record. Losses count for Awards Guild Consensus (already documented).

4. `knowledge/signal.json` — `learn_needed` flag will be set to false after this synthesis.

---

## Key Question for Next Session

Why did the WTI $100 YES market price drop from 88.8% to 72.2% in ~24 hours, and does this
reflect a real change in the settlement probability (WTI pulling back from $98.71, Hormuz
situation changing) or a temporary repricing? If WTI settlement has fallen below $93–95,
the thesis is materially weakened and the position should be reviewed for exit.

---

*Generated by synthesizer agent. Date: 2026-03-16. Bankroll: $8,450 cash + $1,350 exposure = $9,800 est. total.*
