---
id: 04-ui-design/data-visualisation
name: Design data visualisation
stage: 04-ui-design
fires-when: The product shows charts, dashboards or metrics; "which chart should we use", "design the dashboard".
inputs: [the data and the questions people ask of it, colour roles from this stage]
output: work/04-ui-spec.md#charts
draws-on: [designer-skills/ui-design/data-visualization]
version: 1.0
updated: 2026-10-22
---

# Design data visualisation

Picks the right chart for the question, encodes data honestly, and makes charts readable for everyone.

## Steps
1. **Start from the question** the viewer asks: comparison, change over time, part of a whole, distribution or relationship.
2. **Choose the chart:** bars for comparing categories, lines for trends over time, stacked bars or a single bar for parts of a whole (pie only with two or three parts), histograms or box plots for distributions, scatter for relationships. A single number with context (previous value, target) often beats a chart.
3. **Encode honestly:** bars start at zero, axes are labelled, scales stay consistent across small multiples, no 3D or decorative effects.
4. **Reduce clutter:** light grid lines, direct labels instead of legends where possible, highlight the series that matters and grey the rest.
5. **Use accessible colour:** a distinct series palette that also differs in lightness, never more than about six series, and never colour alone; add labels, patterns or shapes.
6. **Make it accessible:** a text summary of the main point, data available as a table, keyboard-reachable tooltips.
7. **Plan responsive behaviour:** simplify or switch chart type on small screens rather than shrinking.
8. **Put the summary before the detail** on dashboards: key numbers and their state first, then charts, then tables.

## Guardrails
- Never truncate an axis to exaggerate change without saying so.
- Every number shows its unit and time period.

## Output
Per chart: the question, the chart type, encodings, colours, text alternative and small-screen behaviour.

## Done when
- Each chart answers a named question and has a text alternative.

## Sources
Rewritten in this repository's format from:
- [designer-skills / data-visualization](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/data-visualization/SKILL.md) by Marie Claire Dean (MIT)
