# Agent Entry Point

**Read this file first. Every session. One read = full situational awareness.**

Last updated: 2026-03-16

---

## Mission Status

| | |
|--|--|
| **Goal** | $100,000 total portfolio |
| **Starting bankroll** | $10,000 |
| **Cash** | $8,450 |
| **Open exposure** | $1,350 |
| **Total (est.)** | $9,800 |
| **Realized P&L** | −$200 (1 loss: Oscars) |
| **Progress to goal** | 0% (need +$90,200) |

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
| WTI Oil ≥ $100 | YES | 88.8% | $300 | 2026-03-31 | Check CME settlement daily |
| WTI Oil ≥ $120 | NO | 54.0% | $400 | 2026-03-31 | Check CME settlement daily |
| Arsenal EPL winner | YES | 89.5% | $300 | 2026-05-27 | Monitor weekly |
| Musk 300–319 tweets | YES | 28.5% | $150 | 2026-03-17 | **PAST END DATE — resolve** |
| Iran regime fall June | NO | 70.5% | $200 | 2026-06-30 | Monitor monthly |

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
| sports | 0 | — | — | No data — use category defaults |
| commodities | 0 | — | — | No data — 2 open trades |
| politics | 0 | — | — | No data — 1 open trade |
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

1. Read `knowledge/signal.json` — act on flags
2. Run `python3 scripts/calibration.py --summary`
3. If `resolve_needed`: run `/resolve` first
4. If `scan_needed`: run `/scan`
5. For each trade candidate: read `knowledge/market_types/<category>.md` before researching
6. After any trade: update `output/positions.json` and `output/bankroll.json`
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
| Settlement gap (commodities) | TESTING | — | Oil positions open |
| EPL large points lead | TESTING | — | Arsenal open |
| Status quo NO (geopolitical) | TESTING | — | Iran NO open |
| Guild predictor (awards) | UNDERPERFORMING | 0/1 | SAG failed vs Oscars 2026 |
