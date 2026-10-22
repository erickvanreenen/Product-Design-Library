---
id: 08-analysis/read-analytics
name: Read the analytics
stage: 08-analysis
fires-when: Someone asks why people drop off or what the numbers mean; "look at this dashboard", "where do users get stuck"; after launch.
inputs: [analytics exports or access, work/08-measurement.md#plan, release and campaign dates]
output: work/08-measurement.md#readout
draws-on: [designer-skills/design-research/behavioural-analytics, designer-skills/design-research/qual-quant-triangulation, S39]
version: 1.0
updated: 2026-10-22
---

# Read the analytics

Reads behavioural data carefully (checking the data before the conclusion) and turns its shape into hypotheses that research or experiments can test.

## Steps
1. **Check the data before trusting it:**
   - Read what each event actually tracks, not its name.
   - Check whether the denominator changed (traffic or acquisition shifts).
   - Check whether the funnel steps are really ordered, or users skip and return.
   - Line up releases, holidays and campaigns with any change.
   - Split by platform and segment; an average can hide one group falling and another rising.
2. **Read the shape:**
   - A cliff at one step: something is blocking (a requirement, an error, a demand for information people do not have).
   - A slope across many steps: the flow is too long overall.
   - Retention that falls then flattens: a real core of users and a weak first run.
   - Retention that keeps falling: no core yet; the value proposition is the problem.
   - Two clusters in time on task: two groups doing different things; segment before designing.
3. **Form hypotheses** that name the mechanism, and say how confident you are and why.
4. **Ask the right source.** Data answers what, how often and where. Research answers why. If data and research disagree, use `synthesise-findings` (01) triangulation.
5. **Check the size of the effect,** not only whether it is statistically significant.
6. Compare results against the success metrics and targets.

## Guardrails
- Never attribute a change to design without checking what else shipped.
- Report confidence alongside every finding.

## Output
Data checks done, the shape observed, hypotheses with confidence, results against targets and the suggested next study or experiment.

## Done when
- Each hypothesis names a mechanism and a way to test it, and results are compared with targets.

## Sources
Rewritten in this repository's format from:
- [designer-skills / behavioural-analytics](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/behavioural-analytics/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / qual-quant-triangulation](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/qual-quant-triangulation/SKILL.md) by Marie Claire Dean (MIT)
- S39: [Top 7 MCPs for product designers](https://www.linkedin.com/posts/ai-design-claudecode-share-7472622080522551297-YfIq) by Author profile not captured (post, read: read)
