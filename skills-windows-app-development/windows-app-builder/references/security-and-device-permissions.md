# Security And Device Permissions

Model local capabilities as explicit permissions, not implicit assumptions.

## Checklist

- required filesystem paths and access mode
- network endpoint allowlist
- device integrations (camera, mic, USB, clipboard)
- token storage strategy
- encryption requirements at rest and in transit

## Baseline Controls

- least privilege by default
- secure credential storage
- redact sensitive values from logs
- explicit user consent for sensitive actions
- signed artifacts for release distribution

