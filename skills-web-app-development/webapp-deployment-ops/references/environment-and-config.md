# Environment and Config

Environment discipline prevents most "works in staging, breaks in prod" failures.

## Environment Model

Define clear purpose for each environment:
- local: developer iteration
- test/preview: PR validation
- staging: production-like release rehearsal
- production: user traffic

Do not skip staging for risky changes.

## Configuration Taxonomy

Classify configuration as:
- static build-time config
- dynamic runtime config
- secrets

Each class should have separate handling and ownership.

## Configuration Rules

- Keep config in declarative source of truth (infra as code).
- Validate config shape in CI before deployment.
- Version config changes with code changes when coupled.
- Avoid hidden config defaults that differ by environment.

## Secret Management

- Inject secrets at runtime from managed secret systems.
- Rotate secrets with documented procedure.
- Restrict secret access by least privilege.
- Never print secrets in logs or command output.

## Environment Parity

Parity goals:
- same runtime major versions
- same key dependencies and backing services
- same critical feature flags default states

Perfect parity is unrealistic, but critical dependency parity is mandatory.

## Feature Flags and Kill Switches

Use flags for risky behavior changes:
- define owner and expiry date per flag
- document blast radius
- include immediate kill switch for high-risk features

Remove stale flags after stabilization.
