# Operations Security

Operations paths are high-value attack surfaces. Secure them like production code.

## Access Control

- enforce least privilege for CI, CD, cloud, and database access
- require MFA for privileged operator access
- use short-lived credentials where possible
- review and remove stale access regularly

## CI/CD Security Controls

- pin and review external CI actions/scripts
- protect release branches and deployment workflows
- require code review for pipeline changes
- separate build and deploy permissions

## Artifact and Runtime Integrity

- sign artifacts or track provenance metadata
- scan dependencies and container images
- block known critical vulnerabilities from release
- run with minimal runtime permissions

## Secret Hygiene

- inject secrets only at runtime
- prohibit plain-text secrets in pipeline logs
- rotate credentials after exposure events
- audit secret access and usage

## Network and Perimeter Controls

- restrict management interfaces to trusted networks
- enforce TLS everywhere for service communication
- apply WAF/rate limits where exposed publicly
- isolate critical data plane from control plane

## Auditability

Log and retain:
- deployment initiator identity
- artifact/version deployed
- target environment and timestamp
- config and permission changes

Operational changes must be traceable for incident and compliance needs.
