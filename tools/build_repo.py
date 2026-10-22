"""Rebuilds the generated parts of the repository.

Source of truth:
  - each skill file in <stage>/skills/*.md (front matter + body)
  - tools/sources.json (repos, original skills, posts, backlog)
Generated: the Sources section of each skill, stage READMEs, sources/*.md, NOTICES.md,
templates/work/*, index.json, dashboard.html and tools/dashboard.artifact.html.

Run from anywhere:  python3 tools/build_repo.py
"""
import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S = json.load(open(os.path.join(ROOT, "tools", "sources.json"), encoding="utf-8"))
for _o in S["originals"]:
    _o["desc"] = re.sub(r"\s*\u2014\s*", ": ", _o["desc"]).replace("\u2013", "-")
ORIG = {o["key"]: o for o in S["originals"]}
POSTS = {p["id"]: p for p in S["posts"]}
REPOS = S["repos"]

# The run order for a full brief. A stage folder can appear in more than one step (UI design does).
PIPELINE = [
 {"step": 0, "title": "Intake", "stage": "00-governance", "skills": ["intake-brief", "context-pack"], "writes": "work/00-brief.md, work/context/",
  "gate": "G0 Scope", "checks": ["Problem stated without a solution", "Out of scope listed", "Bottleneck layer named", "Stages to run agreed by a person"]},
 {"step": 1, "title": "Research", "stage": "01-research", "skills": ["research-plan", "interview-guide", "synthesise-findings", "needs-and-jobs", "inclusive-personas", "journey-map", "competitive-scan", "domain-glossary"],
  "writes": "work/01-research.md", "gate": "G1 Evidence", "checks": ["Each finding links to raw evidence", "Confidence stated for each finding", "Assumptions separated from findings", "Gaps listed"]},
 {"step": 2, "title": "Ideation", "stage": "02-ideation", "skills": ["frame-problem", "assumptions-and-bets", "design-principles", "explore-concepts", "select-concept", "08-analysis/success-metrics"],
  "writes": "work/02-direction.md", "gate": "G2 Direction", "checks": ["More than one concept explored", "Criteria fixed before scoring", "One direction chosen by a person", "Success metrics defined"]},
 {"step": 3, "title": "UX design", "stage": "03-ux-design", "skills": ["conceptual-model", "information-architecture", "user-flows", "states-and-errors", "form-design", "ux-writing", "ai-experience", "wireframe-spec"],
  "writes": "work/03-ux-spec.md", "gate": "G3 Spec", "checks": ["Every flow lists empty, loading, error, success and edge states", "Copy written in the agreed vocabulary", "AI behaviour defined where relevant", "Works without a mouse"]},
 {"step": 4, "title": "UI foundations", "stage": "04-ui-design", "skills": ["visual-direction", "layout-and-spacing", "typography", "colour", "motion"],
  "writes": "work/04-ui-spec.md (direction, layout, type, colour, motion)", "gate": "G4 Look", "checks": ["A person chose the visual direction", "Every colour pairing passes contrast in both themes", "Type survives 200 per cent text size"]},
 {"step": 5, "title": "Design system", "stage": "05-ai-design-systems", "skills": ["audit-system", "design-tokens", "component-spec", "context-files", "design-tool-sync", "system-governance"],
  "writes": "work/05-system/", "gate": "G5 System", "checks": ["Tokens and components exist before screens", "Audit verdict recorded (existing systems)", "DESIGN.md and UX.md tested with an AI"]},
 {"step": 6, "title": "Screens", "stage": "04-ui-design", "skills": ["visual-hierarchy", "data-visualisation", "compose-screen"],
  "writes": "work/04-ui-spec.md (hierarchy, charts, screens)", "gate": "G6 Taste", "checks": ["Screens use system tokens and components only", "Every state built", "Pre-delivery check passed", "Taste pass done by a person"]},
 {"step": 7, "title": "Critique", "stage": "06-design-critique", "skills": ["critique-screen", "heuristic-review", "coherence-check", "slop-check", "critique-session"],
  "writes": "work/06-critique.md", "gate": "G7 Fixes", "checks": ["Each point accepted or rejected with a reason", "Deeper issues routed to the right layer"]},
 {"step": 8, "title": "QA and accessibility", "stage": "07-qa-accessibility", "skills": ["accessibility-audit", "cognitive-load-check", "compliance-check", "usability-test-plan", "design-qa"],
  "writes": "work/07-qa-report.md", "gate": "G8 Ship", "checks": ["No open critical accessibility issues", "No high-severity design QA issues", "Legal applicability checked"]},
 {"step": 9, "title": "Analysis", "stage": "08-analysis", "skills": ["read-analytics", "experiment-design", "ai-feature-evaluation", "impact-report"],
  "writes": "work/08-measurement.md", "gate": "G9 Next", "checks": ["Results read against targets", "Attribution stated honestly", "Next iteration named"]},
]
STEP_OF = {}
for p in PIPELINE:
    for k in p["skills"]:
        STEP_OF[k if "/" in k else f"{p['stage']}/{k}"] = p["step"]

