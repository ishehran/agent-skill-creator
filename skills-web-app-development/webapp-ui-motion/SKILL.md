---
name: webapp-ui-motion
description: "Design and implement web UI from prompts and reference screenshots, then add production-ready motion by researching current animation patterns on the web. Trigger: 'replicate this UI', 'animate this interface', '3D button effect', 'match screenshot and add motion'."
---

# Web App UI Motion

Turn UI intent and reference screenshots into clean, responsive interfaces with purposeful animations.

## Default Mode: Reference-First, Motion-Second

Start by matching structure, hierarchy, and interaction states before adding motion polish.

Motion should improve clarity and feedback, not just decoration.

## STOP: Before Writing Final UI Code

Define these first:
1. Primary user journey on this screen
2. Must-match elements from references
3. Can-vary elements (layout, colors, type scale, spacing)
4. Motion style keywords (subtle, premium, playful, crisp)
5. Interaction states required (hover, focus, active, disabled, loading)
6. Performance and accessibility constraints (mobile targets, reduced motion)
7. Available visual references (screenshots, video clips, or motion examples)
8. Acceptance criteria (visual + behavior + console cleanliness)

If unclear, stay in wireframe/prototype mode.

## Reference Files

Read these before the relevant work:

| When working on... | Read first |
|---|---|
| Searching the web for animation patterns | `references/web-animation-research-protocol.md` |
| Matching references and iterating to target UI | `references/reference-to-ui-matching-loop.md` |
| Pressable and depth-driven controls (3D button behavior) | `references/pressable-3d-button-pattern.md` |
| Motion accessibility and runtime performance | `references/motion-accessibility-and-performance.md` |
| Converting user intent into implementation inputs | `references/ui-intent-brief-template.md` |

## Workflow

1. Capture a short UI intent brief and required states.
2. Analyze prompt + screenshots and map must-match vs can-vary areas.
3. Run targeted web research for animation patterns and implementation options.
4. Choose implementation strategy: CSS-only, WAAPI, or library-based.
5. Build static UI and responsive layout first.
6. Add state-driven motion (hover, focus, active, enter/exit, feedback).
7. Validate with screenshot comparison, console checks, and interaction tests.
8. Refine until acceptance criteria are met.

## Web Research Rule

For each non-trivial motion request:
1. Search the web for at least two implementation approaches.
2. Prefer official docs and maintained project docs first.
3. Cross-check accessibility and performance implications.
4. Record which approach was chosen and why.

Source priority:
- official standards/docs (for example MDN)
- official library/framework docs
- maintained repositories and trusted technical write-ups
- inspiration galleries (for style direction only)

## Missing Asset Rule

If required visual or interaction details are missing, ask the user before final implementation.

Ask for the minimum needed assets:
1. at least one screenshot for layout/style matching
2. short video or GIF when motion behavior is important
3. interaction state expectations if not visible in provided assets

If the user cannot provide assets:
- proceed with explicit assumptions
- label assumptions clearly in the output
- request confirmation before polishing/finalizing

## Non-Negotiables

- Ship all required interaction states, not just static visuals.
- Keep motion tied to user intent and state transitions.
- Honor reduced-motion preferences for non-essential animation.
- Keep console clean during interaction flows.
- Keep animations performant on typical hardware.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Copy a visual style without state behavior | UI looks right but feels broken | Implement full state model first |
| Add motion before layout is stable | Rework cost increases | Lock hierarchy and spacing first |
| Animate everything constantly | Noise and fatigue | Animate state changes and key feedback only |
| Ignore browser console during iteration | Hidden runtime issues survive | Validate console before/after major actions |
| Pick animation library without constraints | Mismatch and bloat | Choose based on stack and performance goals |

## Handoff Rule

After UI + motion behavior is stable:
1. Validate behavior quality using `../webapp-testing/SKILL.md`.
2. Continue delivery with `../webapp-deployment-ops/SKILL.md` when release-ready.

## Remember

Great UI motion makes interfaces easier to understand and trust.

Prioritize clarity, feedback, and consistency over visual gimmicks.
