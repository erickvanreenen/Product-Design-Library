---
id: 08-analysis/success-metrics
name: Define success metrics
stage: 08-analysis
fires-when: During ideation, before building; "how will we know it worked", "what should we measure", "set KPIs for this feature".
inputs: [work/00-brief.md success criteria, work/02-direction.md#problem and #decision]
output: work/02-direction.md#metrics, then work/08-measurement.md#plan
draws-on: [designer-skills/ux-strategy/metrics-definition, ai-design-skills/evaluation/task-success-metrics]
version: 1.0
updated: 2026-10-22
---

# Define success metrics

Chooses three to five metrics that show whether the design worked, with baselines and targets, before anything is built.

## Use when
- In the ideation stage, so the selected concept has measurable targets. Revisit in analysis.

## Not for
- Reading data that already exists, use `read-analytics`.

## Steps
1. **Start from the outcome** in the problem frame and the change in behaviour the design should cause.
2. **Pick metrics across the HEART dimensions** that fit: happiness (satisfaction, ease ratings), engagement (frequency, depth), adoption (activation, feature uptake), retention (return rate, churn), task success (completion, time, errors).
3. **Balance behaviour and attitude:** at least one measure of what people do and one of how they feel.
4. **For AI features add:** completion of the user's actual task (not just a response), first-attempt success, number of turns, how often users correct or override, and abandonment.
5. **Write each metric fully:** name, definition, how it is collected (event, survey, test), baseline, target, time frame, segment, and the hypothesis it tests.
6. **Add guardrail metrics** that must not get worse (for example support contacts, error rate, accessibility score).
7. **Check the instrumentation exists.** If not, specify the events needed in the handoff.

## Guardrails
- Three to five primary metrics. More than that and none get attention.
- No metric without a baseline; no target without a time frame.

## Output
A metric table: metric, definition, source, baseline, target, time frame, segment, hypothesis, guardrail or primary.

## Done when
- Every primary metric has a baseline, a target and a data source.

## Sources
Rewritten in this repository's format from:
- [designer-skills / metrics-definition](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/metrics-definition/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / task-success-metrics](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/evaluation/task-success-metrics/SKILL.md) by Marie Claire Dean (MIT)
