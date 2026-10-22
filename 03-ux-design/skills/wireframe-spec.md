---
id: 03-ux-design/wireframe-spec
name: Specify wireframes
stage: 03-ux-design
fires-when: Flows and states are settled and layout must be decided; "wireframe this", "lay out the screen"; also first-run and onboarding screens.
inputs: [work/03-ux-spec.md (model, ia, flows, states, forms, copy)]
output: work/03-ux-spec.md#wireframes
draws-on: [designer-skills/prototyping-testing/wireframe-spec, designer-skills/interaction-design/onboarding-design]
version: 1.0
updated: 2026-10-22
---

# Specify wireframes

Turns flows into annotated, greyscale layouts that fix content priority and behaviour before any visual design.

## Steps
1. Choose fidelity for the question: boxes and labels for structure, mid-fidelity with real copy for review, annotated for handoff.
2. Lay out each place from the breadboard. Put content in priority order and number it.
3. Use real copy from `ux-writing` and real data lengths, never lorem ipsum.
4. Annotate: what each element does on click, hover and focus; dynamic or personalised content; responsive behaviour; heading levels; accessibility notes (focus order, landmarks, alt text needs).
5. Include each designed state (empty, loading, error) for key screens.
6. Check against `references/ux-laws.md`: fewer choices at decision points, large targets for frequent actions, familiar patterns, short steps.
7. For first-run screens: get users to value fast, ask only what is needed now, make tours skippable, use empty states as onboarding, and label any sample data clearly.

## Guardrails
- Greyscale only. Colour and type belong to UI design.
- A wireframe that skips states is not ready for handoff.

## Output
Wireframes (any tool, or text layout for AI hand-over) with numbered priorities and annotations, linked from the spec.

## Done when
- Every place in the flows has a wireframe with annotations and its key states.

## Sources
Rewritten in this repository's format from:
- [designer-skills / wireframe-spec](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/wireframe-spec/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / onboarding-design](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/onboarding-design/SKILL.md) by Marie Claire Dean (MIT)
