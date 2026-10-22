---
id: 06-design-critique/heuristic-review
name: Run a heuristic review
stage: 06-design-critique
fires-when: Reviewing a flow or product for usability before testing; "do a heuristic evaluation", "expert review"; reviewing an AI feature.
inputs: [the flows or prototype, work/03-ux-spec.md, work/03-ux-spec.md#ai-behaviour if relevant]
output: work/06-critique.md#heuristics
draws-on: [designer-skills/prototyping-testing/heuristic-evaluation, ai-design-skills/evaluation/heuristic-evaluation-ai]
version: 1.0
updated: 2026-10-22
---

# Run a heuristic review

Walks through the product against recognised usability heuristics, adapted for AI features where present, and rates each problem by severity.

## Steps
1. Set scope: which flows and tasks.
2. Walk each task twice: as a new user, then as an experienced one.
3. Check the ten heuristics:
   1. System status is visible (for AI: what it is doing, using and how sure it is).
   2. It speaks the user's language (no model internals or jargon).
   3. Users can undo, exit and stop (including stopping generation and overriding AI).
   4. Consistency with conventions and with itself (AI gives a consistent format for similar requests).
   5. Errors are prevented (AI asks to clarify before producing weak output).
   6. Recognition over recall (show what is possible, including what the AI can do).
   7. Flexibility for novices and experts.
   8. Minimal design (no irrelevant content; AI output without padding or needless caveats).
   9. Errors are explained in plain terms with a way to recover.
   10. Help is available in context.
4. For AI features, also check: trust is calibrated, failure is partial rather than total, users can correct it and see it adapt, limits are clear before users hit them, and the AI takes the right amount of initiative.
5. Record each issue: heuristic, location, description, severity, recommendation.
6. Rate severity 0 to 4: not a problem, cosmetic, minor, major, catastrophic (fix before release).
7. Where possible use two or three reviewers and merge findings; one reviewer misses many issues.

## Guardrails
- A heuristic review is not user testing. Plan `usability-test-plan` (07) for what it cannot answer.

## Output
An issue table sorted by severity, with the heuristic violated and the recommendation.

## Done when
- Every task in scope has been walked, and every issue rated 3 or 4 has a recommendation.

## Sources
Rewritten in this repository's format from:
- [designer-skills / heuristic-evaluation](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/heuristic-evaluation/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / heuristic-evaluation-ai](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/evaluation/heuristic-evaluation-ai/SKILL.md) by Marie Claire Dean (MIT)