STAGES = [
 {"id": "00-governance", "title": "Governance", "purpose": "Rules that apply to every stage: intake, context, gates, decisions and checks on AI output.",
  "output": "work/00-brief.md, work/context/, work/decisions.md", "note": "`stage-gate`, `decision-log` and `ai-output-check` run at every gate.",
  "alone": "Run `intake-brief` on any new request, even a small one. `context-pack` in light mode needs only the brief."},
 {"id": "01-research", "title": "Research", "purpose": "What is true about users, their domain and the market, with confidence marked.",
  "output": "work/01-research.md, research and glossary sections of UX.md",
  "alone": "Needs only a short brief: the decision the research serves and by when. Existing notes or transcripts go to `synthesise-findings` first."},
 {"id": "02-ideation", "title": "Ideation and strategy", "purpose": "Which problem to solve, which bets to place, and which direction to take, chosen on criteria set in advance.",
  "output": "work/02-direction.md", "alone": "Needs a problem and some evidence. Without research, mark every opportunity as assumed and plan the cheapest test."},
 {"id": "03-ux-design", "title": "UX design", "purpose": "How it works: the model, structure, flows, states, forms, words and AI behaviour.",
  "output": "work/03-ux-spec.md", "alone": "Needs the job story and the chosen direction. For a small change, start at `user-flows` and `states-and-errors`."},
 {"id": "04-ui-design", "title": "UI design", "purpose": "How it looks: direction, layout, type, colour and motion first; then hierarchy, charts and finished screens on top of the design system.",
  "output": "work/04-ui-spec.md and screens", "note": "Runs in two parts: foundations before the design system, screens after it.",
  "alone": "Foundations need the brief and brand files. Screens need wireframes or a clear description, and the design system if one exists."},
 {"id": "05-ai-design-systems", "title": "AI-ready design systems", "purpose": "The source of truth AI builds from: tokens, components, DESIGN.md and UX.md.",
  "output": "work/05-system/ (tokens.json, components/, DESIGN.md, UX.md)",
  "alone": "For an existing product start with `audit-system`. For a new one, run the UI foundations first, then `design-tokens`."},
 {"id": "06-design-critique", "title": "Design critique", "purpose": "Is it good, is it coherent with what was decided underneath, and does it avoid AI slop.",
  "output": "work/06-critique.md", "alone": "Needs only the screen or flow, plus the goal it serves. Principles and DESIGN.md make the review sharper."},
 {"id": "07-qa-accessibility", "title": "QA and accessibility", "purpose": "Does it work for everyone, as specified, within the law.",
  "output": "work/07-qa-report.md", "alone": "Needs the design or build. Accessibility and design QA can run on any existing product."},
 {"id": "08-analysis", "title": "Analysis and measurement", "purpose": "Did it work, why, and what to do next.",
  "output": "work/08-measurement.md", "alone": "`read-analytics` needs only data access and release dates. `success-metrics` runs during ideation (step 2)."},
 {"id": "09-workflow-tooling", "title": "Workflow and tooling", "purpose": "Setting up projects, handing off, explaining decisions and extending this repository.",
  "output": "project set-up, work/handoff.md, rationale, new skills", "alone": "Use any skill here on its own at any time."},
]
for st in STAGES:
    st["steps"] = [p["step"] for p in PIPELINE if p["stage"] == st["id"]]
    st["gates"] = [{"gate": p["gate"], "title": p["title"], "checks": p["checks"]} for p in PIPELINE if p["stage"] == st["id"]]
