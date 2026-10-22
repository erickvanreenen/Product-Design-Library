---
id: 01-research/interaction-teardown
name: Tear down competitor interactions
stage: 01-research
fires-when: Benchmarking how others handle a flow in detail; "how do the best apps do this", "break down their interactions", "macro and micro interactions"; step 4 of erick_process.
inputs: [work/00-landscape.md#placement, work/01-research.md#competitors]
output: work/01-research.md#teardown
draws-on: [designer-skills/ux-strategy/competitive-analysis, designer-skills/interaction-design/micro-interaction-spec, designer-skills/interaction-design/feedback-patterns, designer-skills/interaction-design/animation-principles, S21]
version: 1.0
updated: 2026-10-22
---

# Tear down competitor interactions

Takes the best competitors apart at two levels: the big flow (macro) and the small moments inside it (micro), so you learn the principles behind what makes them feel good, not just what they look like.

## Use when
- After `competitive-scan` has picked the products worth studying, for the flows this feature covers.

## Steps
1. **Pick three to five products** from the scan: two direct competitors, one best-in-class from another field, and optionally one known for a bad version (to learn what to avoid).
2. **Record each flow** end to end (screen recording or a sequence of screenshots from a flow library such as Mobbin). Note the date and the platform.
3. **Macro teardown, per flow:** entry point, number of steps, what is asked first and what waits, where the user commits, where it branches, how errors and empty states are handled, where it hands over to email, notification or a person, and how it ends.
4. **Micro teardown, per notable moment:** trigger, what the system does, feedback (visual, motion, sound, haptic), timing and easing as best you can judge, what happens on repeat, and how it behaves with reduced motion or a screen reader.
5. **Capture language:** button labels, headings, error and empty-state wording, and the terms they use for key objects. Add them to the domain glossary.
6. **Score each flow** on clarity, effort (steps and decisions), confidence (feedback and reassurance), recovery (errors), accessibility and delight, 1 to 5 each.
7. **Extract principles, not pixels:** for each strong moment, write the principle in one line ("show the total before asking for card details"). For each weak moment, the anti-pattern.
8. **Map table stakes, gaps and signature moments:** what everyone does (users expect it), what everyone does badly (your opening), and the one or two moments worth designing your own version of.

## Guardrails
- Learn from, never copy. No lifting of brand, illustration or proprietary patterns.
- Respect terms of service; do not scrape or bypass sign-ups you have no right to.
- Note anything you could not access instead of guessing.

## Output
```
## Teardown
Products and flows studied (with date, platform, recording link)
Macro table per flow: entry, steps, commit point, branches, errors, hand-offs, ending
Micro moments: trigger, rules, feedback, timing, repeat, accessibility
Language captured
Scores per flow
Principles to adopt / anti-patterns to avoid
Table stakes, shared gaps, signature moments to design
```

## Done when
- Each flow has a macro table, at least three micro moments are specified, and the principles list is written in your own words.

## Sources
Rewritten in this repository's format from:
- [designer-skills / competitive-analysis](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/competitive-analysis/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / micro-interaction-spec](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/micro-interaction-spec/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / feedback-patterns](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/feedback-patterns/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / animation-principles](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/animation-principles/SKILL.md) by Marie Claire Dean (MIT)
- S21: [Websites for UX research beyond Dribbble](https://www.linkedin.com/posts/rasel-ahmed-628b7239_uxdesign-productdesign-designleadership-share-7488790255249293312-btpL) by Rasel Ahmed (post, read: partial)
