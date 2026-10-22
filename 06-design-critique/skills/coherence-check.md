---
id: 06-design-critique/coherence-check
name: Check coherence with the layers below
stage: 06-design-critique
fires-when: After screens exist; "the UI is fine but something is off", "are we consistent"; before handoff; when surface fixes keep coming back.
inputs: [screens, work/03-ux-spec.md (model, vocabulary, flows), work/01-research.md#needs]
output: work/06-critique.md#coherence
draws-on: [layers-skills/layers/layers-surface]
version: 1.0
updated: 2026-10-22
---

# Check coherence with the layers below

Checks that what users see matches what was decided underneath (the model, vocabulary, flows and needs), and separates true surface fixes from problems that need a lower layer revisited.

## Steps
1. **Vocabulary check:** compare every label, heading, button, error, notification and help text with the vocabulary list. Flag wrong terms, terms not in the list, and mixed terms for one thing.
2. **Object check:** for each object in the model, where does it appear and in how many forms? Flag objects that change shape between contexts, and forms where users cannot tell what kind of thing they are looking at.
3. **Completeness both ways:** every action in the flows exists on screen, and nothing on screen lacks a model or flow behind it.
4. **Error check:** every error state diagnoses, explains and offers recovery.
5. **Prominence check:** what the flow needs users to notice is what stands out.
6. **Emotional register:** tone and emphasis fit the emotional and social jobs from research, not the product's own self-promotion.
7. **Accessibility is decided:** focus order, names and announcements were specified rather than left to defaults.
8. **Route each finding:** surface fix (copy, layout, style) or deeper issue. Deeper issues go back to `conceptual-model`, `user-flows` or `needs-and-jobs`, logged with `decision-log`.

## Guardrails
- Do not patch a model problem with copy. If two things share a name because the model merged them, fix the model.

## Output
A findings table: issue, layer of origin (surface, flow, model, needs), fix, owner.

## Done when
- Every finding has a layer of origin, and deeper issues are routed back with an owner.

## Sources
Rewritten in this repository's format from:
- [layers-skills / layers-surface](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-surface/SKILL.md) by Jamie Mill (MIT)
