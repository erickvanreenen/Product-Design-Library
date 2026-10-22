---
id: 07-qa-accessibility/usability-test-plan
name: Plan a usability test
stage: 07-qa-accessibility
fires-when: A prototype or build needs testing with users; "plan a usability test", "write test tasks", "test with assistive technology users".
inputs: [prototype or build, work/03-ux-spec.md#flows, work/01-research.md#personas, success metrics]
output: work/07-qa-report.md#usability-plan
draws-on: [designer-skills/design-research/usability-test-plan, designer-skills/prototyping-testing/test-scenario, designer-skills/prototyping-testing/accessibility-test-plan]
version: 1.0
updated: 2026-10-22
---

# Plan a usability test

Designs a usability study (objectives, participants, tasks and measures), including sessions with disabled people using their own set-ups.

## Steps
1. **Objectives:** the specific questions the test must answer, tied to risky assumptions and the success metrics.
2. **Method:** moderated or unmoderated, remote or in person, and the fidelity of what is tested. Five participants per distinct user group usually reveal the main problems; more for measurement.
3. **Participants:** screening criteria, including people with relevant disabilities using their own devices and assistive technology, and people in realistic conditions.
4. **Write task scenarios:** give motivation, not instructions; use the participant's words, not product terms; one goal per task; never reveal the path. Mix exploratory, specific and open-ended tasks, ordered from easier to harder.
5. **Define measures per task:** completed or not, time, errors and wrong paths, help needed, and a difficulty rating (1 to 5). Add a standard questionnaire such as SUS if comparing over time.
6. **Write the session guide:** introduction and consent, warm-up, tasks with neutral probes, debrief.
7. **Pilot** the plan with one person and fix confusing tasks.
8. **Plan analysis:** how issues will be logged, rated and fed into fixes.

## Guardrails
- Do not lead participants or explain the interface during tasks.
- Pay participants fairly and offer accessible formats.

## Output
A ready-to-run plan: objectives, method, screener, tasks with success criteria, measures, guide and analysis plan.

## Done when
- Every objective has at least one task and a measure, and the pilot has run.

## Sources
Rewritten in this repository's format from:
- [designer-skills / usability-test-plan](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/usability-test-plan/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / test-scenario](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/test-scenario/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / accessibility-test-plan](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/accessibility-test-plan/SKILL.md) by Marie Claire Dean (MIT)
