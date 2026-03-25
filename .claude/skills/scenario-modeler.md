---
name: scenario-modeler
description: Systematically decompose a market into 2-4 exhaustive scenarios, assign probabilities and per-scenario win rates, and compute a weighted fair value. Use before sizing any bet with a pending high-profile catalyst (endorsement, vote, announcement, external decision).
performance:
  uses: 0
  wins_contributed: 2
  losses_contributed: 0
  status: ACTIVE
---

# Scenario Modeler

Use this skill whenever a market outcome depends on a near-term binary or categorical catalyst. Formalizes the mental model that has already produced 2 high-conviction trades (Paxton entry and Paxton top-up).

## When to Use

- Any market with a pending high-profile catalyst: endorsements, scheduled votes, announcements, rulings
- Any market where the "base case" and the "adversarial case" produce materially different win probabilities
- Before sizing up a position beyond 2% bankroll — the scenario model is a required check

## Step-by-Step Process

### 1. Enumerate Scenarios Exhaustively

List all 2-4 distinct scenarios. They must be:
- Mutually exclusive
- Collectively exhaustive (must sum to 100%)
- Named after the key catalyst state, not the outcome

Example (Paxton):
- Scenario A: Trump endorses Paxton (P = 35%)
- Scenario B: Trump endorses Cornyn (P = 30%)
- Scenario C: No Trump endorsement by primary day (P = 35%)

### 2. Assign Scenario Probabilities

For each scenario, ask:
- What is the base rate for this scenario type?
- Is there polling or data that measures this directly?
- What have public statements, insiders, or prediction markets said?

Write the rationale for each probability. Do not skip this.

### 3. Assign Win Probability Per Scenario

For each scenario, estimate: P(market resolves YES | this scenario)

**Critical check**: Look for polling or data that directly tests the adversarial scenario.
- "If Trump endorses Cornyn, does Cornyn win?" → Find a poll that asked this directly
- "If the Fed cuts rates, does the party holding the presidency gain seats?" → Find historical base rate

This is the most important step. If empirical data for the adversarial scenario exists, use it. If not, use historical base rates from `knowledge/market_types/<category>.md`.

### 4. Compute Weighted Fair Value

```
Fair Value = Σ [P(scenario_i) × P(YES | scenario_i)]
```

Example (Paxton):
```
FV = 0.35 × 0.80 + 0.30 × 0.45 + 0.35 × 0.60
   = 0.280 + 0.135 + 0.210
   = 0.625 → 62.5% YES
```

### 5. Sensitivity Check

What is the fair value under the most pessimistic plausible assumption for each scenario probability?

- If the adversarial scenario is 20pp more likely than estimated: does FV still beat the market price with ≥4pp edge?
- If the adversarial win probability is 10pp worse: does FV still clear the threshold?

If the bet passes the pessimistic sensitivity check, confidence = HIGH. If it only passes at base case, confidence = MEDIUM.

### 6. Output Format

```
## Scenario Model: [Market Name]
Market price: X%

| Scenario | P(Scenario) | P(YES|Scenario) | Contribution |
|----------|------------|----------------|-------------|
| [name] | X% | X% | X×X% |
| [name] | X% | X% | X×X% |
| [name] | X% | X% | X×X% |
| **Total** | **100%** | | **Fair Value: X%** |

Edge: +Xpp | Confidence: [LOW/MEDIUM/HIGH]
Empirical adversarial scenario data: [source if found]
Sensitivity: FV under pessimistic case = X% (edge = +Xpp)
```

## Integration with Other Skills

- **Run AFTER `multi-outcome-enumerator`**: Make sure all market outcomes are enumerated before modeling scenarios
- **Run BEFORE `size-position`**: The scenario model's confidence level feeds into Kelly fraction selection
- **Run BEFORE `evaluate-edge`**: The weighted fair value from this skill IS the fair value input to evaluate-edge

## Example: Paxton Texas Senate (Applied March 17-18, 2026)

```
## Scenario Model: Ken Paxton wins 2026 TX GOP Senate Primary
Market price: 38.5%

| Scenario | P(Scenario) | P(YES|Scenario) | Contribution |
|----------|------------|----------------|-------------|
| Trump endorses Paxton | 35% | 80% | 28.0% |
| Trump endorses Cornyn | 30% | 45% | 13.5% |
| No Trump endorsement | 35% | 60% | 21.0% |
| **Total** | **100%** | | **Fair Value: 62.5%** |

Edge: +24pp | Confidence: HIGH
Empirical adversarial scenario data: Fox 26 Houston poll (March 2026) — Paxton leads 44-43 even if Trump endorses Cornyn. Direct test of adversarial scenario.
Sensitivity: If endorsement priors shift 10pp toward Cornyn (40%/40%/20%): FV = 62.5% → 59.5%, still +21pp edge.
```

## Error Patterns to Avoid

- **Scenarios that don't sum to 100%**: Add an "Other/Unexpected" scenario
- **Circular reasoning**: P(YES|scenario) should be estimated from base rates, NOT from "what do I think will happen overall"
- **Ignoring the adversarial scenario**: If you haven't tested "what if the worst case happens, do I still win?", the model is incomplete
- **Stale scenario probabilities**: Update them if principal actors make public statements — see `knowledge/market_types/politics.md` Rule 8
