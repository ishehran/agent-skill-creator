---
name: webapp-deployment-ops
description: "Plan and run safe web app delivery in production: CI/CD gates, release strategies, environment/config discipline, observability, incident response, rollback, and operational security. Trigger: 'deploy web app', 'production release', 'rollback', 'SLO', 'incident response'."
---

# Web App Deployment Ops

Ship changes safely, detect regressions quickly, and recover fast when things break.

## Default Mode: Requirements-First (No Fixed Stack)

Operations should stay stack-agnostic by default.

Start from release risk, user impact, and reliability goals. Use stack profiles only when the current repository clearly matches one.

## Philosophy: Safety and Speed Together

Reliable delivery is not slow delivery. Reliability comes from:
- clear release strategies
- measurable health signals
- automated guardrails
- tested rollback paths

## STOP: Before Any Production Deployment

Define these first:
1. Release objective and expected user impact
2. Change risk level (low, medium, high)
3. Release strategy (rolling, canary, blue-green, etc.)
4. Rollback trigger and rollback command
5. Health checks and SLO impact thresholds
6. Migration plan and sequencing

If these are unclear, do not deploy.

## Reference Files

Read these before the relevant work:

| When working on... | Read first |
|---|---|
| Requirements-first release planning | `../requirements-first-template.md` |
| CI pipeline design and release gates | `references/ci-cd-pipeline-design.md` |
| Environment model, config, and secret handling | `references/environment-and-config.md` |
| Rollout strategies and rollback playbooks | `references/release-strategies.md` |
| Monitoring, SLOs, and release verification | `references/observability-and-slos.md` |
| Live incident handling and post-incident work | `references/incident-response.md` |
| Ops-side security controls | `references/operations-security.md` |

Optional stack-specific overlays (only if stack is clearly known):
- `profiles/README.md`
- one matching profile in `profiles/`

## Core Deployment Workflow

1. Classify release risk and choose strategy.
2. Run CI gates and produce immutable artifact.
3. Apply schema/config changes in approved order.
4. Deploy with staged exposure (if risk is medium/high).
5. Verify technical and business health signals.
6. Roll back immediately if guardrails breach.
7. Record release notes and operational learnings.

## Non-Negotiables

- Immutable build artifacts between staging and production.
- No manual production edits outside approved emergency path.
- Secrets come from managed stores, never repo files.
- Release decisions based on observable metrics, not intuition.
- Every production service has health endpoints and runbooks.
- On-call ownership is clear before release starts.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Force a stack profile without clear match | Wrong commands and checks | Use core flow first; add profile only on clear stack detection |
| Deploy and "watch logs manually" | Slow, inconsistent detection | Predefined SLO/alert gates |
| Run risky migrations during cutover blindly | Locks and outages | Expand-contract and staged cutover |
| Rebuild separately for prod | Artifact drift | Promote same tested artifact |
| One giant Friday release | High blast radius | Small, frequent, observable releases |
| Rollback plan not tested | Recovery fails under pressure | Dry-run rollback in staging |
| Stack-specific assumptions in core process | Process brittle across projects | Stack-agnostic core + optional profile |

## Stack Profile Rule

Use this order:
1. Apply core skill guidance first.
2. Load exactly one stack profile only if repository signals clearly match.
3. If no clear match exists, continue stack-agnostic using the core flow.
4. If needed later, use `profiles/README.md` to create a profile.

This keeps the core stable while allowing stack-specific acceleration.

## Remember

Deployment is part of product behavior. Users experience your release process directly through uptime, latency, and correctness.

Optimize for predictable operations, not heroic interventions.
