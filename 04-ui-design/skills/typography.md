---
id: 04-ui-design/typography
name: Set typography
stage: 04-ui-design
fires-when: Choosing typefaces, sizes or text styles; "the text hierarchy is off", "set up the type scale".
inputs: [work/04-ui-spec.md#direction]
output: work/04-ui-spec.md#type, type tokens via design-tokens (05)
draws-on: [designer-skills/ui-design/typography-scale, inclusive-design-skills/adaptive-interfaces/flexible-typography]
version: 1.0
updated: 2026-10-22
---

# Set typography

Sets a small type scale, weights and spacing that create clear hierarchy, read well and scale with users' text-size settings.

## Steps
1. **Choose typefaces** to suit the direction: usually one family for interface text, optionally a display face for headings. Check language and character support, weights available, licence and loading cost. `references/ui-data/typography.csv` lists tested pairings.
2. **Build a scale from a ratio** (1.2 to 1.333) with four to six sizes, for example 14, 16, 20, 24, 32, 40. Body text is 16 pixels (1rem) or more; small text no less than 14 (0.875rem).
3. **Set line height:** 1.5 or more for body text, 1.2 to 1.3 for headings, up to 1.75 for long reading. Paragraph spacing at least 1.5 times the font size.
4. **Limit weights** to two or three (for example 400, 600, 700). Use size and weight together for hierarchy; a step of about 1.5 times in size reads as a clear level.
5. **Letter spacing:** slightly tighter for large headings, normal for body, slightly wider for small uppercase labels.
6. **Use relative units** so text grows with browser and system settings. Check the layout at 200 per cent text size and with the largest system text.
7. **Map styles to roles:** display, heading 1 to 3, body, small, label, caption, code. Name them by role, not by size.

## Guardrails
- No body text under 16 pixels; no text that cannot be resized.
- Avoid long runs of uppercase, italics or centred text.

## Output
Typefaces with reasons, a scale table (role, size, line height, weight, letter spacing) and resize test notes.

## Done when
- Every text role has one style, and the layout survives 200 per cent text size.

## Sources
Rewritten in this repository's format from:
- [designer-skills / typography-scale](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/typography-scale/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / flexible-typography](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/flexible-typography/SKILL.md) by Marie Claire Dean (MIT)
