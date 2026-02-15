---
name: windows-app-ideation
description: "Turn desktop app ideas into validated opportunities: user pain, workflow fit, value proposition, MVP scope, and go/no-go criteria. Trigger: 'Windows app idea', 'desktop app idea', 'what should I build for Windows', 'validate app idea'."
---

# Windows App Ideation

Convert broad ideas into clear, testable desktop product bets before writing implementation code.

## Default Mode: Problem-First (No Fixed Stack)

Focus on user outcomes, not frameworks.

Do not lock WinUI, Electron, or Tauri during ideation unless constraints are already fixed.

## STOP: Before Build Work

Define these first:
1. Target user segment and usage environment
2. Core workflow pain and frequency
3. Current alternatives and why they fail
4. One-sentence value proposition
5. MVP scope and explicit exclusions
6. Adoption and success metric
7. Validation plan and timeline
8. Go/no-go threshold

If unclear, continue ideation.

## Reference Files

| When working on... | Read first |
|---|---|
| Problem definition and audience fit | `references/problem-framing.md` |
| Prioritizing multiple ideas | `references/opportunity-scoring.md` |
| Build handoff output | `references/solution-brief-template.md` |

## Workflow

1. Capture the idea in one sentence.
2. Reframe as a user problem in a specific context.
3. Pick one primary user segment for v1.
4. Score opportunity strength and feasibility.
5. Define MVP boundary and validation plan.
6. Decide go, pivot, or stop with measurable criteria.

## Non-Negotiables

- Keep problem statement separate from solution assumptions.
- Define one primary user segment for v1.
- Set success metric before running experiments.
- Document "not in v1" explicitly.
- Make go/no-go measurable.

## Handoff Rule

When decision is go:
1. Fill `references/solution-brief-template.md`.
2. Continue with `../windows-app-builder/SKILL.md`.

## Remember

Strong desktop products start with strong workflow clarity, not stack choice.

