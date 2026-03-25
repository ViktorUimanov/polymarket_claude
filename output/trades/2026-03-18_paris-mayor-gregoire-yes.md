# Trade: Paris Mayor Grégoire YES
**Date**: 2026-03-18
**Market ID**: 646003
**Market**: Will Emmanuel Grégoire win the Paris mayor election?
**Direction**: YES
**Entry price**: 71.5¢
**Size**: $200
**Shares**: 279.7 (~279)
**Bankroll at entry**: $6,427.30 (after OKC trade)
**Resolves**: ~2026-03-22 (runoff March 22, 2026)

---

## Pre-Trade Research

### Market Structure
- This is a **short-term bet**: runoff election is March 22, 2026 (4 days from now)
- Polymarket: 71.5% YES for Grégoire ($806k volume — large market)
- My fair value estimate: **80%**
- Edge: **8.5pp**
- Expected value: EV per $1 = $0.119 × $200 = **$23.80**

### Election Background
Paris holds a two-round municipal election. Round 1 was March 15, 2026.

**Round 1 results (actual votes counted):**
| Candidate | First Round % |
|-----------|--------------|
| Emmanuel Grégoire (PS / Left alliance) | **37.98%** |
| Rachida Dati (LR / MoDem / Bournazel merged) | 25.46% + ~11.34% (Bournazel list merge) = effective ~36.8% |
| Sophia Chikirou (LFI) | 11.72% (staying in Round 2) |
| Sarah Knafo (far-right) | 10.40% (withdrew → endorsing Dati) |
| Other candidates | ~3.1% |

**Runoff (Round 2) is a triangular race: Grégoire vs Dati vs Chikirou**

### Post-Round 1 Polling
**Elabe poll (most recent, post-R1):**
| Candidate | Round 2 Vote Share |
|-----------|------------------|
| Grégoire | **47.5%** |
| Dati | 37.5% |
| Chikirou | 15% |

→ Grégoire leads by 10pp in the actual runoff configuration.

**Head-to-head (hypothetical two-way Elabe):** Grégoire 51%, Dati 49% — very close in pure H2H, but Chikirou staying on the ballot is structurally favorable to Grégoire (draws votes from LFI pool that Dati wouldn't get anyway, while most LFI voters useful-vote for Grégoire over Dati).

### Key Factors Supporting Grégoire (80% win probability)
1. **12.5pp first-round lead**: Grégoire 37.98% vs Dati 25.46%
2. **Paris structural left majority**: Left-wing mayors since 2001 (Delanoë 2001, 2008; Hidalgo 2014, 2020)
3. **Left consolidation**: Chikirou (LFI, 11.7%) voters will largely useful-vote left (~75% → Grégoire)
4. **Bournazel-Dati merger: weaker than expected** — Bournazel withdrew himself from the merged list; centrist voters aren't guaranteed to follow Dati
5. **Knafo withdrawal (10.4%)**: ~70-80% of far-right voters go to Dati, but this is a 7-8pp boost at most
6. **Historical base rate**: First-round leader (+12pp) wins French municipal runoffs ~80-90% of the time
7. **2020 precedent**: Hidalgo led R1 over Dati by ~10pp and won the runoff comfortably

### Downside Risk Factors (Dati wins scenario — ~20%)
- If LFI voters stay with Chikirou or abstain (not useful-voting): Grégoire vote share stays ~42-44%
- If right-wing voter motivation is very high (Knafo GOTV message): Dati could hit 42-44%
- Near head-to-head in 2-way: 51-49 means the race is winnable for Dati if triangular dynamics shift

### Resolution Criteria Check
Market asks "Will Emmanuel Grégoire win the Paris mayor election?" — straightforward majority-vote resolution. In French municipal elections, Round 2 is by relative majority (most votes wins). No ambiguity.

### Category Compliance
- **Politics category**: Min edge 5pp ✓ (I have 8.5pp)
- **Politics cap**: 3% of $9,664 = $290 max. Using $200 ✓ (2.1%)
- **Correlation**: Paris municipal election is completely uncorrelated with Iran, Israel, US politics, or oil
- **Short horizon bonus**: Resolves in 4 days — faster capital recycling, avoids long-term uncertainty compounding

### Kelly Sizing
- Fair value: 80%, Market: 71.5%, Edge: +8.5pp
- Full Kelly: 29.8% ($1,953) — way too large
- 1/6 fractional: 5% ($327) — capped to politics limit
- Using $200 (2.1%) — conservative, accounts for uncertainty in French vote transfer behavior

---

## Decision Tree

- ✅ Edge ≥5pp (politics min): YES (8.5pp)
- ✅ Multiple data sources: YES (actual R1 vote counts + Elabe post-R1 poll + structural Paris left majority)
- ✅ Resolution criteria clear: YES (relative majority, no ambiguity)
- ✅ Within politics cap: YES ($200 < $290)
- ✅ No calibration penalty: YES (no resolved politics trades yet)
- ✅ Not correlated to existing positions: YES (Paris municipal ≠ Iran/Israel/US)

**Decision: BET $200 YES (Grégoire wins Paris runoff)**

---

## Exit Criteria
- **No action needed**: This resolves in 4 days (March 22). Hold to resolution.
- **Early exit if**: A major scandal breaks about Grégoire before March 22 (extremely unlikely in 4 days), OR unexpected poll shows Dati leading by 5pp+ (reassess)
- **Expected outcome**: WIN (Grégoire wins runoff ~80% probability)

---

## Resolution — 2026-03-22

**Outcome**: WIN
**Resolution**: Resolved YES — Emmanuel Grégoire elected Paris mayor, defeating Rachida Dati in the runoff
**P&L**: +$79.70
**Shares**: 279.7 × $1.00 = $279.70
**Net**: $279.70 - $200.00 = +$79.70

---

## Post-Resolution — WIN (+$79.70)

**Edge source**: Structural left-majority framework for Paris municipal elections. First-round leader (+12pp) combined with left vote consolidation (Chikirou's LFI voters useful-voting left) and Paris's 25-year unbroken left-wing governance record. Polymarket priced the race at 71.5% when structural base rate supports ~80%.

**Reproducible**: yes

**Added to edge_sources.md**: yes — "Structural incumbent advantage in French municipal runoffs: first-round leader +10pp in left-majority city at < 80% on Polymarket = long YES edge." Confirms Edge Source 7 (Electoral Framework — see below).

**What worked**:
1. Actual vote counts (R1 37.98% vs 25.46%) were superior to polling — used hard data not opinion
2. Structural left majority (Paris unbroken since 2001) correctly weighted as base rate
3. Vote transfer model (Chikirou LFI → useful-vote Grégoire) confirmed directionally correct
4. Short 4-day horizon eliminated long-run uncertainty and allowed tight Kelly sizing

**Note on Elabe March 20 final poll**: The 45.5% vs 44.5% final poll (1pp MoE, extremely tight) made this feel like a coin flip in final days. The actual result was a comfortable Grégoire win. Lesson: structural factors (25-year left dominance in Paris, 12pp R1 lead) dominate late-horizon "tightening" narrative polls. Market had drifted up to 83% pre-resolution, reflecting same realization.
