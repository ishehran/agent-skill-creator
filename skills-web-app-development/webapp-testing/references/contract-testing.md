## Contract Testing

Contract tests prevent producer/consumer breakage before deployment.

## When To Use

Use contract tests when:
- frontend and backend release independently
- multiple clients consume the same API
- external consumers depend on your public API

## Contract Sources

Choose one primary source:
- OpenAPI schemas
- JSON schema bundles
- typed RPC definitions

Keep generated clients and validators aligned to this source.

## Producer-Side Contract Checks

In backend CI:
1. validate responses against published schema
2. verify required fields and formats
3. reject undocumented response shape changes

Treat compatibility failures as build blockers.

## Consumer-Side Contract Checks

In frontend CI:
1. validate expected response fixtures against schema
2. run tests against mock server generated from contract
3. verify handling for optional/missing fields and known error codes

This catches drift before integration environments.

## Compatibility Rules

Usually safe changes:
- add optional response fields
- add new endpoints

Usually breaking:
- remove/rename fields
- change field types
- change status code semantics
- alter error code vocabulary

Document compatibility policy clearly for the team.

## Release Workflow

1. Propose contract changes.
2. Run producer and consumer contract suites.
3. Publish versioned contract artifact.
4. Roll out producer changes behind compatibility checks.
5. Roll out consumer updates.

Never deploy a contract change that only one side has validated.
