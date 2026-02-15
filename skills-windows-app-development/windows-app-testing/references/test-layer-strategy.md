# Test Layer Strategy

Use layers by cost and signal:

- Unit: pure rules, parsing, transforms, validators
- Integration: module boundaries, storage adapters, sync logic
- UI automation: critical user workflows and visual states
- Installer/update: install, upgrade, rollback, uninstall
- Resilience: restart, crash recovery, data integrity

Prioritize one reliable smoke path before broad expansion.

