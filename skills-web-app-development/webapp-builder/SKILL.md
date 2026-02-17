---
name: webapp-builder
description: "Design and build production web apps (frontend + backend): architecture, API/data modeling, auth, security, migrations, deployment, and observability. Trigger: 'build web app', 'full stack app', 'API + frontend', 'web architecture'."
---

# Web App Builder

Build web applications as thin, testable vertical slices with explicit contracts between UI, API, and data.

## Default Mode: Requirements-First (No Fixed Stack)

This skill assumes you may not want to choose frameworks up front.

Start from product requirements and user outcomes. Let Codex choose a fitting stack for each project based on constraints. Lock a specific stack only when:
- the repo already exists
- integrations force a choice
- business or platform constraints require it

## Philosophy: Risk-First Delivery

Ship the smallest slice that proves the highest-risk assumptions first:
- auth and permissions
- data model and migrations
- external integrations
- performance on realistic data

If a decision is hard to reverse later, make it explicit now.

## STOP: Before Writing Feature Code

Create a short requirements brief first:
1. User problem and target outcome
2. One critical user journey (start to success)
3. Must-have features for v1
4. Data to store and sensitivity level
5. External integrations
6. Security and compliance level
7. Scale/performance expectation
8. Asset strategy for UI visuals (source files available vs placeholders)
9. Timeline and success metric

Then capture implementation decisions:
1. Rendering strategy: SPA, SSR, SSG, or hybrid
2. API style: REST, RPC, or GraphQL
3. Data ownership: single database schema boundaries and transaction rules
4. Authn/authz model: session or token, role model, permission checks
5. Deployment shape: single service, modular monolith, or split services

Do not start implementation until the requirements brief and decision notes are written down.

## Reference Files

Read these before implementing the related area:

| When working on... | Read first |
|---|---|
| Requirements-first planning | `../requirements-first-template.md` |
| Top-level architecture and stack choices | `references/architecture-decisions.md` |
| Client-side boundaries, state, and UX performance | `references/frontend-system-design.md` |
| Endpoints, contracts, idempotency, and error model | `references/backend-api-design.md` |
| Schema design, indexing, and migrations | `references/data-and-migrations.md` |
| Auth, validation, secrets, and web security controls | `references/security-baseline.md` |
| Release readiness and operational gates | `references/delivery-checklist.md` |

## Execution Workflow

1. Create the requirements brief.
2. Choose stack and architecture from constraints (and record why).
3. Specify API and data contracts for one critical journey.
4. Implement backend handler + migration + validation first.
5. Implement frontend flow against the contract.
6. Add tests by layer: unit, integration, E2E smoke.
7. Add observability for success/failure signals.
8. Ship behind a flag when risk is high.

## Non-Negotiables

- Validate all inputs at API boundaries.
- Enforce authorization in backend handlers, not only UI.
- Use reversible migration strategy (expand, migrate, contract).
- Keep secrets out of source and logs.
- Emit structured logs with request correlation IDs.
- Add at least one E2E smoke path for each critical journey.
- Record why the stack was chosen for this project.
- Use proper source assets for shipped UI (do not use cropped screenshot fragments).

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Pick stack first out of habit | Solves implementation before user problem | Start with requirements brief, then select stack |
| Start with pages before contracts | UI and backend drift | Define API/data contracts first |
| Shared mutable global state in frontend | Race conditions and stale UI | Isolated state + cache invalidation rules |
| One migration that drops and recreates data | Irreversible outages | Expand-contract with backfill |
| Auth only in frontend guards | Easy privilege bypass | Server-side policy checks per action |
| Retry everything blindly | Duplicate writes and hidden incidents | Idempotency keys + explicit retry policy |
| Logs without request context | Impossible incident debugging | Correlation IDs + structured events |

## Variation Guidance

Vary approach based on constraints:
- No fixed stack workflow: let Codex choose stack after requirements.
- MVP startup: optimize for speed, but keep migration and auth discipline.
- Regulated domain: stricter audit trails, permission granularity, and change controls.
- High read scale: add caching strategy and read replicas early.
- Heavy workflows: emphasize background jobs, idempotency, and compensation logic.

## Remember

A web app is a distributed system with a UI. Most failures happen at boundaries:
- browser to API
- API to database
- service to service
- release to production runtime

Make boundaries explicit, test them directly, and instrument them from day one.
