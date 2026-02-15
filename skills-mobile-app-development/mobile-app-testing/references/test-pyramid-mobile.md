# Test Pyramid Mobile

Recommended layering:

- Unit: view models, reducers, validators, formatters
- Integration: service adapters, persistence, sync boundaries
- UI automation: critical user journeys
- Exploratory/manual: edge-case and UX quality checks

Keep E2E targeted and deterministic. Do not use E2E for all logic validation.

