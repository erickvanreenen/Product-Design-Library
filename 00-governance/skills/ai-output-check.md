---
id: 00-governance/ai-output-check
name: Check AI output
stage: 00-governance
fires-when: Any AI-produced research summary, copy, spec, screen or code is about to be shown to a person or used by the next stage.
inputs: [the AI output, the context pack, its source material]
output: notes added to the stage output; failures logged in work/decisions.md
draws-on: [ai-design-skills/evaluation/output-quality-rubrics, ai-design-skills/evaluation/failure-taxonomy, ai-design-skills/ai-alignment-reasoning/harm-anticipation, S15]
version: 1.0
updated: 2026-10-22
---

# Check AI output

A quick, consistent quality check on anything an AI produced, before people rely on it.

## Use when
- At every gate, and whenever AI output feeds another stage.

## Not for
- Evaluating an AI feature inside the product being designed, use `ai-feature-evaluation` (08).
- Visual craft review, use `critique-screen` (06).

## Steps
1. Score five dimensions from 1 to 5: accuracy (claims verifiable, nothing invented), relevance (answers the actual task), completeness (no gaps against the inputs), clarity, and fit (tone, brand, constraints).
2. Trace claims. Every user insight, quote, number or standard must point to a source in the inputs. Mark anything without one as unverified.
3. Classify any failure: invented content, wrong detail, missing content, off-task, contradiction, wrong format, generic output, tone mismatch, or a safety or privacy issue.
4. Set severity: critical (could mislead or harm), high (would derail the next stage), medium (needs a fix), low (note it).
5. For products that affect people, ask who could be harmed, how, how likely and how severe, and write a testable mitigation for anything likely or severe.
6. Fix or return the output. Critical and high failures block the gate.

## Guardrails
- Weight accuracy highest for research and specs, fit highest for copy and UI.
- Score frequency times severity, not severity alone. Common moderate failures add up.
- Do not let the AI that produced the work be the only checker on high-stakes work.

## Output
```
AI check: accuracy n/5, relevance n/5, completeness n/5, clarity n/5, fit n/5
Unverified claims: ...
Failures: <type, severity, fix>
```

## Done when
- No critical or high failures remain, and unverified claims are labelled.

## Sources
Rewritten in this repository's format from:
- [ai-design-skills / output-quality-rubrics](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/evaluation/output-quality-rubrics/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / failure-taxonomy](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/evaluation/failure-taxonomy/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / harm-anticipation](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/harm-anticipation/SKILL.md) by Marie Claire Dean (MIT)
- S15: [7 AI concepts every product designer should know](https://www.linkedin.com/posts/mayuri-salunke-b9a19b178_uxdesign-productdesign-artificialintelligence-share-7479958806672642048-9WVs) by Mayuri Salunke (post, read: partial)
