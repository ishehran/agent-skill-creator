# Delivery Checklist

Use this checklist before promoting features to production.

## Build and Test Gates

- Unit tests cover core domain logic.
- Integration tests cover API and persistence seams.
- E2E smoke test covers at least one critical journey.
- Static analysis and formatting pass in CI.
- Build is reproducible in clean environment.

## Runtime Safety Gates

- Feature flags for high-risk behavior changes.
- Migration rollout order documented and reviewed.
- Rate limits and timeout defaults configured.
- Health checks and readiness probes in place.
- Rollback command or procedure tested.

## Observability Gates

- Structured logs include request IDs.
- Metrics include latency, error rate, and saturation.
- Alerts mapped to user impact, not only infrastructure events.
- Dashboards exist for core journey success metrics.

## Product Quality Gates

- Empty, loading, and error states implemented.
- Permission-denied states handled gracefully.
- Forms return actionable validation messages.
- Accessibility checks pass for keyboard flow and labels.

## Launch Readiness Questions

1. What is the blast radius if this feature fails?
2. How quickly can we detect failure?
3. How quickly can we disable or rollback?
4. Who is on point during and after release?

If any answer is unclear, release readiness is incomplete.

## Post-Launch Verification

- Confirm adoption and success metrics after rollout.
- Inspect error logs and retries for hidden regressions.
- Remove temporary logging and temporary retries after stabilization.
- Document lessons learned in short decision notes.
