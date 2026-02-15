# Observability And Crash Triage

Instrument failures so triage is fast and reproducible.

## Minimum Signals

- crash-free session rate
- startup failure rate
- critical flow error rate
- API failure class distribution

## Triage Loop

1. Reproduce on closest matrix device.
2. Collect logs, traces, and build metadata.
3. Isolate root cause category.
4. Patch and run targeted regression set.
5. Confirm production signal recovery after release.

