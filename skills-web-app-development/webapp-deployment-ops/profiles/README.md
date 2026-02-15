# Stack Profiles

Profiles are optional overlays for stack-specific commands and conventions.

## Rule

- Start with the core deployment skill first.
- Load one profile only when the current project stack clearly matches it.
- If no profile matches, keep using the core skill and create a new profile from this template.

## Template

Copy and fill for a new stack profile:

```md
# <stack-name> Deployment Profile

## Applies when
- <stack detection signals>

## Build and test commands
- <exact commands>

## Migration flow
- <ordered schema/data steps>

## Release strategy defaults
- <rolling/canary/blue-green guidance>

## Health checks
- <required endpoints and checks>

## Rollback specifics
- <exact rollback commands and limits>
```

## Existing Profiles

- `nextjs-node-postgres.md`
- `react-fastapi-postgres.md`
