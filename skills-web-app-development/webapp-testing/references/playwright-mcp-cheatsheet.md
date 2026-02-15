## Playwright MCP Cheatsheet (Web Apps)

Use this when driving browser tests via MCP tools in Codex.

### Core Sequence

1. Navigate to app URL.
2. Wait for explicit readiness signal.
3. Capture diagnostics baseline (console + network).
4. Perform user actions.
5. Assert outcomes and collect evidence on failure.

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
