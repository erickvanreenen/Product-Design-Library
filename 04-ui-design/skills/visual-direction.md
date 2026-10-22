---
id: 04-ui-design/visual-direction
name: Set the visual direction
stage: 04-ui-design
fires-when: A new product, page or redesign needs a look; "what style should this be", "art direct this", "it looks generic"; before any screens are composed.
inputs: [work/00-brief.md, work/02-direction.md#principles, brand files in work/inputs/, work/05-system/ if a system exists]
output: work/04-ui-spec.md#direction, then DESIGN.md via context-files (05)
draws-on: [ui-ux-pro-max-skill/uupm/ui-ux-pro-max, ui-ux-pro-max-skill/uupm/design, S24, S12, S05]
version: 1.0
updated: 2026-10-22
---

# Set the visual direction

Chooses a deliberate visual direction from the product type, audience and brand, explores a few options, and has a person pick one, so screens do not default to the generic AI look.

## Use when
- No visual system exists, or a redesign needs a new direction.

## Not for
- Products with an established design system. Apply that system instead and go to `compose-screen`.

## Steps
1. **Read the brief for style signals:** product type (SaaS, e-commerce, dashboard, content, tool), audience and context of use, brand values, and words the stakeholders used ("calm", "expert", "playful").
2. **Shortlist styles that fit the product.** Use `references/ui-data/` (products, styles, colours, typography and reasoning rules) to see which styles suit this product type and which to avoid. Check each style's notes on accessibility, dark mode and performance.
3. **Gather references.** A few sites or brands the team admires, and DESIGN.md files of similar brands from getdesign.md as study material (S05). Record what to take from each: a principle, never a copy.
4. **Set the dials:** how bold or restrained (variance), how much motion, and how dense (spacious marketing page versus dense dashboard).
5. **Produce two or three directions** at the same fidelity: palette, type pairing, spacing density, shape language (radius, borders, shadows), iconography and one key screen rendered in each.
6. **List anti-patterns to avoid** for this product, for example purple gradients by default, emoji as icons, gratuitous glass effects, one radius and shadow on everything, centring everything.
7. **A person picks one direction** (gate G4). Record why with `decision-log`.
8. Hand the chosen direction to `design-tokens` and `context-files` (05) so it becomes the source of truth.

## Guardrails
- Brand assets are used as supplied; do not redraw logos or invent brand marks.
- Do not imitate a real brand's identity for a different company.
- Every direction must pass contrast checks in light and dark themes before it is shown.

## Output
```
## Direction
Signals from the brief
Shortlisted styles (fit, risks)
References and what to take from each
Dials: variance / motion / density
Directions A, B, C (palette, type, spacing, shape, icons, sample screen)
Anti-patterns to avoid
Chosen direction and reason
```

## Done when
- A person has chosen one direction, its reasons are logged, and it is written into DESIGN.md.

## Sources
Rewritten in this repository's format from:
- [ui-ux-pro-max-skill / ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-ux-pro-max/SKILL.md) by Next Level Builder (MIT)
- [ui-ux-pro-max-skill / design](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/design/SKILL.md) by Next Level Builder (MIT)
- S24: [UI redesign as art direction (Codex skill)](https://www.linkedin.com/posts/timothynice_codex-productdesign-genai-share-7488387102556983296-y74B) by Timothy Nice (post, read: read)
- S12: [Claude Code is terrible at design: a 9-step workflow](https://www.linkedin.com/posts/charlie-hills_claude-code-is-terrible-at-design-the-9-share-7472226424129736704-iC5A) by Charlie Hills (post, read: partial)
- S05: [getdesign.md](https://getdesign.md/) by VoltAgent team (site); format from Google Labs (site, read: read)
