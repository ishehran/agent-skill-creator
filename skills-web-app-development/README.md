# Web App Development Skill Suite

This folder is a stack-agnostic skill set for building, validating, and operating production web apps.

## Included Skills

- `webapp-ideation/`: turn ideas into validated product bets before implementation.
- `webapp-builder/`: design and implement web apps from requirements to vertical slices.
- `webapp-ui-motion/`: turn prompts and screenshots into polished UI with researched animation patterns.
- `webapp-testing/`: plan and stabilize tests by risk layer (unit/integration/contract/E2E/visual/a11y).
- `webapp-deployment-ops/`: ship safely with release gates, observability, rollback, and incident response.

## Default Operating Mode

Use requirements-first execution with no fixed stack by default.

Choose a specific stack only when:
- repository reality already constrains the stack
- integration/platform constraints require a stack
- business requirements force a stack

## Recommended End-to-End Flow

1. Start with `webapp-ideation/SKILL.md` to validate the problem and define a clear bet.
2. Convert the bet into implementation inputs using `requirements-first-template.md`.
3. Use `webapp-builder/SKILL.md` to design and implement one critical journey.
4. Use `webapp-ui-motion/SKILL.md` to match UI references and implement state-driven motion.
5. Use `webapp-testing/SKILL.md` to add high-signal coverage for that journey.
6. Use `webapp-deployment-ops/SKILL.md` to release with explicit guardrails.
7. Repeat in small slices.

## Stack Profile Rule

For deployment, stack-specific profiles are optional overlays:
- use `webapp-deployment-ops/profiles/` only when stack signals are clear
- otherwise stay on core stack-agnostic guidance

## Session Continuity

At the end of each session:
1. Commit changes with a clear message.
2. Update `PROJECT_CONTEXT.md` when project direction changes.
3. Save a structured handoff using `session-checkpoint-template.md`.
