---
name: webapp-testing
description: "Plan, implement, and stabilize web app tests across unit, integration, contract, E2E, visual, and accessibility layers. Use for Playwright/Vitest/Jest/RTL test strategy, flake triage, CI stabilization, and deterministic browser checks."
---

# Web App Testing

Build test suites that fail for real product issues, not timing noise.

## Default Mode: Requirements-First (No Fixed Stack)

Testing strategy follows product risk, not framework preference.

If stack/tooling is already present, Codex should detect and use it.
If stack/tooling is not fixed yet, start with stack-agnostic test planning and map it to tools after architecture is chosen.

## Philosophy: Confidence Per Minute

Every test should answer:
1. Which user risk does this cover?
2. Why is this the cheapest layer to cover it?
3. What would make this flaky?
4. What evidence will failure include?

Favor fewer high-signal tests over a large brittle suite.

## Layer Selection

Use the lowest layer that can catch the bug class:
- Unit: pure logic, reducers, formatters, business rules
- Integration: API handlers, data access, cross-module behavior
- Contract: API schema/compatibility between producer and consumer
- E2E: critical user journeys across browser + backend
- Visual: layout/regression checks after rendering is deterministic
- A11y: semantic and keyboard behavior checks

## Quick Start Workflow

1. Pick one critical user journey and define failure impact.
2. Define clear pass/fail outcomes for that journey.
3. Choose the cheapest layers that cover the risk.
4. Add explicit readiness signal in app (`window.__TEST__.ready` or DOM marker).
5. Capture console baseline after readiness, then re-check console after each major action.
6. Fail on unexpected console errors and failed required network calls.
7. Add state seam for diagnostics (`window.__TEST__.state()`).
8. Lock test environment (viewport, locale, timezone, seeded data).

## Playwright Guidance

Use Playwright for full user-flow confidence:
- wait on readiness condition, never fixed sleeps
- interact by role/label/text where possible
- capture screenshot + console + network on failure
- assert stable business outcomes, not incidental DOM structure

For MCP-driven browser automation, apply the same principles and enforce a console loop:
- capture console messages immediately after readiness
- perform one action block
- capture console messages again and triage only new entries
- treat uncaught errors and unhandled promise rejections as test failures unless explicitly allowlisted

If console tooling is unavailable in the current runner, add temporary logging hooks in test code and keep the same fail rules.

## Browser Console Rule

Browser console is a required signal, not optional debug output.

Always do all of the following:
1. Read console at baseline after app-ready signal.
2. Read console after each major interaction block.
3. Capture console + network + screenshot on failure.
4. Keep a small allowlist for known benign warnings; fail everything else.

## Contract Testing Guidance

For API-driven apps:
- validate request/response schemas in CI
- test backward compatibility for existing consumers
- treat contract drift as a release blocker

Read `references/contract-testing.md` when adding or changing endpoints.

## Server Lifecycle Helper

Use `scripts/with_server.py` to run tests with one or more local servers.
- run `python scripts/with_server.py --help` first
- wait by `--port` and optionally by `--url`
- run tests only after services are healthy

## Anti-Patterns

| Anti-pattern | Failure mode | Better approach |
|---|---|---|
| Sleep-based waits | Random failures under load | Wait on explicit ready signals |
| Overreliance on E2E | Slow, noisy suites | Move logic checks to unit/integration |
| Snapshot explosion | High churn, low signal | Targeted snapshots for critical screens |
| Ignoring console errors | Hidden regressions pass CI | Fail tests on unexpected console errors |
| Retrying flaky tests forever | Incident risk hidden | Remove nondeterminism and isolate causes |

## Variation Guidance

Adjust strategy by app profile:
- No fixed stack: keep tests layer-driven and tool-agnostic until stack is clear.
- Admin/internal tools: emphasize integration + authz tests.
- Consumer web app: prioritize key E2E journeys and visual checks.
- API-heavy app: contract tests become first-class.
- Regulated workflows: audit trail and permission tests are mandatory.

## Bundled Resources

Read only what is needed:
- `../requirements-first-template.md`
- `references/playwright-mcp-cheatsheet.md`
- `references/dom-testing-strategy.md`
- `references/contract-testing.md`
- `references/flake-reduction.md`

Scripts:
- `scripts/with_server.py`
- `scripts/imgdiff.py`
