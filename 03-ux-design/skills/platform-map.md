---
id: 03-ux-design/platform-map
name: Map the platform
stage: 03-ux-design
fires-when: Before designing any feature on an existing or planned platform; "how does the whole thing fit together", "show me the big picture", "map the platform"; step 1 of erick_process.
inputs: [work/00-brief.md, sitemaps, analytics, existing screens, API or data docs, org charts in work/inputs/]
output: work/00-landscape.md#platform
draws-on: [designer-skills/ux-strategy/information-architecture, designer-skills/ux-strategy/experience-map, designer-skills/ux-strategy/service-blueprint, layers-skills/layers/layers-domain, layers-skills/layers/layers-conceptual-model]
version: 1.0
updated: 2026-10-22
---

# Map the platform

Draws the whole platform on one page as a few zones and the main streams of information flowing between them, so everyone sees the big picture before anyone designs a part of it.

## Use when
- At the start of any feature or product work inside a larger platform.
- Joining a project, or when a team keeps being surprised by side effects.

## Not for
- The detailed structure inside one feature, use `information-architecture`.
- Placing one feature and tracing its effects, use `feature-placement` next.

## Inputs
- Whatever exists: sitemap, navigation, analytics top paths, screenshots, data or API docs, team ownership. If little exists, walk the live product and interview one person from product and one from engineering.

## Steps
1. **Collect the raw parts.** Walk every top-level area of the product (or the plan). List areas, the main things (objects) each one handles, and every way people get in: web, app, email, notifications, support, partners, staff tools.
2. **Find the main objects.** Which few things does the whole platform revolve around (for example customer, product, order, payment, content)? Use the conceptual-model test: many instances, own attributes, people care about it.
3. **Group into zones.** Five to seven zones at most, named in the user's language, not the org chart: for example "Discover", "Buy", "Account", "Support", "Back office".
4. **Draw the streams.** Arrows between zones, each labelled with what information moves ("order details", "stock level", "customer profile"), not with screen names. Mark which streams are real-time and which are delayed.
5. **Mark the edges of the platform:** outside systems (payments, CRM, warehouse, analytics), the people and teams behind the scenes, and the line between what users see and what they do not.
6. **Mark the single sources of truth:** for each main object, where the master record lives.
7. **Simplify until it reads in ten seconds.** Remove anything that does not change a design decision. One colour per stream type. If a newcomer cannot explain it back in a sentence, simplify again.
8. **Mark the unknowns** with a question mark rather than guessing, and list who can answer each.
9. **Produce it in two forms:** a clean visual for people (Figma, FigJam or a whiteboard) and a text version (Mermaid diagram plus a short zone list) that any AI can read.

## Guardrails
- Map the platform as it is today first; draw the future state separately.
- Never present guessed system behaviour as fact. Unknowns stay visible.
- Keep it to one page. Detail belongs in the feature-level maps.

## Output
```
## Platform
Zones (5-7): name, purpose, main objects, owner
Streams: from -> to, information carried, timing (live / delayed)
Outside systems and people
Sources of truth per main object
Diagram (Mermaid) + link to the visual
Unknowns and who can answer
```

## Done when
- Someone new can explain the platform back in one sentence after ten seconds with the map.
- Every main object has one named source of truth, and unknowns are listed with an owner.

## Sources
Rewritten in this repository's format from:
- [designer-skills / information-architecture](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/information-architecture/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / experience-map](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/experience-map/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / service-blueprint](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/service-blueprint/SKILL.md) by Marie Claire Dean (MIT)
- [layers-skills / layers-domain](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-domain/SKILL.md) by Jamie Mill (MIT)
- [layers-skills / layers-conceptual-model](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-conceptual-model/SKILL.md) by Jamie Mill (MIT)
