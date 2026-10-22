---
id: 08-analysis/ai-feature-evaluation
name: Evaluate an AI feature
stage: 08-analysis
fires-when: An AI feature is live or about to launch; "is the AI getting better or worse", "how do we measure the assistant", "the model changed".
inputs: [work/03-ux-spec.md#ai-behaviour, success metrics, usage data, feedback]
output: work/08-measurement.md#ai-evaluation
draws-on: [ai-design-skills/evaluation/comparative-evaluation, ai-design-skills/evaluation/user-satisfaction-signals, ai-design-skills/evaluation/longitudinal-measurement]
version: 1.0
updated: 2026-10-22
---

# Evaluate an AI feature

Measures whether an AI feature helps people complete their tasks, how satisfied they are, and whether quality drifts over time.

## Steps
1. **Build a fixed test set:** representative real inputs (with personal data removed) and what a good result looks like for each.
2. **Score quality** with a rubric (accuracy, relevance, completeness, clarity, fit and safety) and weights suited to the feature. Calibrate with example outputs at each score.
3. **Compare versions blind:** show reviewers two outputs for the same input without saying which is which, with structured criteria and at least three reviewers.
4. **Track task success,** not just responses: completion, first-attempt success, turns, correction rate and abandonment. When quality scores and task success disagree, investigate why.
5. **Watch satisfaction signals:** explicit (ratings, comments) and implicit. Positive: using output as-is, copying it, coming back. Negative: regenerating, heavy editing, rephrasing the same request, abandoning, switching to doing it by hand.
6. **Measure over time:** rerun the test set on a schedule and after every model or prompt change. Alert on significant changes, diagnose the cause (model update, prompt change, new kinds of input, shifting expectations) and decide whether it is harm, noise or improvement.
7. **Classify failures** using the categories in `ai-output-check` (00) and fix the most frequent and severe first.

## Guardrails
- Never use real user data in test sets without consent and anonymisation.
- A single average score hides regressions in specific task types; segment.

## Output
Test set description, rubric, latest scores and trend, task success and satisfaction, failures by type and actions.

## Done when
- A fixed test set runs on a schedule, and every model or prompt change is compared against the previous version.

## Sources
Rewritten in this repository's format from:
- [ai-design-skills / comparative-evaluation](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/evaluation/comparative-evaluation/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / user-satisfaction-signals](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/evaluation/user-satisfaction-signals/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / longitudinal-measurement](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/evaluation/longitudinal-measurement/SKILL.md) by Marie Claire Dean (MIT)
