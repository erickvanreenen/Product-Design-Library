---
id: 01-research/research-plan
name: Plan the research
stage: 01-research
fires-when: Starting research; "what should we find out", "plan a study", "do we need interviews or a survey"; the brief's bottleneck is observed behaviour or user needs.
inputs: [work/00-brief.md, existing research or analytics in work/inputs/]
output: work/01-research.md#plan
draws-on: [layers-skills/layers/layers-observed-behaviour, designer-skills/design-research/diary-study-plan, designer-skills/design-research/survey-design, S04]
version: 1.0
updated: 2026-10-22
---

# Plan the research

Turns "we should understand users" into two or three sharp questions, checks what is already known, and picks the cheapest method that can answer them.

## Use when
- Research is needed before decisions can be made, or the team is arguing from beliefs.

## Not for
- Planning a usability test of a design, use `usability-test-plan` (07).

## Inputs
- The brief. Any existing evidence: past studies, support tickets, reviews, analytics. If there is existing material, run `synthesise-findings` on it first, then plan only for the gaps.

## Steps
1. **Get clarity.** Agree the decision this research serves, who makes it and by when. Work back from that date.
2. **List what you know and what you do not.** Separate evidence from team belief. Mark each known item observed, inferred or assumed.
3. **Brainstorm questions before methods.** Keep a running list. Research questions are not interview questions; they are what you need to learn.
4. **Pick two or three priority questions.** Prefer the ones that block work or carry the most risk. Push past "understand users better" to something specific, such as "what makes someone hesitate before inviting a colleague".
5. **Refine each question.** Do you need ideas or a description of real behaviour? Are you evaluating a solution or testing cause and effect? Qualitative or quantitative? Agree how much evidence is enough.
6. **Choose the method that produces that evidence:**
   - Why and how people behave: interviews about real past events (6 to 10 usually reach saturation), contextual observation.
   - Behaviour spread over time: diary study (8 to 15 people, 1 to 4 weeks, prompts and a plan for drop-out).
   - How many people share a need: survey (behaviour questions before attitude, under 5 minutes, about 385 responses for plus or minus 5 per cent at 95 per cent confidence).
   - Pain at scale with no recruiting: support tickets, reviews, analytics.
7. **Plan analysis before collection.** Decide how notes will be tagged (one observation per note, tied to a question) and who synthesises.
8. **Plan how findings will be shared** and where they will live (`01-research.md` and `05-system/UX.md`).

## Guardrails
- Never present planned research as findings. Never simulate participants and report them as real.
- Recruit beyond the easiest participants. Include disabled people and people in difficult contexts (see `inclusive-personas`).
- Get consent and handle personal data under local law (for example POPIA in South Africa, GDPR in Europe).

## Output
```
## Plan
Decision this serves / by when / decider
Known (with confidence) / Unknown
Priority questions (2-3)
Method per question, sample, timing, recruiting criteria
Analysis approach
Where findings will live
```

## Done when
- Each priority question has a method that can actually answer it, and an agreed bar for "enough".

## Sources
Rewritten in this repository's format from:
- [layers-skills / layers-observed-behaviour](https://github.com/jamiemill/layers-skills/blob/main/skills/layers-observed-behaviour/SKILL.md) by Jamie Mill (MIT)
- [designer-skills / diary-study-plan](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/diary-study-plan/SKILL.md) by Marie Claire Dean (MIT)
- [designer-skills / survey-design](https://github.com/Owl-Listener/designer-skills/blob/main/design-research/skills/survey-design/SKILL.md) by Marie Claire Dean (MIT)
- S04: [UX Research Framework](https://www.linkedin.com/posts/vitalyfriedman_ux-research-framework-pdf-httpslnkdin-share-7455888543983390720-8YU7) by Vitaly Friedman (framework by Erika Hall) (post, read: partial)
