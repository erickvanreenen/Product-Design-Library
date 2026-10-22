---
id: 00-governance/context-pack
name: Build the context pack
stage: 00-governance
fires-when: Before any AI generates design work for a project; when output feels generic; when starting a new session on an existing project.
inputs: [work/00-brief.md, work/01-research.md if present, work/05-system/ if present]
output: work/context/ (project.md, plus pointers to DESIGN.md and UX.md)
draws-on: [ai-design-skills/prompt-architecture/context-engineering, ai-design-skills/prompt-architecture/constraint-specification, S08, S12, S13, S29, S46]
version: 1.0
updated: 2026-10-22
---

# Build the context pack

Assembles the small set of files an AI must read before it designs anything, so output follows the real project instead of generic defaults.

## Use when
- Starting a run, or opening a new AI session on a project already under way.
- Output keeps ignoring the brand, the system or the users. Weak output is usually missing context, not a weak model (S08).

## Not for
- Writing the design system files themselves, use `context-files` (05).

## Inputs
- The brief. Whatever exists from research and the design system. In light mode (single-stage use), the brief alone is enough.

## Steps
1. Write `project.md`: the problem, audience, success criteria, scope, constraints and glossary terms, each in a line or two.
2. Point to the sources of truth instead of copying them: `05-system/DESIGN.md` for visual rules, `05-system/UX.md` for research-backed UX rules, the component library.
3. Order the pack by importance: hard constraints first, then the current task, then background. Models attend most to the start and the end.
4. Separate hard constraints (must hold) from soft preferences (try to hold), and state which wins when they clash, for example "accessibility over brevity".
5. Remove anything stale, duplicated or generic. Every line should change an output if removed.
6. List what the AI must not do on this project: banned patterns, off-brand choices, unapproved claims.
7. Test it: ask the AI to restate the problem and three constraints from the pack. Fix any gap it reveals.

## Guardrails
- Never put personal data, credentials or client secrets in the pack.
- Keep `project.md` under one page. Long packs bury the rules that matter.
- Point to one source of truth per topic. Two versions of the palette will both get used.

## Output
```
work/context/project.md
- Problem / Audience / Success criteria
- Hard constraints (ordered) and which wins in a clash
- Soft preferences
- Glossary (link to UX.md)
- Never do
- Sources of truth: DESIGN.md, UX.md, component library
```

## Done when
- An AI can restate the problem and the top constraints correctly from the pack alone.
- Each topic has one source of truth.

## Sources
Rewritten in this repository's format from:
- [ai-design-skills / context-engineering](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/prompt-architecture/context-engineering/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / constraint-specification](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/prompt-architecture/constraint-specification/SKILL.md) by Marie Claire Dean (MIT)
- S08: [Claude Code for enterprise design](https://www.linkedin.com/posts/fivepluszero_uxdesign-claudecode-designsystems-share-7457839779913707521-cD7_) by Karen Ng (post, read: partial)
- S12: [Claude Code is terrible at design: a 9-step workflow](https://www.linkedin.com/posts/charlie-hills_claude-code-is-terrible-at-design-the-9-share-7472226424129736704-iC5A) by Charlie Hills (post, read: partial)
- S13: [UX.md: a design artefact for AI](https://www.linkedin.com/posts/tonyalicea_what-artifacts-do-ux-design-and-user-research-share-7490021157350367232-Li6K) by Tony Alicea (post, read: partial)
- S29: [Updated Claude design workflow](https://www.linkedin.com/posts/carmenerincon_heyy-designers-ive-updated-my-claude-share-7490007425178222592-uMJ6/) by Carmen Erincon (post, read: partial)
- S46: [Ultimate Claude Code setup for product designers](https://uxplanet.org/ultimate-claude-code-setup-for-product-designers-f8b2fff4ac69) by UX Planet (article, read: partial)
