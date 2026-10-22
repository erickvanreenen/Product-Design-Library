---
id: 04-ui-design/compose-screen
name: Compose a screen
stage: 04-ui-design
fires-when: Building a high-fidelity screen or page from the spec and the system; "design this screen", "build the page".
inputs: [work/03-ux-spec.md (wireframes, states, copy), work/04-ui-spec.md, work/05-system/ (DESIGN.md, tokens, components)]
output: screens or coded pages, listed in work/04-ui-spec.md#screens
draws-on: [ui-ux-pro-max-skill/uupm/ui-styling, S24, S01]
version: 1.0
updated: 2026-10-22
---

# Compose a screen

Assembles a high-fidelity screen from the agreed wireframe, copy, states and design system, then runs a pre-delivery check before anyone reviews it.

## Use when
- After the design system exists (G5) and the direction is chosen (G4).

## Steps
1. **Load the sources of truth:** DESIGN.md, tokens, the component library and any page-specific overrides. If a page override exists, it wins over the master file.
2. **Build from existing components.** If a needed component does not exist, stop and spec it with `component-spec` (05) rather than inventing one inline.
3. **Apply the wireframe priorities** with `visual-hierarchy`, real copy, and real data lengths.
4. **Build every state** listed for the screen: empty, loading, error, success.
5. **Use tokens only** for colour, type, spacing, radius, shadow and motion.
6. **Run the pre-delivery check:**
   - Icons from one consistent family; no emoji as icons; brand assets used as supplied.
   - Every control has clear hover, focus, pressed and disabled states; pressing does not shift the layout.
   - Touch targets at least 44 by 44 points (48 by 48 on Android).
   - Contrast passes in light and dark themes, tested separately.
   - Focus order matches visual order; labels are descriptive.
   - Safe areas respected; content not hidden behind fixed bars.
   - Checked at 375 pixels wide, in landscape, on tablet and desktop, with reduced motion and the largest text size.
7. Hand the screen to critique (06).

## Guardrails
- No values outside the system. If the system is missing something, fix the system first.
- Label AI-generated screens as drafts until they pass critique.

## Output
The screen (file, link or code) and a short checklist result in `04-ui-spec.md#screens`.

## Done when
- The screen uses only system tokens and components, every state exists, and the pre-delivery check passes.

## Sources
Rewritten in this repository's format from:
- [ui-ux-pro-max-skill / ui-styling](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/ui-styling/SKILL.md) by Next Level Builder (MIT)
- S24: [UI redesign as art direction (Codex skill)](https://www.linkedin.com/posts/timothynice_codex-productdesign-genai-share-7488387102556983296-y74B) by Timothy Nice (post, read: read)
- S01: [designer-skills (repo)](https://github.com/Owl-Listener/designer-skills) by Owl-Listener (repo, read: partial)
