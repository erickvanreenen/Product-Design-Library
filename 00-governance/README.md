# Governance

Rules that apply to every stage: intake, context, gates, decisions and checks on AI output.

**Position in the line:** step 0 of `playbooks/run-brief.md`.  
**Writes:** work/00-brief.md, work/context/, work/decisions.md  
**Gate:** G0 Scope

`stage-gate`, `decision-log` and `ai-output-check` run at every gate.

## Running this stage alone

Run `intake-brief` on any new request, even a small one. `context-pack` in light mode needs only the brief.

## Skills, in running order

| # | Skill | Step | Use when |
|---|---|---|---|
| 1 | [Intake a brief](skills/intake-brief.md) | 0 | A new brief, request or project arrives; someone says "here is the brief", "start this project" or "where do we begin". |
| 2 | [Build the context pack](skills/context-pack.md) | 0 | Before any AI generates design work for a project; when output feels generic; when starting a new session on an existing project. |
| 3 | [Run a stage gate](skills/stage-gate.md) | any | A stage finishes; before moving to the next stage; when someone asks "can we move on" or "is this ready". |
| 4 | [Log a decision](skills/decision-log.md) | any | A choice is made between options; a gate is passed; something is deliberately not done; a pattern departs from the norm. |
| 5 | [Check AI output](skills/ai-output-check.md) | any | Any AI-produced research summary, copy, spec, screen or code is about to be shown to a person or used by the next stage. |

## Gate checklist: G0 Scope (Intake and landscape)

- [ ] Problem stated without a solution
- [ ] Out of scope listed
- [ ] Platform mapped and feature placed, ripple owners named
- [ ] Stages to run agreed by a person

## Posts and articles that informed this stage

- S04: [UX Research Framework](https://www.linkedin.com/posts/vitalyfriedman_ux-research-framework-pdf-httpslnkdin-share-7455888543983390720-8YU7) by Vitaly Friedman (framework by Erika Hall) (post, read: partial)
- S07: [Product Designer Agent plugin](https://www.linkedin.com/posts/waqarahmed-ux_productdesign-designsystems-claudecode-share-7467139160177274881-489q) by Waqar Ahmed (post, read: partial)
- S08: [Claude Code for enterprise design](https://www.linkedin.com/posts/fivepluszero_uxdesign-claudecode-designsystems-share-7457839779913707521-cD7_) by Karen Ng (post, read: partial)
- S11: [2026 AI Product Design Stack, idea to launch](https://www.linkedin.com/posts/toqeer-ali_ai-isnt-replacing-the-design-process-most-share-7505270917539717124-IYdM) by Toqeer Ali (post, read: read)
- S12: [Claude Code is terrible at design: a 9-step workflow](https://www.linkedin.com/posts/charlie-hills_claude-code-is-terrible-at-design-the-9-share-7472226424129736704-iC5A) by Charlie Hills (post, read: partial)
- S13: [UX.md: a design artefact for AI](https://www.linkedin.com/posts/tonyalicea_what-artifacts-do-ux-design-and-user-research-share-7490021157350367232-Li6K) by Tony Alicea (post, read: partial)
- S15: [7 AI concepts every product designer should know](https://www.linkedin.com/posts/mayuri-salunke-b9a19b178_uxdesign-productdesign-artificialintelligence-share-7479958806672642048-9WVs) by Mayuri Salunke (post, read: partial)
- S25: [Autonomous design-ops audits](https://www.linkedin.com/posts/stanislau_claudecode-productdesign-designops-share-7484931629862477824-4Fsv) by Stanislau (post, read: partial)
- S29: [Updated Claude design workflow](https://www.linkedin.com/posts/carmenerincon_heyy-designers-ive-updated-my-claude-share-7490007425178222592-uMJ6/) by Carmen Erincon (post, read: partial)
- S46: [Ultimate Claude Code setup for product designers](https://uxplanet.org/ultimate-claude-code-setup-for-product-designers-f8b2fff4ac69) by UX Planet (article, read: partial)

## More skills in the original repositories

Not rewritten here, either because a consolidated skill covers most of it or because it is specialist. Use them directly when you need the depth.

- [layers-skills / layers-intro](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-intro/SKILL.md): Framework orientation for Layers of Product Design: load this first; provides the context all other skills depend on

Back to the [index](../README.md).
