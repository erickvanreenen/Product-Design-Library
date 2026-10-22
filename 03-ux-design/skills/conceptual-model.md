---
id: 03-ux-design/conceptual-model
name: Define the conceptual model
stage: 03-ux-design
fires-when: Before flows or screens; "what are the objects", "what do we call this"; naming arguments; a redesign where the product feels inconsistent.
inputs: [work/01-research.md#domain, #needs, work/02-direction.md#decision]
output: work/03-ux-spec.md#model, vocabulary section of work/05-system/UX.md
draws-on: [layers-skills/layers/layers-conceptual-model, designer-skills/interaction-design/state-machine]
version: 1.0
updated: 2026-10-22
---

# Define the conceptual model

Decides the objects the product recognises, how they relate, what users can do to them, what states they pass through, and one name for each. It is the most neglected layer, and every flow and screen above depends on it.

## Use when
- Starting UX work on anything with more than one type of thing in it.
- Users or the team use different words for the same thing.

## Not for
- Recording users' messy real-world language, use `domain-glossary` (01). This step decides.

## Steps
1. **Harvest candidate objects** from the noun list, the needs and the chosen concept. Sort into objects, attributes, instances or values, and set-aside (UI elements, vague abstractions).
2. **Test each object.** A real object can have many instances, has its own attributes, and users care about it in its own right. Being able to be an object does not mean it should be first-class; justify each promotion.
3. **Define each object:** one sentence from the user's view, its attributes, its relationships (how many, and the role where it plays several: "belongs to one user, as referrer"), and its actions. Where an attribute is just another object's name, model it as a relationship.
4. **Trace everything to a need.** Remove objects, attributes or actions that serve no stated need.
5. **Model states** for any object whose status changes what users can do: list states, events that move between them, guards, and what each state forbids. Check there are no impossible states and every state has a way out.
6. **Inventory actions** across all objects in one list. Fix inconsistent verbs (Add, Create and New for one operation) and generic verbs that hide different outcomes ("edit address" for a typo versus a house move).
7. **Settle vocabulary:** for each contested concept, the chosen term, rejected alternatives and why. One name per concept, one concept per name, in UI, help and code alike.
8. **Probe time:** what happens to history, deletion, and things that referred to a deleted object.

## Guardrails
- Keep implementation out. When talk turns to storage, return to what the user can do; flag real engineering questions separately.
- Mark the model provisional if domain research has not been done.

## Output
```
## Model
Objects: name, definition, attributes, relationships (cardinality, role), actions
Relationship map (diagram)
State diagrams for stateful objects
Action inventory
Vocabulary: term / rejected / reason
Open questions
```

## Done when
- Every object traces to a need, every stateful object has a state diagram with no dead ends, and each concept has exactly one name.

## Sources
Rewritten in this repository's format from:
- [layers-skills / layers-conceptual-model](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-conceptual-model/SKILL.md) by Jamie Mill (MIT)
- [designer-skills / state-machine](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/state-machine/SKILL.md) by Marie Claire Dean (MIT)
