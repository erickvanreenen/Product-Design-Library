---
id: 00-governance/intake-brief
name: Intake a brief
stage: 00-governance
fires-when: A new brief, request or project arrives; someone says "here is the brief", "start this project" or "where do we begin".
inputs: [raw brief in work/inputs/, any existing research, data, screens or brand files]
output: work/00-brief.md
draws-on: [designer-skills/ux-strategy/design-brief, layers-skills/layers/layers-orient, ux-pgm-skills/program-planning/scoping-framework, S04, S11]
version: 1.0
updated: 2026-10-22
---

# Intake a brief

Turns a raw brief into a structured one with clear scope, finds the weakest layer of thinking, and recommends which stages to run.

## Use when
- A project or feature starts and the brief is loose, long or mixed with solutions.
- You need to decide whether to run the full line or only some stages.

## Not for
- Long-range product vision across many projects, use `design-principles` (02).
- Prioritising between several problems, use `frame-problem` (02).

## Inputs
- The raw brief. If there is none, ask five questions: what product, what problem, for whom, by when, and how success will be judged.
- Anything already known: research, analytics, screens, brand files, constraints.

## Steps
1. Restate the problem in one sentence without solution language. If the brief names a solution, record it under "proposed solutions" and keep it out of the problem.
2. Fill the brief structure: overview, problem, audience, goals and success criteria, scope, constraints, existing inputs, deliverables and deadline.
3. Write the out-of-scope list deliberately. Name the tempting adjacent work so it cannot creep in.
4. List assumptions. Each is a hidden risk; mark which ones a stage could test.
5. Audit the seven layers of thinking and rate each Strong, Partial, Assumed, Weak, Not started or N/A: observed behaviour, domain, user needs, product strategy, conceptual model, interaction flow, surface.
6. Name the bottleneck: the lowest layer rated Weak, Assumed or Not started. Flag any layer treated as decided but rated Assumed.
7. Recommend the stages to run, in order, with one reason each. Start at the bottleneck. If a deadline argues for skipping, say what risk that carries.
8. Present the brief for gate G0 with `stage-gate`.

## Guardrails
- Do not invent users, research or numbers. Unknowns go under assumptions or open questions.
- Success criteria must be measurable or observable. "Users love it" is not a criterion.
- Keep it short enough to read in five minutes.

## Output
```
# Brief: <project>
Problem: <one sentence>
Audience: <primary, secondary>
Success criteria: <measurable>
In scope / Out of scope: <lists>
Constraints: <time, tech, brand, legal, budget>
Assumptions: <list, with "testable in stage N">
Layer audit: <table of 7 layers with ratings and notes>
Bottleneck: <layer and the risk it creates>
Stages to run: <ordered list with reasons>
Open questions: <list>
```

## Done when
- The problem statement contains no solution.
- Out of scope has at least three entries.
- A bottleneck layer is named and the stage plan starts from it.
- A person has approved G0.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-brief](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/design-brief/SKILL.md) by Marie Claire Dean (MIT)
- [layers-skills / layers-orient](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-orient/SKILL.md) by Jamie Mill (MIT)
- [ux-pgm-skills / scoping-framework](https://github.com/Owl-Listener/ux-pgm-skills/blob/main/program-planning/skills/scoping-framework/SKILL.md) by Marie Claire Dean (MIT)
- S04: [UX Research Framework](https://www.linkedin.com/posts/vitalyfriedman_ux-research-framework-pdf-httpslnkdin-share-7455888543983390720-8YU7) by Vitaly Friedman (framework by Erika Hall) (post, read: partial)
- S11: [2026 AI Product Design Stack, idea to launch](https://www.linkedin.com/posts/toqeer-ali_ai-isnt-replacing-the-design-process-most-share-7505270917539717124-IYdM) by Toqeer Ali (post, read: read)
