---
name: playwright-testing
description: "Plan, implement, and stabilize frontend tests for games and web UIs: unit/integration/E2E/visual/a11y with deterministic Playwright patterns. Trigger: 'Playwright test', 'flake triage', 'canvas testing', 'game regression'."
---

# Frontend Testing

Build tests that fail for real product bugs, not timing noise.

## Default Mode: Risk-First Testing

Choose the cheapest test layer that catches the target bug class.

Prefer deterministic inputs and explicit readiness signals over retries.

## Core Questions Before Writing Tests

1. Which user risk does this test cover?
2. What is the lowest useful test layer?
3. What nondeterminism can make this flaky?
4. Which readiness signal replaces sleep-based waits?
5. What evidence will failures produce in CI?

## Layer Selection

- Unit: pure logic, rules, scoring, deterministic simulation.
- Integration: module interaction and boundary behavior.
- E2E: critical player flow in a real browser runtime.
- Visual: targeted screenshot checks after determinism is enforced.
- Accessibility: semantic and keyboard checks for DOM-driven UI.

## Quick Start Workflow

1. Define one critical smoke flow.
2. Add explicit readiness seam (`window.__TEST__.ready` or equivalent).
3. Fail on console errors and required network failures.
4. Lock environment (viewport, locale, timezone, seeded data).
5. Capture screenshot + logs + state snapshot on failure.

## Playwright Guidance For 2D Games

- Wait on game-ready signals, never fixed sleeps.
- Drive inputs through keyboard/mouse/touch like real players.
- Expose a small stable state seam for assertions.
- Keep screenshot environments fixed (viewport, DPR, fonts, animation state).
- Use dedicated harness scenes for canvas UI regression checks.

## Server Lifecycle Helper

Use `scripts/with_server.py` to run tests with local server lifecycle handling.
- run `python scripts/with_server.py --help` first
- wait by `--port` and optionally `--url`
- run tests only after services are healthy

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Sleep-based waits | Random failures under load | Wait on explicit readiness signals |
| Testing internal engine details only | Brittle and low-signal assertions | Assert stable gameplay outcomes |
| Retry-first flake strategy | Hides real instability | Remove nondeterminism at source |
| Uncontrolled RNG/time | Non-repeatable failures | Seed RNG and control clocks |
| Snapshot explosion | High maintenance, weak insight | Keep targeted visual checks |

## Bundled Resources

Read only what is needed:
- `references/playwright-mcp-cheatsheet.md`
- `references/phaser-canvas-testing.md`
- `references/flake-reduction.md`

Scripts:
- `scripts/with_server.py`
- `scripts/imgdiff.py`
