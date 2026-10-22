---
id: 06-design-critique/slop-check
name: Check for AI slop
stage: 06-design-critique
fires-when: Any AI-written copy or AI-generated UI is about to ship or be reviewed; "this sounds like AI", "this looks generic", "clean up this copy".
inputs: [copy or screens produced with AI, work/05-system/DESIGN.md, voice and tone in UX.md]
output: work/06-critique.md#slop, with corrected copy
draws-on: [stop-slop/writing/stop-slop, humanizer/writing/humanizer, ui-ux-pro-max-skill/uupm/ui-ux-pro-max, S23]
version: 1.0
updated: 2026-10-22
---

# Check for AI slop

Finds and removes the tells that make writing and interfaces read as machine-made and generic, so the work sounds and looks like this product.

## Use when
- On every AI-assisted output before a person reviews it closely.

## Steps

### Writing
1. **Filler:** throat-clearing openers ("Here's the thing"), emphasis crutches, stock phrases, adverbs that add nothing.
2. **Formulaic structures:** "not X, it is Y" contrasts, staged run-ups before the point, one-line dramatic closers, sayings that sound deep, arguing with nobody.
3. **Rhythm by rule:** forced groups of three, repeated sentence openings, dashes as the default joiner, stacked qualifiers, every sentence the same length.
4. **Inflation:** overused AI words, inflated significance, vague associations, sales language, borrowed authority.
5. **Voice:** passive voice with no actor, inanimate things doing human actions, narrator-from-a-distance instead of "you".
6. **Formatting by rule:** bold used as decoration, headings that repeat the first sentence, chatbot leftovers ("I hope this helps").
7. Fix by stating the point directly, naming the specific thing, using active voice and varying rhythm. Check against the product's voice; do not strip a deliberate voice.

### Interface
1. Default AI looks: purple-to-blue gradients, emoji used as icons, glass effects everywhere, the same radius and shadow on every block, everything centred, one accent colour on near-black, a generic serif-on-cream editorial look when nobody chose it.
2. Off-system values: colours, sizes or spacing not in DESIGN.md.
3. Mixed icon styles, placeholder imagery left in, lorem ipsum.
4. Visual confidence on uncertain content: bold headers and decisive layout around guesses.

## Guardrails
- Keep meaning. A shorter sentence that loses the point is worse.
- Do not apply writing rules to legal or regulated text without the owner.

## Output
A list of tells found (type, location), the corrected copy, and interface fixes.

## Done when
- A read-through finds none of the listed tells, and every interface value is from the system.

## Sources
Rewritten in this repository's format from:
- [stop-slop / stop-slop](https://github.com/hardikpandya/stop-slop/blob/main/SKILL.md) by Hardik Pandya (MIT)
- [humanizer / humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md) by Siqi Chen (MIT)
- [ui-ux-pro-max-skill / ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md) by Next Level Builder (MIT)
- S23: [15 free skills to fix AI slop](https://www.linkedin.com/posts/you-dont-need-a-paid-tool-to-fix-ai-slop-share-7496167624318500864-QBef) by Author profile not captured (post, read: partial)
