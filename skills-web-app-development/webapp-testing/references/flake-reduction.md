## Flake Reduction (Web Apps)

Flakes are defects in test design or environment control.

## Classify The Flake First

1. Readiness: app not ready when action/assertion runs
2. Timing: race between async operations
3. Environment: locale, timezone, fonts, viewport, CPU
4. Data: non-deterministic backend state
5. Isolation: leakage across tests

Fix by class, not by guessing.

## Triage Workflow

For failing test, collect:
- console errors/warnings
- network failures and response status
- screenshot at failure
- app state dump (`window.__TEST__.state()` if available)

Re-run with CI-like settings locally before changing assertions.

## Highest-Leverage Fixes

### Readiness

- Replace sleeps with explicit conditions.
- Expose deterministic "ready" seam in app.

### Determinism

- Seed random behavior.
- Freeze/control clock where feasible.
- Turn off non-essential animation/transitions.

### Data

- Use isolated test users/tenants.
- Reset database state per test suite.
- Avoid dependence on shared mutable fixtures.

### Environment

- Lock viewport, DPR, locale, timezone.
- Ensure font availability or use consistent fallback.

### Isolation

- Clear storage/cookies/session between tests.
- Avoid global mutable state in test runtime.

## Retry Policy

Retries are a temporary guardrail, not a solution.

If retries are enabled:
- track flaky test rate by test ID
- set deadline to remove retry
- prioritize root-cause fix in backlog
