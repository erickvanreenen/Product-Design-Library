---
id: 03-ux-design/form-design
name: Design forms
stage: 03-ux-design
fires-when: Any form, sign-up, checkout or data entry; "people drop out of this form", "design the form".
inputs: [work/03-ux-spec.md#flows, #model]
output: work/03-ux-spec.md#forms
draws-on: [designer-skills/interaction-design/form-design, inclusive-design-skills/accessible-content/form-labelling]
version: 1.0
updated: 2026-10-22
---

# Design forms

Designs forms that ask for less, are easy to complete and accessible, and recover gracefully from mistakes.

## Steps
1. **Cut fields.** Remove everything not needed now; defer the rest. Each field costs completions.
2. **Single column**, with field width hinting at the expected length.
3. **Visible labels above fields**, always. Placeholder text is never the only label. Put format hints in the label or help text ("Date of birth (DD/MM/YYYY)").
4. **Mark optional fields**, not required ones; most fields should be required by design.
5. **Pick the right input:** radios for up to five visible options, a select or combobox for more, checkboxes for several choices, segmented or picker inputs for dates, masked inputs for phone and card numbers, a show-and-hide toggle for passwords.
6. **Group related fields** under headings, with fieldsets and legends for radio and checkbox groups.
7. **Validate when the user leaves a field**, not while typing. Put errors directly under the field, linked to it for screen readers. Show success where correctness is not obvious (password strength, username free). For several errors on submit, add a focusable summary at the top that links to each field.
8. **Multi-step forms:** clear progress, related questions together, back without losing data, save and continue for long forms, confirm before discarding.
9. **Accessibility:** programmatic labels, help text linked to the field, focus order matching visual order, nothing signalled by colour alone.
10. Write the copy with `ux-writing`.

## Guardrails
- Never clear the user's input on error.
- Test with real data lengths and formats, including long names and non-local addresses.

## Output
Field list (label, type, required, help, validation rule, error message), grouping, step plan.

## Done when
- Every field has a reason to exist, a visible label, a validation rule and a helpful error.

## Sources
Rewritten in this repository's format from:
- [designer-skills / form-design](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/form-design/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / form-labelling](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/form-labelling/SKILL.md) by Marie Claire Dean (MIT)
