---
id: 06-design-critique/brief-traceability
name: Check the design against the brief
stage: 06-design-critique
fires-when: A design or prototype is close to done; "does this answer the brief", "have we missed anything"; before critique and before client presentation; step 12 of erick_process.
inputs: [work/00-brief.md, work/00-landscape.md#placement, the prototype or screens, work/decisions.md]
output: work/06-critique.md#brief-check
draws-on: [designer-skills/design-ops/design-review-process, designer-skills/ux-strategy/design-brief, ux-pgm-skills/program-planning/scoping-framework, ux-pgm-skills/delivery-execution/launch-readiness, layers-skills/layers/layers-surface]
version: 1.0
updated: 2026-10-22
---

# Check the design against the brief

Traces every requirement, success criterion and constraint in the refined brief to where the design answers it, with evidence, so gaps surface before the client finds them.

## Use when
- After the prototype is refined, before critique and again before the final presentation.

## Steps
1. **Break the brief into checkable lines:** each goal, success criterion, user need, constraint (brand, legal, technical, accessibility, timeline), deliverable, and each dependency or ripple marked "design for it" in the placement map.
2. **Trace each line** to the screens, states, flows or copy that answer it. Link the frame or prototype step.
3. **Mark each line:** met (with evidence), partly met (what is missing), not met, or deliberately out of scope (with the decision that put it there).
4. **Check the reverse direction:** list anything in the design that no brief line asks for. Keep it only if it serves a stated goal; otherwise flag it as scope creep.
5. **Check the ripples:** confirm every downstream effect from `feature-placement` has a designed answer or an agreed owner.
6. **Check readiness domains:** flows and edge states, accessibility, content and copy, measurement (are success metrics measurable in this design), and hand-off completeness.
7. **Summarise:** a one-line verdict per goal, the gaps to close before presenting, and the risks to name openly to the client.

## Guardrails
- "Met" needs evidence a reviewer can click on, not a statement.
- Do not quietly drop a brief requirement; out-of-scope items need a logged decision.

## Output
```
## Brief check
| Brief line | Type | Where answered (link) | Status | Evidence / gap |
Design elements not asked for (keep or cut)
Ripples covered / owned
Verdict per goal; gaps to close; risks to present
```

## Done when
- Every brief line has a status with evidence, and every gap has an owner or a fix.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-review-process](https://github.com/Owl-Listener/designer-skills/blob/main/design-ops/skills/design-review-process/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / design-brief](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/design-brief/SKILL.md) by Marie Claire Dean (MIT)
- [ux-pgm-skills / scoping-framework](https://github.com/Owl-Listener/ux-pgm-skills/blob/main/program-planning/skills/scoping-framework/SKILL.md) by Marie Claire Dean (MIT)
- [ux-pgm-skills / launch-readiness](https://github.com/Owl-Listener/ux-pgm-skills/blob/main/delivery-execution/skills/launch-readiness/SKILL.md) by Marie Claire Dean (MIT)
- [layers-skills / layers-surface](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-surface/SKILL.md) by Jamie Mill (MIT)
