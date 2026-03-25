# Agent Entry Point

**Read this file first. Every session. One read = full situational awareness.**

Last updated: 2026-03-23 ~17:00 UTC (SESSION: Resolve=0 resolutions. Scan complete. No new trades — politics (10/10) + commodities caps both full. KEY UPDATES: Iran ceasefire NO adverse -13.5pp (entry 60.5%, now 47% NO) — Iran DENIED talks occurred, FV revised to 60-70% NO, still +13-23pp edge, HOLD. Oil $90 YES recovered to 82.2% YES (WTI at $98.23, never CME-settled below $90). Denmark Frederiksen YES resolves TOMORROW Mar 24 — hold. PRIORITY QUEUE: After Denmark resolves, enter "Military action continues through March 31 YES" at 82% (+6-12pp edge, politics slot opens). Oil $105 NO +38pp favorable. 20 open positions.)

---

## Mission Status

| | |
|--|--|
| **Goal** | $100,000 total portfolio |
| **Starting bankroll** | $10,000 |
| **Cash** | $6,956.70 |
| **Open exposure** | $3,557.80 |
| **Total (est.)** | $10,514.50 |
| **Realized P&L** | +$514.52 (Oscars −$200, WTI $100 exit −$56.10, Musk tweets −$150, Trump China YES exit +$70.40, Slovenia exit $0, Oil-120 exit +$133.33, Hungary Fidesz exit $0, Kucherov exit +$578.57, Trump China NO exit +$64.45, Paris Mayor WIN +$79.70, **F1 Russell NO exit −$5.83**) |
| **Progress to goal** | 0% (need +$90,256) |

---

## Signal — Check Before Acting

```bash
cat knowledge/signal.json
```
Or read it directly. Flags set by heartbeat every 13 min:
- `scan_needed` → run `/scan`
- `resolve_needed` → run `/resolve` first
- `learn_needed` → run `/learn`
- `expiring_soon` → check those positions immediately

---

## Open Positions

