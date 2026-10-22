# Product Design Library

Browse it visually: download `dashboard.html` and open it in a browser.

A consolidated, platform-independent set of product design skills for AI-assisted work. It takes the strongest parts of 297 skills from 10 open-source repositories and 46 posts and articles, rewrites them into 64 skills in one format, and arranges them by stage.

Use it three ways:

- **Erick's ninja playbook.** The owner's own process: map the platform, place the feature and trace its ripples, research, refine the brief, design, check, align to the design system and present. See [playbooks/Erick_ninja_playbook.md](playbooks/Erick_ninja_playbook.md).
- **Run a brief end to end.** Give an AI the brief and `playbooks/run-brief.md`. It works through the stages in order, writes a hand-off file at each one, and stops at each gate for a person to decide.
- **Use one stage or one skill.** For a task that only needs research, open `01-research/` and follow `playbooks/run-one-stage.md`. Every skill file also works on its own.

Any AI that can read files can use it. Start with [AGENTS.md](AGENTS.md).

## Stages

Folders are numbered by topic. In a full brief, UI design runs in two parts: foundations first, then the design system is built from them, then screens are composed from the system.

| Run order | Folder | Stage | Skills | Gate |
|---|---|---|---|---|
| 0 | [00-governance](00-governance/README.md) | Intake, context, gates, decisions, AI output checks (plus platform map and feature placement from 03) | 5 | G0 Scope |
| 1 | [01-research](01-research/README.md) | Users, needs, journeys, competitors, interaction teardown, domain | 9 | G1 Evidence |
| 2 | [02-ideation](02-ideation/README.md) | Problem, bets, principles, concepts, selection | 5 | G2 Direction |
| 3 | [03-ux-design](03-ux-design/README.md) | Platform map, feature placement, model, structure, flows, states, forms, copy, AI behaviour | 10 | G3 Spec |
| 4 and 6 | [04-ui-design](04-ui-design/README.md) | Foundations (direction, layout, type, colour, motion), then screens | 8 | G4 Look, G6 Taste |
| 5 | [05-ai-design-systems](05-ai-design-systems/README.md) | Audit, tokens, components, DESIGN.md and UX.md, tool sync | 6 | G5 System |
| 7 | [06-design-critique](06-design-critique/README.md) | Brief check, screen critique, heuristics, coherence, slop | 6 | G7 Fixes |
| 8 | [07-qa-accessibility](07-qa-accessibility/README.md) | Accessibility, cognitive load, compliance, testing, design QA | 5 | G8 Ship |
| 9 | [08-analysis](08-analysis/README.md) | Metrics, analytics, experiments, AI evaluation, impact | 5 | G9 Next |
| any | [09-workflow-tooling](09-workflow-tooling/README.md) | Project set-up, handoff, rationale, client presentation, writing new skills | 5 | none |

## What is in the repository

```
AGENTS.md               instructions for any AI using this repository
playbooks/              Erick_ninja_playbook.md, run-brief.md (general line), run-one-stage.md
00-... to 09-.../       one folder per stage: README.md (playbook) and skills/*.md
references/             ux-laws.md, perception.md, ui-data/ (style, colour, type and UX tables)
templates/              skill.md (the shared format) and work/ (hand-off files for a run)
sources/                register.md (posts) and repos.md (repositories and the original-to-skill map)
index.json              everything above in machine-readable form
dashboard.html          browsable view of stages, skills and sources
tools/                  build_repo.py, check_repo.py, sources.json, dashboard template
NOTICES.md              licences of the source repositories
```

## The skill format

Every skill has the same parts, so an AI always knows where to look: front matter (id, stage, fires-when, inputs, output, draws-on, version), then Use when, Not for, Inputs, Steps, Guardrails, Output, Done when, and Sources. See [templates/skill.md](templates/skill.md).

## Keeping it current

Edit a skill file, then run `python3 tools/build_repo.py` and `python3 tools/check_repo.py`. See [CONTRIBUTING.md](CONTRIBUTING.md) for adding, replacing and retiring skills.

## Status

Version 1.1, 22 October 2026. 161 of 297 original skills feed the consolidated set; the rest are listed under each stage for depth. 37 links from the collection are still unread (see `sources/register.md`).

## Licence

MIT, see [LICENSE](LICENSE). The skills are rewritten from MIT-licensed repositories; their notices are in [NOTICES.md](NOTICES.md).
