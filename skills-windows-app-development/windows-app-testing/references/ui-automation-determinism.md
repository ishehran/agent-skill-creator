# UI Automation Determinism

Flake usually comes from timing and environment variability.

## Stabilization Checklist

- wait on explicit UI-ready markers
- control window size and scaling
- disable or control animations in test mode
- seed deterministic data where possible
- fail fast on unhandled exceptions

## Failure Evidence

Capture on failure:
- screenshot
- app logs
- automation trace
- relevant state snapshot

