---
name: phaser-gamedev
description: "Build 2D browser games with Phaser 3 (JS/TS): scenes, sprites, physics (Arcade/Matter), tilemaps (Tiled), animations, input, and level integration. Trigger: 'Phaser scene', 'Arcade physics', 'tilemap', '2D level', 'Phaser 3 game'."
---

# Phaser Game Development

Build 2D browser games as small, testable playable slices with clear scene boundaries and data-driven content.

## Default Mode: Gameplay-First

Start from player experience and core loop behavior before adding polish.

Do not hard-lock architecture details before the first playable is defined.

## STOP: Before Writing Gameplay Code

Define these first:
1. Core loop in one sentence
2. Win and failure conditions
3. Player verbs and input model
4. Scene map (Boot, Menu, Game, UI, GameOver)
5. First level objective and progression target
6. Asset constraints (sprite/tile sizes, collision model)

If unclear, stay in planning mode.

## Reference Files

Read these before the related work:

| When working on... | Read first |
|---|---|
| Loading spritesheets and nine-slice assets | `references/spritesheets-nineslice.md` |
| Core scene and system architecture | `references/core-patterns.md` |
| Tilemaps, collision layers, and map integration | `references/tilemaps.md` |
| Arcade physics tuning and pooling | `references/arcade-physics.md` |
| Performance profiling and optimization | `references/performance.md` |
| Building and tuning level flow | `references/level-design-and-progression.md` |

## Core Workflow

1. Write a short game brief and first playable goal.
2. Implement scene skeleton and boot pipeline.
3. Implement one complete gameplay interaction (movement + one challenge).
4. Integrate graybox level data from tilemap/object layers.
5. Add checkpoint and failure/restart loop.
6. Tune balance and performance on target hardware.
7. Prepare regression hooks for testing.

## Non-Negotiables

- Keep level data outside scene hardcode whenever possible.
- Use deterministic update patterns for time-sensitive logic.
- Keep physics choice explicit and justified.
- Use object pooling for high-frequency entities.
- Keep scene responsibilities narrow and composable.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| One giant scene for all systems | Hard to debug and extend | Split gameplay, UI, and flow scenes |
| Frame-count based gameplay timers | Behavior drifts across FPS | Use delta-time and explicit clocks |
| Hardcoded enemy placement in code | Slow level iteration | Move placements to map/object data |
| Add art before graybox validation | Expensive rework | Validate flow first, then polish |
| Physics retrofitted late | Breaks interaction assumptions | Choose collision model early |

## Level Creation Rule

When building levels, use `references/level-design-and-progression.md` and the dedicated `../game-level-design/SKILL.md` flow.

Keep progression intentional: introduce, reinforce, then combine mechanics.

## Remember

Phaser gives strong primitives, but system design and level quality determine the player experience.

Optimize for clarity, fairness, and iteration speed.
