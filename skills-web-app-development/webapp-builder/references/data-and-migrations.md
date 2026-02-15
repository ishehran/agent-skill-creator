# Data and Migrations

Most production incidents in web apps involve schema drift, unsafe migrations, or missing indexes.

## Schema Design Basics

- Model invariants in the database when possible (constraints, unique keys, checks).
- Use explicit foreign keys unless there is a strong reason not to.
- Add indexes for known query patterns, not every column.
- Keep naming conventions consistent (`created_at`, `updated_at`, `tenant_id`).

## Expand-Contract Migration Pattern

Use this sequence for breaking changes:
1. Expand: add new columns/tables/indexes without removing old ones.
2. Dual write: update application to write old + new structures.
3. Backfill: migrate historical data in batches.
4. Cutover: switch reads to new structure.
5. Contract: drop old fields only after verification.

This avoids downtime and enables rollback.

## Backfill Strategy

Backfills should be:
- chunked (bounded batch size)
- resumable (checkpoint cursor)
- observable (progress metrics, error counts)
- safe to re-run (idempotent)

Never run massive one-shot writes in peak traffic.

## Transaction Boundaries

For each use case, define:
- what must be atomic
- what can be eventual
- what should be retried on conflict

Keep transactions short and predictable.

## Indexing Playbook

Before adding an index:
1. verify query shape
2. inspect current execution plan
3. estimate write amplification impact
4. test on realistic row counts

After adding index, verify read latency and write overhead.

## Soft Delete and Auditing

If recovery/audit is required:
- use `deleted_at` for soft delete
- track actor and reason where needed
- ensure unique constraints handle soft-deleted rows correctly

For compliance-heavy systems, add append-only audit tables for key actions.

## Data Seeding

Separate:
- deterministic test fixtures
- local dev seed data
- one-time production bootstrap data

Avoid ad-hoc manual data mutation in shared environments.

## Migration Review Checklist

- Is migration reversible?
- Are locks bounded and acceptable?
- Is rollout order documented (schema first, app second)?
- Is there a rollback path?
- Are metrics/alerts defined for cutover?
