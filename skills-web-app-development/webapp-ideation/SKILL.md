---
name: webapp-ideation
description: "Turn product ideas into validated web app opportunities: problem framing, user segments, value proposition, MVP scope, experiment design, and go/no-go decisions. Trigger: 'web app idea', 'startup idea', 'what should I build', 'validate idea', 'MVP scope'."
---

# Web App Ideation

Convert broad ideas into clear, testable product bets before writing implementation code.

## Default Mode: Problem-First (No Fixed Stack)

Ideation is about user outcomes and business evidence, not framework selection.

Do not lock technical stack during ideation unless hard constraints already exist.

## Philosophy: De-Risk Before Build

Most failed products are scope or problem mistakes, not coding mistakes.

Use ideation to reduce:
- problem risk (is this painful enough?)
- audience risk (who needs this first?)
- value risk (will they adopt/pay?)
- execution risk (can v1 be delivered simply?)

## STOP: Before Starting Build Work

Define these first:
1. User segment and context
2. Top painful workflow to improve
3. Existing alternatives and why they are insufficient
4. One-sentence value proposition
5. MVP boundary (must-have vs later)
6. Success metric for first release window
7. Validation plan (interviews, prototype test, concierge, preorders, etc.)
8. Go/no-go threshold

If these are unclear, stay in ideation mode.

## Reference Files

Read these before the related work:

| When working on... | Read first |
|---|---|
| Problem framing and customer pain clarity | `references/problem-framing.md` |
| Comparing and selecting opportunities | `references/opportunity-scoring.md` |
| Defining MVP scope and validation experiments | `references/mvp-scope-and-experiments.md` |
| Final ideation output for build handoff | `references/solution-brief-template.md` |

## Ideation Workflow

1. Start with a raw idea statement in one sentence.
2. Reframe as a user problem with context and urgency.
3. Identify the narrowest high-pain user segment for v1.
4. Score opportunity strength and delivery feasibility.
5. Draft value proposition and differentiator.
6. Define MVP scope with explicit exclusions.
7. Choose the cheapest validation experiment.
8. Produce a solution brief and decision: go, pivot, or stop.

## Non-Negotiables

- Keep problem definition separate from solution assumptions.
- Choose one primary user segment for v1.
- Set success metrics before experiments run.
- Document explicit "not in v1" boundaries.
- Make go/no-go criteria measurable.

## Anti-Patterns

| Anti-pattern | Why it fails | Better approach |
|---|---|---|
| Start from tech preference | Solves implementation, not user pain | Start from user workflow and measurable pain |
| Target everyone at once | No focused distribution or fit | Narrow v1 segment with clear urgency |
| Build full platform first | Long cycle before evidence | Validate with smallest usable slice |
| Add features without evidence | Scope balloons, no traction | Tie each feature to a risk or metric |
| "Looks useful" as proof | No real adoption signal | Define and measure behavior outcomes |

## Handoff Rule

When ideation reaches a go decision:
1. Fill `references/solution-brief-template.md`.
2. Move to `../requirements-first-template.md`.
3. Continue with `../webapp-builder/SKILL.md`.

## Variation Guidance

Vary ideation emphasis by context:
- B2B workflow products: pain frequency, ROI, and switching friction.
- Consumer apps: habit loop, activation, and retention.
- Regulated domains: compliance constraints and auditability.
- Internal tools: operational efficiency and failure cost.

## Remember

Ideation quality determines build quality.

Strong products come from clear problems, sharp scope, and measurable bets.

