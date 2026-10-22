---
id: 00-governance/stage-gate
name: Run a stage gate
stage: 00-governance
fires-when: A stage finishes; before moving to the next stage; when someone asks "can we move on" or "is this ready".
inputs: [the stage's output file, the gate checklist for that stage]
output: work/decisions.md (gate entry)
draws-on: [designer-skills/design-ops/design-review-process, ai-design-skills/design-agent-orchestration/human-in-the-loop, S11, S12, S25]
version: 1.0
updated: 2026-10-22
---

# Run a stage gate

Stops the line at the end of each stage so a person checks the evidence and decides, instead of letting AI speed carry weak assumptions forward.

## Use when
- Any stage of `run-brief` ends.
- An automated loop reaches its stop condition.

## Not for
- Reviewing visual quality in depth, use `critique-screen` (06).

## Inputs
- The stage output and its gate checklist, listed below.

## Gate checklists
- **G0 Scope:** problem has no solution in it; out of scope listed; bottleneck named; stages agreed.
- **G1 Evidence:** each finding links to raw evidence; confidence stated; assumptions separated from findings.
- **G2 Direction:** more than one concept explored; selection criteria fixed before scoring; one direction chosen by a person; success metrics defined.
- **G3 Spec:** every flow lists empty, loading, error, success and edge states; copy written; AI behaviours defined where relevant.
- **G4 Look:** a person chose the visual direction; every colour pairing passes contrast in both themes; type survives 200 per cent text size.
- **G5 System:** tokens and components exist (and pass audit, for an existing system) before screens are made; DESIGN.md and UX.md tested with an AI.
- **G6 Taste:** screens use system tokens and components only; every state built; pre-delivery check passed; a person did the taste pass.
- **G7 Fixes:** each critique point accepted or rejected with a reason; deeper issues routed to the right layer.
- **G8 Ship:** no open critical accessibility or QA issues; legal applicability checked.
- **G9 Next:** results read against the success metrics; next iteration named.

## Steps
1. Load the checklist for this gate.
2. Check each item against the output. Mark pass, fail or not applicable, with the evidence.
3. Run `ai-output-check` on AI-produced content in the output.
4. Present a one-screen summary: what passed, what failed, what is assumed, and the decision needed.
5. Wait for a person to choose: proceed, proceed with named risks, rework, or stop.
6. Record the decision with `decision-log`.

## Guardrails
- An AI never passes its own gate. A person decides.
- Automated loops must have a stop condition, for example a maximum number of turns (S25).
- Scale the gate to the risk. A small fix may need only G3 and G8.

## Output
```
## Gate G<n> <name> <date>
Result: proceed | proceed with risks | rework | stop
Passed: ... Failed: ... Assumed: ...
Decided by: <person>
```

## Done when
- A named person recorded a decision, and failures have an owner.

## Sources
Rewritten in this repository's format from:
- [designer-skills / design-review-process](https://github.com/Owl-Listener/designer-skills/blob/main/design-ops/skills/design-review-process/SKILL.md) by Marie Claire Dean (MIT)
- [ai-design-skills / human-in-the-loop](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/design-agent-orchestration/human-in-the-loop/SKILL.md) by Marie Claire Dean (MIT)
- S11: [2026 AI Product Design Stack, idea to launch](https://www.linkedin.com/posts/toqeer-ali_ai-isnt-replacing-the-design-process-most-share-7505270917539717124-IYdM) by Toqeer Ali (post, read: read)
- S12: [Claude Code is terrible at design: a 9-step workflow](https://www.linkedin.com/posts/charlie-hills_claude-code-is-terrible-at-design-the-9-share-7472226424129736704-iC5A) by Charlie Hills (post, read: partial)
- S25: [Autonomous design-ops audits](https://www.linkedin.com/posts/stanislau_claudecode-productdesign-designops-share-7484931629862477824-4Fsv) by Stanislau (post, read: partial)
