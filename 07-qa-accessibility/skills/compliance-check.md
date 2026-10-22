---
id: 07-qa-accessibility/compliance-check
name: Check legal accessibility requirements
stage: 07-qa-accessibility
fires-when: Planning or releasing a product; "which accessibility laws apply", "do we need to meet WCAG"; entering a new market.
inputs: [work/00-brief.md (markets, audience, sector)]
output: work/07-qa-report.md#compliance
draws-on: [inclusive-design-skills/accessibility-decisions/compliance-mapping, S26]
version: 1.0
updated: 2026-10-22
---

# Check legal accessibility requirements

Works out which accessibility rules apply to this product, based on where its users are, who they are and what it does, and maps design decisions to the criteria behind them. This is guidance for design decisions, not legal advice.

## Steps
1. **List the facts:** countries and regions served, sector (public, banking, transport, e-commerce, health), product type (website, app, kiosk, document), organisation size, and whether it sells to the public or to businesses.
2. **Identify likely frameworks** and confirm each with the legal owner. Common ones: WCAG 2.2 AA as the usual technical baseline; the European Accessibility Act, in force since 28 June 2025, with EN 301 549 as its standard; the ADA and Section 508 in the United States; the Equality Act and public sector accessibility regulations in the UK. For other regions, including South Africa, check current local law and procurement rules; do not assume.
3. **Map design decisions to criteria,** for example: contrast to 1.4.3 and 1.4.11, colour not the only signal to 1.4.1, resize and reflow to 1.4.4 and 1.4.10, keyboard to 2.1.1, focus visible to 2.4.7, target size to 2.5.8, labels to 3.3.2, error identification to 3.3.1, name, role and value to 4.1.2.
4. **Note obligations beyond the interface:** an accessibility statement, a feedback route, accessible documents and support channels.
5. **Record gaps and decisions** with `decision-log`.

## Guardrails
- Laws change. Date this check and re-run it for new markets.
- Have a qualified person confirm legal conclusions.

## Output
Applicable frameworks with confidence and source, a decision-to-criterion map, obligations and open questions for legal review.

## Done when
- Each market has a confirmed or flagged framework, and the target standard is agreed.

## Sources
Rewritten in this repository's format from:
- [inclusive-design-skills / compliance-mapping](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/compliance-mapping/SKILL.md) by Marie Claire Dean (MIT)
- S26: [Digital accessibility laws for UX designers](https://www.uxdesigninstitute.com/blog/digital-accessibility-laws-for-ux/) by UX Design Institute (post, read: partial)
