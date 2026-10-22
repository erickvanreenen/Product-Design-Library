---
id: 03-ux-design/ai-experience
name: Design the AI experience
stage: 03-ux-design
fires-when: The product has an AI feature (assistant, generation, recommendations, agents); "design the AI feature", "how should the AI behave", "what happens when it is wrong".
inputs: [work/03-ux-spec.md#flows, #states, work/02-direction.md#decision]
output: work/03-ux-spec.md#ai-behaviour
draws-on: [ai-design-skills/ai-alignment-reasoning/trust-calibration, ai-design-skills/ai-alignment-reasoning/transparency-patterns, ai-design-skills/model-interaction-design/mixed-initiative-flow, ai-design-skills/model-interaction-design/generative-ui, ai-design-skills/design-agent-orchestration/failure-recovery, ai-design-skills/ai-alignment-reasoning/escalation-design, S14, S17]
version: 1.0
updated: 2026-10-22
---

# Design the AI experience

Specifies how an AI feature behaves for users: who leads, how confident it sounds, what it shows about its sources and limits, what it can generate, and what happens when it fails or should hand over.

## Use when
- Any flow where AI produces content, takes actions or makes suggestions.

## Steps
1. **Decide who leads at each step.** The user leads for judgement calls, high stakes, expertise or consent. The AI can lead when the user is exploring, the steps are well known, or they asked for help. Make each hand-over explicit, so it is always clear whose turn it is.
2. **Calibrate trust.** Match confidence wording to real certainty. Show sources where possible; say when there are none. Offer alternatives with the reason for the choice. State what it can and cannot do. Avoid hedging everything, and avoid confident formatting on uncertain output.
3. **Decide what to make visible:** that it is AI, sources, confidence, limits and reasoning. Show more when stakes are high or confidence is low; let users drill in rather than showing everything.
4. **Constrain generated UI** to the design system: allowed components, layout and style rules, interaction patterns and accessibility. Define a fallback when generation fails, and use plain text when it is clearer.
5. **Design the extra states AI adds:** thinking or working, streaming, partial result, low confidence, refused, can't answer, error, stopped by user, and corrected after feedback.
6. **Design failure handling:** retry with a limit, fall back, deliver a partial result and say what is missing, or fail honestly with alternatives. Let users stop, undo and edit.
7. **Design escalation:** triggers (low confidence, high stakes, distress, out of scope, policy, unresolved disagreement), where it goes (a person, a specialist, or back to the user), carrying the full context so users never repeat themselves, and what happens next.
8. **Plan feedback capture:** how users correct, rate or report outputs, and what changes as a result.

## Guardrails
- Never hide that the user is dealing with an AI.
- Never inflate confidence to match what the user seems to want.
- Irreversible or costly actions need human approval.
- Run harm anticipation from `ai-output-check` for features that affect health, money, safety or rights.

## Output
```
## AI behaviour
Initiative map (step: who leads, hand-over)
Confidence and source rules
Transparency per feature
Generated UI constraints and fallback
AI states table
Failure and escalation matrix: trigger, threshold, response, what the user sees
Feedback loop
```

## Done when
- Every AI state has a designed response, every escalation trigger has a destination, and users can always stop or undo.

## Sources
Rewritten in this repository's format from:
- [ai-design-skills / trust-calibration](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/trust-calibration/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / transparency-patterns](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/transparency-patterns/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / mixed-initiative-flow](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/mixed-initiative-flow/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / generative-ui](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/generative-ui/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / failure-recovery](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/design-agent-orchestration/failure-recovery/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / escalation-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/escalation-design/SKILL.md) by Marie Claire Dean (MIT)
- S14: [AI Designer Playbook](https://www.linkedin.com/posts/antivirusakash_ux-uxdesign-aidesign-share-7464923833121271808-p4zB) by Akash Solanki (post, read: partial)
- S17: [10 AI skills product designers should understand](https://www.linkedin.com/posts/imen-mlika_ux-ui-uxdesign-share-7498120402737582080-MQek) by Imen Mlika (post, read: partial)
