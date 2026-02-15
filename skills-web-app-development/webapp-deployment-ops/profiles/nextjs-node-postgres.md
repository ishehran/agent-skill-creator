# Next.js + Node + Postgres Deployment Profile

## Applies when

- frontend is Next.js (App Router or Pages Router)
- backend is Node.js service(s) or Next.js API routes
- primary datastore is Postgres

## Build and Test Commands (Example)

Adjust package manager as needed:

```bash
pnpm install --frozen-lockfile
pnpm -r lint
pnpm -r test
pnpm -r build
```

For monorepos, ensure workspace filters include all deployable units.

## Migration Flow

1. apply backward-compatible migration
2. deploy app version compatible with old/new schema
3. run backfill jobs if needed
4. switch feature flag or traffic
5. remove deprecated schema in later release

Never tie irreversible schema changes to same-step app cutover.

## Release Strategy Defaults

- default: rolling for low-risk changes
- medium/high risk: canary with guarded ramp
- critical path changes: blue-green when fast rollback is required

## Health Checks

Required:
- app health endpoint (`/health` or `/api/health`)
- dependency check (database reachability)
- synthetic smoke for one key user path

Optional but useful:
- readiness endpoint separate from liveness
- build/version endpoint for release tracing

## Rollback Specifics

- rollback app image to prior release tag
- if migration is expand-only, no DB rollback needed
- if cutover flag was enabled, disable flag first
- verify error rate and latency normalize after rollback