SBY = {s["id"]: s for s in STAGES}
FOLDER_ORDER = [s["id"] for s in sorted(STAGES, key=lambda s: s["id"])]


def parse_skill(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    fm, body = m.groups()
    meta = {}
    for line in fm.split("\n"):
        k, _, v = line.partition(":")
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            v = [x.strip() for x in v[1:-1].split(",") if x.strip()]
        meta[k.strip()] = v
    body = re.split(r"\n## Sources\n", body)[0].rstrip()
    first = re.search(r"^# .+\n\n(.+?)\n", body, re.M)
    meta["summary"] = first.group(1).strip() if first else ""
    steps = re.search(r"\n## Steps\n(.*?)(\n## |\Z)", body, re.S)
    meta["steps"] = [re.sub(r"\*\*(.+?)\*\*", r"\1", l.strip())[3:].strip() for l in (steps.group(1).split("\n") if steps else []) if re.match(r"^\d+\. ", l.strip())]
    return fm, body, meta


def source_line(key):
    if key in POSTS:
        p = POSTS[key]
        return f"- {key}: [{p['title']}]({p['url']}) by {p['author']} ({p['type']}, read: {p['status']})"
    o = ORIG[key]; r = REPOS[o["repo"]]
    return f"- [{o['repo']} / {o['name']}]({o['url']}) by {r['author']} ({r['licence']})"


def write(rel, text):
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, "w", encoding="utf-8").write(text.rstrip() + "\n")


skills = []
for stage in FOLDER_ORDER:
    order = S["stage_order"].get(stage, [])
    files = sorted(glob.glob(os.path.join(ROOT, stage, "skills", "*.md")),
                   key=lambda p: (order.index(os.path.basename(p)[:-3]) if os.path.basename(p)[:-3] in order else 99, p))
    for i, path in enumerate(files, 1):
        fm, body, meta = parse_skill(path)
        draws = meta.get("draws-on", [])
        missing = [d for d in draws if d not in ORIG and d not in POSTS]
        if missing:
            raise SystemExit(f"{path}: unknown sources {missing}")
        src = "\n".join(source_line(d) for d in draws)
        open(path, "w", encoding="utf-8").write(f"---\n{fm}\n---\n{body}\n\n## Sources\nRewritten in this repository's format from:\n{src}\n")
        name = os.path.basename(path)[:-3]
        skills.append({"id": meta["id"], "file": f"{stage}/skills/{name}.md", "slug": name, "stage": stage, "order": i, "step": STEP_OF.get(meta["id"]),
                       "name": meta.get("name", name), "summary": meta["summary"], "fires_when": meta.get("fires-when", ""),
                       "inputs": meta.get("inputs", []), "output": meta.get("output", ""), "steps": meta["steps"],
                       "draws_on": draws, "version": meta.get("version", ""), "updated": meta.get("updated", "")})

# references
refs = []
for path in sorted(glob.glob(os.path.join(ROOT, "references", "*.md"))):
    if path.endswith("README.md"):
        continue
    fm, body, meta = parse_skill(path)
    draws = meta.get("draws-on", [])
    open(path, "w", encoding="utf-8").write(f"---\n{fm}\n---\n{body}\n\n## Sources\nRewritten from:\n" + "\n".join(source_line(d) for d in draws) + "\n")
    refs.append({"file": "references/" + os.path.basename(path), "name": meta.get("name"), "draws_on": draws})

