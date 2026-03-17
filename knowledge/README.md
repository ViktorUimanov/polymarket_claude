# Agent Entry Point

**Read this file first. Every session. One read = full situational awareness.**

Last updated: 2026-03-17 22:45 UTC

---

## Mission Status

| | |
|--|--|
| **Goal** | $100,000 total portfolio |
| **Starting bankroll** | $10,000 |
| **Cash** | $7,609.30 |
| **Open exposure** | $2,055 |
| **Total (est.)** | $9,664.30 |
| **Realized P&L** | −$335.70 (Oscars −$200, WTI $100 exit −$56.10, Musk tweets −$150, Trump China exit +$70.40) |
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
| WTI Oil ≥ $120 | NO | 54.0% | $400 | 2026-03-31 | Thesis STRONG — settlement $93.50, needs +28% |
| WTI Oil $110 settlement | NO | 51.5% | $200 | 2026-03-31 | Thesis STRONG — settlement $93.50, needs +18% |
| Arsenal EPL winner | YES | 89.5% | $300 | 2026-05-27 | Monitor weekly |
| Iran ceasefire Apr 30 | NO | 60.5% | $200 | 2026-04-30 | Both sides maximalist — monitor weekly |
| Iran regime fall June | NO | 70.5% | $200 | 2026-06-30 | IRGC intact — monitor monthly |
| Iran regime fall 2027 | NO | 60.5% | $200 | 2026-12-31 | Succession smooth — monitor monthly |
| Slovenia SDS NO | NO | 19.0% | $100 | 2026-03-22 | **[RESOLVES MARCH 22] Check election results** |
| Ken Paxton TX Senate | YES | 38.5% | $170 | 2026-05-26 | Exit if Trump endorses Cornyn |
| US confirms aliens exist | NO | 84.5% | $200 | 2026-12-31 | Monitor quarterly |
| Colorado Avalanche Cup | YES | 21.6% | $85 | 2026-06-30 | Topped up $50 Mar 17. Sportsbooks 24-28%, at cap ($385 sports) |

**CLOSED this period:** WTI ≥ $100 YES — exited at 72.2¢ (entry 88.8¢), loss −$56.10. Bessent + IEA supply changed thesis.
**CLOSED this period:** Trump China YES — exited at 48.5¢ (entry 33.0¢), gain +$70.40. Trump requested delay; fair value dropped below market.
**RESOLVED LOSS:** Musk 300-319 tweets — resolved NO, loss −$150. Weekend slowdown; weekday extrapolation failed. Live data required.

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
| sports | 0 | — | — | No data — 2 open trades |
| commodities | 0 | — | — | No data — 2 open, 1 voluntary exit |
| politics | 0 | — | — | No data — 5 open, Slovenia resolves Mar 22 |
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
| Status quo NO (geopolitical) | TESTING | 0/0 | 3 Iran NOs open |
| Sportsbook vs Polymarket gap | TESTING | 0/0 | Avalanche Cup open |
| Tightening-race proportional election | TESTING | 0/0 | Slovenia SDS NO resolves Mar 22 — FIRST LIVE TEST |
| Short-window count frequency | TESTING | 0/1 | Musk tweets LOSS — revised: live data required |
| Guild predictor (awards) | UNDERPERFORMING | 0/1 | SAG failed vs Oscars 2026 |