| Position | Direction | Entry | Size | Ends | Alert |
|----------|-----------|-------|------|------|-------|
| ~~F1 George Russell 2026 champion~~ | ~~NO~~ | ~~44.5%~~ | ~~$260~~ | ~~2026-11-22~~ | **EXITED Mar 23 at -$5.83.** Post-Chinese GP: SB upgraded Russell to -125 (58% implied). PM 56.5% vs SB 58% = 1.5pp gap (exit rule: within 5pp). Edge source eliminated. Small loss accepted over holding directional with no edge. Russell then WON Australian GP — great exit timing. |
| **Kimi Antonelli F1 2026 champion** | **YES** | **17.8%** | **$200** | **2026-12-06** | **NEW Mar 23.** Antonelli WON Chinese GP (Race 2). Russell leads by only 4pts. Mercedes dominant (1-2 both races). PM at 17.8% = stale vs sportsbook ~25-28%. FV 28-35%. +14.2pp edge (mid). EXIT if PM hits 30%+ and gap <5pp, or gap inverts >10pp. Edge Source 5: sportsbook-PM lag. |
| Denmark PM Mette Frederiksen | YES | 80% | $200 | 2026-03-24 | **NEW Mar 23.** Danish election: red bloc won 90 seats (majority). Frederiksen confirmed next PM. FV 95% YES, market 80%, +15pp edge. Resolves 24-48h. EXIT trigger: resolves automatically on PM confirmation. |
| WTI Oil $105 HIGH | NO | 36.5% | $186 | 2026-03-31 | Market now 58.9% NO (+22.4pp from entry). WTI ~$98 after recovering from $90.10 intraday low. Trump POSTPONED strikes 5 days (until ~March 28). Settlement $105 requires +7% gain in 8 days — essentially impossible. FV 72-78% NO. HOLD. EXIT only if CME settlement CLOSES above $102. |
| WTI Oil $110 settlement | NO | 51.5% | $200 | 2026-03-31 | Market now 77.9% NO (+26.4pp from entry). Excellent. WTI $98 vs $110 threshold = +12.2% required in 8 days. Thesis STRONG. |
| Arsenal EPL winner | YES | 89.5% | $300 | 2026-05-27 | CL QF draw vs Bodo/Glimt or Sporting. Monitor weekly |
| Iran ceasefire Apr 30 | NO | 60.5% | $200 | 2026-04-30 | Market drifted to 52.5% NO (adverse -8pp). Trump's 5-day pause adds uncertainty. FV revised to 65-75% NO. Still +12-20pp edge. HOLD. |
| Iran regime fall June | NO | 70.5% | $200 | 2026-06-30 | IRGC intact — monitor monthly |
| Iran regime fall 2027 | NO | 60.5% | $200 | 2026-12-31 | **WATCH: market drifted 5pp against us** — monitor |
| Ken Paxton TX Senate | YES | 38.5% avg | $460 | 2026-05-26 | **Topped up $290 Mar 18.** FV upgraded to **67%** (Mar 22 session: new Mar 7-8 poll Paxton 49-41 w/o endorsement). +28.5pp edge. Exit if Trump endorses Cornyn AND Cornyn polls >40% |
| US confirms aliens exist | NO | 84.5% | $200 | 2026-12-31 | Monitor quarterly |
| Colorado Avalanche Cup | YES | 21.1% avg | $235 | 2026-06-30 | **Topped up $150 Mar 18.** Total 1,114 shares. Sportsbooks 24-28%. Best NHL record (95 pts). |
| Scottie Scheffler Masters | YES | 17.64% avg | $190 | 2026-04-13 | Topped up $50 Mar 18 (Players Champ: healthy). **Gap CLOSED: PM 21% vs sportsbooks 22-25% (1-4pp only).** Hold only, NO further top-ups. Monitor withdrawal before Apr 9. |
| Netanyahu out by June 30 | NO | 85.5% | $150 | 2026-06-30 | War rally protecting him. Budget vote on track. |
| Netanyahu out by End 2026 | NO | 52.5% | $125 | 2026-12-31 | **NEW Mar 22.** Market drifted to 42.5% NO (adverse -10pp). Thesis intact: no-confidence impossible (61 votes needed). War rally. FV 81% NO = massive +38.5pp edge now. HOLD. |
| Greenland sovereignty NO | NO | 90.3% | $193 | 2026-12-31 | **NEW Mar 18.** Legal process impossible in 2026. Monitor monthly. |
| ~~Kucherov Hart Trophy~~ | ~~YES~~ | ~~5.6%~~ | ~~$100~~ | ~~2026-06-30~~ | **EXITED Mar 22 at +$578.57.** PM 41.6% vs sportsbooks 27% — gap inverted 15pp. Exit at ~38¢ avg. |
| Israel-Saudi normalize NO | NO | 79.5% | $139 | 2026-12-31 | **NEW Mar 17.** Iran war + Palestinian block. Inversely correlated w/ Iran NOs. Monitor monthly. |
| OKC Thunder NBA YES | YES | 37.5% | $120 | 2026-07-01 | **11-game win streak, record 56-15.** SB +125/+135 (42-44%). PM 37.5%. Gap 4.5-6pp. Exit at 50%+. Top-up only if ≤32% AND gap ≥8pp. |
| ~~Paris Mayor Grégoire YES~~ | ~~YES~~ | ~~71.5%~~ | ~~$200~~ | ~~2026-03-22~~ | **RESOLVED WIN +$79.70 (2026-03-22 21:00 UTC).** Grégoire elected Paris mayor defeating Dati. Thesis confirmed: structural left majority + R1 lead +12pp dominated. Rule 13 confirmed. |
| Tampa Bay Lightning NHL Cup | YES | 12.3% | $75 | 2026-06-30 | **NEW Mar 18.** DK +400 (20%) vs PM 12.3%. +7.7pp gap. EC leaders 40-21-4. Kucherov 106pts. NHL YES total: $310 |
| Italy 2026 WC Qualifying | NO | 39% | $150 | 2026-04-12 | **8 injuries: Verratti, Di Lorenzo, Calafiori, Udogie, Rovella, Leoni, Gabbia, Tonali (in squad but <100%).** Chiesa returning (match sharpness risk). P(qualify) ~40-46%. Semi-final vs Northern Ireland March 26 effectively resolves. |
| WTI Oil $90+ settlement | YES | 76.5% | $34.80 | 2026-03-31 | **NEW Mar 23.** WTI $98.23 must drop 8.4% in 8 days to lose. Iran war + Hormuz closure = structural floor. FV 94%. +17.5pp edge. Fills commodities cap. |
| ~~Trump visits China by Apr 30~~ | ~~NO~~ | ~~60.5%~~ | ~~$150~~ | ~~2026-04-30~~ | **EXITED Mar 22 session2 at +$64.45.** Market (86.5% NO) overshot fair value (75% NO) by 11.5pp — negative EV from current price. Holding above FV destroys edge. |
**CLOSED this session (Mar 18, session10):** Hungary Fidesz YES — exited at break-even ($0 P&L). Tisza 14-20pp lead in independent polls triggered 10pp exit threshold. Structural mechanism (~8-10pp) cannot overcome that margin.
**CLOSED earlier (Mar 18, session9):** Oil-120 NO — exited at +$133.33 gain (+18pp). Position had 0pp remaining edge (WTI at $96 vs $120 threshold). Capital recycled into Oil-105 NO (+39.5pp edge, same expiry).
**CLOSED earlier (Mar 18):** Slovenia SDS NO — exited at break-even ($0 P&L). Original thesis (one poll showing statistical tie) invalidated by 7/8 polls showing SDS +5-8.6pp lead. Capital redeployed.
**CLOSED Mar 17:** Trump China YES — exited at 48.5¢ (entry 33.0¢), gain +$70.40.
**CLOSED Mar 16:** WTI ≥ $100 YES — exited early, loss −$56.10.
**RESOLVED LOSS:** Musk tweets — resolved NO, loss −$150.

