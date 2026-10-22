---
id: 04-ui-design/motion
name: Design motion
stage: 04-ui-design
fires-when: Adding transitions, micro-interactions or animation; "make it feel alive", "spec the animation"; defining motion tokens.
inputs: [work/03-ux-spec.md#states, work/04-ui-spec.md#direction]
output: work/04-ui-spec.md#motion, motion tokens via design-tokens (05)
draws-on: [designer-skills/interaction-design/animation-principles, designer-skills/interaction-design/micro-interaction-spec, designer-skills/design-systems/motion-system, inclusive-design-skills/inclusive-interaction/motion-sensitivity]
version: 1.0
updated: 2026-10-22
---

# Design motion

Uses motion to explain change (where something came from, what happened) with a small set of shared timings, and makes it safe for people sensitive to movement.

## Steps
1. **Give motion a job:** show cause and effect, keep continuity between states, draw attention once, or give feedback. If it does none of these, remove it.
2. **Define duration tokens,** four to six at most: about 50 to 100 ms for state changes, 150 to 250 for small transitions, 250 to 400 for panels and modals, up to 600 for rare emphasis.
3. **Define easing tokens:** standard for moving between states, decelerate for entering, accelerate for leaving, and an optional spring for playful touches.
4. **Choreograph:** stagger related items by 30 to 50 ms, lead with the most important, and keep a whole sequence under about 500 ms.
5. **Spec micro-interactions:** trigger, rules, feedback, and what happens on repeat or interruption.
6. **Respect reduced motion:** when the setting is on, replace movement with instant changes or fades. No autoplaying motion without a pause control. Nothing flashes more than three times a second. Avoid parallax and large zooms.
7. Animate opacity and transform, not size and layout, to avoid jank.

## Guardrails
- One duration for everything feels mechanical; dozens feel chaotic. Use the tokens.
- Motion never blocks input or delays a task.

## Output
Motion tokens, a list of motions per component and screen (trigger, property, duration, easing, reduced-motion alternative).

## Done when
- Every motion has a purpose, uses tokens and has a reduced-motion alternative.

## Sources
Rewritten in this repository's format from:
- [designer-skills / animation-principles](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/animation-principles/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / micro-interaction-spec](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/micro-interaction-spec/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / motion-system](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/motion-system/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / motion-sensitivity](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/motion-sensitivity/SKILL.md) by Marie Claire Dean (MIT)
