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
  - ui motion from prompt/screenshot references
  - testing
  - deployment ops
- 2D suite upgraded with:
  - suite-level README and checkpoint template
  - cleaner core SKILL docs
  - dedicated game UI design skill and references
  - dedicated level design skill and references
- Windows app suite baseline created with:
  - ideation
  - builder
  - testing
  - deployment ops
- Mobile app suite baseline created with:
  - ideation
  - builder
  - testing
  - release ops

## Next Priority: Improve 2D Game Suite

Completed in this phase:
- added `skills-2d-game-development/README.md`
- added `skills-2d-game-development/session-checkpoint-template.md`
- updated:
  - `skills-2d-game-development/phaser-gamedev/SKILL.md`
  - `skills-2d-game-development/playwright-testing/SKILL.md`
- added game UI design capability:
  - `skills-2d-game-development/game-ui-design/SKILL.md`
  - `skills-2d-game-development/game-ui-design/references/`
- added level design capability:
  - `skills-2d-game-development/game-level-design/SKILL.md`
  - `skills-2d-game-development/game-level-design/references/`
  - `skills-2d-game-development/phaser-gamedev/references/level-design-and-progression.md`

Suggested next additions:
- `game-ideation/`: player problem, game loop hypothesis, retention hooks, test plan
- `game-release-ops/`: build pipeline, crash telemetry, progression-safe rollouts
- `game-economy-and-balance/`: reward loops, tuning workflow, anti-inflation controls

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

Status:
- baseline implemented with core skills and deployment profiles

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

Status:
- baseline implemented with core skills and release profiles

## Execution Order

1. Finish web app suite stabilization and examples.
2. Upgrade 2D suite structure and quality.
3. Create game-ideation, game-release-ops, and game-economy skills.
4. Add concrete examples and scenario packs to Windows and mobile suites.
