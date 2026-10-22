---
id: 02-ideation/select-concept
name: Select a concept
stage: 02-ideation
fires-when: Concepts exist and a direction must be chosen; "which one do we go with", "help us decide".
inputs: [work/02-direction.md#concepts, #problem, #principles, success criteria from the brief]
output: work/02-direction.md#decision, work/decisions.md
draws-on: [designer-skills/prototyping-testing/concept-selection]
version: 1.0
updated: 2026-10-22
---

# Select a concept

Chooses one direction on criteria fixed in advance and records why the others lost, so preference is not passed off as reasoning.

## Use when
- Closing a parallel exploration, before detailed UX work.

## Not for
- A change that can ship and let real traffic decide, use `experiment-design` (08).

## Steps
1. Name the decider before the review.
2. **Write the criteria before comparing.** Take them from the success criteria and principles. Each must be able to fail a concept: "completes the core task in three steps or fewer", not "better UX".
3. Mark each criterion as a threshold (fail it and the concept is out) or a trade-off (weighed against others).
4. Re-level fidelity if needed. Polish should not decide.
5. Apply every criterion to every concept, including the current design if there is one. Use evidence (test results, constraints) over the number of people who liked something.
6. If two concepts each win on different criteria, the criteria conflict. Escalate the priority question; do not average the two into a compromise.
7. Choose one. State what it costs and what would make you revisit it.
8. For each rejected concept, record what it tested, what it lost on and what would bring it back.
9. Pass gate G2 with `stage-gate`, then log with `decision-log`.

## Guardrails
- Do not graft features from losing concepts onto the winner.
- An AI may score and summarise, but a person makes the choice.

## Output
```
## Decision
Decider / date
Criteria (threshold or trade-off)
Scores per concept with evidence
Chosen: <concept>, cost, revisit trigger
Rejected: <concept>: tested / lost on / would return if
```

## Done when
- Criteria were written before scoring, the winner's cost is named, and every loser has a record.

## Sources
Rewritten in this repository's format from:
- [designer-skills / concept-selection](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/concept-selection/SKILL.md) by Marie Claire Dean (MIT)
