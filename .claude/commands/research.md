Deep research on a specific market before making a trade decision.

**Usage**: `/research <market_slug_or_question>`

## Minimum Research Bar

Do NOT proceed to trade unless ALL boxes are checked:
- [ ] Resolution criteria fully understood (exactly what must happen for YES)
- [ ] At least 2 independent sources consulted
- [ ] Historical base rate identified
- [ ] Calibration correction applied for this category
- [ ] Kelly sizing calculated
- [ ] Similar past trades reviewed

## Research Steps

### 1. Fetch Market Data
```bash
python3 /root/workspace/polymarket/scripts/fetch_markets.py --search "$ARGUMENTS" --limit 5
```
If multiple results, identify the correct one by question and ID.

### 2. Understand Resolution Criteria
Read the full `description` field carefully. Key questions:
- What EXACTLY must happen for YES to resolve?
- What oracle/source determines resolution?
- Are there edge cases that could cause unexpected resolution?
- Is the resolution criteria unambiguous?

If ambiguous: tag `[AMBIGUOUS_RESOLUTION]` and PASS.

### 3. Check Past Learnings
```bash
# Category-specific learnings
cat /root/workspace/polymarket/knowledge/market_types/<category>.md

# Similar past trades
grep -rl "<topic_keyword>" /root/workspace/polymarket/output/trades/
```
If the agent has lost on this category recently: note what the rule change was and how this market is different.

### 4. Research (3+ sources minimum)
```
WebSearch("<market question> latest news")
WebSearch("<key entity> <date> update")
WebSearch("<topic> expert forecast prediction")
```

Look for:
- Recent developments (last 7 days)
- Expert forecasts or prediction aggregators (Metaculus, PredictIt, FiveThirtyEight)
- Historical base rates for this type of outcome
- Sentiment divergence (what do experts say vs market price?)

### 5. Build Probability Estimate
Use the **evaluate-edge** skill:
1. Base rate
2. Evidence updates
3. Market signal blend (for volume > $50k)
4. Uncertainty penalty for category
5. Calibration correction:
```bash
python3 /root/workspace/polymarket/scripts/calibration.py --category <category>
```

### 6. Size the Position
```bash
python3 /root/workspace/polymarket/scripts/kelly.py \
  --fair-value <X> \
  --market-price <Y> \
  --confidence <low|medium|high> \
  --bankroll $(python3 /root/workspace/polymarket/scripts/portfolio.py --bankroll-only)
```

### 7. Write Research File
Save to `research/{market_slug}.md` — full notes including sources, probability derivation, and Kelly calculation.

### 8. Decision Output

```
## Research Decision: {market_question}

Action: BET YES / BET NO / PASS
Confidence: low / medium / high
Fair Value: {X}% (range: {low}–{high}%)
Market Price: {Y}%
Edge: {+Z pp}
Recommended Size: ${amount}
Expected Value: ${EV}

Resolution Criteria: {precise summary}
Key Facts: {3 bullet points with sources}
Base Rate: {X% historical frequency}
Edge Source: {why does this edge exist?}
Risk: {main scenario where we lose}
Past Learnings Applied: {reference or "none"}
```

If PASS: write to `output/passes/{date}_{market}.md` with reason.
If BET: proceed to write `output/trades/{date}_{market}.md` with full reasoning before executing.
