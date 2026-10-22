---
id: 05-ai-design-systems/context-files
name: Write the AI context files
stage: 05-ai-design-systems
fires-when: Preparing a project so any AI can design or build consistently; "write our DESIGN.md", "make the system AI-readable"; after tokens and the visual direction are set.
inputs: [tokens.json, component specs, work/04-ui-spec.md#direction, work/01-research.md, work/03-ux-spec.md#model]
output: work/05-system/DESIGN.md, work/05-system/UX.md
draws-on: [ui-ux-pro-max-skill/uupm/design-system, S05, S07, S12, S13, S40]
version: 1.0
updated: 2026-10-22
---

# Write the AI context files

Writes two plain-text files that carry the visual system and the UX knowledge to any AI tool: DESIGN.md for how it looks, UX.md for how it should work and why.

## Use when
- Once a direction and tokens exist, and again whenever they change.

## Steps
1. **DESIGN.md** (following the open DESIGN.md format, S05):
   - A token block at the top for colour, type, spacing and radius, mirrored from `tokens.json`.
   - Prose beneath: the visual direction and its reasons, how to apply hierarchy, components to use for common needs, and the anti-patterns to avoid.
   - Page-specific overrides in separate files if pages differ (a master file plus overrides; the override wins).
2. **UX.md** (S13):
   - Research findings that act as guardrails, with confidence levels.
   - User models: personas and needs in short form.
   - World models: the conditions people use the product in (devices, environment, stress, access needs).
   - The glossary and vocabulary from the conceptual model.
   - Interaction standards: states, errors, feedback, forms, AI behaviour rules.
   - Design principles, ranked.
   - Pointers to DESIGN.md, the component library and the decision log.
3. **Add a decision log section** or link `decisions.md`, so future sessions inherit choices (S07).
4. **Keep them short and ordered:** hard rules first. Remove anything an AI would not act on.
5. **Test:** give an AI only these files and a small task, then check the result against the system with `slop-check` and `critique-screen`. Fix what it got wrong by improving the files.

## Guardrails
- One source of truth per topic. These files point to tokens; they do not fork them.
- No personal data, client secrets or raw interview transcripts in either file.

## Output
`DESIGN.md` and `UX.md` in `work/05-system/`, ready to copy into the product repository.

## Done when
- An AI given only these files produces a screen that uses the right tokens, components and vocabulary.

## Sources
Rewritten in this repository's format from:
- [ui-ux-pro-max-skill / design-system](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/design-system/SKILL.md) by Next Level Builder (MIT)
- S05: [getdesign.md](https://getdesign.md/) by VoltAgent team (site); format from Google Labs (site, read: read)
- S07: [Product Designer Agent plugin](https://www.linkedin.com/posts/waqarahmed-ux_productdesign-designsystems-claudecode-share-7467139160177274881-489q) by Waqar Ahmed (post, read: partial)
- S12: [Claude Code is terrible at design: a 9-step workflow](https://www.linkedin.com/posts/charlie-hills_claude-code-is-terrible-at-design-the-9-share-7472226424129736704-iC5A) by Charlie Hills (post, read: partial)
- S13: [UX.md: a design artefact for AI](https://www.linkedin.com/posts/tonyalicea_what-artifacts-do-ux-design-and-user-research-share-7490021157350367232-Li6K) by Tony Alicea (post, read: partial)
- S40: [Creating an AI-ready design system: 4-step checklist](https://www.linkedin.com/posts/ai-design-ui-share-7470486486128336896-Zfn4) by Author profile not captured (post, read: read)
