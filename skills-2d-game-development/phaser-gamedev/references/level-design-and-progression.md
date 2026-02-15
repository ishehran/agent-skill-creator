# Level Design And Progression

Use this guide when converting game mechanics into playable level sequences.

## Core Rule

Each level should teach, test, and reward.

## Practical Flow

1. Define level goal and exit condition.
2. Build graybox layout in Tiled or simple placeholders.
3. Place encounters by design intent.
4. Tune checkpoint spacing by failure cost.
5. Add art and polish only after flow is stable.

## Progression Pattern

- Level N introduces one new demand.
- Level N+1 reinforces that demand.
- Level N+2 combines it with earlier skills.

## Common Failure Modes

- Visual noise hides threats.
- Enemy placement creates unavoidable damage.
- Recovery from failure is too slow.
- Difficulty jumps without tutorial reinforcement.

## Integration Notes For Phaser

- Keep level data in tilemaps or JSON, not hardcoded in scene logic.
- Separate spawn points, checkpoints, and scripted events into named layers or object groups.
- Keep entity tuning values in config so difficulty changes do not require code rewrites.

