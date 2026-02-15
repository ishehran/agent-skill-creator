# Architecture Decisions

Choose architecture from operational constraints, not preference.

## Core Decisions

1. UI shell and state model
2. Domain service boundaries
3. IO adapters (filesystem, network, device)
4. Background task orchestration
5. Error and retry policy

## Suggested Boundary Rule

- UI layer: interaction and presentation only
- Domain layer: business rules and workflow policy
- Infrastructure layer: file, network, system APIs

Keep dependencies pointing inward toward domain rules.

