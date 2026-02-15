# Backend API Design

Build APIs as explicit contracts with stable semantics, typed validation, and predictable failures.

## Endpoint Design Rules

- Name resources/actions consistently.
- Use versioning strategy before public release.
- Keep write operations idempotent when possible.
- Return machine-parseable error codes.
- Avoid leaking internal exception strings.

## Request and Response Contracts

Define per endpoint:
1. authentication requirement
2. authorization policy
3. input schema and constraints
4. response schema and status codes
5. side effects (writes, events, external calls)

Treat schema as source of truth for docs and tests.

## Idempotency

Use idempotency keys for create/payment-like operations:
- client sends `Idempotency-Key`
- server stores key + outcome for a bounded window
- repeat requests return the original outcome

Do this before handling retries in clients or queues.

## Error Model

Example shape:

```json
{
  "error": {
    "code": "INVALID_INPUT",
    "message": "Email is required",
    "details": [{ "field": "email", "reason": "required" }],
    "request_id": "req_123"
  }
}
```

Guidelines:
- `code` is stable for automation.
- `message` is user-safe and localizable.
- include `request_id` for support and tracing.

## Pagination

Prefer cursor pagination for mutable lists:
- request: `?limit=50&cursor=...`
- response: `items`, `next_cursor`

Offset pagination can be acceptable for small, mostly static datasets.

## Concurrency Controls

For update conflicts use one:
- optimistic concurrency (`version` or `updated_at` check)
- explicit locking for high-contention workflows

Never rely on "last write wins" for business-critical entities.

## Authorization Pattern

Enforce policy in handler/service layer:

```txt
authenticate -> load actor + tenant -> authorize(action, resource) -> validate -> execute
```

UI guards are not security controls.

## Integration Boundaries

When calling external systems:
- set timeout and retry budget
- classify retryable vs non-retryable errors
- capture request/response metadata safely
- add circuit-breaker or fallback for unstable dependencies

## Observability Contract

Each request should emit:
- request ID
- actor/tenant context (non-sensitive)
- endpoint + status + latency
- error code when failed

Without this, incident response is slow and speculative.
