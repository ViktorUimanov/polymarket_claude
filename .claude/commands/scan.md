Perform a systematic market opportunity scan across all Polymarket categories.

## Scan Steps

### 1. Load Context
```bash
python3 /root/workspace/polymarket/scripts/portfolio.py --bankroll-only
```
Read `knowledge/README.md` and `knowledge/edge_sources.md` to know what to look for.

### 2. Fetch Markets by Category (run in parallel)

Use the researcher agent to scan all 5 categories simultaneously:

```bash
# Sports — events in next 14 days
python3 /root/workspace/polymarket/scripts/fetch_markets.py --category sports --min-volume 3000 --limit 30

# Politics — elections, policy, geopolitical
python3 /root/workspace/polymarket/scripts/fetch_markets.py --category politics --min-volume 5000 --limit 30

# Commodities — oil, gold, gas
python3 /root/workspace/polymarket/scripts/fetch_markets.py --category commodities --min-volume 2000 --limit 20

# Crypto — BTC/ETH price, regulatory
python3 /root/workspace/polymarket/scripts/fetch_markets.py --category crypto --min-volume 5000 --limit 20

# High volume everything else
python3 /root/workspace/polymarket/scripts/fetch_markets.py --min-volume 10000 --limit 50
```

### 3. Initial Screen

For each market, do a quick price check:
- If YES price is 95–100% or 0–5%: market is near-resolved, skip
- If volume < $2,000: skip [LOW_LIQUIDITY]
- If resolves in < 6 hours: skip [EXPIRES_SOON]
- If resolution criteria mention "at discretion" or "admin": skip [AMBIGUOUS_RESOLUTION]

### 4. Edge Screen

For remaining markets, estimate fair value using:
- Known base rates (from `knowledge/market_types/`)
- Current news (1 search per market: `WebSearch("<question> latest")`)
- Calibration adjustment (`python3 scripts/calibration.py --category <cat>`)

Flag as **candidate** if estimated edge ≥ 4pp.

### 5. Rank Candidates

Sort by expected value: `edge_pp × recommended_kelly_size / 100`
Take top 5 for deep research.

### 6. Output Scan Report

Write to `output/reports/scan_{datetime}.md`:

```markdown
# Market Scan — {datetime}

## Summary
- Markets fetched: {N}
- After liquidity filter: {N}
- After resolution filter: {N}
- Candidates with edge ≥ 4pp: {N}

## Top Candidates

| Rank | Market | Cat | Market % | Fair Value | Edge | Action |
|------|--------|-----|----------|-----------|------|--------|
| 1 | {question} | sports | 42% | 55–60% | +15pp | BET YES |

## Passed Markets ({N})
{brief reason per category — e.g., "Sports: 8 markets scanned, all well-priced"}

## Next Steps
- Deep research: {list top 3 by name}
- Monitor (expiring soon): {list}
```

### 7. Trigger Deep Research

For each top candidate, run `/research <market_question>`.

## Scan Constraints

- If bankroll < $1,000: reduce all position sizes by 50%
- If 3+ losses in last 5 trades: require edge > 8pp for candidates
- If a category has 3+ consecutive losses: add +4pp to edge requirement for that category only
- Never flag [LOW_LIQUIDITY] or [AMBIGUOUS_RESOLUTION] markets as candidates
