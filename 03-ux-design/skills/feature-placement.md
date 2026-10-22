---
id: 03-ux-design/feature-placement
name: Place the feature and trace its ripples
stage: 03-ux-design
fires-when: A feature or product is being designed inside a larger platform; "where does this sit", "what will this affect", "what does it depend on"; step 2 of erick_process.
inputs: [work/00-landscape.md#platform, work/00-brief.md]
output: work/00-landscape.md#placement
draws-on: [ux-pgm-skills/program-planning/dependency-map, ux-pgm-skills/delivery-execution/risk-register, designer-skills/ux-strategy/service-blueprint, layers-skills/layers/layers-conceptual-model, ai-design-skills/ai-alignment-reasoning/harm-anticipation]
version: 1.0
updated: 2026-10-22
---

# Place the feature and trace its ripples

Puts the feature on the platform map and traces what it depends on, what depends on it, and the knock-on effects two and three steps away, so nothing downstream breaks by surprise.

## Use when
- Right after `platform-map`, before research and before the brief is final.

## Not for
- Delivery scheduling between teams. This maps design dependencies; the programme plan uses them.

## Steps
1. **Pin the feature on the platform map.** Which zone it lives in, which zones it touches, and which main objects it reads, creates, changes or deletes.
2. **Trace upstream (what it needs):** the data, objects, services, content and decisions that must exist for it to work. For each: where it comes from, who owns it, how reliable it is, and whether it is hard (blocking) or soft (nice to have).
3. **Trace downstream (what relies on it):** screens, emails, reports, staff tools, analytics, partner feeds and other features that use what this feature produces or changes.
4. **Find co-dependencies:** places where this feature and another both change the same object or flow, so changes must be designed together.
5. **Run the ripple test** for every change the feature makes to an object or flow:
   - First order: what changes directly?
   - Second order: what reacts to that change (notifications, totals, stock, permissions, analytics events)?
   - Third order: who notices later (support team, finance, reporting, SEO, other markets, accessibility users)?
6. **Check the edges of each object:** what happens to things that refer to it when it is edited, archived or deleted; what history must be kept.
7. **Score each ripple** by likelihood times impact, and name an owner and a response (design for it, agree with the owning team, accept, or rule out of scope).
8. **Draw the placement map:** the feature in the middle, upstream on the left, downstream on the right, co-dependencies above, coloured by risk. Keep it as simple as the platform map.
9. **Feed the brief:** list the dependencies that change scope, the teams to involve, and the questions research must answer.

## Guardrails
- Every hard dependency has an owner. A dependency nobody owns is a risk, not a fact.
- Do not resolve another team's design inside this feature; flag it and agree it with them.
- Re-run the ripple test whenever scope changes.

## Output
```
## Placement
Zone and objects touched (read / create / change / delete)
Upstream: item, source, owner, hard or soft, reliability
Downstream: item, how it is affected, owner
Co-dependencies: shared object or flow, other feature, agreement needed
Ripple table: change, 1st / 2nd / 3rd order effect, severity, owner, response
Placement diagram (Mermaid) + visual link
Brief impacts: scope changes, teams to involve, research questions
```

## Done when
- Every object the feature touches has its upstream source and downstream users listed, every high-severity ripple has an owner and a response, and the brief impacts are written down.

## Sources
Rewritten in this repository's format from:
- [ux-pgm-skills / dependency-map](https://github.com/Owl-Listener/ux-pgm-skills/blob/main/program-planning/skills/dependency-map/SKILL.md) by Marie Claire Dean (MIT)
- [ux-pgm-skills / risk-register](https://github.com/Owl-Listener/ux-pgm-skills/blob/main/delivery-execution/skills/risk-register/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / service-blueprint](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/service-blueprint/SKILL.md) by Marie Claire Dean (MIT)
- [layers-skills / layers-conceptual-model](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-conceptual-model/SKILL.md) by Jamie Mill (MIT)
- [ai-design-skills / harm-anticipation](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/harm-anticipation/SKILL.md) by Marie Claire Dean (MIT)
