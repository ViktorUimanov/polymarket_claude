Start a deep autonomous trading session. ralph-wiggum keeps this loop alive until the $100k goal is reached or this session's work is complete.

## Goal Check — Run First

```python
import json
b = json.loads(open('output/bankroll.json').read())
total = b['cash'] + b['open_exposure']
print(f"Portfolio: ${total:,.0f} / $100,000 goal")
```

**If total ≥ $100,000** → mission complete. Output:
```
GOAL_REACHED
```
Then write `output/reports/goal_reached.md` with final P&L breakdown and stop all crons.

---

## Session Workflow

If goal not yet reached, execute this checklist in order:

### Step 0 — Load state (required before anything else)
Read `knowledge/README.md` — this gives full situational awareness in one read.

### Step 1 — Resolve expiring positions
Check `knowledge/signal.json`:
```bash
python3 scripts/heartbeat.py   # refresh signal flags
cat knowledge/signal.json
```
If `resolve_needed: true` or any position in `expiring_soon`:
- Run `/resolve` before scanning for new opportunities

### Step 2 — Calibration check
```bash
python3 scripts/calibration.py --summary
```
Note any category with error < −10pp — apply stricter edge requirements (Rule 3).

### Step 3 — Market scan (if scan_needed: true)
Run `/scan`:
- Fetch markets, screen for edge ≥ 4pp, volume ≥ $5k
- Apply Golden Rules pre-trade checklist to every candidate
- Log to `output/reports/scan_{datetime}.md`

### Step 4 — Research top candidates
For each candidate with edge ≥ 4pp:
- Read `knowledge/market_types/<category>.md`
- Run `/research <market>`
- Check correlated exposure: `knowledge/skills/correlated-position-check.md`
- For vol > $50k: `python3 scripts/cross_platform.py --query "..." --my-prob X`

### Step 5 — Execute trades
For each approved trade:
1. Write `output/trades/{date}_{market}.md` with full reasoning (BEFORE executing)
2. Calculate size: `python3 scripts/kelly.py --fair-value X --market-price Y --confidence Z --bankroll B`
3. Execute on Polymarket
4. Update `output/positions.json`
5. Update `output/bankroll.json`
6. Record to DB: `python3 scripts/db.py` (via record_trade)

### Step 6 — Learn (if learn_needed: true)
Run `/learn` — synthesize recent outcomes into `knowledge/market_types/`.

### Step 7 — Report
Run `/report` if this is an end-of-day session or major trades were placed.

---

## Session Complete

When ALL applicable checklist items are done for this session, output exactly:
```
SESSION_COMPLETE
```

ralph-wiggum re-feeds this prompt if the session ends without a completion token.
The cron job will trigger the next session automatically.

---

## Completion Tokens

| Token | Condition | Effect |
|-------|-----------|--------|
| `SESSION_COMPLETE` | All signal flags handled, no more action needed | ralph stops this session; cron wakes next one |
| `<promise>I FINALLY EARNED</promise>` | Portfolio cash + open_exposure ≥ $100,000 (verified) | ralph stops permanently — mission complete |

### CRITICAL RULES for `<promise>I FINALLY EARNED</promise>`

- **NEVER output this token unless you have verified `cash + open_exposure ≥ 100000`**
- Run the check explicitly before outputting it:
  ```bash
  python3 -c "import json; b=json.loads(open('output/bankroll.json').read()); total=b['cash']+b['open_exposure']; print(f'Portfolio: \${total:,.0f}'); exit(0 if total >= 100000 else 1)"
  ```
- If the check fails (exit code 1), output `SESSION_COMPLETE` instead
- Do NOT output it as a farewell, summary, or sign-off — only as a verified goal confirmation
- Outputting it falsely wastes money by terminating a loop that should keep running
