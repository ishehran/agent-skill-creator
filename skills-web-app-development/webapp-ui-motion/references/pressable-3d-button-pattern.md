# Pressable 3D Button Pattern

Use this pattern when the user asks for "3D button" behavior.

## Interaction Goal

Button should feel raised at rest, then compress on press with clear tactile feedback.

## Visual Model

- rest: raised element with depth shadow
- hover/focus: slightly elevated emphasis
- active/pressed: lower position and reduced shadow depth
- disabled: reduced contrast and no tactile motion

## Core CSS Pattern (Concept)

- use layered shadow for depth
- use `transform: translateY(...)` on active state
- shorten active transition for tactile response
- keep focus-visible style explicit and high contrast

Example state mapping:
- rest: `translateY(0)`
- hover: `translateY(-1px)` with stronger shadow
- active: `translateY(2px)` with shallower shadow

## Timing Guidance

- hover/focus transitions: around 120 to 180 ms
- active press feedback: around 60 to 120 ms
- avoid spring-like overshoot for critical controls unless intentional

## Accessibility Notes

- preserve clear keyboard focus ring
- do not rely only on motion to indicate press
- ensure disabled state remains distinguishable without animation
- respect reduced-motion settings by minimizing non-essential movement

## Common Mistakes

- depth effect only in default state, no press response
- active transform with no shadow adjustment
- removing focus outline for aesthetics
- excessive press distance that feels unrealistic

