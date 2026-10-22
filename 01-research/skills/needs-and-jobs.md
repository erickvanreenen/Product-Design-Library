---
id: 01-research/needs-and-jobs
name: Define needs and jobs
stage: 01-research
fires-when: After synthesis; "what are users trying to do", "write job stories", "what are the needs and pains".
inputs: [work/01-research.md#findings]
output: work/01-research.md#needs
draws-on: [designer-skills/design-research/jobs-to-be-done, layers-skills/layers/layers-user-needs, designer-skills/design-research/empathy-map]
version: 1.0
updated: 2026-10-22
---

# Define needs and jobs

Turns findings into prioritised needs, pains and desires, written as job stories that keep solutions out.

## Use when
- Findings exist and you need opportunities to build strategy on.

## Not for
- Choosing which opportunity to pursue, use `frame-problem` (02).

## Steps
1. **Settle who and when.** Name the user type and situation. If there are distinct types with different needs, work them separately.
2. **Write job stories:** "When [situation], I want to [motivation], so I can [outcome]."
   - The "when" must be picturable: an event, a feeling, a rhythm or a threshold.
   - Strip the mechanism. If the "when" or "want" names your product, feature or channel, restate it without them.
   - "I want to export to CSV" is a solution. Ask what the export is for.
3. **Cover three kinds of job:** functional (the task), emotional (how they want to feel or avoid feeling) and social (how they want to be seen). Emotional and social jobs are usually missed unless asked about directly.
4. **List pains and desires** alongside needs.
5. **Map current solutions.** What do people use or improvise now? Workarounds signal strong needs.
6. **Mark confidence** for each: observed, inferred or assumed.
7. **Prioritise roughly** by importance times how poorly it is served today. Keep it rough; precise scoring belongs in strategy.
8. Optionally, summarise as an empathy map (says, thinks, does, feels) for stakeholders, built only from evidence.

## Guardrails
- Do not let needs drift into features.
- Keep surfaced but unprioritised needs in a list so they are not lost.

## Output
```
## Needs
User type and situation:
| Job story | Type (functional/emotional/social) | Pain or desire | Current workaround | Confidence | Priority |
Contradictions between user types:
Gaps:
```

## Done when
- No job story contains a solution or product name, and each has a confidence level.

## Sources
Rewritten in this repository's format from:
- [designer-skills / jobs-to-be-done](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/jobs-to-be-done/SKILL.md) by Marie Claire Dean (MIT)
- [layers-skills / layers-user-needs](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-user-needs/SKILL.md) by Jamie Mill (MIT)
- [designer-skills / empathy-map](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/empathy-map/SKILL.md) by Marie Claire Dean (MIT)
