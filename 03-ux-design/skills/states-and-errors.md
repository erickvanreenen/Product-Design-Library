---
id: 03-ux-design/states-and-errors
name: Design states, feedback and errors
stage: 03-ux-design
fires-when: Any flow or component is specified; "what does it show while loading", "write the error states", "what if it fails"; before handoff.
inputs: [work/03-ux-spec.md#flows, #model]
output: work/03-ux-spec.md#states
draws-on: [designer-skills/interaction-design/state-machine, designer-skills/interaction-design/loading-states, designer-skills/interaction-design/error-handling-ux, designer-skills/interaction-design/feedback-patterns, inclusive-design-skills/cognitive-accessibility/error-prevention-recovery]
version: 1.0
updated: 2026-10-22
---

# Design states, feedback and errors

Specifies every state a screen or component can be in, the feedback for every action, and how errors are prevented, explained and recovered from.

## Use when
- For every flow, before UI work and handoff.

## Steps
1. **List the states** per screen and component: empty (first use, no results, cleared), loading, partial, success, error, offline, disabled, and permission denied. Make impossible combinations impossible (never loading and error at once). Every state has a way out.
2. **Loading by duration:** under 0.1 s show nothing; up to 1 s a subtle change or skeleton; 1 to 10 s a clear indicator with progress if known; over 10 s progress, an estimate and the option to leave it running. Never show a blank screen. Match skeletons to real content. Avoid layout shift.
3. **Feedback for every action,** as close to the action as possible: inline first, then component, page, then system notification. Use more than colour (text, icon, shape) and make status changes announceable to screen readers. Toasts for minor confirmations disappear after 3 to 5 seconds; errors stay until fixed.
4. **Prevent errors first:** forgiving input (accept several date and phone formats, trim spaces), smart and safe defaults, constrained inputs, autosave, and asking only for what is needed.
5. **Write error messages that answer three questions:** what happened, why (if useful), and what to do now. Never blame the user. "Enter a date like 15/03/2026", not "Invalid input".
6. **Design recovery:** keep the user's input, offer retry for temporary failures, give an alternative path, and prefer undo over "are you sure?". For destructive actions, confirm with specifics: "Delete 'Project Alpha'? This removes 23 files and cannot be undone."
7. **Design empty states as guidance:** what will appear here, why it is empty, and the first action to take.

## Guardrails
- "Something went wrong" is never acceptable on its own.
- Respect reduced-motion settings for shimmer and transitions.

## Output
A state table per screen (state, trigger, what shows, what is announced, way out) and an error message list.

## Done when
- Every screen has its empty, loading, error and success states, and every error message says what to do next.

## Sources
Rewritten in this repository's format from:
- [designer-skills / state-machine](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/state-machine/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / loading-states](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/loading-states/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / error-handling-ux](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/error-handling-ux/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / feedback-patterns](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/feedback-patterns/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / error-prevention-recovery](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/error-prevention-recovery/SKILL.md) by Marie Claire Dean (MIT)
