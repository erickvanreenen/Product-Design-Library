---
id: 04-ui-design/visual-hierarchy
name: Compose visual hierarchy
stage: 04-ui-design
fires-when: Laying out a screen so the important thing is seen first; "nothing stands out", "everything shouts", "what should people notice first".
inputs: [work/03-ux-spec.md#wireframes (priority numbers), type, colour and spacing from this stage]
output: work/04-ui-spec.md#hierarchy
draws-on: [designer-skills/ui-design/visual-hierarchy, designer-skills/ui-design/von-restorff-effect, designer-skills/ui-design/aesthetic-usability]
version: 1.0
updated: 2026-10-22
---

# Compose visual hierarchy

Arranges size, weight, colour, space and position so people see the right thing first and can scan the rest.

## Use when
- Composing new screens. To judge an existing screen, use `critique-screen` (06).

## Steps
1. **Rank the content** using the wireframe priority numbers: primary (page title, main action), secondary (section headings, key content), tertiary (supporting text, metadata) and quaternary (fine print).
2. **Give each level a distinct treatment** using a few tools at once: size (about 1.5 times between levels), weight, contrast, space and position. Top-left and top-centre are seen first in left-to-right languages.
3. **One primary action per view.** Make it the most prominent control; secondary actions step down clearly.
4. **Use isolation sparingly.** One element that differs is noticed; several compete. Keep emphasis for what truly matters.
5. **Group with space and shared containers** so related items read as one unit (see `references/perception.md`).
6. **Squint test:** blur the screen. The primary content and action should still stand out.
7. Remember that a polished look makes people more forgiving of usability problems; do not let it hide them in testing.

## Guardrails
- Do not add emphasis by adding new colours or styles outside the system.
- Do not give every block the same card, border and shadow; that flattens hierarchy.

## Output
Per screen: the content ranking, the treatment for each level, and the squint-test result.

## Done when
- In a blur test, the primary content and action are identifiable on every screen.

## Sources
Rewritten in this repository's format from:
- [designer-skills / visual-hierarchy](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/visual-hierarchy/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / von-restorff-effect](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/von-restorff-effect/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / aesthetic-usability](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/aesthetic-usability/SKILL.md) by Marie Claire Dean (MIT)
