"""Checks the repository after a build. Exit code 1 on any failure.

- every skill has the required front matter and sections
- every skill appears in its stage README
- every skill input refers to a hand-off file written earlier in the run order (or to the brief inputs)
- no em dashes in authored markdown
- every original key in draws-on exists
- every relative markdown link points to a file that exists
"""
import json, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
idx = json.load(open(os.path.join(ROOT, "index.json"), encoding="utf-8"))
REQ_FM = ["id", "name", "stage", "fires-when", "inputs", "output", "draws-on", "version", "updated"]
REQ_SEC = ["## Steps", "## Guardrails", "## Output", "## Done when", "## Sources"]
step = {s["id"]: s.get("step") for s in idx["skills"]}
problems = []

writes = {}
for s in idx["skills"]:
    for f in re.findall(r"work/([\w./-]+?)(?:#|,|$| )", s["output"] + " "):
        writes.setdefault(f.split("#")[0].rstrip("/,"), set()).add(s.get("step"))

for s in idx["skills"]:
    path = os.path.join(ROOT, s["file"])
    text = open(path, encoding="utf-8").read()
    fm = text.split("---")[1]
    for k in REQ_FM:
        if not re.search(rf"^{re.escape(k)}:", fm, re.M):
            problems.append(f"{s['file']}: missing front matter '{k}'")
    for sec in REQ_SEC:
        if sec not in text:
            problems.append(f"{s['file']}: missing section '{sec}'")
    readme = open(os.path.join(ROOT, s["stage"], "README.md"), encoding="utf-8").read()
    if f"skills/{s['slug']}.md" not in readme:
        problems.append(f"{s['file']}: not linked from stage README")
    mine = s.get("step")
    for inp in s["inputs"]:
        m = re.search(r"work/([\w.-]+(?:/[\w.-]*)?)", inp)
        if not m or m.group(1).startswith("inputs"):
            continue
        f = m.group(1).split("#")[0].rstrip("/")
        f = f if f in writes else next((w for w in writes if w.startswith(f) or f.startswith(w)), f)
        if f not in writes:
            problems.append(f"{s['file']}: input '{inp}' is not written by any skill")
        elif mine is not None and all(w is not None and w > mine for w in writes[f]) and "if present" not in inp and "if any" not in inp:
            problems.append(f"{s['file']}: input '{inp}' is only written later in the run order")

for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
    if "—" in open(path, encoding="utf-8").read():
        problems.append(f"{os.path.relpath(path, ROOT)}: contains an em dash")

for path in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
    for link in re.findall(r"\]\(([^)#]+?)(?:#[^)]*)?\)", open(path, encoding="utf-8").read()):
        if link.startswith(("http://", "https://", "mailto:")):
            continue
        if not os.path.exists(os.path.normpath(os.path.join(os.path.dirname(path), link))):
            problems.append(f"{os.path.relpath(path, ROOT)}: broken link {link}")

keys = {o["key"] for o in idx["originals"]} | {p["id"] for p in idx["posts"]}
for s in idx["skills"]:
    for d in s["draws_on"]:
        if d not in keys:
            problems.append(f"{s['file']}: unknown source {d}")

if problems:
    print("\n".join(problems)); sys.exit(1)
print(f"ok: {len(idx['skills'])} skills checked")