# stage READMEs
for st in STAGES:
    mine = [s for s in skills if s["stage"] == st["id"]]
    further = [o for o in S["originals"] if o["stage"] == st["id"] and not o["used_by"]]
    posts = sorted({d for s in mine for d in s["draws_on"] if d in POSTS})
    lines = [f"# {st['title']}", "", st["purpose"], ""]
    if st["steps"]:
        lines += [f"**Position in the line:** step {' and '.join(str(n) for n in st['steps'])} of `playbooks/run-brief.md`.  ", f"**Writes:** {st['output']}  ",
                  f"**Gate:** {', '.join(g['gate'] for g in st['gates'])}", ""]
    else:
        lines += [f"**Writes:** {st['output']}", ""]
    if st.get("note"):
        lines += [st["note"], ""]
    lines += ["## Running this stage alone", "", st["alone"], "", "## Skills, in running order", "", "| # | Skill | Step | Use when |", "|---|---|---|---|"]
    for s in mine:
        lines.append(f"| {s['order']} | [{s['name']}](skills/{s['slug']}.md) | {s['step'] if s['step'] is not None else 'any'} | {s['fires_when']} |")
    for g in st["gates"]:
        lines += ["", f"## Gate checklist: {g['gate']} ({g['title']})", ""] + [f"- [ ] {c}" for c in g["checks"]]
    if posts:
        lines += ["", "## Posts and articles that informed this stage", ""] + [source_line(p) for p in posts]
    if further:
        lines += ["", "## More skills in the original repositories", "",
                  "Not rewritten here, either because a consolidated skill covers most of it or because it is specialist. Use them directly when you need the depth.", ""]
        for o in sorted(further, key=lambda o: (o["repo"], o["plugin"], o["name"])):
            lines.append(f"- [{o['repo']} / {o['name']}]({o['url']}): {o['desc']}")
    lines += ["", "Back to the [index](../README.md)."]
    write(f"{st['id']}/README.md", "\n".join(lines))

# sources/register.md (posts) and sources/repos.md
reg = ["# Posts and articles", "", "Every post, article and site from the WhatsApp collection that was read. Quality: core, useful, reference, low. Status: how much was read.", "",
       "| ID | Source | Author | Quality | Status | Used by |", "|---|---|---|---|---|---|"]
for p in S["posts"]:
    users = [s["slug"] for s in skills if p["id"] in s["draws_on"]]
    reg.append(f"| {p['id']} | [{p['title']}]({p['url']}) | {p['author']} | {p['quality']} | {p['status']} | {', '.join(users) or '-'} |")
reg += ["", "## Flags", ""] + [f"- **{p['id']}**: {' '.join(p['flags'])}" for p in S["posts"] if p["flags"]]
reg += ["", "## Not yet read", ""] + [f"- [{b['title']}]({b['url']})" for b in S["backlog"]]
reg += ["", "## Unavailable", ""] + [f"- {d['title']}: {d['reason']}" for d in S["dead"]]
write("sources/register.md", "\n".join(reg))

rep = ["# Source repositories", "", "Repositories whose skills were read and consolidated. All are MIT licensed; see NOTICES.md.", "",
       "| Repository | Author | Skills read | Used in consolidated skills | Covers |", "|---|---|---|---|---|"]
for k, r in REPOS.items():
    mine = [o for o in S["originals"] if o["repo"] == k]
    rep.append(f"| [{k}]({r['url']}) | {r['author']} | {len(mine)} | {sum(1 for o in mine if o['used_by'])} | {r['summary']} |")
rep += ["", "## Original to consolidated map", "", "| Original skill | Consolidated into |", "|---|---|"]
for o in S["originals"]:
    if o["used_by"]:
        rep.append(f"| [{o['repo']} / {o['name']}]({o['url']}) | {', '.join(o['used_by'])} |")
write("sources/repos.md", "\n".join(rep))

