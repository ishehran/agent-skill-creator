---
name: windows-app-testing
description: "Plan and stabilize Windows app tests across unit, integration, UI automation, installer/update checks, and crash regression. Trigger: 'test Windows app', 'desktop QA strategy', 'UI automation', 'installer testing'."
---

# Windows App Testing

Build test suites that catch real failures in desktop workflows and release mechanics.

## Default Mode: Risk-First Layering

Choose the lowest-cost layer that can catch the risk.

Treat installer, updater, and crash recovery checks as first-class quality gates.

## Reference Files

| When working on... | Read first |
|---|---|
| Layer selection and confidence planning | `references/test-layer-strategy.md` |
| UI automation determinism | `references/ui-automation-determinism.md` |
| Installer, update, and crash checks | `references/crash-and-installer-testing.md` |

## Workflow

1. Identify highest-risk workflow and release risk.
2. Define pass/fail evidence per layer.
3. Implement unit and integration coverage first.
4. Add deterministic UI automation for critical path.
5. Add installer and update validation.
6. Add crash recovery and state-resume checks.
7. Gate releases on stable evidence.

## Non-Negotiables

- No sleep-based waits in UI automation.
- Fail tests on unexpected error dialogs and critical logs.
- Verify startup on clean machine state.
- Verify update and rollback behavior before release.
- Capture artifacts on failure: logs, screenshots, crash traces.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Only manual desktop testing | Slow and inconsistent | Automate critical paths and release checks |
| Skip installer and updater tests | Production-only failures | Treat install/update as release blockers |
| Retry flaky UI tests forever | Hides instability | Remove nondeterminism at source |
| Assert fragile UI structure | High test churn | Assert stable outcomes and labels |

## Remember

Desktop quality is not just feature behavior. Install, update, restart, and recovery are part of the product.

