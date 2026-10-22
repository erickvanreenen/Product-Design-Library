---
id: 07-qa-accessibility/accessibility-audit
name: Audit accessibility
stage: 07-qa-accessibility
fires-when: A design or build needs an accessibility check; "is this accessible", "run a WCAG audit", "check contrast and keyboard"; before release.
inputs: [screens, prototype or build, component specs]
output: work/07-qa-report.md#accessibility
draws-on: [designer-skills/design-systems/accessibility-audit, inclusive-design-skills/inclusive-interaction/keyboard-navigation, inclusive-design-skills/inclusive-interaction/touch-target-design, inclusive-design-skills/accessible-content/heading-structure, inclusive-design-skills/accessible-content/alt-text-design]
version: 1.0
updated: 2026-10-22
---

# Audit accessibility

Checks a design or build against WCAG 2.2 AA and the practical needs behind it, with each issue rated by how badly it blocks people.

## Use when
- Before handoff (on designs) and before release (on the build).

## Not for
- Scheduling sessions with disabled users, use `usability-test-plan`.

## Steps
1. **Automated pass** on every page and state (for example axe, Lighthouse, WAVE). This catches roughly a third of issues; it is the start, not the audit.
2. **Perceivable:** text alternatives for meaningful images (empty for decorative ones), captions and transcripts, contrast (4.5:1 text, 3:1 large text and interface parts), nothing by colour alone, content reflows at 400 per cent zoom and text resizes to 200 per cent, headings form a logical outline.
3. **Operable:** everything works by keyboard in visual order; focus is always visible (at least a 2 pixel outline at 3:1); focus moves into dialogs and returns afterwards; no keyboard traps; skip links and landmarks; targets at least 24 by 24 pixels on desktop and 44 by 44 on touch, with spacing; no timing without a way to extend; no flashing more than three times a second; gestures have simple alternatives.
4. **Understandable:** plain language, predictable behaviour, labels and instructions for inputs, errors identified and explained.
5. **Robust:** semantic markup, correct names, roles and states for custom components, status messages announced.
6. **Manual checks with assistive technology:** a screen reader (VoiceOver, NVDA or TalkBack), voice control, magnification, high contrast and reduced motion.
7. **Rate each issue:** critical (blocks access), major (serious difficulty), minor (workaround exists), enhancement. Record the WCAG criterion, location, who is affected and the fix.

## Guardrails
- Never claim compliance from automated tools alone.
- A decision not to fix gets a `decision-log` entry with the impact.

## Output
An issue table: severity, WCAG criterion, location, who is affected, fix, owner.

## Done when
- Automated, manual and assistive-technology passes are done, and no critical issue is open at release.

## Sources
Rewritten in this repository's format from:
- [designer-skills / accessibility-audit](https://github.com/Owl-Listener/designer-skills/blob/main/design-systems/skills/accessibility-audit/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / keyboard-navigation](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/keyboard-navigation/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / touch-target-design](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/touch-target-design/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / heading-structure](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/heading-structure/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / alt-text-design](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/alt-text-design/SKILL.md) by Marie Claire Dean (MIT)
