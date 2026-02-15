# Mobile App Development Skill Suite

This folder is a stack-agnostic skill suite for planning, building, testing, and releasing mobile applications.

## Included Skills

- `mobile-app-ideation/`: turn mobile app ideas into validated opportunities.
- `mobile-app-builder/`: design and implement mobile app architecture and core flows.
- `mobile-app-testing/`: build reliable quality coverage across devices and environments.
- `mobile-app-release-ops/`: ship safely with staged rollout, store readiness, and rollback planning.

## Recommended End-to-End Flow

1. Start with `mobile-app-ideation/SKILL.md` to validate the problem and segment.
2. Use `mobile-app-builder/SKILL.md` to build one critical user journey.
3. Use `mobile-app-testing/SKILL.md` to stabilize quality and reduce flake.
4. Use `mobile-app-release-ops/SKILL.md` for safe production rollout.
5. Repeat in small, measurable slices.

## Default Operating Mode

Stay requirements-first and avoid stack lock-in early.

Choose a specific stack only when:
- existing repository constraints require it
- integrations/platform demands force it
- business constraints make one option mandatory

## Session Continuity

At the end of each session:
1. Commit all intended changes with a clear message.
2. Update `PROJECT_CONTEXT.md` when priorities shift.
3. Save a short handoff using `session-checkpoint-template.md`.

