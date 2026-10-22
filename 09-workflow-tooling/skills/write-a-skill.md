---
id: 09-workflow-tooling/write-a-skill
name: Write or update a skill
stage: 09-workflow-tooling
fires-when: Adding a new method to this repository, replacing a weaker one, or turning a repeated task into a skill; "add this to the repo", "make this a skill".
inputs: [the source material, templates/skill.md, CONTRIBUTING.md]
output: a new or updated file in <stage>/skills/
draws-on: [S31, S01]
version: 1.0
updated: 2026-10-22
---

# Write or update a skill

Adds a method to this repository in the shared format, so any AI can find it, trigger it correctly and know when it is finished.

## Steps
1. **Search first.** Check the stage folders and `index.json` for an existing skill that covers it. Improve that one rather than adding a near-duplicate.
2. **Choose the stage** by what the skill produces, not by the tool it uses.
3. **Copy `templates/skill.md`** and fill the five essentials (S31):
   - Name: the job, in plain words.
   - Fires when: the exact requests that should trigger it. A vague trigger means it is never picked.
   - Steps: in order, one action each.
   - Guardrails: what it never does, approvals and stop conditions.
   - Done when: observable proof it is finished.
4. **Add inputs and output** using the `work/` hand-off files, so it fits the run-brief playbook.
5. **Rewrite in your own words.** Do not paste a source verbatim. List every source in `draws-on` with its licence; only use sources whose licence allows adaptation, or link without copying.
6. **Mark tool-specific steps** clearly and keep the method usable with any tool.
7. **Run the build** (`python3 tools/build_repo.py`) to refresh the stage index, `index.json` and the dashboard.
8. **Record the change** in `CHANGELOG.md`. When replacing a skill, keep the old one's history in the changelog.

## Guardrails
- One skill, one job. Split skills that do two things.
- Never include instructions that tell an AI to bypass approvals, hide information or act outside the project.

## Output
The skill file, updated index and a changelog entry.

## Done when
- The build passes, the skill appears under its stage, and its trigger does not overlap another skill's.

## Sources
Rewritten in this repository's format from:
- S31: [The DNA of a Claude skill that fires](https://www.linkedin.com/posts/ericmelillo_the-dna-of-a-claude-skill-that-fires-you-share-7501255429528809472-AJXt) by Eric Melillo (post, read: partial)
- S01: [designer-skills (repo)](https://github.com/Owl-Listener/designer-skills) by Owl-Listener (repo, read: partial)
