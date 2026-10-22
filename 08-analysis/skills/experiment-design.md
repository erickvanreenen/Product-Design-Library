---
id: 08-analysis/experiment-design
name: Design an experiment
stage: 08-analysis
fires-when: A change can ship to some users and traffic can decide; "should we A/B test this", "design the test".
inputs: [hypothesis from read-analytics or bets, work/08-measurement.md#plan]
output: work/08-measurement.md#experiments
draws-on: [designer-skills/prototyping-testing/a-b-test-design]
version: 1.0
updated: 2026-10-22
---

# Design an experiment

Plans an A/B or multi-variant test that can actually answer its question, or says when not to run one.

## Steps
1. **Write the hypothesis:** "If we [change], then [metric] will [move by how much] for [segment], because [reason]."
2. **Define variants:** control and one treatment that changes one thing. Add more variants only with traffic to support them.
3. **Choose one primary metric** sensitive enough to move, plus secondary and guardrail metrics.
4. **Calculate sample size and duration** before starting, from the baseline, the smallest effect worth detecting and the traffic. Run whole weeks to cover weekly patterns.
5. **Plan for known traps:** no peeking or stopping early, watch for novelty effects, segment the results, and do not run overlapping tests on the same users without a plan.
6. **For AI features:** output varies, so use larger samples; segment by task type; add side-by-side blind comparisons with structured criteria and at least three reviewers when traffic is low.
7. **Decide in advance** what result means ship, iterate or stop.

## Guardrails
- Do not stop early or change the primary metric mid-test.
- Do not run a test when:
  - Too little traffic to reach the sample size.
  - Withholding a fix would harm people (accessibility, safety, legal).
  - Foundational changes that touch everything.
  - When the question is "why", which needs research.

## Output
Hypothesis, variants, metrics, sample size, duration, analysis plan and decision rules.

## Done when
- Sample size and decision rules are written before the test starts.

## Sources
Rewritten in this repository's format from:
- [designer-skills / a-b-test-design](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/a-b-test-design/SKILL.md) by Marie Claire Dean (MIT)
