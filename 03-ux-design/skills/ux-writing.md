---
id: 03-ux-design/ux-writing
name: Write interface copy
stage: 03-ux-design
fires-when: Labels, buttons, errors, empty states, onboarding or help text are needed; "write the copy", "what should this button say", "review this microcopy".
inputs: [work/03-ux-spec.md#model vocabulary, #states, voice and tone from work/05-system/UX.md]
output: work/03-ux-spec.md#copy
draws-on: [designer-skills/designer-toolkit/ux-writing, designer-skills/ux-strategy/content-strategy, inclusive-design-skills/cognitive-accessibility/plain-language-design, inclusive-design-skills/accessible-content/link-text-design, stop-slop/writing/stop-slop]
version: 1.0
updated: 2026-10-22
---

# Write interface copy

Writes clear, plain interface copy in the product's voice that uses the model's vocabulary and helps people act.

## Steps
1. **Use the vocabulary.** One name per concept, as decided in the conceptual model. Never internal jargon.
2. **Set voice and tone.** Voice stays constant; tone shifts with context (reassuring in errors, brief in success, neutral in legal text). Record examples and counter-examples.
3. **Write by type:**
   - Buttons and calls to action: start with a verb, name the outcome ("Send invoice", not "Submit"), and match what the user wants to do.
   - Labels: short, sentence case, describe what to enter.
   - Errors: what happened, why, what to do.
   - Empty states: what goes here and the first step.
   - Confirmations: what just happened, next step, undo where possible.
   - Onboarding: one idea at a time, action over reading, always skippable.
   - Links: describe the destination. Never "click here" or "read more" alone.
4. **Keep it plain.** One idea per sentence, 15 to 20 words at most, active voice, everyday words. Aim for a reading age of about 11 to 13 for the public and simpler still for buttons and errors.
5. **Remove filler and AI tells:** throat-clearing openers, intensifiers, "not just X, it is Y" constructions, stacked adjectives and vague claims. See `slop-check` (06).
6. **Check with real content:** longest names, translations (allow about 30 per cent extra length), screen-reader reading order.

## Guardrails
- Never blame the user. Never use humour in errors about money, health or loss.
- Legal and regulated wording is approved by the owner, not rewritten freely.

## Output
A copy table: screen, element, state, copy, notes. Voice and tone notes go into `UX.md`.

## Done when
- Every element in the spec has final copy, every button starts with a verb, and no copy uses a term outside the vocabulary.

## Sources
Rewritten in this repository's format from:
- [designer-skills / ux-writing](https://github.com/Owl-Listener/designer-skills/blob/main/designer-toolkit/skills/ux-writing/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / content-strategy](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/content-strategy/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / plain-language-design](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/plain-language-design/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / link-text-design](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/link-text-design/SKILL.md) by Marie Claire Dean (MIT)
- [stop-slop / stop-slop](https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md) by Hardik Pandya (MIT)
