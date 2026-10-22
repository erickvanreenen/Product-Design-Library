---
id: 09-workflow-tooling/client-presentation
name: Present to the client
stage: 09-workflow-tooling
fires-when: The final or milestone presentation to a client or stakeholders; "prepare the client presentation", "walk them through it"; step 16 of erick_process.
inputs: [work/00-brief.md, work/00-landscape.md, work/01-research.md, work/06-critique.md#brief-check, work/decisions.md, the prototype]
output: work/presentation.md and the deck or live walkthrough
draws-on: [designer-skills/designer-toolkit/presentation-deck, designer-skills/designer-toolkit/design-rationale, designer-skills/designer-toolkit/design-negotiation, ux-pgm-skills/stakeholder-comms/executive-update, designer-skills/ux-strategy/business-design]
version: 1.0
updated: 2026-10-22
---

# Present to the client

Tells the story of the work so the client sees the thinking, trusts the decisions and leaves with a clear yes and next step.

## Steps
1. **Know the room:** who decides, who influences, what each cares about (revenue, cost, risk, brand, users), and what they last saw.
2. **Build the story arc:**
   - The goal, in their words, and the measure of success.
   - The big picture: the platform map and where this feature sits, with its ripples handled. This is where you show you understood their whole business, not just a screen.
   - What we learned: three to five research and benchmark insights, each linked to a decision.
   - The direction and why: options considered, the choice, and what it costs.
   - The experience: a live walkthrough of the prototype following one real user story, including an error or edge case handled well and one signature micro-interaction.
   - Proof it answers the brief: the brief check summary.
   - What it needs from them: the decision, the next steps, owners and dates.
3. **Translate into business terms:** which metric each key decision moves, and the cost of not doing it. Separate evidence from craft judgement.
4. **Prepare for pushback:** list the three hardest likely questions with short answers. For "can we change X", ask what outcome they want, then offer options that meet it.
5. **Rehearse the demo** on the device and connection you will present on. Have screenshots ready as a fallback.
6. **Follow up within a day:** a one-page summary (decision made, open items with owners, next date) and the prototype link.

## Guardrails
- Never present unverified claims or invented numbers. Assumptions are labelled.
- One ask per meeting. Bundled asks get deferred.
- Do not hide known gaps; name them with the plan to close them.

## Output
`presentation.md` with the audience notes, story outline, objection answers and follow-up summary, plus the deck or walkthrough script.

## Done when
- The client made a clear decision in the meeting, and the follow-up summary is sent.

## Sources
Rewritten in this repository's format from:
- [designer-skills / presentation-deck](https://github.com/Owl-Listener/designer-skills/blob/main/designer-toolkit/skills/presentation-deck/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / design-rationale](https://github.com/Owl-Listener/designer-skills/blob/main/designer-toolkit/skills/design-rationale/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / design-negotiation](https://github.com/Owl-Listener/designer-skills/blob/main/designer-toolkit/skills/design-negotiation/SKILL.md) by Marie Claire Dean (MIT)
- [ux-pgm-skills / executive-update](https://github.com/Owl-Listener/ux-pgm-skills/blob/main/stakeholder-comms/skills/executive-update/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / business-design](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/business-design/SKILL.md) by Marie Claire Dean (MIT)