```bash
python3 scripts/portfolio.py   # MTM valuations + alerts
```

---

## Calibration State

```bash
python3 scripts/calibration.py --summary
```

| Category | Trades | Win% | Error | Status |
|----------|--------|------|-------|--------|
| oscars | 1 | 0% | −24pp | OVERCONFIDENT — 8pp min edge, max 2% |
| other | 1 | 0% | −38pp | OVERCONFIDENT — 8pp min edge, max 2% |
| sports | 0 | — | — | No data — 7 open trades (Arsenal, Avalanche, Scheffler, Kucherov, OKC Thunder, Lightning, Italy WC NO) |
| commodities | 0 | — | — | No data — 2 open ($120 NO + $110 NO), resolve 2026-03-31 |
| politics | 1 | 100% | +9.5pp avg | Paris Mayor WIN (80% stated, WIN). 10 open trades. |
| crypto | 0 | — | — | No data |

---

## Golden Rules (Critical — Apply Every Trade)

**Pre-trade:**
1. **CHECK ALL OPTIONS** — list every outcome before forming a view (Oscars lesson: Bugonia at 2% won)
2. **READ RESOLUTION CRITERIA** — title ≠ resolution text. Build YES/NO decision tree.
3. **CHECK CALIBRATION** — `python3 scripts/calibration.py --category <cat>` before sizing
4. **SETTLEMENT ≠ INTRADAY** — CME settlement can be 20% below intraday high (oil lesson)
5. **4pp minimum edge** — no exceptions. Transaction costs eat anything less.
6. **CORRELATED EXPOSURE** — max 10% bankroll in one macro scenario
7. **NEVER BET AT 97%+** — no edge, only downside

