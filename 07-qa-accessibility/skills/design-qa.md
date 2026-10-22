---
id: 07-qa-accessibility/design-qa
name: Check the build against the design
stage: 07-qa-accessibility
fires-when: Something has been built; "QA this build", "does it match the design", "check for drift"; before release; on a schedule.
inputs: [the build or staging link, work/04-ui-spec.md, work/05-system/ tokens and components, work/03-ux-spec.md#states]
output: work/07-qa-report.md#design-qa
draws-on: [designer-skills/design-ops/design-qa-checklist, inclusive-design-skills/adaptive-interfaces/responsive-review, S25]
version: 1.0
updated: 2026-10-22
---

# Check the build against the design

Compares what was built with the spec and the system, and catches drift over time with scheduled checks.

## Steps
1. **Visual accuracy:** colours, type, spacing, radius, shadows and icons match tokens; no hard-coded values.
2. **Layout:** grid alignment, behaviour at each breakpoint, reflow, no clipping or unexpected overflow, safe areas respected.
3. **Interaction:** every state renders (default, hover, focus, pressed, disabled, loading, error, empty); motion matches tokens and respects reduced motion; target sizes; keyboard order and visible focus.
4. **Content:** real content fits, truncation works as specified, copy matches the copy table, no placeholder text.
5. **Responsive review:** small phone, large phone, tablet and desktop, portrait and landscape, with the largest text size.
6. **Log issues** with screenshot, expected versus actual, severity and owner.
7. **Automate drift checks** where possible: a scheduled audit comparing the build against token values and contrast rules, with a clear stop condition and a report for a person to review (S25).

## Guardrails
- An automated check reports; a person decides what ships.
- Fix the system, not just the screen, when the same drift appears in several places.

## Output
A QA log by category with severity, plus the schedule and scope of any automated drift check.

## Done when
- No high-severity mismatches remain and the release gate G8 is ready.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-qa-checklist](https://github.com/Owl-Listener/designer-skills/blob/main/design-ops/skills/design-qa-checklist/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / responsive-review](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/responsive-review/SKILL.md) by Marie Claire Dean (MIT)
- S25: [Autonomous design-ops audits](https://www.linkedin.com/posts/stanislau_claudecode-productdesign-designops-share-7484931629862477824-4Fsv) by Stanislau (post, read: partial)
