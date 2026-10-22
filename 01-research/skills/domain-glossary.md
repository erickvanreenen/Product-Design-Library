---
id: 01-research/domain-glossary
name: Map the domain and glossary
stage: 01-research
fires-when: The domain is complex or unfamiliar; teams or users use different words for the same thing; before the conceptual model.
inputs: [work/01-research.md#findings, domain documents in work/inputs/]
output: work/01-research.md#domain, glossary section of work/05-system/UX.md
draws-on: [layers-skills/layers/layers-domain, S13]
version: 1.0
updated: 2026-10-22
---

# Map the domain and glossary

Maps the real-world concepts, words and processes users bring with them before any product exists, so the product's model and copy match how people think.

## Use when
- Users, staff or teams use the same word differently, or different words for the same thing.
- The space is process-heavy or regulated.

## Not for
- Deciding the product's objects and names, use `conceptual-model` (03). This step records; that one decides.

## Steps
1. Ask what domain this is, who works in it, and what they are trying to do before your product enters the picture.
2. **Harvest nouns** from research, documents and interviews. Mark each: object (many can exist, it has its own attributes, people care about it), attribute, instance or value, or unclear.
3. **Audit terminology.** For each concept: the names used, who uses which, and whether the clash is two words for one thing or one word for two things. Do not pick a winner yet.
4. **Mark the seams** where groups share words internally but differ from each other.
5. **Sketch relationships** with a simple concept map when they are unclear.
6. For process-heavy domains, list key events in past tense on a timeline ("order placed", "refund approved") with their triggers.
7. Note where this map is the team's belief rather than researched fact.
8. Write the glossary into `UX.md`: term, definition, synonyms in use, and who uses it.

## Guardrails
- Stay in the real world. Push back when the conversation turns to screens or features.
- Record contradictions; resolving them happens in the conceptual model.

## Output
Noun harvest table, terminology conflicts, seams, concept map, key events and the glossary.

## Done when
- Every conflicting term is recorded with who uses it, and the noun harvest is ready for the conceptual model.

## Sources
Rewritten in this repository's format from:
- [layers-skills / layers-domain](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-domain/SKILL.md) by Jamie Mill (MIT)
- S13: [UX.md: a design artefact for AI](https://www.linkedin.com/posts/tonyalicea_what-artifacts-do-ux-design-and-user-research-share-7490021157350367232-Li6K) by Tony Alicea (post, read: partial)
