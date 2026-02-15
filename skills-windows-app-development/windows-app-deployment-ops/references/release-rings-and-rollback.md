# Release Rings And Rollback

Use staged exposure to reduce blast radius.

## Ring Model Example

- Ring 0: internal and QA users
- Ring 1: small trusted external cohort
- Ring 2: broader cohort
- Ring 3: full rollout

Advance only when health gates pass for each ring.

## Rollback Triggers

- crash rate above threshold
- startup failure spike
- critical workflow failure
- severe support incident volume

Define rollback command/process before release starts.

