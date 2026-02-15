## DOM Testing Strategy (Unit + Integration)

Use DOM testing to validate user-visible behavior quickly without full E2E overhead.

## Test Shape

Focus assertions on:
- rendered text and labels
- enabled/disabled action states
- validation and error presentation
- navigation and callback side effects

Avoid asserting framework internals or exact markup nesting.

## Test Pyramid For UI

- High count: pure logic and utility tests
- Medium count: component integration tests
- Low count: route-level full render tests

Reserve E2E for cross-boundary workflows only.

## Mocking Guidance

Mock only external dependencies:
- network clients
- clock/time sources
- random generators
- browser APIs unavailable in test runtime

Do not mock your own domain logic unless needed for isolation.

## Async UI Patterns

Rules:
- wait for expected state transitions, not arbitrary delays
- assert loading -> success/error transitions explicitly
- verify retry and cancellation behavior where applicable

## Forms

Cover:
- required fields
- type/format constraints
- server-returned field errors
- success reset/redirect behavior

Field-level and form-level errors should both be tested.

## Accessibility Checks

At minimum validate:
- inputs associated with labels
- dialog focus trap and escape behavior
- keyboard navigation path
- visible focus indicators

DOM tests can catch many a11y regressions early.
