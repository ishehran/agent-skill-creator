# Windows App Development Skill Suite

This folder is a stack-agnostic skill suite for planning, building, testing, and operating Windows desktop applications.

## Included Skills

- `windows-app-ideation/`: turn product ideas into validated desktop app opportunities.
- `windows-app-builder/`: design and implement desktop app architecture and core features.
- `windows-app-testing/`: create reliable automated and manual quality coverage.
- `windows-app-deployment-ops/`: ship safely with signing, staged rollout, and rollback.

## Recommended End-to-End Flow

1. Start with `windows-app-ideation/SKILL.md` to define the problem and validate demand.
2. Use `windows-app-builder/SKILL.md` to design and build one critical user workflow.
3. Use `windows-app-testing/SKILL.md` to stabilize quality and prevent regressions.
4. Use `windows-app-deployment-ops/SKILL.md` to release with operational guardrails.
5. Repeat in small, evidence-driven slices.

## Default Operating Mode

Stay requirements-first and avoid locking stack early.

Choose a specific stack only when:
- repository reality already defines it
- integrations or platform constraints force it
- business constraints make one path mandatory

## Session Continuity

At the end of each session:
1. Commit all intended changes with a clear message.
2. Update `PROJECT_CONTEXT.md` when priorities change.
3. Save a short handoff using `session-checkpoint-template.md`.

