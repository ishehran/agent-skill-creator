# UI Feedback and Motion

Feedback should confirm actions and state changes quickly, with minimal noise.

## Signal Priority

- Critical: player death risk, incoming damage, objective failure.
- Important: objective progress, resource depletion, cooldown completion.
- Informational: pickups, score increments, non-blocking status updates.

Use the strongest visual treatment only for critical events.

## Feedback Matrix

| Event | Visual feedback | Audio feedback | Timing target |
|---|---|---|---|
| Player takes damage | short red flash on health region and hit indicator | hit cue | within 100 ms |
| Cooldown becomes ready | icon highlight pulse once | soft ready ping | within 150 ms |
| Objective updates | compact banner near top center | short confirm cue | within 200 ms |
| Invalid action | small shake or tint on blocked control | subtle error tick | immediate |

## Motion Rules

- Animate state changes, not idle UI loops.
- Keep short UI transitions in the 120 to 220 ms range.
- Keep modal transitions in the 180 to 300 ms range.
- Use easing that supports readability over flair.
- Cancel or shorten non-critical animation during combat intensity.

## Avoiding UI Noise

- Do not stack multiple simultaneous banners for the same event class.
- Coalesce repeated events into one update when possible.
- Rate-limit low-priority toasts and score popups.
- Reserve screen shake and strong flashes for rare high-impact moments.

## Test Pass

1. Trigger all critical events in a test scene.
2. Verify each event has one unambiguous signal path.
3. Verify feedback remains readable on low-end frame rate conditions.
