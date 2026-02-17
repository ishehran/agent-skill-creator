## Playwright MCP Cheatsheet (Web Apps)

Use this when driving browser tests via MCP-compatible tools in an AI coding assistant.

### Core Sequence

1. Navigate to app URL.
2. Wait for explicit readiness signal.
3. Capture diagnostics baseline (console + network).
4. Perform user actions.
5. Assert outcomes and collect evidence on failure.

### Server Port Reservation

Use whatever server topology the scenario requires.

Reserve port `3000` for manual preview and avoid it for automation runs.

Suggested automation ports:
- frontend: `4173` (or `5173`)
- API: `4100`-`4199`
- extra services: `4200+`

### Readiness Patterns

Preferred:
- wait for stable DOM marker (`data-testid="app-ready"`)
- or evaluate `window.__TEST__?.ready === true`

Avoid:
- blind fixed delays
- broad "wait for network idle" on apps with polling/websocket traffic

### Diagnostic Collection

Always gather on failure:
- console messages
- failed network requests
- screenshot
- optional state dump (`window.__TEST__.state()`)

This reduces triage time significantly.

### Console-First Loop

Use this loop for every critical test flow:
1. Collect console immediately after readiness.
2. Run one user action block.
3. Collect console again.
4. Triage only newly added messages.
5. Fail on unexpected errors and unhandled promise rejections.

Do not defer console checks until the end of a long flow.

### MCP Command Checklist

When available in your environment, use:
- `browser_console_messages` before and after major actions
- `browser_network_requests` to correlate console errors with failed calls
- `browser_evaluate` for `window.__TEST__.ready` and optional state seam checks
- `browser_take_screenshot` when failures occur

If MCP console commands are unavailable, capture equivalent output through test-runner hooks and keep the same fail policy.

### Selector Strategy

Prefer in this order:
1. role + accessible name
2. visible text
3. label/placeholder
4. stable test IDs

Avoid brittle structural selectors based on class chains.

### Determinism Controls

For stable visual and timing checks:
- fix viewport and device scale factor
- set locale/timezone explicitly
- disable animations when possible
- seed server data and random client behaviors

### Suggested Test Seam

```js
window.__TEST__ = {
  ready: false,
  version: "2026-02-15",
  state: () => ({ route: location.pathname, user: null, pendingRequests: 0 }),
  commands: {
    reset: async () => {},
    seed: async (name) => {}
  }
};
```

Keep seam small and stable. Do not expose internal mutable objects directly.
