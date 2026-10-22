# Run a brief end to end

The general-purpose line. Erick's own process, which this library is built to serve, is [Erick_ninja_playbook.md](Erick_ninja_playbook.md).

Use this when you have a brief and want the full line, from intake to a measured result. Each stage reads the hand-off file before it and writes its own. A person approves each gate before the next stage starts.

## Set up

1. Create a `work/` folder in the project, not in this repository.
2. Copy `templates/work/` into it. Each file has the headings the skills fill.
3. Put the raw brief, and any research, data, screens or brand files you have, in `work/inputs/`.

## The line

| Step | Stage | Run these skills | Writes | Gate (a person decides) |
|---|---|---|---|---|
| 0 | Intake and landscape (00, 03) | intake-brief, platform-map, feature-placement (when the work sits inside a larger platform), context-pack | `00-brief.md`, `00-landscape.md`, `context/` | G0 Scope: which stages run, what is out of scope, ripple owners named |
| 1 | Research (01) | research-plan, then the skills the plan calls for (including competitive-scan and interaction-teardown), then synthesise-findings | `01-research.md` | G1 Evidence: findings trace to sources, confidence stated |
| 2 | Ideation (02) | frame-problem, assumptions-and-bets, design-principles, explore-concepts, select-concept, success-metrics (08) | `02-direction.md` | G2 Direction: one concept chosen, criteria recorded |
| 3 | UX design (03) | conceptual-model, information-architecture, user-flows, states-and-errors, form-design, ux-writing, ai-experience (if AI), wireframe-spec | `03-ux-spec.md` | G3 Spec: every flow has its states, copy and edge cases |
| 4 | UI foundations (04) | visual-direction, layout-and-spacing, typography, colour, motion | `04-ui-spec.md` (foundations) | G4 Look: a person picks the direction; contrast passes |
| 5 | Design system (05) | audit-system (existing products), design-tokens, component-spec, context-files, design-tool-sync (if a design tool is used) | `05-system/` | G5 System: tokens and components exist before screens |
| 6 | Screens (04) | visual-hierarchy, data-visualisation (if charts), compose-screen | `04-ui-spec.md` (screens), screens | G6 Taste: screens use the system only; a person does the taste pass |
| 7 | Critique (06) | brief-traceability, critique-screen, heuristic-review, coherence-check, slop-check, critique-session (optional) | `06-critique.md` | G7 Fixes: each point accepted or rejected with a reason |
| 8 | QA (07) | accessibility-audit, cognitive-load-check, compliance-check, design-qa, usability-test-plan | `07-qa-report.md` | G8 Ship: no open critical issues |
| 9 | Analysis (08) | read-analytics, experiment-design, ai-feature-evaluation (if AI), impact-report | `08-measurement.md` | G9 Next: what the next iteration tackles |

UI design runs in two parts. Foundations (direction, layout, type, colour, motion) come first because the design system is built from them. Screens come after the system, because screens built on a system that does not exist yet invent their own values (S10, S29).

`stage-gate` runs at every gate and `decision-log` records each decision in `work/decisions.md`. `ai-output-check` runs on anything an AI produced before a person sees it.

## Rules for the AI running the line

- Read `00-governance/README.md` first.
- Never skip a gate. Stop, present the gate checklist and wait for a person.
- If a skill needs an input that does not exist, say which one, and either run the skill that makes it or ask. Do not invent research, users or numbers.
- Write only to `work/`. Never edit this repository during a run.
- Cite the skill IDs used in each output section.

## Scaling down

Not every brief needs every stage. `intake-brief` recommends which stages to run and why. A small change might be UX design, critique and QA only.
