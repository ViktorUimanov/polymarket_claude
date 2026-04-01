---
name: polymarket-signals
description: Discover which Polymarket markets other agents are actively trading via the AI-Trader signal feed. Use as lead-generation for scan — never copy trades.
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-25
---

# Polymarket Signal Feed — Market Discovery

Use the AI-Trader signal feed to discover which Polymarket markets other agents are actively trading. This is **lead-generation only** — never copy trades. We do our own research on any market we find here.

## When to Use

- During scan, as an additional market discovery source alongside volume-based search
- When a market surfaces here that we haven't looked at: add it to the research queue
- Token IDs in the feed can be cross-referenced with the CLOB API to identify the market

## Command

```bash
python3 scripts/market_intel.py --signals
```

## Extracting Market IDs from Signals

Token IDs in the feed map to Polymarket CLOB token IDs. To identify the market:

```python
import requests

# Get market from token_id
token_id = "43405923061432342444068280231425984241466554526190162032713551250996348746557"
r = requests.get("https://gamma-api.polymarket.com/markets", params={"clob_token_ids": token_id}, timeout=10)
markets = r.json()
if markets:
    print(markets[0]["question"])
```

Or use the CLOB API directly:
```bash
curl "https://clob.polymarket.com/book?token_id=TOKEN_ID"
```

## Signal Types to Watch

| signal_type | meaning |
|-------------|---------|
| `realtime` | Active trade being executed now — market is liquid |
| `strategy` | Discussion only — less time-sensitive |
| `[Copied from X]` | Copy trade — ignore, it's derivative |

## Rules

1. **Never copy a trade** — even if an agent has a great track record on this platform
2. **Use token_id to identify the market**, then run our own research (`/research <market>`)
3. **Arbitrage signals** (two-leg trades, Chinese-language) are usually 2-market arbitrage plays — skip unless we independently see edge on one leg
4. **Filter noise**: most activity is a handful of agents copying each other — look for unique signals, not crowd consensus

## Integration with Scan

After running `--signals`, cross-reference any Polymarket token IDs against our open positions. If a market we don't hold appears multiple times from independent agents (not copies), add it to the research queue for the current scan session.
