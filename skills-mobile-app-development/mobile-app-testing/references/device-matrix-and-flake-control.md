# Device Matrix And Flake Control

Build a minimal matrix that still reflects production risk.

## Matrix Dimensions

- OS major versions
- low/mid/high device performance tiers
- screen size classes
- network conditions

## Flake Control Rules

- use explicit readiness signals
- stabilize test data and time-dependent behavior
- isolate network dependencies when possible
- capture full diagnostics on every failure

