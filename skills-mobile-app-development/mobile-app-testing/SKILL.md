---
name: mobile-app-testing
description: "Plan and stabilize mobile test strategy across unit, integration, UI automation, device matrix validation, and crash triage. Trigger: 'test mobile app', 'mobile QA', 'device matrix', 'Appium strategy', 'flake triage'."
---

# Mobile App Testing

Build tests that fail for real user risk across device, OS, and network variation.

## Default Mode: Risk-First Layering

Use lowest-cost test layer that covers the risk.

Treat device matrix and lifecycle transitions as first-class test concerns.

## Reference Files

| When working on... | Read first |
|---|---|
| Layer planning and signal strategy | `references/test-pyramid-mobile.md` |
| Device matrix and flake reduction | `references/device-matrix-and-flake-control.md` |
| Crash diagnostics and triage loops | `references/observability-and-crash-triage.md` |

## Workflow

1. Identify highest-risk user journey.
2. Define pass/fail evidence by layer.
3. Add unit/integration coverage first.
4. Add deterministic UI automation for critical flows.
5. Run selected device and OS matrix.
6. Capture crashes, logs, and traces on failure.
7. Gate release on stable results.

## Non-Negotiables

- No fixed sleep waits in UI automation.
- Include weak network and offline scenarios.
- Cover lifecycle transitions: foreground, background, relaunch.
- Capture artifacts on failure: screenshot, logs, crash trace.
- Keep a minimal but representative device matrix.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Single-device confidence only | Fails in production diversity | Use a defined matrix by OS/version/device tier |
| Retry-heavy flake masking | Real defects remain hidden | Remove nondeterminism and readiness issues |
| Skip lifecycle tests | State corruption and regressions | Add pause/resume/cold-start checks |
| Pure manual store-release testing | Slow and inconsistent | Automate critical regression paths |

## Remember

Mobile quality depends on consistency across changing device and network conditions.

