---
name: mobile-app-builder
description: "Design and build production mobile apps: architecture, offline sync, security, platform permissions, performance, and app lifecycle resilience. Trigger: 'build mobile app', 'mobile architecture', 'React Native app', 'Flutter app', 'iOS Android app'."
---

# Mobile App Builder

Build mobile apps as thin, testable slices with clear boundaries between UI, domain logic, and platform services.

## Default Mode: Requirements-First (No Fixed Stack)

Start from user journey and platform constraints.

Pick runtime only after requirements, delivery timeline, and release constraints are clear.

## STOP: Before Feature Implementation

Define these first:
1. Primary journey and time-to-value target
2. Runtime choice criteria and platform scope
3. Data model and offline/sync behavior
4. Authentication and session model
5. Permissions and device capability model
6. Performance and battery budget expectations

If unclear, stay in design mode.

## Reference Files

| When working on... | Read first |
|---|---|
| Architecture and boundary decisions | `references/architecture-decisions.md` |
| Data ownership, offline, and sync logic | `references/offline-sync-and-data.md` |
| Security and permission controls | `references/security-and-platform-permissions.md` |
| Performance and startup baseline | `references/performance-baseline.md` |

## Workflow

1. Define requirements and platform constraints.
2. Choose architecture and runtime with rationale.
3. Implement one critical journey end-to-end.
4. Add offline and recovery behavior.
5. Add observability and failure signals.
6. Add tests by layer.
7. Validate performance and lifecycle behavior on real devices.

## Non-Negotiables

- Validate all API and local input boundaries.
- Enforce authorization on backend and app action boundaries.
- Keep secrets out of source, logs, and client bundles.
- Handle app background/foreground transitions explicitly.
- Record why stack/runtime was chosen.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Build online-only assumptions | Breaks in weak network conditions | Design explicit offline and retry behavior |
| Ignore app lifecycle events | State corruption and user frustration | Handle pause/resume and cold start clearly |
| Permission requests without context | Lower trust and denial rates | Request just-in-time with clear purpose |
| Stack choice by trend only | Long-term mismatch | Choose from constraints and team needs |
| No performance guardrails | Slow startup and drop-off | Set startup and frame-time budgets early |

## Remember

Mobile apps run in variable network and device conditions. Design for resilience first.

