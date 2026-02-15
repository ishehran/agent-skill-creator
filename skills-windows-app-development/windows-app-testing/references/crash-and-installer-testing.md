# Crash And Installer Testing

Treat packaging and recovery as core acceptance criteria.

## Installer Coverage

- clean install
- upgrade from previous version
- uninstall cleanup behavior
- install with restricted permissions scenario

## Recovery Coverage

- forced process kill and restart
- corrupted or partial local state
- failed update rollback
- first run after rollback

Release should be blocked until these checks are stable.

