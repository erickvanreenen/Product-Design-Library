---
id: 03-ux-design/information-architecture
name: Structure the information architecture
stage: 03-ux-design
fires-when: Organising content or features; designing navigation; "where does this live", "users cannot find X"; content volume is growing.
inputs: [work/03-ux-spec.md#model, work/01-research.md#domain, card sort or tree test data if any]
output: work/03-ux-spec.md#ia
draws-on: [designer-skills/ux-strategy/information-architecture, designer-skills/design-research/card-sort-analysis, designer-skills/interaction-design/navigation-patterns, inclusive-design-skills/cognitive-accessibility/wayfinding-navigation]
version: 1.0
updated: 2026-10-22
---

# Structure the information architecture

Organises content and features into a structure and navigation that match how users think, so they always know where they are, where they can go and how to get back.

## Use when
- New product or section, a navigation redesign, or findability complaints.

## Steps
1. **Audit what exists:** inventory screens, sections and content types. Flag orphans, duplicates and dead ends.
2. **Design from tasks inward,** not from the homepage outward or from the org chart.
3. **Define content types** from the conceptual model: attributes and relationships.
4. **Label from user language.** Use card sorts (open for new structures, closed to validate) and the glossary. Test labels with users, not colleagues.
5. **Draft the hierarchy.** Prefer moderate depth with clear labels; keep primary content within three levels.
6. **Choose navigation patterns:**
   - Mobile with three to five main destinations: bottom tab bar.
   - Desktop app with many or nested destinations: side navigation.
   - Simple site or docs: top navigation.
   - Deep hierarchy: breadcrumbs plus local side navigation.
   - Parallel views of the same content: tabs or segmented control.
   - Account, help, settings: utility navigation, kept visually separate.
   - Avoid hiding primary navigation in a hamburger menu.
7. **Design wayfinding for memory and attention limits:** page titles match the link that led there, the current location is always marked (not by colour alone), step indicators in multi-step flows, important actions within two clicks, more than one route to key content (search, browse, shortcuts).
8. **Validate** with a tree test or first-click test on key tasks before building.

## Guardrails
- Search does not replace structure; it fails when users do not know the right words.
- Navigation stays in the same place and order on every screen.

## Output
Sitemap, content types, navigation model (global, local, utility, contextual), labels with their source, and test results.

## Done when
- Every key task maps to a findable path, labels come from user language, and the structure has been tested or the test is planned.

## Sources
Rewritten in this repository's format from:
- [designer-skills / information-architecture](https://github.com/Owl-Listener/designer-skills/blob/main/ux-strategy/skills/information-architecture/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / card-sort-analysis](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/card-sort-analysis/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / navigation-patterns](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/navigation-patterns/SKILL.md) by Marie Claire Dean (MIT)
- [inclusive-design-skills / wayfinding-navigation](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/wayfinding-navigation/SKILL.md) by Marie Claire Dean (MIT)
