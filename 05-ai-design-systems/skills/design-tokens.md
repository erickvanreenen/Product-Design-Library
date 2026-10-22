---
id: 05-ai-design-systems/design-tokens
name: Define design tokens
stage: 05-ai-design-systems
fires-when: Creating or extending tokens for colour, type, spacing, radius, elevation or motion; adding themes or dark mode; "set up our tokens".
inputs: [work/04-ui-spec.md (direction, layout, type, colour, motion) or the audit]
output: work/05-system/tokens.json and the tokens section of DESIGN.md
draws-on: [designer-skills/design-systems/design-token, designer-skills/design-systems/naming-convention, designer-skills/design-systems/theming-system]
version: 1.0
updated: 2026-10-22
---

# Define design tokens

Turns visual decisions into named tokens in three tiers, so every screen, theme and AI output draws from the same values.

## Steps
1. **Global tokens** hold raw values: the colour scales, the spacing scale, type sizes, radii, shadows, durations and easings.
2. **Semantic (alias) tokens** describe purpose and point to globals: `color-text-primary`, `color-surface-raised`, `color-action-primary`, `space-stack-md`. Themes override this tier only.
3. **Component tokens** are optional and scoped: `button-color-background-primary`. Use them only where a component needs to diverge.
4. **Name consistently:** `{category}-{property}-{concept}-{variant}-{state}`, lower case with hyphens, named by purpose not appearance ("danger", not "red").
5. **Theme by overriding semantic tokens:** light, dark, high contrast, and density modes. Record which tokens are themeable and which are fixed.
6. **Document each token** with its use and a do-not-use note where people tend to misuse it.
7. **Export in a neutral format** (for example the W3C design tokens JSON) and generate platform outputs (CSS variables, design-tool variables) from it.
8. **Version** tokens with the system and note changes.

## Guardrails
- Components never reference global tokens or raw values directly.
- Keep scales short. If people keep adding one-off values, a scale step is missing.

## Output
`tokens.json` with tiers and modes, and a readable token table in DESIGN.md.

## Done when
- Every value in the UI spec maps to a semantic token, and each theme overrides only semantic tokens.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-token](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/design-token/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / naming-convention](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/naming-convention/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / theming-system](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/theming-system/SKILL.md) by Marie Claire Dean (MIT)
