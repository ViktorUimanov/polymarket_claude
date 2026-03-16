---
name: resolution-parser
description: How to read and interpret Polymarket resolution criteria before placing any bet
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Resolution Parser Skill

**GOLDEN_RULES Rule 2**: Read the resolution criteria, not the title.
The market title and the resolution text often differ materially.

## Step-by-Step Process

### 1. Fetch the full description
```python
import urllib.request, json
m = json.loads(urllib.request.urlopen(
    f"https://gamma-api.polymarket.com/markets/{market_id}"
).read())
description = m.get("description", "")
print(description)
```

Or with the fetch script:
```bash
python3 scripts/fetch_markets.py --market-id <id>
# The description field contains full resolution criteria
```

### 2. Build the decision tree

For every market, answer these before forming a probability estimate:

**For YES resolution:**
- What EXACTLY must happen? (price level? specific date? specific source?)
- Which data source is used? (CME settlement vs intraday? AP call vs final count?)
- Is there a specific cutoff time or date?
- What if the event is ambiguous or delayed?

**For NO resolution:**
- Does NO resolve if YES criteria simply don't happen by deadline?
- Are there specific NO triggers (e.g., ceasefire agreement)?
- What happens if market resolves N/A?

**Edge cases:**
- What if data source is unavailable?
- Does partial resolution count?
- Is there an early resolution trigger?

### 3. Key Patterns to Watch For

| Title Says | Often Actually Means |
|-----------|---------------------|
| "WTI hits $100" | CME settlement price, not intraday |
| "Trump wins election" | AP call, not official certification |
| "Regime falls" | Requires all core structures to cease (high bar) |
| "Ceasefire" | Formal agreement signed, not just reported talks |
| "Best Picture" | Academy Award ceremony only, not critics' awards |
| "IPO before date" | First trading day, not filing date |

### 4. Commodities — Settlement vs Intraday (Rule 4)

**CRITICAL**: CME WTI settlement ≠ intraday price.
- Settlement is volume-weighted average near close
- Intraday high can exceed settlement by 20%+ during volatile sessions
- Example: March 9, 2026 — intraday $119.94, settlement $94.65 (−21%)
- **Never estimate settlement probability using intraday data**

### 5. Output Template

Before every bet, write this to your trade file:

```markdown
## Resolution Analysis

**Exact YES condition**: [quote directly from description]
**Data source**: [CME settlement / AP call / etc.]
**Cutoff**: [specific date/time]
**Edge cases identified**: [list any ambiguities]
**Decision tree check**: COMPLETE
```

## When This Skill Was Critical

- **Oil $100 market**: Title implied intraday; description specified CME settlement.
  Settlement systematically 15-25% below intraday during high-volatility days.
- **Oscars Best Picture**: Resolution criteria require Academy Award only —
  critics' awards and guild wins are NOT sufficient.
