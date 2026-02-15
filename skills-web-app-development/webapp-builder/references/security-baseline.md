# Security Baseline

Security is a delivery requirement, not a follow-up task.

## Authentication and Sessions

- Prefer mature auth providers/libraries over custom auth.
- Use secure cookie settings for session auth:
  - `HttpOnly`
  - `Secure`
  - `SameSite` aligned to flow requirements
- Expire sessions and rotate tokens/keys with clear policy.

## Authorization

Rules:
- authorization checks on every backend action
- tenant scoping validated server-side
- deny by default for unknown roles/permissions

Log authorization failures with actor, action, and resource context.

## Input and Output Safety

- validate and parse all input at trust boundaries
- encode/escape output contextually in HTML
- sanitize rich text with allowlist-based sanitization
- reject unknown fields where feasible

## CSRF, CORS, and Clickjacking

- CSRF protection for cookie-authenticated state-changing requests
- strict CORS allowlist (never `*` with credentials)
- frame protections for sensitive routes (`frame-ancestors` / `X-Frame-Options`)

## Secrets Management

- keep secrets in managed secret stores or environment injection
- never commit secrets to source
- do not log raw secrets, tokens, or PII
- rotate leaked credentials immediately

## Dependency and Supply Chain Hygiene

- pin critical dependency ranges
- run automated vulnerability scans in CI
- review transitive dependency risks for auth/crypto/network packages
- verify provenance of setup scripts and CI actions

## File Upload Controls

If uploads exist:
- check MIME type and file signature
- enforce size limits
- store outside executable/static roots
- generate randomized object keys
- scan files where policy requires

## Security Headers Baseline

Set and verify:
- `Content-Security-Policy`
- `Strict-Transport-Security`
- `X-Content-Type-Options: nosniff`
- `Referrer-Policy`
- `Permissions-Policy`

## Incident Readiness

Before production:
- centralize security-relevant logs
- alert on unusual auth failures and privilege changes
- document key rotation and forced session invalidation runbooks
