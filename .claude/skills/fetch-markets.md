---
name: fetch-markets
description: How to efficiently fetch and filter Polymarket market data using the Gamma API and local scripts
type: tool
performance:
  uses: 0
  wins_contributed: 0
  losses_contributed: 0
  status: ACTIVE
  last_reviewed: 2026-03-16
---

# Fetch Markets Skill

## Quick Commands

```bash
# Scan top markets by volume
python3 /root/workspace/polymarket/scripts/fetch_markets.py --min-volume 5000 --limit 50

# Filter by category
python3 /root/workspace/polymarket/scripts/fetch_markets.py --category sports --min-volume 3000
python3 /root/workspace/polymarket/scripts/fetch_markets.py --category commodities --min-volume 2000

# Search by keyword
python3 /root/workspace/polymarket/scripts/fetch_markets.py --search "oil" --min-volume 1000
python3 /root/workspace/polymarket/scripts/fetch_markets.py --search "Champions League"

# Get specific market by ID
python3 /root/workspace/polymarket/scripts/fetch_markets.py --market-id 1467766

# Price only (for portfolio marking)
python3 /root/workspace/polymarket/scripts/fetch_markets.py --market-id 1467766 --price-only

# Raw JSON output
python3 /root/workspace/polymarket/scripts/fetch_markets.py --search "bitcoin" --json
```

## Direct API (if script unavailable)

```python
import requests, json

# Top markets by volume
r = requests.get("https://gamma-api.polymarket.com/markets", params={
    "active": "true", "closed": "false",
    "limit": "50", "order": "volumeNum", "ascending": "false"
})
markets = r.json()
for m in markets:
    prices = json.loads(m['outcomePrices'])
    print(f"{m['question'][:60]} | YES: {float(prices[0])*100:.1f}% | Vol: ${m['volumeNum']:,.0f}")
```

## Key Fields

| Field | Type | Description |
|-------|------|-------------|
| `question` | string | The market question |
| `outcomePrices` | JSON string | `[YES_price, NO_price]` in decimal (0.888 = 88.8%) |
| `outcomes` | JSON string | `[YES_label, NO_label]` |
| `volumeNum` | float | Total USD volume |
| `liquidityNum` | float | Current liquidity |
| `endDateIso` | string | UTC resolution date |
| `description` | string | Full resolution criteria — ALWAYS READ |
| `resolved` | bool | True if market is closed |
| `id` | string | Market ID for API calls |
| `slug` | string | URL-friendly identifier |

## Common Gotchas

- `outcomePrices` is a **JSON string**, not an array — must parse with `json.loads()`
- `endDateIso` is UTC — note when converting to local time for display
- Binary markets have 2 outcomes; multi-outcome markets have more (parse accordingly)
- Market can be "active" but have very low liquidity — always check `liquidityNum`
- Volume ≠ liquidity — high volume market can have low current liquidity if one side is thin

## Category Keywords Used by Script

| Category | Keywords Searched |
|----------|-----------------|
| sports | nba, nfl, epl, mlb, nhl, tennis, golf, soccer, football, basketball |
| politics | election, president, senate, trump, biden, parliament, vote |
| commodities | oil, wti, brent, gold, silver, natural gas, crude, barrel |
| crypto | bitcoin, ethereum, btc, eth, crypto, defi, solana |
