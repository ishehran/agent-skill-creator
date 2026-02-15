# Playtest Telemetry

Tune levels using evidence from real runs.

## Minimum Signals To Track

- completion rate per level
- median completion time
- deaths per checkpoint segment
- top failure locations (heatmap)
- retry count before success

## Playtest Loop

1. Define hypothesis for the next revision.
2. Run a focused test with 3 to 8 target players.
3. Capture metrics and short qualitative notes.
4. Apply one tuning change cluster.
5. Re-test and compare deltas.

## Decision Guide

- If completion is low and time is high: reduce complexity or improve readability.
- If completion is high and time is very low: add pressure or complexity.
- If failures cluster at one point: adjust telegraphing, spacing, or checkpoint.

