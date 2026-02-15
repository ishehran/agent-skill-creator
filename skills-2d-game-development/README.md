# 2D Game Development Skill Suite

This folder is a practical skill suite for building and shipping 2D games with predictable quality.

## Included Skills

- `phaser-gamedev/`: build gameplay systems, scenes, entities, physics, and asset pipelines.
- `game-ui-design/`: design HUD, menus, readability, and interaction feedback for 2D games.
- `game-level-design/`: design and tune levels, progression, pacing, and difficulty curves.
- `playwright-testing/`: create deterministic browser and canvas test coverage.

## Recommended End-to-End Flow

1. Use `phaser-gamedev/SKILL.md` to define core loop and first playable.
2. Use `game-ui-design/SKILL.md` to design HUD, menus, and interaction readability.
3. Use `game-level-design/SKILL.md` to shape production-ready levels and pacing.
4. Use `playwright-testing/SKILL.md` to lock reliability and prevent gameplay and UI regressions.
5. Iterate in small slices and keep each slice playable.

## Default Operating Mode

Stay gameplay-first and stack-agnostic where possible.

If you are using Phaser, use the Phaser-specific references directly.
If you are using another engine, keep the same workflow and adapt engine commands.

## Session Continuity

At the end of each session:
1. Commit changes with clear intent in the message.
2. Update `PROJECT_CONTEXT.md` if priorities or architecture changed.
3. Save a short handoff using `session-checkpoint-template.md`.
