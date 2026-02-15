# Incident Response

Incidents are managed with process discipline, not improvisation.

## Severity Model (Example)

- Sev1: broad user outage or data integrity risk
- Sev2: major degradation with significant user impact
- Sev3: limited impact, workaround available
- Sev4: minor issue, no immediate user impact

Define service-specific criteria before incidents happen.

## Response Loop

1. Acknowledge and assign incident commander.
2. Stabilize user impact (mitigation or rollback).
3. Investigate with evidence (logs, metrics, traces, deploy timeline).
4. Communicate status updates on fixed cadence.
5. Resolve and verify sustained recovery.
6. Run blameless post-incident review.

## Roles

Minimum roles for severe incidents:
- Incident Commander: coordination and decision flow
- Operations Lead: mitigation execution
- Communications Lead: stakeholder updates
- Subject Matter Experts: focused diagnosis

One person can hold multiple roles only for low-severity incidents.

## Communication Template

Use concise structured updates:
- impact summary
- current status
- mitigation in progress
- next update time
- owner

Consistent updates reduce confusion and duplicate work.

## Evidence To Capture

- timeline of alerts and deploy events
- affected endpoints and error codes
- mitigation and rollback actions
- exact timestamps for state transitions

This is required for useful post-incident analysis.

## Post-Incident Output

Blameless review should include:
- root causes and contributing factors
- what detection worked or failed
- immediate corrective actions
- prevention backlog items with owners and due dates

Close incident work only when prevention actions are tracked.
