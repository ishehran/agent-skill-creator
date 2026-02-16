# Web Animation Research Protocol

Use this protocol whenever motion behavior is requested.

## Objective

Find implementation approaches that are:
- technically sound
- accessible
- performant
- suitable for the current stack

## Search Query Patterns

Use targeted queries like:
- `<effect name> css animation example`
- `<effect name> web animations api`
- `<effect name> <framework> animation`
- `reduced motion <effect name>`
- `animation performance <effect name>`

For "3D pressable button" examples:
- `css 3d press button active transform`
- `pressable button depth shadow translateY`

## Source Priority

1. Official web standards/docs (for example MDN)
2. Official framework or library docs
3. Maintained repository examples
4. Inspiration galleries for style direction

## Evaluation Checklist

For each candidate approach, check:
1. Does it support all required states?
2. Does it support reduced-motion behavior?
3. Is it readable and maintainable in this codebase?
4. Is runtime cost acceptable for target devices?
5. Does it create console warnings/errors?

## Selection Rule

Pick the simplest approach that satisfies behavior and quality constraints.

Prefer CSS-only for lightweight effects.
Use WAAPI or libraries when orchestration complexity justifies it.

