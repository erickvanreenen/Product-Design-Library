---
id: 07-qa-accessibility/cognitive-load-check
name: Check cognitive load
stage: 07-qa-accessibility
fires-when: Flows feel heavy or people drop out; "is this too complicated", "simplify this flow"; before release of any multi-step task.
inputs: [flows, screens, copy]
output: work/07-qa-report.md#cognitive-load
draws-on: [inclusive-design-skills/cognitive-accessibility/cognitive-load-assessment, inclusive-design-skills/cognitive-accessibility/memory-load-reduction, inclusive-design-skills/cognitive-accessibility/focus-attention-design]
version: 1.0
updated: 2026-10-22
---

# Check cognitive load

Walks a flow as a tired, stressed, unfamiliar user and measures the decisions, memory and new ideas it demands, then removes the load that is not essential.

## Steps
1. Walk the flow as someone tired, distracted and new to the product.
2. At each screen, count decisions, things to remember, new concepts, steps, reading difficulty and visual clutter. Rate each low, medium or high:
   - Decisions: 0 to 1 low, 2 to 3 medium, 4 or more high.
   - Things to remember: none, 1 to 2, 3 or more.
   - New concepts: none, 1, 2 or more.
   - Steps: 1 to 2, 3 to 5, 6 or more.
3. Mark the spikes: where you pause, re-read or feel unsure.
4. Separate essential load (the task is genuinely complex) from added load (caused by the design).
5. Reduce added load: show only what this step needs, use smart defaults, group into sets of three to five, show options instead of asking people to recall, keep earlier choices visible, one primary action per screen, plain language.
6. Support attention: no needless interruptions, distractions or autoplay; let people pause and resume without losing work.

## Guardrails
- Never remove information people need to make a safe decision just to cut load.

## Output
A load table per screen, the spikes, and specific reductions.

## Done when
- No screen rates high on more than one dimension without a recorded reason.

## Sources
Rewritten in this repository's format from:
- [inclusive-design-skills / cognitive-load-assessment](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/cognitive-load-assessment/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / memory-load-reduction](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/memory-load-reduction/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / focus-attention-design](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/focus-attention-design/SKILL.md) by Marie Claire Dean (MIT)
