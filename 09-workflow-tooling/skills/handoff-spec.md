---
id: 09-workflow-tooling/handoff-spec
name: Write the handoff spec
stage: 09-workflow-tooling
fires-when: Design is ready for engineering; "prepare handoff", "write the dev spec".
inputs: [work/03-ux-spec.md, work/04-ui-spec.md, work/05-system/, work/07-qa-report.md]
output: work/handoff.md
draws-on: [designer-skills/design-ops/handoff-spec, inclusive-design-skills/accessibility-decisions/handoff]
version: 1.0
updated: 2026-10-22
---

# Write the handoff spec

Packages everything engineers need to build the design as intended, referenced to the system rather than to raw values.

## Steps
1. **Visual:** token names (not hex codes or pixel values) for colour, type, spacing, radius and shadow; responsive behaviour per breakpoint.
2. **Interaction:** every state, transitions with motion tokens, gestures, keyboard order and shortcuts, focus handling.
3. **Content:** final copy, character limits and truncation, dynamic content rules, translation expansion and right-to-left needs, empty, loading and error content.
4. **Accessibility:** names, roles and states for custom components, announcements, heading structure, alt text, target sizes, and accessibility decisions with their reasons.
5. **AI behaviour** where relevant: states, confidence and source rules, escalation and fallbacks.
6. **Analytics:** events needed to measure the success metrics.
7. **Assets:** icons as SVG named by convention, images with formats and sizes, fonts.
8. **Edge cases and open questions,** each with an owner.
9. **Walk engineers through it** and agree how design QA will run.

## Guardrails
- Link to specs and tokens; do not duplicate them in the handoff.
- Every open question has an owner and a date.

## Output
A handoff document with the sections above and links.

## Done when
- Engineering has walked through it and has no unowned questions.

## Sources
Rewritten in this repository's format from:
- [designer-skills / handoff-spec](https://github.com/Owl-Listener/designer-skills/blob/main/design-ops/skills/handoff-spec/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / handoff](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/handoff/SKILL.md) by Marie Claire Dean (MIT)
