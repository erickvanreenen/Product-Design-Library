---
id: 06-design-critique/critique-screen
name: Critique a screen
stage: 06-design-critique
fires-when: A screen, mockup or screenshot needs review; "what is wrong with this screen", "review this design", "why does this feel off"; after compose-screen.
inputs: [the screen, work/03-ux-spec.md (priorities, copy), work/05-system/DESIGN.md, work/02-direction.md#principles]
output: work/06-critique.md#screens
draws-on: [designer-skills/visual-critique/critique-visual-hierarchy, designer-skills/visual-critique/critique-typography, designer-skills/visual-critique/critique-color, designer-skills/visual-critique/critique-composition, designer-skills/visual-critique/critique-information-density, designer-skills/visual-critique/critique-affordance, designer-skills/visual-critique/critique-brand-consistency]
version: 1.0
updated: 2026-10-22
---

# Critique a screen

Reviews one screen against seven craft lenses and returns a prioritised fix list, each point with an observation, the problem and a specific fix.

## Use when
- Judging an existing or newly composed screen. To compose new work, use `visual-hierarchy` (04).

## Not for
- A whole-product usability review, use `heuristic-review`.

## The seven lenses
1. **Hierarchy:** Is the first thing seen the most important? Does the eye move in a sensible order to the main action? Are levels at least about 1.5 times apart? Is there exactly one primary emphasis?
2. **Typography:** Does it stick to the type scale? Are line length, line height and weights doing their job? Is anything too small or too faint?
3. **Colour:** Do colours come from roles and tokens? Does text pass contrast? Is meaning carried by more than colour? Is the accent used sparingly?
4. **Composition:** Do alignment, grid and spacing hold? Is space grouping related items? Is the balance intentional?
5. **Density and load:** How many decisions does the main task need? Is the critical content visible and primary? Does the layout support scanning? Is detail revealed progressively?
6. **Affordance:** Do interactive things look interactive and static things look static? Are all states (hover, focus, pressed, disabled, selected, loading) visible? Is the main action obvious and specifically labelled? Are actions hidden behind hover on touch screens?
7. **Brand consistency:** Does it follow DESIGN.md: type, colour, shape, iconography, imagery, tone? Any off-system values?

## Steps
1. State the screen's purpose and its primary user goal before judging.
2. Run each lens. For each finding write: observation (neutral), problem (and why it matters to users), fix (specific and actionable).
3. Rate each lens pass, minor issue or major issue.
4. Check principles: does the screen honour the ranked design principles?
5. Prioritise: major issues that block the user goal first, then accessibility, then polish. Limit the list to what can be fixed in the next round.

## Guardrails
- Judge against the goal, principles and system, not personal taste. Name taste calls as taste.
- Separate surface fixes from problems rooted in the flow or model; send those to `coherence-check`.

## Output
```
Screen / goal
Lens ratings
Findings: # | lens | observation | problem | fix | severity
Top 5 fixes
```

## Done when
- Every major issue has a specific fix, and the list is ordered by impact on the user goal.

## Sources
Rewritten in this repository's format from:
- [designer-skills / critique-visual-hierarchy](https://github.com/Owl-Listener/designer-skills/blob/main/visual-critique/skills/critique-visual-hierarchy/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / critique-typography](https://github.com/Owl-Listener/designer-skills/blob/main/visual-critique/skills/critique-typography/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / critique-color](https://github.com/Owl-Listener/designer-skills/blob/main/visual-critique/skills/critique-color/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / critique-composition](https://github.com/Owl-Listener/designer-skills/blob/main/visual-critique/skills/critique-composition/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / critique-information-density](https://github.com/Owl-Listener/designer-skills/blob/main/visual-critique/skills/critique-information-density/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / critique-affordance](https://github.com/Owl-Listener/designer-skills/blob/main/visual-critique/skills/critique-affordance/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / critique-brand-consistency](https://github.com/Owl-Listener/designer-skills/blob/main/visual-critique/skills/critique-brand-consistency/SKILL.md) by Marie Claire Dean (MIT)
