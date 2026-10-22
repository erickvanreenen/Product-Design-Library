---
id: 00-governance/decision-log
name: Log a decision
stage: 00-governance
fires-when: A choice is made between options; a gate is passed; something is deliberately not done; a pattern departs from the norm.
inputs: [the decision, options considered, evidence]
output: work/decisions.md
draws-on: [designer-skills/designer-toolkit/design-rationale, inclusive-design-skills/accessibility-decisions/decision-documentation, ux-pgm-skills/cross-functional-alignment/decision-log, S07]
version: 1.0
updated: 2026-10-22
---

# Log a decision

Records what was decided and why, so settled questions stay settled and later sessions (human or AI) inherit the reasoning.

## Use when
- Two or more options were weighed, a trade-off was accepted, or something was deliberately left out.
- A gate is passed.

## Not for
- Writing a persuasive case for stakeholders, use `write-rationale` (09).

## Steps
1. Write the decision plainly and specifically.
2. Add the context: the problem and constraints that prompted it.
3. List the options considered and why each was rejected, so they are not re-proposed.
4. Cite the evidence: research findings, data, standards, test results, skill IDs.
5. State the trade-offs accepted and who they affect.
6. Name the decider and date. A decision without a decider is not one.
7. Set a revisit trigger: a date, a metric threshold or "permanent".

## Guardrails
- Log at the moment of deciding, not afterwards.
- Never record "we discussed it" as a decision.
- Accessibility trade-offs always get an entry, including decisions not to fix something.

## Output
```
## D<nn> <searchable title>
Date / Decider:
Context:
Decision:
Options rejected: <option: reason>
Evidence:
Trade-offs:
Revisit when:
```

## Done when
- Someone new could read the entry and understand why without asking.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-rationale](https://github.com/Owl-Listener/designer-skills/blob/main/designer-toolkit/skills/design-rationale/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / decision-documentation](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/decision-documentation/SKILL.md) by Marie Claire Dean (MIT)
- [ux-pgm-skills / decision-log](https://github.com/Owl-Listener/ux-pgm-skills/blob/main/cross-functional-alignment/skills/decision-log/SKILL.md) by Marie Claire Dean (MIT)
- S07: [Product Designer Agent plugin](https://www.linkedin.com/posts/waqarahmed-ux_productdesign-designsystems-claudecode-share-7467139160177274881-489q) by Waqar Ahmed (post, read: partial)
