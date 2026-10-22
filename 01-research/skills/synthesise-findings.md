---
id: 01-research/synthesise-findings
name: Synthesise findings
stage: 01-research
fires-when: Research material exists (transcripts, notes, tickets, survey results, analytics); "make sense of this research", "what did we learn", "summarise these interviews".
inputs: [raw research in work/inputs/, work/01-research.md#plan]
output: work/01-research.md#findings, and the research section of work/05-system/UX.md
draws-on: [designer-skills/design-research/summarize-interview, designer-skills/design-research/affinity-diagram, designer-skills/design-research/qual-quant-triangulation, designer-skills/design-research/research-repository, layers-skills/layers/layers-observed-behaviour]
version: 1.0
updated: 2026-10-22
---

# Synthesise findings

Turns raw research into findings the team can trust and reuse: grounded in evidence, marked for confidence, and honest about gaps.

## Use when
- After any study, or when inheriting old research before planning new work.

## Not for
- Turning findings into needs and job stories, use `needs-and-jobs` next.

## Steps
1. **Index every source evenly.** Give each participant or source an ID (P1, P2...). Read all of them before grouping. AI tends to build themes from the first one or two transcripts; do not.
2. **Extract observations.** One per note: what someone said, did or felt, as close to verbatim as possible, tagged with source ID and the research question it speaks to. No interpretation yet.
3. **Group from the bottom up.** Cluster by recurring situations, motivations, anxieties and workarounds. Do not start with categories.
4. **Name clusters and write insight statements.** One clear sentence each, with the "so what" for design.
5. **Mark confidence.** Observed (a quotable piece of evidence supports it), inferred, or assumed. Note how many sources support each insight. Flag single-source patterns; do not discard them.
6. **Check coverage.** Every participant should appear somewhere. If one is missing, go back.
7. **Triangulate.** Where analytics and research disagree, treat the disagreement as information. Data answers what happened, how often and where; research answers why. Check both describe the same population. Weight what people did over what they said. Do not average the two into a middle finding.
8. **Flag gaps** as open questions for a follow-up plan.
9. **Prioritise** insights by their impact on decisions.
10. **Hand over.** Write findings to `01-research.md` and copy the decision-relevant ones into `UX.md` as guardrails for later stages.

## Guardrails
- Never invent quotes or participants. Every quote must exist in the source.
- Keep raw data, findings and conclusions visibly separate.
- Remove personal identifiers before findings leave the research folder.

## Output
```
## Findings
| # | Insight | Confidence | Sources (P-ids) | Design implication |
Key quotes (verbatim, with P-id)
Workarounds seen
Contradictions and how they were resolved
Gaps / open questions
```

## Done when
- Every insight has sources and a confidence level, every participant is represented, and gaps are listed.

## Sources
Rewritten in this repository's format from:
- [designer-skills / summarize-interview](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/summarize-interview/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / affinity-diagram](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/affinity-diagram/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / qual-quant-triangulation](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/qual-quant-triangulation/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / research-repository](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/research-repository/SKILL.md) by Marie Claire Dean (MIT)
- [layers-skills / layers-observed-behaviour](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-observed-behaviour/SKILL.md) by Jamie Mill (MIT)
