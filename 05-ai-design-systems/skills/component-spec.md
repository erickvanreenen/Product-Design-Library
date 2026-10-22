---
id: 05-ai-design-systems/component-spec
name: Specify a component
stage: 05-ai-design-systems
fires-when: A new or changed component is needed; "spec this component", "we need a date picker"; a screen needs something the library lacks.
inputs: [work/03-ux-spec.md#states, tokens, existing library]
output: work/05-system/components/<name>.md
draws-on: [designer-skills/design-systems/component-spec, claude2figma/claude2figma/component-rules, S09]
version: 1.0
updated: 2026-10-22
---

# Specify a component

Writes a complete, implementable component spec once, so design files and code are generated from the same definition.

## Steps
1. **Check the library first:** connected library, then local components, then build new only if nothing fits. Never rebuild basic parts the system already has (buttons, inputs, checkboxes, toggles, badges, avatars, icons, tabs, alerts, toasts, spinners).
2. **Research before drawing:** look at how mature libraries handle the same component (anatomy, variants, naming) and at accessible patterns (ARIA roles, keyboard behaviour, focus). Record what you took and why (S09).
3. **Write the spec:**
   - Overview: what it is, when to use it, when not to.
   - Anatomy: parts, required and optional.
   - Properties: one table with name, type, default, constraints and description. This single table drives both the design tool's component properties and the code's props (S09).
   - Variants: size, style, layout.
   - States: default, hover, focus, active, disabled, loading, error, selected.
   - Behaviour: interactions, motion tokens, responsive rules, edge cases (long text, empty, overflow, right-to-left).
   - Accessibility: role, name, keyboard keys, focus handling, announcements, target size.
   - Usage: do and do not examples, content rules, related components.
4. **Bind every visual value to a token.** If one is missing, flag the gap and decide: use the nearest token or add one through `design-tokens`.
5. **Specify the layout model** (auto layout or flex) so it resizes predictably.

## Guardrails
- One component, one spec, one source. Do not keep a second definition in a design file.
- Describe behaviour, not just appearance.

## Output
A spec file per component in the structure above.

## Done when
- The property table could generate both the design component and the code props, and every state and keyboard behaviour is defined.

## Sources
Rewritten in this repository's format from:
- [designer-skills / component-spec](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/component-spec/SKILL.md) by Marie Claire Dean (MIT)
- [claude2figma / component-rules](https://github.com/senlindesign/claude2figma/blob/main/.claude/skills/component-rules/SKILL.md) by Sen Lin (MIT)
- S09: [Component workflow: research to Figma to Storybook](https://www.linkedin.com/posts/benjaminchristine_designsystems-ai-claudecode-share-7463544631411032064-XfDb) by Ben Christine (post, read: partial)
