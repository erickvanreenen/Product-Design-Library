---
id: 03-ux-design/user-flows
name: Map user flows
stage: 03-ux-design
fires-when: Designing how a user completes a job; "map the flow", "what are the steps", "what happens if it fails"; before wireframes.
inputs: [work/03-ux-spec.md#model, #ia, the job story being served]
output: work/03-ux-spec.md#flows
draws-on: [layers-skills/layers/layers-interaction-flow, designer-skills/prototyping-testing/user-flow-diagram, inclusive-design-skills/inclusive-interaction/design-flow]
version: 1.0
updated: 2026-10-22
---

# Map user flows

Settles the interaction logic of a flow, with every place, action, destination and edge case, before visual design makes changes expensive.

## Use when
- After the conceptual model is stable, for each priority job story.

## Steps
1. Name the job story, the starting point and what success looks like. For a redesign, describe the current flow first.
2. **Breadboard the flow** in text:
   ```
   Place name
   - action -> destination place
   [content shown here]
   ```
   Name places by what they mean to the user ("Referral dashboard", not "Page 3").
3. **Every action needs a named destination.** "Submit, then where?" An unnamed destination is an unmade decision.
4. **Map the edges as required steps:** validation failure, server error, lost connection, timeout, someone else editing at the same time, empty states, loading, the state after the action, cancel and back.
5. **Walk it as the user:** "I am [situation], I arrive at [place], I see [content], I want to [motivation], so I [action]." Walk the happy path, then each edge.
6. **Check the model:** each object's attributes and actions are available together, relationships are navigable, and words match the vocabulary.
7. **Plan every input method:** each action works by keyboard, pointer or touch, and voice where relevant. Note focus order, focus handling for dialogs and dynamic content, and target sizes. Flag any action that only works one way.
8. **Simplify.** More than five or six places for one job story is a sign something can merge.
9. Add a flow diagram if it helps orientation; the breadboard stays the main record.

## Guardrails
- No visual design here. Boxes and words only.
- Do not leave an edge case as "TBC". Decide it or log it as an open decision.

## Output
Breadboard per job story, a flow diagram, an input-method table, open decisions and risks from unsettled lower layers.

## Done when
- Every action has a destination, every listed edge has a decided outcome, and the flow works without a mouse.

## Sources
Rewritten in this repository's format from:
- [layers-skills / layers-interaction-flow](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-interaction-flow/SKILL.md) by Jamie Mill (MIT)
- [designer-skills / user-flow-diagram](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/user-flow-diagram/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / design-flow](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/design-flow/SKILL.md) by Marie Claire Dean (MIT)
