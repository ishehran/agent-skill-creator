# Skill Roadmap

This roadmap keeps expansion aligned with idea-first, stack-agnostic execution.

## Guiding Rule

For each domain, keep:
1. core skill flow stack-agnostic
2. optional stack profiles as overlays
3. explicit handoff between ideation, build, test, and operations

## Current Status

- Web app suite exists with:
  - ideation
  - builder
  - testing
  - deployment ops

## Next Priority: Improve 2D Game Suite

Suggested additions:
- `game-ideation/`: player problem, game loop hypothesis, retention hooks, test plan
- `game-release-ops/`: build pipeline, crash telemetry, progression-safe rollouts
- `game-economy-and-balance/`: reward loops, tuning workflow, anti-inflation controls

Immediate improvement suggestions for existing 2D skills:
- normalize file encoding and remove malformed characters
- add a suite-level README with end-to-end flow
- add session checkpoint template (same pattern as web app suite)

## New Domain: Windows App Development

Suggested folder:
- `skills-windows-app-development/`

Suggested core skills:
- `windows-app-ideation/`
- `windows-app-builder/`
- `windows-app-testing/`
- `windows-app-deployment-ops/`

Optional profiles can cover common stacks, for example:
- .NET WinUI/WPF
- Electron
- Tauri

## New Domain: Mobile App Development

Suggested folder:
- `skills-mobile-app-development/`

Suggested core skills:
- `mobile-app-ideation/`
- `mobile-app-builder/`
- `mobile-app-testing/`
- `mobile-app-release-ops/`

Optional profiles can cover common stacks, for example:
- React Native
- Flutter
- native iOS/Android

## Execution Order

1. Finish web app suite stabilization and examples.
2. Upgrade 2D suite structure and quality.
3. Create Windows suite baseline.
4. Create mobile suite baseline.

