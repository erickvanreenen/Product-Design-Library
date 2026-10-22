# AI-ready design systems

The source of truth AI builds from: tokens, components, DESIGN.md and UX.md.

**Position in the line:** step 5 of `playbooks/run-brief.md`.  
**Writes:** work/05-system/ (tokens.json, components/, DESIGN.md, UX.md)  
**Gate:** G5 System

## Running this stage alone

For an existing product start with `audit-system`. For a new one, run the UI foundations first, then `design-tokens`.

## Skills, in running order

| # | Skill | Step | Use when |
|---|---|---|---|
| 1 | [Audit the design system](skills/audit-system.md) | 5 | Before binding AI to an existing system; "is our design system AI-ready", "audit our tokens", "the build has drifted"; inheriting a product. |
| 2 | [Define design tokens](skills/design-tokens.md) | 5 | Creating or extending tokens for colour, type, spacing, radius, elevation or motion; adding themes or dark mode; "set up our tokens". |
| 3 | [Specify a component](skills/component-spec.md) | 5 | A new or changed component is needed; "spec this component", "we need a date picker"; a screen needs something the library lacks. |
| 4 | [Write the AI context files](skills/context-files.md) | 5 | Preparing a project so any AI can design or build consistently; "write our DESIGN.md", "make the system AI-readable"; after tokens and the visual direction are set. |
| 5 | [Sync with the design tool](skills/design-tool-sync.md) | 5 | An AI writes to or reads from a design tool (for example Figma) or syncs design and code; "build this in Figma", "push the system to Figma", "keep design and code in step". |
| 6 | [Govern the design system](skills/system-governance.md) | 5 | The system is used by more than one person or team; "who decides what goes in the system", "how do we deprecate this"; setting up contribution rules. |

## Gate checklist: G5 System (Design system)

- [ ] Tokens and components exist before screens
- [ ] Audit verdict recorded (existing systems)
- [ ] DESIGN.md and UX.md tested with an AI

## Posts and articles that informed this stage

- S05: [getdesign.md](https://getdesign.md/) by VoltAgent team (site); format from Google Labs (site, read: read)
- S07: [Product Designer Agent plugin](https://www.linkedin.com/posts/waqarahmed-ux_productdesign-designsystems-claudecode-share-7467139160177274881-489q) by Waqar Ahmed (post, read: partial)
- S09: [Component workflow: research to Figma to Storybook](https://www.linkedin.com/posts/benjaminchristine_designsystems-ai-claudecode-share-7463544631411032064-XfDb) by Ben Christine (post, read: partial)
- S10: [Design-system compliance needs an audited system](https://www.linkedin.com/posts/bevinmohabeer_ai-claudeai-foundingdesigner-share-7468597142522257409-QJAo) by Bevin Mohabeer (post, read: read)
- S12: [Claude Code is terrible at design: a 9-step workflow](https://www.linkedin.com/posts/charlie-hills_claude-code-is-terrible-at-design-the-9-share-7472226424129736704-iC5A) by Charlie Hills (post, read: partial)
- S13: [UX.md: a design artefact for AI](https://www.linkedin.com/posts/tonyalicea_what-artifacts-do-ux-design-and-user-research-share-7490021157350367232-Li6K) by Tony Alicea (post, read: partial)
- S27: [Figma skills for Claude Code](https://www.linkedin.com/posts/nbabich_ai-coding-claude-share-7469775707645149184-kxrp) by Nick Babich (post, read: partial)
- S29: [Updated Claude design workflow](https://www.linkedin.com/posts/carmenerincon_heyy-designers-ive-updated-my-claude-share-7490007425178222592-uMJ6/) by Carmen Erincon (post, read: partial)
- S40: [Creating an AI-ready design system: 4-step checklist](https://www.linkedin.com/posts/ai-design-ui-share-7470486486128336896-Zfn4) by Author profile not captured (post, read: read)

## More skills in the original repositories

Not rewritten here, either because a consolidated skill covers most of it or because it is specialist. Use them directly when you need the depth.

- [designer-skills / icon-system](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/icon-system/SKILL.md): Specify an icon system: grid, sizing, stroke weight, naming, categories, and implementation. Use when standardising iconography. For broader illustration, use `illustration-style` (ui-design).
- [designer-skills / localization-design](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/localization-design/SKILL.md): Design for multiple languages, writing directions, and cultural contexts: text expansion, RTL mirroring, and locale formats. Use when shipping beyond one locale. For the words themselves, use `ux-writing` (designer-tool

Back to the [index](../README.md).
