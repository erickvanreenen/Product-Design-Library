---
id: 05-ai-design-systems/system-governance
name: Govern the design system
stage: 05-ai-design-systems
fires-when: The system is used by more than one person or team; "who decides what goes in the system", "how do we deprecate this"; setting up contribution rules.
inputs: [work/05-system/, team structure]
output: work/05-system/governance.md
draws-on: [designer-skills/design-systems/design-system-governance, designer-skills/design-systems/documentation-template, designer-skills/design-systems/pattern-library]
version: 1.0
updated: 2026-10-22
---

# Govern the design system

Sets how the system changes over time (who owns it, how changes are proposed, versioned and retired), so it grows without splitting into variants.

## Steps
1. **Choose an ownership model:** a central team owns everything (consistent, can bottleneck), anyone contributes through review (fast, needs strong standards), or a hybrid where a core team owns foundations and product teams own domain components.
2. **Define contribution:** how to propose (a short request with the problem, evidence and proposed spec), who reviews, the quality bar (spec complete, accessible, tokens only, documented), and how decisions are logged.
3. **Version and communicate:** semantic versions, a changelog, and notice for breaking changes with migration help.
4. **Deprecate deliberately:** mark it, give a replacement and a timeline, then remove.
5. **Document patterns, not just components:** recurring solutions (search with filters, empty states, bulk actions) with when to use them and examples.
6. **Use one documentation template** per component and pattern so people and AI find the same sections in the same place.
7. **Review regularly:** adoption, drift (from `design-qa`, 07), open gaps and requests.

## Guardrails
- AI-generated additions go through the same review as human ones.
- Changes to DESIGN.md or UX.md are versioned like code.

## Output
A governance page: owners, contribution steps, quality bar, versioning, deprecation and review rhythm.

## Done when
- Anyone can tell how to propose a change and who approves it.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-system-governance](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/design-system-governance/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / documentation-template](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/documentation-template/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / pattern-library](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/pattern-library/SKILL.md) by Marie Claire Dean (MIT)
