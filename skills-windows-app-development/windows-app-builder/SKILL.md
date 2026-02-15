---
name: windows-app-builder
description: "Design and build production Windows desktop apps: architecture, local data, permissions, packaging choices, update model, and reliability. Trigger: 'build Windows app', 'desktop architecture', 'WinUI app', 'Electron app', 'Tauri app'."
---

# Windows App Builder

Build Windows apps as thin, testable slices with explicit boundaries between UI, domain logic, and platform services.

## Default Mode: Requirements-First (No Fixed Stack)

Start with workflow requirements and constraints.

Pick runtime only after requirements and deployment constraints are clear.

## STOP: Before Feature Implementation

Define these first:
1. App type: utility, workflow tool, or background-heavy app
2. Runtime choice criteria and target architecture
3. Data model and storage strategy
4. Offline behavior and sync requirements
5. Permission and local resource access model
6. Installer and update expectations

If unclear, continue design mode.

## Reference Files

| When working on... | Read first |
|---|---|
| Overall architecture and boundaries | `references/architecture-decisions.md` |
| Local storage, cache, and offline behavior | `references/data-and-offline-state.md` |
| Permissions and secure local operations | `references/security-and-device-permissions.md` |
| Packaging/runtime tradeoffs | `references/packaging-choices.md` |

## Workflow

1. Define requirements and constraints.
2. Pick architecture and runtime with recorded rationale.
3. Implement one critical workflow end-to-end.
4. Add data persistence and recovery path.
5. Add error handling and logging seams.
6. Add tests by layer.
7. Verify install/update behavior in local environment.

## Non-Negotiables

- Validate all external and file inputs.
- Keep secrets and tokens out of logs and source.
- Separate UI from domain and IO adapters.
- Handle app restart and crash recovery explicitly.
- Record why stack/runtime was selected.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Pick runtime from habit only | Mismatch to constraints | Choose from requirements and ops model |
| Mix UI and business logic deeply | Hard to test and evolve | Use service boundaries and adapters |
| Ignore offline or file lock scenarios | Data loss and corruption risk | Add resilience and retry policies |
| No update strategy during build | Risky late-stage rework | Design update model early |
| Unbounded local logging | Disk bloat and privacy risk | Structured logs with retention controls |

## Remember

Desktop apps are long-lived processes. Design for interruption, recovery, and predictable updates.