**Sizing:**
8. Category caps: politics 3% | awards 2% | single-game sports 2% | commodities 4%
9. Fractional Kelly only: high confidence → 1/4K | medium → 1/6K | low → 1/10K
10. Losing streak (3+ losses in cat): require 8pp edge, max 2% size

**Research:**
11. Status quo wins ~70% of "will X change?" markets — start there
12. Guild predictors weakened post-2020 Academy expansion — give dark horses 5–8% floor
13. Cross-platform check for vol > $50k: `python3 scripts/cross_platform.py --query "..." --my-prob X`

**Learning:**
14. **POST-MORTEM EVERY LOSS immediately** — classify error, extract rule, update `knowledge/market_types/<cat>.md`

Full rules: `knowledge/GOLDEN_RULES.md`

---

## What To Do This Session

Every session runs the full cycle — all steps, every time:

1. If `resolve_needed` → run `/resolve` first
2. **Always run `/scan`** — every session, regardless of `scan_needed` flag. Find edge. Try new angles.
3. If `learn_needed` → run `/learn`
4. After any trade: update `output/positions.json` and `output/bankroll.json`

Scanning is never optional. The goal is continuous research.
7. Check goal: `python3 -c "import json; b=json.loads(open('output/bankroll.json').read()); print(b['cash']+b['open_exposure'])"`

## Active Monitoring Triggers (Next 7 Days)

