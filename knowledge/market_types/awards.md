# Awards Markets — Knowledge Base (General)

For Academy Awards specifics, see `knowledge/market_types/oscars.md`.
This file covers the awards category broadly: Oscars, BAFTAs, Grammys, Emmys, Golden Globes, BAFTA, etc.

## Category Profile

| Attribute | Value |
|-----------|-------|
| Variance level | EXTREME |
| Calibration status | OVERCONFIDENT — 1 trade, 0% win rate, −24pp error (Oscars 2026) |
| Max position size | **2% bankroll per bet** (hard cap — non-negotiable) |
| Min edge required | **8pp** (calibration probation — applies until 5+ trades with >0% win rate) |
| Current ban | None — but 2% cap and 8pp floor are enforced |

---

## Research Checklist (MANDATORY — run before every awards bet)

This checklist exists because the Oscars 2026 loss was caused by skipping step 3.

### Step 1 — Identify the full nominee list
- Do NOT rely on the market title or top-2 narrative
- Run: `python3 scripts/fetch_markets.py --search "<award category>" --limit 1` and check the `outcomes` field
- If outcomes are incomplete: WebSearch `"<year> <award> nominees complete list"`
- The actual winner is often NOT the market favorite

### Step 2 — Identify the voting body
- Academy Awards: ~10,000 expanded members (post-2020 expansion); more international, arthouse voters
- BAFTAs: UK-heavy membership; often diverges from US guilds
- SAG Awards: US guild actors only; strong bellwether but not infallible
- DGA: Directors only; strong predictor for directing categories, moderate for Best Picture
- Grammy: Recording Academy; ~12,000 members; wide taste range

### Step 3 — Run multi-outcome-enumerator (NON-NEGOTIABLE)
Use the `multi-outcome-enumerator` skill. Build a complete probability table:

| Nominee | Category Type | Predictor Signals | My Fair Value | Market Price | Edge |
|---------|--------------|------------------|---------------|--------------|------|
| (every nominee) | commercial / auteur / genre | guild wins, critic awards | X% | Y% | ±Zpp |

**Floor rules for fair-value assignment:**
- Any official nominee: minimum 1%
- Auteur filmmaker (Lanthimos, Lynch, P.T. Anderson, Haneke, Noe, Malick, von Trier): minimum 5–8% for Best Picture/Best Film
- Genre-crossover with massive cultural impact (Parasite, Chicago, Crash model): minimum 5%
- The full table MUST sum to ≤ 100%

### Step 4 — Check predictor reliability for this voting body

| Predictor | Category | Reliability (post-2020) |
|-----------|----------|------------------------|
| SAG Ensemble | Oscars Best Picture | 45–55% (was 60–65%) |
| DGA Director | Oscars Best Picture | 50–60% (was 65–75%) |
| DGA Director | Oscars Best Director | 65–75% (was 75–85%) |
| PGA | Oscars Best Picture | 50–60% (alone); 65%+ when combined with DGA |
| BAFTA Best Picture | Oscars Best Picture | 55–65% |
| SAG Actor/Actress | Oscars Lead Actor/Actress | 65–70% |
| Grammy Album of Year | — | No strong external predictor |

**Key post-2020 update**: Academy voter expansion introduced ~5,000+ new international members. This has increased variance across all categories and reduced the predictive power of US guild consensus.

### Step 5 — Check calibration before sizing
Run: `python3 scripts/calibration.py --category oscars`
If error < −10pp: require +2pp additional edge and reduce size by 25% (or apply 8pp minimum floor if on probation).

### Step 6 — Apply category size cap
Maximum 2% bankroll per award bet. No exceptions.
Require 8pp minimum edge while on calibration probation.

---

## Base Rates for Major Award Categories

### Oscars Best Picture
- Major upset year (frontrunner loses): ~1 in 5 years (20%)
- Auteur dark horse wins despite no guild sweep: ~1 in 4 years (25%)
- All guild consensus wins: ~1 in 3 years (33%)
- Actor sweep (same film wins acting + picture): ~1 in 8 years (12%)
- Genre film wins (horror, sci-fi, comedy, animation): ~1 in 6 years (17%)
- **Known upset year pattern**: In upset years, upsets cluster across categories (2026: ALL major categories went to underdogs)

### Oscars Best Director
- DGA winner takes Oscar: 65–75% (post-2020 expansion; was 75–85%)
- Non-DGA winner takes Oscar: 25–35%

### Grammy Album of the Year
- No reliable external predictor
- Treat as high-variance — avoid unless very strong price discrepancy (>15pp) is visible

### BAFTA Best Film
- Often predicts Oscars (55–65% alignment post-2020)
- Divergence from Oscars most common for: international films, genre films, prestige UK productions

---

## Resolution Criteria Notes

- Oscars: Academy members vote by secret ballot; winners announced at ceremony. No recounts.
- BAFTAs: Announced at ceremony in February (London). Typically 2–3 weeks before Oscars.
- Grammys: Recording Academy members vote. Announced at Grammy ceremony (January/February).
- Emmys: Television Academy members vote. Announced in September.
- Golden Globes: Hollywood Foreign Press Association (now expanded). Announced January.

**Key resolution pitfall**: Some Polymarket award markets resolve on the "winner announced on stage" moment, not on the final published results. Read resolution criteria carefully for any claim that a recount or error could affect.

---

## Category Cap Reminder

**Hard limit: 2% bankroll per award category bet.**

This cap is in effect because:
1. Extreme variance — even 90%+ consensus favorites lose (~1 in 5 years)
2. Calibration probation — 0% win rate on the only resolved trade
3. The 2026 Oscars demonstrated that all standard predictors can fail simultaneously

Even after calibration improves, do not exceed 2% until 10+ trades with a calibrated model.

---

## Known Black Swan Events

| Year | Award | What Happened |
|------|-------|---------------|
| 2026 | Oscars Best Picture | Bugonia (Lanthimos) won; ALL guild winners lost; every major category went to underdog |
| 2026 | Oscars Best Director | Chloe Zhao won; PTA was 92.5% favorite via DGA |
| 2022 | Oscars Best Picture | CODA won over The Power of the Dog (BAFTA/DGA winner) |
| 2006 | Oscars Best Picture | Crash late surge beat Brokeback Mountain |

---

## Calibration History

| Date | Market | Award | Stated % | Outcome | Error |
|------|--------|-------|----------|---------|-------|
| 2026-03-15 | Sinners Best Picture | Oscars | 24% | LOSS (Bugonia won) | −24pp |

Current: 0/1 (0% win rate vs 24% avg stated) = −24pp error
Status: **OVERCONFIDENT — PROBATION**
Action: 8pp minimum edge required. Max 2% per bet.
Graduation: Need 3+ wins in ≥5 trades before removing probation.
