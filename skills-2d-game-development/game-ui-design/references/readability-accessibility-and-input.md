# Readability, Accessibility, and Input

Readable UI reduces failure that comes from misunderstanding, not skill.

## Readability Baseline

- Keep critical HUD text large enough for target resolution and play distance.
- Maintain contrast between text/icons and dynamic backgrounds.
- Add stroke, shadow, or backdrop for text on busy scenes.
- Prefer short labels over dense paragraphs during active gameplay.

## Color and State Meaning

- Do not encode critical meaning with color alone.
- Pair color states with shape, icon, text, or motion differences.
- Keep status colors consistent across screens (for example, red always means danger).
- Verify key states under color-vision simulation when possible.

## Input Clarity

- Show prompts using active input style (keyboard keys, controller buttons, or touch hints).
- Keep prompt placement close to interactive objects or decision points.
- Do not show conflicting prompts at the same time.
- Confirm remapped inputs update prompt labels correctly.

## Accessibility Controls to Expose

- UI scale slider
- subtitle on and off, plus size controls if dialogue exists
- motion reduction option for non-essential UI animation
- high-contrast or alternate palette option
- input remapping if action complexity is high

## Layout Safety

- Keep important UI out of edge-clipped regions and notches.
- Use padding from screen edges for all critical HUD elements.
- Validate layout in at least one narrow and one wide aspect ratio.

## Verification Checklist

1. Check HUD readability in bright and dark gameplay backgrounds.
2. Verify each critical state has at least two distinct signals.
3. Test all primary flows with keyboard and pointer, and controller if supported.
4. Confirm pause and settings are reachable without precision input.
