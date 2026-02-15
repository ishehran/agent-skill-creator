# React + FastAPI + Postgres Deployment Profile

## Applies when

- frontend is React SPA (or React with SSR framework where API is FastAPI)
- backend is Python FastAPI service
- primary datastore is Postgres

## Build and Test Commands (Example)

Frontend:

```bash
npm ci
npm run lint
npm run test
npm run build
```

Backend:

```bash
pip install -r requirements.txt
pytest
```

Use lockfiles and pinned dependencies for reproducible builds.

## Migration Flow

1. run schema migration in pre-deploy or controlled deploy step
2. deploy FastAPI version compatible with old/new schema
3. deploy React frontend after backend compatibility is confirmed
4. execute backfill jobs asynchronously if required
5. remove deprecated fields in a separate release

## Release Strategy Defaults

- default: rolling backend + static frontend rollout
- API contract changes: canary backend first
- high-risk permission or billing changes: canary plus feature flag

## Health Checks

Backend:
- `/healthz` or `/readyz`
- database connectivity check
- queue/dependency checks if async jobs exist

Frontend:
- static asset availability check
- API smoke action from browser context

## Rollback Specifics

- rollback backend container/artifact first if API regressions appear
- rollback frontend artifact if UI-only regression
- disable newly introduced flags before full rollback when possible
- confirm contract compatibility after rollback