| Date | Event | Action |
|------|-------|--------|
| ~~Mar 22~~ | ~~Paris Mayor runoff~~ | **RESOLVED WIN +$79.70.** Grégoire elected. |
| Mar 26 | Italy vs Northern Ireland | Italy WC NO $150 open. **Bradley (NI) OUT for season.** P(qualify)~45% = 55% NO. Market at 34% NO (further in our favor vs 39% entry). Check final squad March 25. If Italy lose semi → position wins immediately. |
| Mar 23–24 | Trump endorsement (Paxton/Cornyn) | **No endorsement yet as of March 23.** Paxton market moved to 43.5% (+5pp favorable). FV still 67%. EXIT if Trump endorses Cornyn AND Cornyn polls >40%. |
| ~~Mar 23 TONIGHT~~ | ~~Trump Hormuz ultimatum expires~~ | **SUPERSEDED: Trump postponed strikes 5 days (until ~March 28).** WTI crashed to $90.10 intraday, recovered ~$98. Oil $105/$110 NO thesis STRENGTHENED. CME settlement today — verify Oil $90 YES status. |
| **Mar 28** | **Trump's 5-day Iran pause expires** | New critical date. Watch: deal announcement = Iran ceasefire NO stress test. Breakdown = Oil $105/$110 NO WINS faster. Either way, hold oil NOs through March 31. |
| Mar 31 | WTI oil settlement | Both oil NOs + $90 YES resolve. FV: $105 and $110 NO WIN; $90 YES WIN. |
| Mar 31 | Israel budget vote (2nd + 3rd reading) | Coalition has 62-55 votes — should pass. No action unless fails. |
| Apr 9-13 | Masters Tournament | Scheffler YES $190 open. Trigger already executed (Players Champ top-up done). No further top-ups. |
| Every session | OKC Thunder NBA price | OPEN ($120 YES at 37.5%). Exit if rises to 50%+. No additional entry unless drops to 32% and sportsbook gap ≥8pp. |
| Apr 12 | Hungary parliamentary election | CLOSED — Fidesz YES exited at break-even. Exit condition triggered (Tisza 14-20pp lead). No open position. |
| **Mar 24** | **Denmark PM Frederiksen YES** | **OPEN $200 at 80¢.** Election resolves March 24. Market at 86¢ YES. Hold — if red bloc wins, resolves YES at +$50 gain. |
| Mar 23 | **NCAA March Madness** | Houston gap CLOSED (PM 10.5% vs SB 8.3-9.1%). PASS. Michigan gap 3.9pp. PASS. |
| ~~F1 races~~ | ~~F1 Russell NO~~ | **EXITED Mar 23** — gap closed (SB 58% vs PM 56.5% = 1.5pp). Loss -$5.83. |
| Next session | McIlroy Masters YES | PASS — gap closed to 1-3pp. Below 5pp golf minimum. Revisit only if PM drops below 7%. |
| **Next session** | **Antonelli F1 YES** | **OPEN $200 at 17.8¢.** Exit if PM hits 30%+ and gap narrows to <5pp vs sportsbooks. Monitor after each GP race. |
| Next session | Scheffler Masters top-up | PASS — gap CLOSED to 1-4pp (PM 21% vs sportsbooks 22-25%). Below 5pp minimum. Hold existing $190 only. Revisit only if gap reopens to 5pp+. |
| Next session | US Recession 2026 | PASS this session — politics MAXED. PM 31% YES, expert range 30-49%. Edge ambiguous. Revisit when politics budget rebalances (after Paris Mayor + Trump China close). |
| Next session | Carolina Hurricanes NHL Cup | BLOCKED — NHL YES cap at $310 (Avalanche $235 + Lightning $75). Need one of those to exit first AND confirm 3rd sportsbook. Revisit if Avalanche or Lightning exits. |
| Apr 7 | **Arsenal UCL QF vs Sporting CP** | Arsenal drew Sporting CP — favorable draw (vs PSG/Bayern/Real Madrid alternatives). First leg Apr 7, second leg Apr 15. Strengthens Arsenal EPL YES thesis (manageable schedule congestion). UCL Winner market gap was only 3.3pp as of last check — below 5pp threshold. Revisit if gap reopens to 5pp+. |
| Mar 31 (QUEUED) | **Oil $100 YES — STANDING ORDER** | **QUEUE**: Oil $100 YES at 74.2% — fair value 85-92%, edge 11-18pp. WTI hit **$99.67 intraday Mar 22** (within $0.33 of trigger). ENTER immediately when Oil $105 or $110 NO resolves on March 31 and frees commodities cap. Size: ~$150 (1/4 Kelly at 85% FV). |
| ~~Mar 22 (QUEUED)~~ | ~~**Netanyahu End-2026 NO — QUEUED**~~ | **EXECUTED Mar 22 session6: $125 at 52.5¢ NO. Edge +28.5pp (FV 81% NO). Correlation-discounted. 18 open positions now.** |
| ~~Mar 22 tonight~~ | ~~**Slovenia SDS YES — MONITOR**~~ | **RESOLVED — NO POSITION TAKEN.** Svoboda (Freedom Movement) won: 28.54% vs SDS 28.19% (0.35pp margin). SDS YES would have been a LOSS. Pre-election polls (7/8 showing SDS +5-8.6pp) were WRONG by 5-9pp. **CALIBRATION**: Slovenian polls systematically overestimated SDS. Our break-even exit on SDS NO was the right procedural call. The original SDS NO thesis was directionally correct — we just exited too early based on biased polls. Rule 11 addendum added to politics.md. |

---

## Portfolio-Level Trigger Monitor

Correlated position review triggers. Act immediately when any trigger fires — do not wait for next scheduled session.

