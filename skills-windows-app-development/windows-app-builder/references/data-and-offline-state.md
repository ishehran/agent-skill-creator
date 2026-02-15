# Data And Offline State

Desktop apps frequently work with local files and intermittent connectivity.

## Minimum Design Set

- local storage format and migration strategy
- cache invalidation policy
- conflict handling rules for sync
- backup or restore pathway

## Safety Rules

- write atomically where possible
- guard against partial writes and process interruption
- validate data schema on load
- preserve previous known-good state during migration

