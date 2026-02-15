# Offline Sync And Data

Mobile behavior must remain coherent under unreliable network.

## Minimum Design Set

- source of truth definition
- local cache and persistence model
- sync trigger strategy
- conflict resolution rules
- retry and backoff behavior

## Safety Rules

- preserve last known-good local state
- validate schema and migrations on startup
- design idempotent writes where possible
- expose sync status to users when relevant

