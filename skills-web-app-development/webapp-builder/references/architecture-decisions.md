# Architecture Decisions

Use this guide to make high-impact choices early and document them in short ADRs.

## ADR Template (Use For Every Irreversible Choice)

```md
# ADR-00X: <Decision>

Date: YYYY-MM-DD
Status: Proposed | Accepted | Superseded
Owners: <team>

## Context
- What constraints exist?
- What risk are we reducing?

## Decision
- Chosen option and scope.

## Consequences
- Benefits
- Tradeoffs
- Migration path if this changes later
```

## Rendering Strategy

| Strategy | Best for | Tradeoffs |
|---|---|---|
| SPA | Productive app UX, rich client interactions | Slower first load, more client complexity |
| SSR | SEO + faster first paint for content-heavy pages | Server cost and hydration complexity |
| SSG | Mostly static content, docs, marketing | Dynamic content requires client fetch/invalidation |
| Hybrid | Mixed workloads | Highest operational complexity if unmanaged |

Choose per route class, not once for the whole app.

## Deployment Topology

| Topology | Start with when | Watch out for |
|---|---|---|
| Modular monolith | Most teams and v1 products | Enforce module boundaries or it degrades |
| Split services | Team scale and independent scaling needs | Network failures, contract drift, ops overhead |
| Edge + origin | Latency-sensitive read paths | Harder debugging and cache invalidation |

Prefer modular monolith first unless a hard constraint requires split services.

## API Style

| Style | Strong fit | Weak fit |
|---|---|---|
| REST | Resource-oriented CRUD with broad tooling | Complex graph fetches |
| RPC | Workflow/action-heavy domains | Less discoverable resource model |
| GraphQL | Many clients with variable data needs | Server complexity and caching pitfalls |

Use one dominant style. Mixed styles increase cognitive load.

## Multi-Tenancy Model

| Model | Isolation | Cost | Complexity |
|---|---|---|---|
| Shared schema (`tenant_id`) | Low | Low | Low |
| Schema per tenant | Medium | Medium | Medium |
| Database per tenant | High | High | High |

Decide this early. Migration later is expensive.

## Caching Policy

Define these explicitly:
1. What can be cached? (public, tenant-scoped, user-scoped)
2. Cache key format and TTL policy
3. Invalidation triggers
4. Stale read tolerance

Never add cache without owner + invalidation strategy.

## Background Job Model

Use async jobs for:
- email and notifications
- large imports/exports
- retriable third-party calls

Each job should have:
- idempotency key
- retry policy with cap
- dead-letter or failure queue
- correlation ID

## Data Ownership Rules

For each module/service, define:
- owned tables and write authority
- read-only dependencies
- allowed integration mechanisms (events, direct reads, APIs)

Undefined ownership causes coupling and data corruption.
