---
id: 02-ideation/assumptions-and-bets
name: Place bets and test assumptions
stage: 02-ideation
fires-when: A problem is framed; "what could we build", "what is the riskiest assumption", "how do we test this cheaply".
inputs: [work/02-direction.md#problem]
output: work/02-direction.md#bets
draws-on: [layers-skills/layers/layers-product-strategy, designer-skills/ux-strategy/business-design, designer-skills/ux-strategy/opportunity-framework]
version: 1.0
updated: 2026-10-22
---

# Place bets and test assumptions

Generates several solution bets for the chosen opportunity, names the assumption each depends on, and designs the cheapest test for the riskiest one.

## Use when
- Before committing design effort to one idea.

## Steps
1. Write at least three bets: "We could [solution], which we believe would [serve the opportunity] because [reasoning]." More than one bet per opportunity, always.
2. For each bet, name the riskiest assumption across four kinds: will people want it (desirability), can we build it (feasibility), does it pay (viability), can people use it (usability).
3. Rank assumptions by how much rides on them and how little evidence exists.
4. Design the cheapest test for the top one, in days not months: a fake door, a concierge run, a clickable prototype, a five-person interview round, or a look at existing data.
5. Write the test as a falsifiable claim: what result would kill the bet.
6. State each bet in business terms: which metric it moves, and the cost of not doing it. Separate evidence from craft judgement and say which is which.
7. Defer the bets you will not pursue now, with the reason.

## Guardrails
- Do not let the first idea become the incumbent. Hold bets at equal effort until there is evidence.
- A test with no result that could change your mind is not a test.

## Output
```
## Bets
| Bet | Riskiest assumption | Type | Cheapest test | Kill condition | Metric it moves |
Deferred bets and why
```

## Done when
- The top assumption has a test with a written kill condition.

## Sources
Rewritten in this repository's format from:
- [layers-skills / layers-product-strategy](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-product-strategy/SKILL.md) by Jamie Mill (MIT)
- [designer-skills / business-design](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/business-design/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / opportunity-framework](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/opportunity-framework/SKILL.md) by Marie Claire Dean (MIT)
