# CI/CD Pipeline Design

Pipelines should block unsafe changes and accelerate safe ones.

## Pipeline Stages

Recommended order:
1. Lint and static checks
2. Unit tests
3. Integration and contract tests
4. Build artifact and SBOM/provenance metadata
5. Security scans (dependencies and artifacts)
6. Deploy to staging
7. Smoke tests in staging
8. Production deployment gate
9. Post-deploy verification

Fail fast at the earliest stage that can detect the problem.

## Artifact Strategy

- Build once, promote many.
- Tag artifacts with commit SHA and build ID.
- Store checksums and metadata for traceability.
- Do not rebuild per environment.

## Deployment Gates

Common gate criteria:
- all required tests pass
- migration plan approved
- error budget allows release
- on-call and rollback path confirmed

Use explicit gates for high-risk changes.

## Concurrency Controls

Protect production from overlapping releases:
- one production deployment lock per service
- cancel stale pipelines on new commits (for non-release branches)
- require revalidation if deployment waits too long

## Rollback Automation

Pipeline should support:
- one-command rollback to last known good version
- optional automatic rollback on critical signal breach
- clear notification with rollback result

## Metrics For Pipeline Health

Track:
- lead time to production
- deployment frequency
- change failure rate
- mean time to recovery

These indicate whether delivery is both fast and safe.
