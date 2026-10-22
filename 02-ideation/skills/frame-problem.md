---
id: 02-ideation/frame-problem
name: Frame the problem
stage: 02-ideation
fires-when: Research is done and the team must choose what to solve; "which problem do we tackle", "how might we", "what is the opportunity".
inputs: [work/00-brief.md, work/01-research.md#needs, #journeys, #competitors]
output: work/02-direction.md#problem
draws-on: [layers-skills/layers/layers-product-strategy, designer-skills/ux-strategy/opportunity-framework, S03]
version: 1.0
updated: 2026-10-22
---

# Frame the problem

Connects one measurable outcome to the user opportunities that can move it, then narrows to the problem worth solving now.

## Use when
- There are more opportunities than capacity, or the brief's problem is still vague.

## Not for
- Choosing between solutions to an agreed problem, use `select-concept`.

## Steps
1. **Set one outcome.** Measurable, meaningful and bounded: "more new users activate within 30 days", not "grow the product". One outcome per frame. Note which business line it moves (conversion, retention, order value, support cost, churn).
2. **List opportunities** from the needs and journey work, in the user's first-person words, anchored to a journey moment: "I do not know which plan covers this." Apply the flip test: if it reads as "I need [your feature]", it is a solution in disguise.
3. **Keep only opportunities that move the outcome.** If serving it would not shift the outcome, park it.
4. **Group by journey moment** and draw the tree: outcome at the top, opportunities beneath.
5. **Prioritise** by importance times how poorly it is served, adjusted for evidence strength. Use a second lens to check (impact against effort, or RICE: reach, impact, confidence, effort). Where lenses disagree, discuss why.
6. **Write the problem statement** for the chosen opportunity: who, situation, what gets in the way, evidence, and the cost of leaving it.
7. **Write two or three "how might we" questions** that open the solution space without naming a solution.

## Guardrails
- One outcome. Two outcomes produce a frame that serves neither.
- Every opportunity cites a finding or is marked assumed.
- Record the parked opportunities; they are next quarter's candidates.

## Output
```
## Problem
Outcome (metric):
Opportunity tree (grouped by journey moment)
Chosen opportunity and why
Problem statement
How might we...
Parked opportunities
```

## Done when
- The chosen opportunity links to the outcome and to evidence, and the problem statement names no solution.

## Sources
Rewritten in this repository's format from:
- [layers-skills / layers-product-strategy](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-product-strategy/SKILL.md) by Jamie Mill (MIT)
- [designer-skills / opportunity-framework](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/opportunity-framework/SKILL.md) by Marie Claire Dean (MIT)
- S03: [Product Design Decisions: AI Skills Pack](https://www.linkedin.com/posts/vitalyfriedman_product-design-decisions-ai-skills-share-7457754106817015808-PCWG) by Vitaly Friedman (pack by Jamie Mill) (post, read: partial)
