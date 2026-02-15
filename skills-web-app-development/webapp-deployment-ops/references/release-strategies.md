# Release Strategies

Choose strategy by change risk and blast radius, not by habit.

## Strategy Options

| Strategy | Use when | Risk profile |
|---|---|---|
| Rolling | Low to medium risk, stateless services | Moderate |
| Blue-green | Need near-instant rollback | Low cutover risk, higher infra cost |
| Canary | Medium to high risk changes | Low initial blast radius |
| Shadow | Validate traffic behavior without user impact | Low user risk, extra complexity |
| Big bang | Rarely justified | Highest risk |

Prefer canary or blue-green for risky releases.

## Selection Heuristics

- If migration is backward-compatible: rolling/canary is usually fine.
- If release changes critical workflows: start with canary.
- If rollback must be immediate: blue-green.
- If behavior under real traffic is uncertain: shadow first, then canary.

## Deployment and Migration Order

Use safe order:
1. deploy backward-compatible schema changes
2. deploy code that can read old and new schema
3. perform backfill if needed
4. switch feature flag or traffic weight
5. remove old schema only after stability

Do not deploy code that requires schema not yet present.

## Canary Guardrails

Before increasing traffic:
- latency within threshold
- error rate within threshold
- saturation (CPU/memory/queue) within threshold
- key business conversions unchanged

If any guardrail breaches, halt and roll back.

## Rollback Playbook

For each service define:
- rollback command
- maximum acceptable rollback time
- data compatibility limitations
- owner for decision and execution

Rollback decisions should be pre-authorized for critical thresholds.
