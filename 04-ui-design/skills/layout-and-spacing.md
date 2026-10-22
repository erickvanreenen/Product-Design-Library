---
id: 04-ui-design/layout-and-spacing
name: Set layout, grid and spacing
stage: 04-ui-design
fires-when: Defining page structure, grids, breakpoints or spacing; "it feels cramped", "make it responsive", "what grid should we use".
inputs: [work/04-ui-spec.md#direction, work/03-ux-spec.md#wireframes]
output: work/04-ui-spec.md#layout, spacing tokens via design-tokens (05)
draws-on: [designer-skills/ui-design/layout-grid, designer-skills/ui-design/spacing-system, designer-skills/ui-design/responsive-design, designer-skills/ui-design/readable-measure, designer-skills/ui-design/platform-conventions]
version: 1.0
updated: 2026-10-22
---

# Set layout, grid and spacing

Defines a grid, a spacing scale and responsive rules that keep every screen consistent and readable on every device.

## Steps
1. **Pick a base unit** of 4 or 8 pixels and build a spacing scale from it, for example 4, 8, 12, 16, 24, 32, 48, 64. Choose density: spacious for marketing and reading, compact for data-heavy tools.
2. **Apply spacing by relationship:** less space inside a group than between groups. Related items sit close; separate sections get clear gaps.
3. **Define the grid:** 4 columns on phones, 8 on tablets, 12 on desktops; gutters of 16, 24 or 32; outer margins of 16 on phones and 24 to 48 on desktops.
4. **Set breakpoints from content**, starting from common ranges: phones up to about 639, tablets to 1023, laptops to 1439, large screens above. Design mobile first.
5. **Keep text readable:** 45 to 75 characters per line for body text, 55 to 70 for long reading. Cap text containers (about 65ch) instead of stretching to full width.
6. **Adapt to input:** touch targets at least 44 by 44 points (48 by 48 on Android) with 8 pixels between them; hover is never the only way to reveal something.
7. **Follow platform conventions** for iOS, Android and web where users expect them: navigation placement, back behaviour, safe areas.
8. **Avoid sideways scrolling** of the page; let wide tables scroll inside their own container.

## Guardrails
- Use spacing tokens only. No one-off values.
- Never disable zoom.

## Output
Spacing scale, grid per breakpoint, breakpoint rules, measure limits and target sizes.

## Done when
- Every wireframe fits the grid at each breakpoint using only scale values, with no page-level sideways scroll.

## Sources
Rewritten in this repository's format from:
- [designer-skills / layout-grid](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/layout-grid/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / spacing-system](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/spacing-system/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / responsive-design](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/responsive-design/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / readable-measure](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/readable-measure/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / platform-conventions](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/platform-conventions/SKILL.md) by Marie Claire Dean (MIT)
