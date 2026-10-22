# Keeping the library current

The aim is a focused library: one strong skill per job, not a pile of overlapping ones.

## Change a skill

1. Edit the file in `<stage>/skills/`. Keep the shared format (`templates/skill.md`).
2. Raise `version` (1.0 to 1.1 for a fix, 2.0 for a rewrite) and set `updated`.
3. Run `python3 tools/build_repo.py`, then `python3 tools/check_repo.py`.
4. Add a line to `CHANGELOG.md`.

## Add a skill

Follow `09-workflow-tooling/skills/write-a-skill.md`. In short: search first, pick the stage by what the skill produces, write it in your own words, list every source in `draws-on`, run the build and the check.

## Replace a skill with a better approach

Rewrite the existing file rather than adding a second one, so links and the playbooks keep working. Add the new sources to `draws-on` and drop the ones no longer used. Record what changed and why in `CHANGELOG.md`. If a skill is retired, delete the file, remove it from `tools/sources.json` `stage_order`, and note it in the changelog.

## Add a source

- **A repository:** add it to `repos` in `tools/sources.json` with author, licence and URL, and add its skills to `originals`. Only adapt content whose licence allows it (MIT, Apache 2.0, CC BY); otherwise link and summarise. Add its notice to `NOTICES.md` through the build.
- **A post or article:** add it to `posts` with an ID (S47 onwards), status (read, partial, unverified) and quality (core, useful, reference, low). Summarise in your own words.

## Quality ratings for sources

- **core:** a method the stage relies on.
- **useful:** solid, narrower in scope.
- **reference:** context or a list to dip into.
- **low:** opinion, promotion or image-only. Keep only if it adds a distinct point.

## Review rhythm

Monthly: work through `sources/register.md` "Not yet read", and re-check any `unverified` source. After major AI tool changes: re-test `context-files` with the current tools.
