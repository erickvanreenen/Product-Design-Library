---
id: 04-ui-design/colour
name: Build the colour system
stage: 04-ui-design
fires-when: Choosing a palette, adding dark mode, or fixing contrast; "pick colours", "it fails contrast", "add a dark theme".
inputs: [work/04-ui-spec.md#direction, brand colours]
output: work/04-ui-spec.md#colour, colour tokens via design-tokens (05)
draws-on: [designer-skills/ui-design/color-system, designer-skills/ui-design/dark-mode-design, inclusive-design-skills/adaptive-interfaces/colour-independence]
version: 1.0
updated: 2026-10-22
---

# Build the colour system

Creates a layered colour system (brand, neutrals, meaning) with accessible contrast in light and dark themes, never relying on colour alone.

## Steps
1. **Brand palette:** primary, secondary and accent, each with a tonal scale (for example 50 to 950).
2. **Neutrals:** a grey scale for text, surfaces and borders. Tint it slightly toward the brand hue so it looks intentional.
3. **Semantic colours** for success, warning, error and information, each with a background, border and text value. Keep these separate from the brand accent.
4. **Map to roles,** not raw values: text-primary, text-secondary, surface, surface-raised, border, action, action-hover, focus, and so on. Components use roles only.
5. **Check contrast:** body text 4.5:1 (7:1 for enhanced), large text 3:1, interface parts and focus rings 3:1 against what is next to them. Check every pairing in both themes.
6. **Design dark mode properly:** layered dark surfaces (raised surfaces get lighter), off-white text instead of pure white, accents desaturated by about 10 to 20 per cent, and contrast re-checked. Never invert the light theme.
7. **Never use colour alone** to carry meaning. Pair it with text, icons, patterns or position. About 1 in 12 men has a colour vision deficiency. Test with a simulator.
8. For charts, hand a distinct, accessible series palette to `data-visualisation`.

## Guardrails
- No hard-coded colours in components.
- Brand colours that fail contrast are used for decoration, not for text or controls.

## Output
Palette scales, role mapping for light and dark, a contrast table for every pairing, and colour-blind simulation notes.

## Done when
- Every role has light and dark values, every text and control pairing passes contrast, and nothing relies on colour alone.

## Sources
Rewritten in this repository's format from:
- [designer-skills / color-system](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/color-system/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / dark-mode-design](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/dark-mode-design/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / colour-independence](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/colour-independence/SKILL.md) by Marie Claire Dean (MIT)
