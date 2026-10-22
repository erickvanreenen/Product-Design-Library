---
id: 02-ideation/explore-concepts
name: Explore concepts in parallel
stage: 02-ideation
fires-when: A problem is framed and there is one idea on the table (or none); "give me options", "explore directions", "sketch some concepts".
inputs: [work/02-direction.md#problem, #bets, #principles]
output: work/02-direction.md#concepts
draws-on: [designer-skills/prototyping-testing/parallel-concepts, designer-skills/prototyping-testing/prototype-strategy]
version: 1.0
updated: 2026-10-22
---

# Explore concepts in parallel

Builds a small set of genuinely different concepts at equal effort before choosing, because parallel exploration beats refining the first idea.

## Use when
- Before any one direction gets polished.

## Not for
- Picking the winner, use `select-concept`.

## Steps
1. Write the question the set must answer, for example "should the user commit before or after seeing the price?"
2. Choose the dimension the concepts must differ on. The test is behavioural: does the user do something different? Useful dimensions are sequence (what is asked first), unit of work (one item, a batch, a stream), division of labour (what the person decides versus the system), entry point, and commitment point.
3. Create three concepts as a default. Three cheap sketches beat two polished mockups.
4. Give every concept a fair effort. No strawmen. Do not carry a concept nobody would build.
5. Keep fidelity and visual style the same across the set, so the difference under test stays isolated. Match fidelity to the question: sketches or flows for structure, a clickable prototype for interaction, coded or high-fidelity only for visual or motion questions.
6. Describe each concept in a few lines plus a flow or sketch: what the user does, what it tests that the others do not, and its main risk.
7. If AI generates concepts, check they differ in behaviour, not only appearance. Two layouts of the same steps are one concept; replace one.

## Guardrails
- Do not merge concepts at this stage.
- Label prototypes clearly as prototypes.

## Output
```
## Concepts
Question the set answers / dimension varied
C1 <name>: what the user does, what it tests, risk, sketch or flow link
C2 ...
C3 ...
```

## Done when
- Each concept differs from the others in what the user does, and all sit at comparable fidelity.

## Sources
Rewritten in this repository's format from:
- [designer-skills / parallel-concepts](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/parallel-concepts/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / prototype-strategy](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/prototype-strategy/SKILL.md) by Marie Claire Dean (MIT)
