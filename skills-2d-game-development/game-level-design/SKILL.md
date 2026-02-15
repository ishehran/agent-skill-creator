---
name: game-level-design
description: "Design and tune 2D game levels: grayboxing, pacing, progression, difficulty balancing, checkpoints, and playtest-driven iteration. Trigger: 'design level', 'game progression', 'difficulty curve', 'build level', '2D level design'."
---

# 2D Game Level Design

Build levels that teach mechanics, maintain pacing, and escalate challenge without unfair spikes.

## Default Mode: Graybox-First

Start with blockout geometry and encounter flow before final art polish.

A level is not ready because it looks good. It is ready when players can read intent, learn patterns, and finish with acceptable failure rates.

## STOP: Before Placing Final Tiles

Define these first:
1. Level objective and completion condition
2. Core mechanic(s) being taught or tested
3. Player verbs required in this level
4. Failure states and checkpoint strategy
5. Difficulty target for intended player skill band
6. Telemetry or playtest signals for success

If unclear, continue in graybox mode.

## Reference Files

Read these before the relevant work:

| When working on... | Read first |
|---|---|
| Layout planning and encounter sequencing | `references/level-structure.md` |
| Difficulty tuning and progression pacing | `references/difficulty-and-progression.md` |
| Playtest loop and telemetry-based iteration | `references/playtest-telemetry.md` |

## Workflow

1. Write a level brief in 5 to 10 lines.
2. Graybox the route, jumps, chokepoints, and safe zones.
3. Place enemy and hazard patterns by intent, not random density.
4. Run first-pass playtests and capture failure heatmaps.
5. Adjust spacing, timings, and checkpoint positions.
6. Add art pass only after flow is stable.
7. Run regression tests after each tuning wave.

## Non-Negotiables

- One primary learning objective per level section.
- Introduce, reinforce, then combine mechanics.
- Keep failure recovery time proportional to difficulty.
- Keep critical path readable without hidden information.
- Track changes with playtest evidence, not intuition only.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Increase difficulty by adding more enemies everywhere | Noise replaces intentional challenge | Escalate by pattern complexity and timing |
| Decorative clutter on critical path | Player cannot read hazards quickly | Keep readability high on decision points |
| Long retry loops after failure | Frustration and drop-off | Use checkpoint spacing based on failure cost |
| Ship level without graybox test | Late rework and unstable balance | Validate flow before art polish |
| Tune only from personal skill level | Misaligned for target audience | Use playtest cohorts and telemetry |

## Handoff Rule

After level design decisions are locked:
1. Implement level data and scene integration in `../phaser-gamedev/SKILL.md`.
2. Add deterministic checks in `../playwright-testing/SKILL.md`.

## Remember

Great levels feel fair, legible, and steadily rewarding.

Use deliberate pacing and evidence-driven tuning.

