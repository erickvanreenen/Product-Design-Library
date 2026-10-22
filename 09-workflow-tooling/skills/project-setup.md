---
id: 09-workflow-tooling/project-setup
name: Set up an AI design project
stage: 09-workflow-tooling
fires-when: Starting a project where AI will help design or build; "set up the workspace", "connect the tools", "how should the project be structured".
inputs: [work/00-brief.md, tools available to the team]
output: the project folder structure and its instruction file
draws-on: [S46, S39, S29, S08]
version: 1.0
updated: 2026-10-22
---

# Set up an AI design project

Gives the project a real structure, a single instruction file for AI and the right connections, so every session starts from the same context.

## Steps
1. **Create the structure** (S46):
   ```
   docs/        requirements, user flows, UX principles (UX.md), decisions
   design/      DESIGN.md, tokens, component specs, interaction patterns
   work/        hand-off files from the run-brief playbook
   app/ or src/ code, if any
   ```
2. **Write one instruction file** at the top level (AGENTS.md, CLAUDE.md or the equivalent for your tool) that points to the context pack, DESIGN.md, UX.md and this repository's AGENTS.md. Keep it short; point, do not copy.
3. **Keep the stack small** (S29, S30): one place for thinking (chat), one for building (code editor or design tool), one for sharing (a preview link). Context builds up when tools stay put.
4. **Connect only what earns its place** through MCP or equivalent connectors (S39): live library documentation, the component library, the design tool, the docs or PRD tool, analytics. Note each connection's purpose.
5. **Work on a safe branch** or copy for experiments, and share real preview links for review.
6. **Install skills deliberately:** load the stage skills from this repository the project needs, plus tool-specific ones (for example a design tool's own skills). Avoid stacking overlapping skills.
7. **Record the set-up** in `docs/` so others and future sessions can reproduce it.

## Guardrails
- Never store credentials, API keys or client secrets in the repository or instruction files.
- Check each third-party tool's data handling before connecting client material.

## Output
The folder structure, the instruction file, a list of connections with purposes, and set-up notes.

## Done when
- A new AI session can find the brief, the context pack, DESIGN.md and UX.md from the instruction file alone.

## Sources
Rewritten in this repository's format from:
- S46: [Ultimate Claude Code setup for product designers](https://uxplanet.org/ultimate-claude-code-setup-for-product-designers-f8b2fff4ac69) by UX Planet (article, read: partial)
- S39: [Top 7 MCPs for product designers](https://www.linkedin.com/posts/ai-design-claudecode-share-7472622080522551297-YfIq) by Author profile not captured (post, read: read)
- S29: [Updated Claude design workflow](https://www.linkedin.com/posts/carmenerincon_heyy-designers-ive-updated-my-claude-share-7490007425178222592-uMJ6/) by Carmen Erincon (post, read: partial)
- S08: [Claude Code for enterprise design](https://www.linkedin.com/posts/fivepluszero_uxdesign-claudecode-designsystems-share-7457839779913707521-cD7_) by Karen Ng (post, read: partial)
