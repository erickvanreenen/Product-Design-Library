---
id: 05-ai-design-systems/audit-system
name: Audit the design system
stage: 05-ai-design-systems
fires-when: Before binding AI to an existing system; "is our design system AI-ready", "audit our tokens", "the build has drifted"; inheriting a product.
inputs: [the design files, component library and code, work/00-brief.md]
output: work/05-system/audit.md
draws-on: [designer-skills/design-ops/design-debt-audit, designer-skills/designer-toolkit/design-token-audit, S10, S40]
version: 1.0
updated: 2026-10-22
---

# Audit the design system

Measures how solid an existing design system is and what must be fixed before AI can build from it reliably. AI compliance only works on a system that is already sound (S10).

## Use when
- An existing product or system is about to be used as the source for AI-generated design or code.

## Not for
- Creating a system from nothing, use `design-tokens` and `component-spec`.

## Steps
1. **Set scope:** whole product, one area or one platform. Capture every screen and state in scope.
2. **Check AI-readiness** against four tests (S40):
   - One source of truth, ideally in code, that AI can read.
   - Explicit documentation: definitions, behaviour and usage for each style, token, component and pattern.
   - Real product examples and stated quality criteria.
   - Standard prompts or instructions with guardrails, not reinvented each time.
3. **Audit tokens:** extract every visual value from files and code, match to tokens, and report the share using tokens, hard-coded values, duplicates with different names, deprecated tokens still in use, and gaps.
4. **Audit components:** in use but not in the system, built differently per platform without reason, detached instances in design files, specs that do not match the build.
5. **Audit debt by type:** visual inconsistency, structural (patterns that no longer scale), accessibility (known WCAG failures, components that fail with assistive technology), documentation (decisions only in people's heads).
6. **Prioritise** by how often an issue appears times its impact on users. Accessibility failures go first.
7. **Recommend a plan:** fix now, fix before AI use, and track. State whether the system is ready for AI to build from, ready with named limits, or not ready.

## Guardrails
- Do not let AI bulk-generate new screens on a system rated "not ready".
- Record every "won't fix now" with `decision-log`.

## Output
```
Readiness verdict: ready | ready with limits | not ready
Token adoption: n% ; hard-coded values (list with suggested tokens)
Component gaps and mismatches
Debt by type, prioritised
Plan: now / before AI use / track
```

## Done when
- There is a readiness verdict with evidence and a prioritised plan.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-debt-audit](https://github.com/Owl-Listener/designer-skills/blob/main/design-ops/skills/design-debt-audit/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / design-token-audit](https://github.com/Owl-Listener/designer-skills/blob/main/designer-toolkit/skills/design-token-audit/SKILL.md) by Marie Claire Dean (MIT)
- S10: [Design-system compliance needs an audited system](https://www.linkedin.com/posts/bevinmohabeer_ai-claudeai-foundingdesigner-share-7468597142522257409-QJAo) by Bevin Mohabeer (post, read: read)
- S40: [Creating an AI-ready design system: 4-step checklist](https://www.linkedin.com/posts/ai-design-ui-share-7470486486128336896-Zfn4) by Author profile not captured (post, read: read)
