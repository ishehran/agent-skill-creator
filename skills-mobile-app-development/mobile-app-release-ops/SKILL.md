---
name: mobile-app-release-ops
description: "Plan and run safe mobile app releases: release trains, staged rollout, store readiness, rollback, incident response, and post-release monitoring. Trigger: 'release mobile app', 'App Store rollout', 'Play Store rollout', 'mobile rollback'."
---

# Mobile App Release Ops

Release mobile updates safely with explicit gates, staged exposure, and measurable health checks.

## Default Mode: Safety-First (No Fixed Stack)

Use stack-agnostic release controls by default.

Load stack-specific profiles only when repository signals clearly match one.

## STOP: Before Any Production Release

Define these first:
1. Release objective and risk level
2. Release train and rollout strategy
3. Store compliance and metadata readiness
4. Rollback/mitigation plan
5. Post-release health thresholds
6. Incident owner and response path

If unclear, do not release.

## Reference Files

| When working on... | Read first |
|---|---|
| Release gates and rollout sequencing | `references/release-trains-and-gating.md` |
| Store policy and submission readiness | `references/store-readiness-and-compliance.md` |
| Incident handling and rollback actions | `references/incident-response-mobile.md` |

Optional stack profiles:
- `profiles/README.md`
- one matching profile in `profiles/`

## Core Workflow

1. Classify release risk and choose rollout plan.
2. Build immutable signed artifacts.
3. Validate critical flows on release candidate matrix.
4. Publish to limited rollout cohort.
5. Monitor crash, startup, and critical flow metrics.
6. Expand rollout by passing health gates.
7. Halt, mitigate, or roll back when thresholds fail.

## Non-Negotiables

- Immutable signed artifacts only.
- Staged rollout for non-trivial releases.
- Predefined stop/go criteria before publishing.
- Clear incident ownership through release window.
- Post-release review and learning capture.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Immediate 100 percent rollout | Large blast radius | Progressive rollout with gates |
| Publish without crash baseline | Delayed detection | Define baseline and threshold first |
| Last-minute store metadata fixes | Rejection and delays | Complete compliance checklist earlier |
| No mitigation plan for hot issues | Slow recovery | Define rollback and feature flag plan |

## Stack Profile Rule

1. Apply core guidance first.
2. Load one profile only on clear stack match.
3. Stay stack-agnostic when match is unclear.

## Remember

Mobile release quality is user trust. Stability, quick recovery, and clear communication matter as much as features.

