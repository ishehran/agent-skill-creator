---
name: game-ui-design
description: "Design and tune UI systems for 2D games: HUD hierarchy, menus, readability, feedback timing, and accessibility-aware controls. Trigger: 'game UI', 'HUD design', 'pause menu', 'inventory UI', 'health bar', '2D UI design'."
---

# 2D Game UI Design

Design game UI that helps players make fast, correct decisions without losing focus on gameplay.

## Default Mode: Clarity-First UI

Start from information hierarchy and player decisions before visual polish.

If the UI looks good but players misread state, the UI is not ready.

## STOP: Before Building Final UI Assets

Define these first:
1. Core decisions players must make in each phase (combat, traversal, shop, pause)
2. HUD priority tiers (always visible, contextual, hidden by default)
3. Screen-state map (HUD, pause, settings, inventory, game over)
4. Input model coverage (keyboard, mouse, touch, controller if supported)
5. Feedback rules for critical events (damage, healing, cooldown ready, objective update)
6. Readability targets (minimum text size, contrast, safe area, target resolution)

If unclear, keep UI in wireframe mode.

## Reference Files

Read these before the related work:

| When working on... | Read first |
|---|---|
| HUD information hierarchy and layout zones | `references/hud-information-hierarchy.md` |
| UI feedback timing, motion, and event signaling | `references/ui-feedback-and-motion.md` |
| Readability, accessibility, and input affordances | `references/readability-accessibility-and-input.md` |
| Phaser spritesheet slicing and scalable panels | `../phaser-gamedev/references/spritesheets-nineslice.md` |

## Workflow

1. Write a UI intent brief in 5 to 10 lines.
2. Map screen states and allowed transitions.
3. Wireframe HUD with information tiers and anchor zones.
4. Add event feedback for damage, goals, inventory, and cooldowns.
5. Validate readability at target resolution and distance.
6. Add styling and animation only after hierarchy is stable.
7. Run targeted UI regression checks in deterministic test scenes.

## Non-Negotiables

- Keep critical status visible during action (health, objective, immediate risk).
- Use consistent placement for recurring controls and counters.
- Keep UI state transitions explicit and reversible (pause, settings, overlays).
- Use color plus shape and text cues for important signals.
- Design for low-attention moments and high-pressure gameplay equally.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Put every metric on the HUD | Cognitive overload during play | Keep only decision-critical info always visible |
| Use color only for status meaning | Fails for color-vision variance and glare | Pair color with icons, labels, and motion |
| Animate every UI element constantly | Visual noise and reduced focus | Animate only state changes and high-priority alerts |
| Place menus without a state map | Dead-end flows and inconsistent back behavior | Define transitions and back-stack rules first |
| Final art pass before wireframe validation | Expensive rework after playtests | Validate hierarchy and flow before polish |

## Handoff Rule

After UI design decisions are stable:
1. Implement scenes and UI components in `../phaser-gamedev/SKILL.md`.
2. Add deterministic UI checks in `../playwright-testing/SKILL.md`.

## Remember

Game UI is part of gameplay, not decoration.

Optimize for decision speed, readability, and trust.