MIT = ("Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the \"Software\"), "
       "to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, "
       "and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\n"
       "The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\n"
       "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, "
       "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER "
       "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
notice = ["# Third-party notices", "", "Skills in this repository are rewritten from, and `references/ui-data/` copies data from, the MIT-licensed works below. "
          "Each is used under the MIT licence, reproduced once at the end.", ""]
holders = {}
for k, r in REPOS.items():
    if k == "design-leadership-skills":
        continue
    holders.setdefault((r["author"], r["year"]), []).append(f"[{k}]({r['url']})")
for (a, y), rs in holders.items():
    notice.append(f"- Copyright (c) {y} {a}: {', '.join(rs)}")
notice += ["", "Post and article sources are linked, summarised in our own words and not copied.", "", "## MIT licence", "", MIT]
write("NOTICES.md", "\n".join(notice))

# work templates
WORK = {
 "00-brief.md": ["Brief", ["Problem", "Audience", "Success criteria", "In scope", "Out of scope", "Constraints", "Assumptions", "Layer audit", "Bottleneck", "Stages to run", "Open questions"]],
 "01-research.md": ["Research", ["Plan", "Interview guide", "Findings", "Needs", "Personas", "Journeys", "Competitors", "Domain"]],
 "02-direction.md": ["Direction", ["Problem", "Bets", "Principles", "Concepts", "Decision", "Metrics"]],
 "03-ux-spec.md": ["UX spec", ["Model", "IA", "Flows", "States", "Forms", "Copy", "AI behaviour", "Wireframes"]],
 "04-ui-spec.md": ["UI spec", ["Direction", "Layout", "Type", "Colour", "Hierarchy", "Motion", "Charts", "Screens"]],
 "06-critique.md": ["Critique", ["Screens", "Heuristics", "Coherence", "Slop", "Session"]],
 "07-qa-report.md": ["QA report", ["Accessibility", "Cognitive load", "Compliance", "Usability plan", "Design QA"]],
 "08-measurement.md": ["Measurement", ["Plan", "Readout", "Experiments", "AI evaluation", "Impact"]],
 "decisions.md": ["Decisions", []],
}
for f, (title, secs) in WORK.items():
    owners = {}
    for s in skills:
        if s["output"].startswith("work/" + f):
            for sec in re.findall(r"#([a-z-]+)", s["output"]):
                owners.setdefault(sec, []).append(s["id"])
    body = [f"# {title}", "", "Filled by the skills named under each heading. Cite skill IDs used.", ""]
    for sec in secs:
        anchor = sec.lower().replace(" ", "-")
        who = owners.get(anchor, [])
        body += [f"## {sec}", f"<!-- written by: {', '.join(who) if who else 'see playbooks/run-brief.md'} -->", ""]
    if f == "decisions.md":
        body += ["<!-- One entry per decision, in the decision-log format. Gate results go here too. -->"]
    write(f"templates/work/{f}", "\n".join(body))
write("templates/work/05-system/README.md", "# Design system hand-off\n\nWritten by stage 05: `tokens.json`, `components/`, `DESIGN.md`, `UX.md`, `audit.md`, `governance.md`, `sync-log.md`.")
write("templates/work/context/README.md", "# Context pack\n\nWritten by `00-governance/context-pack`: `project.md` plus pointers to DESIGN.md and UX.md.")

# ui-data README
write("references/ui-data/README.md", "# UI reference data\n\nSearchable tables copied from [ui-ux-pro-max-skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) by Next Level Builder (MIT; see NOTICES.md). "
      "Any AI can read these CSV files directly; no tool needed. Used mainly by `04-ui-design/visual-direction`.\n\n"
      "| File | What it holds |\n|---|---|\n| products.csv | Product types and the styles and patterns that suit them |\n| styles.csv | UI styles with colours, effects, best and worst uses, accessibility notes |\n"
      "| colors.csv | Palettes by product type |\n| typography.csv | Font pairings with mood and use |\n| ui-reasoning.csv | Rules linking product, style, colour and type choices |\n"
      "| ux-guidelines.csv | Do and do-not UX rules with severity |\n| landing.csv | Landing page patterns |\n| charts.csv | Chart types by data question |\n| motion.csv | Motion patterns |\n| app-interface.csv | App interface patterns |\n\n"
      "Treat the data as suggestions to choose from, then record the choice in DESIGN.md.")

# index.json
index = {"generated": S["generated"], "pipeline": PIPELINE, "stages": STAGES, "skills": skills, "references": refs,
         "repos": REPOS, "originals": S["originals"], "posts": S["posts"], "backlog": S["backlog"], "dead": S["dead"]}
write("index.json", json.dumps(index, indent=1, ensure_ascii=False))

# dashboard
tpl = open(os.path.join(ROOT, "tools", "dashboard.template.html"), encoding="utf-8").read()
slim = {"generated": S["generated"], "pipeline": PIPELINE, "stages": STAGES, "skills": skills, "repos": REPOS, "posts": S["posts"],
        "originals": [{k: o[k] for k in ("key", "repo", "name", "url", "desc", "stage", "used_by")} for o in S["originals"]],
        "backlog": S["backlog"], "dead": S["dead"]}
body = tpl.replace("/*DATA*/", json.dumps(slim, ensure_ascii=False).replace("</", "<\\/"))
open(os.path.join(ROOT, "tools", "dashboard.artifact.html"), "w", encoding="utf-8").write(body)
open(os.path.join(ROOT, "dashboard.html"), "w", encoding="utf-8").write(
    "<!doctype html>\n<html lang=\"en-GB\">\n<head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
print(f"built {len(skills)} skills, {len(refs)} references, {len(S['originals'])} originals indexed")
