# Frontend System Design

Design the frontend as a set of stable boundaries: route, feature, component, data cache.

## Feature Slice Structure

Use vertical slices, not type-based sprawl:

```txt
src/
  features/
    billing/
      api.ts
      hooks.ts
      components/
      routes/
      schema.ts
      tests/
```

Each feature owns:
- API adapters
- input/output schemas
- rendering components
- tests

## State Model

Split state by source of truth:
- server state: cache/query library
- UI state: local component state
- cross-route ephemeral state: route state or small store
- durable client state: persisted settings only

Avoid one global store for everything.

## Data Fetching Contract

For each query/mutation define:
1. cache key format
2. freshness window
3. invalidation triggers
4. optimistic update policy
5. rollback behavior on error

Unclear invalidation is a common bug source.

## Forms and Validation

Rules:
- validate in UI for ergonomics
- validate again on server for correctness
- keep validation schema as close to domain model as possible
- map backend field errors to user-facing messages deterministically

## Rendering and UX Performance

Prioritize:
- route-level code splitting
- list virtualization for large datasets
- skeletons over blocking spinners
- prefetch next likely route/data

Measure with real production-like data, not toy mocks.

## Accessibility Baseline

Every feature should include:
- semantic landmarks and labels
- keyboard-only navigation checks
- focus management on modal/dialog open and close
- status/error announcements for async operations

Do not ship feature-complete but keyboard-broken flows.

## Frontend Error Handling

Use layered handling:
- field errors: inline
- feature errors: non-blocking alert in context
- route errors: route-level boundary
- app errors: global boundary + fallback + telemetry

Emit structured telemetry with route and action context.

## Anti-Patterns

| Anti-pattern | Symptom | Fix |
|---|---|---|
| Shared mutable singleton state | Random stale UI bugs | Feature-owned state and explicit events |
| Direct fetch calls in random components | Duplicate logic and error handling drift | Feature API adapters |
| Silent recoveries | Users lose trust | Explicit, user-visible state for failures |
| CSS-only disabled buttons for auth | Unauthorized actions still sent | Backend authz + frontend affordance |
