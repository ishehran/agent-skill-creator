# Observability and SLOs

Use observability as a release safety system, not only a debugging tool.

## Minimum Signals Per Service

Track and dashboard:
- request volume
- error rate
- latency percentiles (p50/p95/p99)
- resource saturation (CPU, memory, queue depth)

For async workflows, add:
- queue lag
- retry and dead-letter counts

## SLI and SLO Model

Define:
- user-facing SLI (availability, latency, correctness)
- SLO targets per SLI
- error budget policy for release decisions

Example:
- Availability SLO: 99.9% monthly
- API p95 latency SLO: < 300 ms

## Alerting Principles

- Alert on user impact, not every infrastructure spike.
- Use severity levels with clear escalation targets.
- Page only for actionable incidents.
- Include links to runbook and dashboard in alert payload.

## Release Verification Checklist

Immediately after deployment:
1. confirm health endpoints and startup checks
2. validate error rate and latency guardrails
3. run one business smoke action end to end
4. confirm logs/traces include current version tag

If checks fail, rollback fast.

## Logging and Tracing

- use structured logs with request and correlation IDs
- include deploy version in logs and spans
- mask sensitive fields
- sample traces intelligently, not randomly for critical paths

## Operational Dashboards

Every service should have:
- real-time health panel
- release comparison panel (before/after)
- dependency health panel
- business KPI sanity panel
