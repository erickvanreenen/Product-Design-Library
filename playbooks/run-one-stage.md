# Use one stage on its own

Use this when the task needs one part of the process, for example "only the research part".

1. Open the stage folder's `README.md`. It lists the skills in running order, what the stage needs and what it produces.
2. Check the stage's inputs. Each stage README has a **Running alone** section that says what to supply when the earlier stages have not run. Usually a short brief is enough.
3. Run `00-governance/skills/context-pack.md` in light mode, so the AI has the project facts.
4. Run the stage's skills in order, or only the one skill you need.
5. Finish with the stage's gate checklist and record decisions with `decision-log`.

## Common single-stage jobs

| Job | Stage | Start with |
|---|---|---|
| Plan interviews for a new feature | 01 Research | research-plan, interview-guide |
| Make sense of research notes | 01 Research | synthesise-findings |
| Choose between three ideas | 02 Ideation | select-concept |
| Map a flow with its edge cases | 03 UX design | user-flows, states-and-errors |
| Rewrite error messages | 03 UX design | ux-writing |
| Prepare a design system for AI | 05 Design systems | audit-system, context-files |
| Review a screen | 06 Critique | critique-screen |
| Check a build before release | 07 QA | design-qa, accessibility-audit |
| Work out why people drop off | 08 Analysis | read-analytics |

## Using one skill

Every skill file stands alone. Give the AI the skill file, the relevant input and the governance README. The skill's **Inputs** section says what to do if something is missing.
