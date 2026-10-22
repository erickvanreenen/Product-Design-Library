---
id: 05-ai-design-systems/design-tool-sync
name: Sync with the design tool
stage: 05-ai-design-systems
fires-when: An AI writes to or reads from a design tool (for example Figma) or syncs design and code; "build this in Figma", "push the system to Figma", "keep design and code in step".
inputs: [work/05-system/ (tokens, components, DESIGN.md), the design file link]
output: design file updates and a compliance report in work/05-system/sync-log.md
draws-on: [claude2figma/claude2figma/figma-preflight, claude2figma/claude2figma/figma-style-binding, claude2figma/claude2figma/reference-interpreter, S27, S29]
version: 1.0
updated: 2026-10-22
---

# Sync with the design tool

Makes AI-driven work in a design tool use the real library and tokens, never raw values, and keeps design and code in step. Written around Figma, the method applies to any tool with a library and variables.

## Use when
- An AI is about to create or edit frames, components or styles in a design tool.

## Steps
1. **Preflight before any work:** confirm the tool connection, that the file can be opened, which libraries are connected, and inventory the styles, variables and components available. Stop if any check fails.
2. **Interpret references against the system:** when given a screenshot or link, describe its layout, type, colour, spacing, focal point and components, then map each observation to an existing token or component. Flag every gap and wait for a decision before building.
3. **Library first:** use library components, then local components, and build from scratch only if nothing matches. Never rebuild primitives the system provides.
4. **Bind every value:** text uses text styles; fills, strokes, spacing, radius and effects bind to variables or styles. Raw values are not allowed. If no match exists, report the gap and wait.
5. **Use layout rules** (auto layout or equivalent) so frames resize correctly.
6. **Verify after each write:** scan the created nodes for unbound values or detached instances and fix them.
7. **Sync both ways only when the system is solid:** pull the system into code and build against real components, then push built work back to the canvas for editing. A half-finished system makes the AI invent the missing half (S29).

## Guardrails
- Never use raw hex values, font sizes or spacing in the design file.
- Never overwrite a master component or library style without explicit approval.
- Tool-specific steps (for example Figma's own skills for generating designs and libraries, S27) belong in the project setup, not in this file.

## Output
A sync log listing what was created, which tokens and components were used, gaps found and decisions taken.

## Done when
- The compliance scan finds no raw values or detached instances in the new work.

## Sources
Rewritten in this repository's format from:
- [claude2figma / figma-preflight](https://github.com/senlindesign/claude2figma/blob/main/.claude/skills/figma-preflight/SKILL.md) by Sen Lin (MIT)
- [claude2figma / figma-style-binding](https://github.com/senlindesign/claude2figma/blob/main/.claude/skills/figma-style-binding/SKILL.md) by Sen Lin (MIT)
- [claude2figma / reference-interpreter](https://github.com/senlindesign/claude2figma/blob/main/.claude/skills/reference-interpreter/SKILL.md) by Sen Lin (MIT)
- S27: [Figma skills for Claude Code](https://www.linkedin.com/posts/nbabich_ai-coding-claude-share-7469775707645149184-kxrp) by Nick Babich (post, read: partial)
- S29: [Updated Claude design workflow](https://www.linkedin.com/posts/carmenerincon_heyy-designers-ive-updated-my-claude-share-7490007425178222592-uMJ6/) by Carmen Erincon (post, read: partial)