| Trigger Event | Positions Affected | Immediate Action |
|--------------|-------------------|-----------------|
| Iran-US ceasefire announced | Iran ceasefire NO ($200), Iran regime June NO ($200), Iran regime 2027 NO ($200), Trump China NO ($150) | Exit all four if revised FV within 5pp of market price |
| Iran regime change (new Supreme Leader + IRGC shift) | Iran regime June NO ($200), Iran regime 2027 NO ($200) | Immediate exit both; re-assess Israel-Saudi NO ($139) |
| Trump endorses Cornyn AND Cornyn polls >40% | Paxton YES ($460) | EXIT full position |
| Trump on-record confirms China visit before April 30 | Trump China NO ($150) | Immediate EXIT |
| Paris Mayor runoff result (March 22) | Paris Mayor YES ($200) | **ALERT: Elabe final poll 45.5% vs 44.5% — much tighter than expected. Revised FV 60-65%.** Record calibration after result. |
| Arsenal lead drops to ≤5 points | Arsenal EPL YES ($300) | Review immediately; may exit |
| WTI settlement ≥$110 on March 31 | WTI $110 NO ($200) | Position loses; record calibration LOSS |
| WTI settlement ≥$105 on March 31 | WTI $105 NO ($186) | Position loses; record calibration LOSS |
| Italy lose March 26 semi-final | Italy WC NO ($150) | Position wins; record calibration WIN |
| OKC Thunder price rises to 50%+ | OKC Thunder YES ($120) | EXIT to lock gain |
| Hungary polls: Tisza gains to 10+pp lead (multiple independent polls) | ~~Hungary Fidesz YES ($80)~~ CLOSED | EXIT executed at break-even — trigger fired Mar 18 session10 |
| F1 SB-PM gap within 5pp | ~~F1 Russell NO ($260)~~ CLOSED | **EXITED Mar 23** — gap closed to 1.5pp, loss -$5.83 |

---

## Per-Category Knowledge

Before researching any market, read the relevant file:

| File | Key Rule |
|------|----------|
| `market_types/oscars.md` | Never >80% on any winner; dark horses real; calibration probation |
| `market_types/sports.md` | Points lead math, head-to-head, injury check |
| `market_types/commodities.md` | CME settlement mechanics, WTI vs Brent, Rule 4 |
| `market_types/politics.md` | Status quo bias (Rule 11), polling aggregators, base rates |
| `market_types/crypto.md` | On-chain data, regulatory catalysts, price patterns |

---

## Key Scripts

```bash
python3 scripts/heartbeat.py                    # update signal.json
python3 scripts/calibration.py --summary        # calibration state
python3 scripts/fetch_markets.py --min-volume 5000 --limit 50   # market scan
python3 scripts/kelly.py --fair-value X --market-price Y --confidence medium --bankroll Z
python3 scripts/check_resolutions.py            # check open positions
python3 scripts/cross_platform.py --query "..." # external probability check
```

---

## Active Strategies

| Strategy | Status | Win Rate | Notes |
|----------|--------|----------|-------|
| Settlement gap (commodities) | TESTING | 0/0 | 2 open oil NOs resolve Mar 31 |
| EPL large points lead | TESTING | 0/0 | Arsenal open, resolves May |
| Status quo NO (geopolitical) | TESTING | 0/0 | 5 trades: 3 Iran NOs + Netanyahu NO + Israel-Saudi normalize NO |
| Sportsbook vs Polymarket gap | ACTIVE (1 early exit win) | 1/0 early | Kucherov exit +$578.57 (gap inverted). 5 open: Avalanche, Scheffler, OKC Thunder, Lightning, **F1 Russell NO (new)**. **New rule: exit when gap inverts >10pp** |
| French two-round election | TESTING | 0/0 | Paris Mayor Grégoire YES — first data point Mar 22 |
| National team injury-adjusted squad | TESTING | 0/0 | Italy WC NO $150 — 7 injuries, resolves effectively Mar 26 |
| Tightening-race proportional election | TESTING | 0/0 | Slovenia exit inconclusive — entry signal tightened to 3+ polls |
| Structural Electoral Mechanism Discount | CAUTION | 0/0 | Hungary Fidesz EXIT break-even — thesis invalidated by wider poll lead than modeled. Rule: require polling composite, don't enter at theoretical tipping point. Revisit only with firmer margin evidence. |
| Short-window count frequency | TESTING | 0/1 | Musk tweets LOSS — revised: live data required |
| Guild predictor (awards) | UNDERPERFORMING | 0/1 | SAG failed vs Oscars 2026 |
