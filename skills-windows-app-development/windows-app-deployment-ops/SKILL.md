---
name: windows-app-deployment-ops
description: "Plan and run safe Windows app releases: build signing, staged rollout rings, update channels, rollback, support telemetry, and incident response. Trigger: 'release Windows app', 'desktop rollout', 'code signing', 'rollback desktop release'."
---

# Windows App Deployment Ops

Release desktop updates safely with clear gates, observability, and tested rollback paths.

## Default Mode: Safety-First (No Fixed Stack)

Use stack-agnostic release controls by default.

Apply stack-specific profiles only when repository signals clearly match one.

## STOP: Before Any Production Release

Define these first:
1. Release objective and risk level
2. Signing strategy and certificate handling
3. Rollout rings/channels
4. Rollback trigger and rollback method
5. Telemetry and support thresholds
6. Installer/update compatibility constraints

If unclear, do not release.

## Reference Files

| When working on... | Read first |
|---|---|
| CI/CD gates and artifact signing | `references/ci-cd-and-signing.md` |
| Staged rollout and rollback design | `references/release-rings-and-rollback.md` |
| Runtime observability and support readiness | `references/observability-and-support.md` |

Optional stack profiles:
- `profiles/README.md`
- one matching profile in `profiles/`

## Core Workflow

1. Classify release risk and choose rollout plan.
2. Build immutable artifacts and sign them.
3. Validate install/upgrade/rollback in staging.
4. Release to ring 0, then expand by health gates.
5. Monitor crash and support signals.
6. Halt or roll back on threshold breach.
7. Record release notes and lessons learned.

## Non-Negotiables

- Signed artifacts only.
- Immutable artifacts between test and production release.
- Explicit channel/ring strategy for every release.
- Rollback path tested before rollout.
- Clear support ownership during release window.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| One-shot global rollout | High blast radius | Use progressive release rings |
| Ad-hoc unsigned hotfixes | Trust and security risk | Emergency path with signing and audit |
| No updater compatibility test | Bricked update paths | Test upgrade matrix in staging |
| Release without support telemetry | Slow detection | Define crash and support gates first |

## Stack Profile Rule

1. Apply core guidance first.
2. Load one profile only on clear stack match.
3. Stay stack-agnostic when match is unclear.

## Remember

Users experience release quality through stability, update reliability, and recovery speed.

