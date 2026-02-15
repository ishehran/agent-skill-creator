# Release Trains And Gating

Use predictable release trains with explicit stop/go thresholds.

## Suggested Sequence

1. Internal build verification
2. Beta cohort rollout
3. Small production percentage rollout
4. Progressive increase after health gates pass

## Minimum Gates

- crash-free sessions above target
- startup success above target
- critical journey success above target
- no unresolved severity-1 issues

