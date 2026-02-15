# HUD Information Hierarchy

Design HUD layers so players can answer the right question at the right time.

## Core Questions the HUD Must Answer

- Can I survive the next few seconds?
- What should I do next?
- How close am I to success or failure?

## Three-Tier Model

### Tier 1: Always Visible

Use for decision-critical status:
- health, shield, lives, stamina, or equivalent survival signal
- immediate objective summary
- one core resource tied to the primary loop (ammo, mana, energy)

Rules:
- fixed placement every screen
- readable in peripheral vision
- no overlap with major action areas

### Tier 2: Contextual

Use for temporary state:
- interaction prompts
- cooldown-ready messages
- combo and streak notifications
- objective update popups

Rules:
- appear only when relevant
- auto-dismiss cleanly
- avoid covering player path or hazard telegraphs

### Tier 3: On-Demand

Use for planning and deep detail:
- map
- inventory and crafting
- codex and advanced stats

Rules:
- explicit open and close action
- preserve return position and prior selection
- do not mix with real-time action clutter

## Anchor-Zone Pattern

Use stable zones so players build muscle memory:

- top-left: player state
- top-right: score, timer, mission progress
- center: short urgent alerts only
- bottom-center: contextual input prompts
- edges or modal center: menus and settings

## Validation Checklist

Before final art pass:
1. Run a combat or high-action segment and check if players can read Tier 1 at a glance.
2. Confirm contextual popups do not hide hazards or enemies.
3. Confirm every screen state has predictable open, close, and back behavior.
