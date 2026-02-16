# Motion Accessibility And Performance

Animation quality includes accessibility and runtime cost.

## Accessibility Requirements

- support `prefers-reduced-motion` for non-essential effects
- keep focus state visible and independent from animation
- avoid motion-only communication for critical status
- keep text readable during and after transitions

## Performance Guidelines

Prefer animating:
- `transform`
- `opacity`

Avoid expensive layout thrash from animating:
- width/height for large surfaces
- top/left for frequently updated elements
- heavy filter chains on large regions

## Practical Validation

1. verify no dropped-frame feel on target devices
2. verify console has no animation/runtime errors
3. verify reduced-motion mode still preserves usability
4. verify interaction latency stays responsive during animations

## Decision Rule

If animation harms clarity, performance, or accessibility, simplify it.

