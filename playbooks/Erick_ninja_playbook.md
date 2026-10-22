# Erick's ninja playbook

Erick Van Reenen's product design process, step for step in his order, with the library working underneath every step. The route is his; the library adds the depth, the rigour and the finish.

The signature: **start from the whole platform, not the screen.** Before anything is drawn, the whole system is mapped, the feature is placed inside it, and every knock-on effect is traced. Everything after that is better because nothing downstream comes as a surprise.

## How to run it

- **With an AI:** give it this file, `AGENTS.md` and the brief, and say "Run Erick_ninja_playbook on this brief. Stop at every checkpoint." It works step by step, writes each output into the project's `work/` folder, and waits for Erick at each checkpoint.
- **By hand:** use each step's moves and skill links as a checklist.
- **Set-up:** copy `templates/work/` into the project as `work/`, and put the brief, screenshots, sitemaps, analytics, brand files and any Figma links in `work/inputs/`. Run `00-governance/skills/context-pack.md` once so the AI knows the project.

Who does what throughout: **the AI drafts, maps, checks and prepares. Erick decides.** Every checkpoint is a decision only Erick (or the client) makes. `00-governance/skills/ai-output-check.md` runs on anything the AI produces before Erick sees it, and `00-governance/skills/decision-log.md` records each decision in `work/decisions.md`.

## The route at a glance

| Phase | Steps | Checkpoint |
|---|---|---|
| 1. Read the landscape | 1 Map the platform, 2 Place the feature, 3 Map the feature | A: Landscape locked |
| 2. Research | 4 Benchmark and tear down, 5 Best practice and domain language, 6 Consolidate into a direction | B: Direction set |
| 3. Define | 7 Refine the brief | C: Brief signed off |
| 4. Design | 8 First wireframes, 9 High-fidelity prototype, 10 Refine the prototype | D: Prototype happy |
| 5. Build and hand over | 11 Figma frames and/or prototype to dev | |
| 6. Check and polish | 12 Check against the brief, 13 Critique, 14 Update, 15 Align to the design system | E: Ready to show |
| 7. Present | 16 Client presentation | F: Client decision |

---

## Phase 1. Read the landscape

### Step 1. Map the platform

**Goal:** one simple page showing the whole platform: its zones and the main streams of information between them.

**Moves**
- Walk every top-level area and every way in (web, app, email, notifications, support, staff tools).
- Name the few main objects the platform revolves around.
- Group into five to seven zones named in the user's language; draw labelled streams of information between them; mark outside systems, behind-the-scenes teams and the source of truth for each main object.
- Simplify until it reads in ten seconds.

**Library:** [platform-map](../03-ux-design/skills/platform-map.md) (lead), [conceptual-model](../03-ux-design/skills/conceptual-model.md) (object test), [domain-glossary](../01-research/skills/domain-glossary.md) (zone names), [journey-map](../01-research/skills/journey-map.md) (only for service-heavy platforms, using the blueprint lanes).

**Produces:** `work/00-landscape.md#platform`: the visual map and a text (Mermaid) version.

**Bar:** a newcomer explains the platform back in one sentence; every main object has one source of truth; unknowns are listed with who can answer.

**Ninja move:** always produce the map twice, as a visual for people and as text for AI. From then on every AI in the project shares Erick's picture of the system, and its output stops ignoring how the platform actually works.

### Step 2. Place the feature and trace the ripples

**Goal:** know exactly where the feature sits, what it depends on, what depends on it, and what changes two and three steps away.

**Moves**
- Pin the feature to its zone and list the objects it reads, creates, changes or deletes.
- Trace upstream (what it needs, who owns it, hard or soft) and downstream (what uses its output).
- Find co-dependencies with other features that touch the same objects.
- Run the ripple test: first, second and third order effects for every change. Score and assign owners.
- Check early ripples that carry legal or accessibility weight.

**Library:** [feature-placement](../03-ux-design/skills/feature-placement.md) (lead), [compliance-check](../07-qa-accessibility/skills/compliance-check.md) (legal ripples), [ai-output-check](../00-governance/skills/ai-output-check.md) harm questions (if the feature uses AI), [decision-log](../00-governance/skills/decision-log.md).

**Produces:** `work/00-landscape.md#placement`: placement diagram, ripple table, brief impacts.

**Bar:** every hard dependency has an owner; every high-severity ripple has a response; the brief impacts are written down.

**Ninja move:** talk to the owners of the top three downstream ripples now, not at hand-off. Problems found here cost a conversation; found at build, they cost a sprint.

### Step 3. Map the feature's own structure

**Goal:** the feature's internal hierarchy: its objects, states, structure and navigation, within its own boundary.

**Moves**
- Define the feature's objects, their attributes, relationships and actions; one name per concept.
- Draw state diagrams for anything whose status changes what users can do.
- Build the feature's hierarchy and navigation from tasks inward; check labels against the glossary.
- Sketch the skeleton of the key flows as text (places, actions, destinations) without visuals.

**Library:** [conceptual-model](../03-ux-design/skills/conceptual-model.md), [information-architecture](../03-ux-design/skills/information-architecture.md) (scoped to the feature), [user-flows](../03-ux-design/skills/user-flows.md) (skeleton only).

**Produces:** `work/03-ux-spec.md#model` and `#ia` (feature level).

**Bar:** every object traces to a need in the brief; every stateful object has states with a way out; no concept has two names.

**Ninja move:** state diagrams before screens. Most "edge cases" found late are states nobody drew.

> **Checkpoint A: Landscape locked.** Erick confirms the platform map, the placement and ripple owners, and the feature structure. Recorded with [stage-gate](../00-governance/skills/stage-gate.md).

---

## Phase 2. Research

### Step 4. Competitive analysis, benchmarking and interaction teardown

**Goal:** learn from the best at both levels: the big flows (macro) and the small moments (micro).

**Moves**
- Pick direct competitors, indirect ones and one best-in-class product from another field.
- Compare whole journeys for the feature's key tasks; score them.
- Tear down three to five products: macro flow tables, then micro moments (trigger, rules, feedback, timing, repeat, accessibility).
- Turn every strong moment into a principle in your own words; spot table stakes, shared gaps and signature moments.

**Library:** [competitive-scan](../01-research/skills/competitive-scan.md), [interaction-teardown](../01-research/skills/interaction-teardown.md) (lead), [references/perception.md](../references/perception.md), [references/ux-laws.md](../references/ux-laws.md).

**Produces:** `work/01-research.md#competitors` and `#teardown`.

**Bar:** each studied flow has a macro table; at least three micro moments are specified; principles are written, not screenshots pasted.

**Ninja move:** hunt for the shared gap, the thing every competitor does badly. That becomes the signature moment the client remembers.

### Step 5. Best practice and domain language

**Goal:** know what good looks like in this field and speak the domain's language fluently.

**Moves**
- Harvest the domain's terms from competitors, documents, support tickets and users; record conflicts rather than resolving them yet.
- Pull the relevant best practice: UX laws, perception principles, interaction patterns, accessibility rules and any legal requirements.
- If users can be reached, run a short research round: plan, interview, synthesise. If not, mine reviews and support tickets.
- Build inclusive personas or at least context-of-use notes, including situational limits.

**Library:** [domain-glossary](../01-research/skills/domain-glossary.md), [research-plan](../01-research/skills/research-plan.md), [interview-guide](../01-research/skills/interview-guide.md), [inclusive-personas](../01-research/skills/inclusive-personas.md), [references/ui-data/ux-guidelines.csv](../references/ui-data/ux-guidelines.csv), [compliance-check](../07-qa-accessibility/skills/compliance-check.md).

**Produces:** `work/01-research.md#domain`, `#plan`, `#personas`; the glossary in `work/05-system/UX.md`.

**Bar:** a glossary exists with who uses which term; every best practice cited applies to this feature.

**Ninja move:** write the glossary into UX.md on day one. Every screen, label and AI output from then on speaks the client's language, which is often the first thing a client notices.

### Step 6. Consolidate into a direction

**Goal:** turn everything learned into one clear starting direction.

**Moves**
- Synthesise all evidence evenly, mark confidence, and triangulate data against research.
- Write the needs as job stories; frame the problem against one measurable outcome.
- Set three to five ranked design principles.
- Sketch two or three genuinely different directions quickly, then choose on criteria written before comparing.

**Library:** [synthesise-findings](../01-research/skills/synthesise-findings.md), [needs-and-jobs](../01-research/skills/needs-and-jobs.md), [frame-problem](../02-ideation/skills/frame-problem.md), [design-principles](../02-ideation/skills/design-principles.md), [explore-concepts](../02-ideation/skills/explore-concepts.md), [select-concept](../02-ideation/skills/select-concept.md).

**Produces:** `work/01-research.md#findings`, `#needs`; `work/02-direction.md`.

**Bar:** every insight links to evidence; criteria were fixed before choosing; the chosen direction states what it costs.

**Ninja move:** keep the rejected directions with why they lost. When the client asks "did you consider...", the answer is already on the table.

> **Checkpoint B: Direction set.** Erick chooses the direction.

---

## Phase 3. Define

### Step 7. Refine the brief

**Goal:** a brief rebuilt on evidence: sharper problem, real constraints, measurable success.

**Moves**
- Restate the problem without a solution; update audience, constraints, scope and out of scope from steps 1 to 6.
- Add the dependencies and ripples that change scope, and the teams involved.
- Name the riskiest assumptions and how they will be tested.
- Set three to five success metrics with baselines and targets.
- Update the AI context pack so every later step works from the refined brief.

**Library:** [intake-brief](../00-governance/skills/intake-brief.md) (re-run as a refinement), [assumptions-and-bets](../02-ideation/skills/assumptions-and-bets.md), [success-metrics](../08-analysis/skills/success-metrics.md), [context-pack](../00-governance/skills/context-pack.md), [decision-log](../00-governance/skills/decision-log.md).

**Produces:** an updated `work/00-brief.md` with a change log of what moved and why.

**Bar:** every change to the original brief has a reason linked to evidence; success metrics are measurable.

**Ninja move:** show the client the brief's before and after. It proves the thinking and makes their sign-off easy.

> **Checkpoint C: Brief signed off** by Erick and, where appropriate, the client.

---

## Phase 4. Design

### Step 8. First wireframe iteration

**Goal:** the structure and behaviour of every screen, in greyscale, with real words and every state.

**Moves**
- Turn the flow skeletons into full flows with every edge case decided.
- Design the states for each screen: empty, loading, error, success, partial; and AI states if relevant.
- Design forms and write real copy in the glossary's terms.
- Lay out each screen in priority order with annotations; check against the UX laws.

**Library:** [user-flows](../03-ux-design/skills/user-flows.md), [states-and-errors](../03-ux-design/skills/states-and-errors.md), [form-design](../03-ux-design/skills/form-design.md), [ux-writing](../03-ux-design/skills/ux-writing.md), [ai-experience](../03-ux-design/skills/ai-experience.md) (if AI), [wireframe-spec](../03-ux-design/skills/wireframe-spec.md).

**Produces:** `work/03-ux-spec.md` (flows, states, forms, copy, wireframes).

**Bar:** every action has a destination; every screen has its states; no lorem ipsum.

**Ninja move:** wireframe the unhappy paths first. If the error and empty states are good, the happy path almost designs itself.

### Step 9. High-fidelity prototype

**Goal:** a realistic, clickable prototype that looks and feels like the product.

**Moves**
- **If the company has a design system:** load it first (tokens, components, DESIGN.md) and build from it.
- **If not:** set the visual direction and foundations (layout, type, colour, motion), then define tokens before composing screens.
- Compose screens with clear hierarchy; spec the key micro-interactions, including the signature moment from step 4.
- Build every designed state into the prototype.

**Library:** [context-files](../05-ai-design-systems/skills/context-files.md), [design-tokens](../05-ai-design-systems/skills/design-tokens.md), [visual-direction](../04-ui-design/skills/visual-direction.md), [layout-and-spacing](../04-ui-design/skills/layout-and-spacing.md), [typography](../04-ui-design/skills/typography.md), [colour](../04-ui-design/skills/colour.md), [visual-hierarchy](../04-ui-design/skills/visual-hierarchy.md), [motion](../04-ui-design/skills/motion.md), [data-visualisation](../04-ui-design/skills/data-visualisation.md), [compose-screen](../04-ui-design/skills/compose-screen.md), [references/ui-data/](../references/ui-data/README.md).

**Produces:** the prototype (Figma or coded HTML) and `work/04-ui-spec.md`.

**Bar:** the prototype runs end to end on the target devices; it uses tokens, not loose values; the pre-delivery check in compose-screen passes.

**Ninja move:** build the high-fidelity prototype from the design system's tokens and components from the first frame. Step 15 then becomes a quick verification instead of a rebuild.

### Step 10. Refine the prototype

**Goal:** get from "it works" to "it is right" before anyone else sees it.

**Moves**
- Self-critique each screen through the seven lenses; remove AI tells in copy and visuals.
- Check cognitive load on the key flows.
- Where possible, run a quick test: five people, the key tasks, no help.
- Iterate, logging what changed and why.

**Library:** [critique-screen](../06-design-critique/skills/critique-screen.md), [slop-check](../06-design-critique/skills/slop-check.md), [cognitive-load-check](../07-qa-accessibility/skills/cognitive-load-check.md), [usability-test-plan](../07-qa-accessibility/skills/usability-test-plan.md), [heuristic-review](../06-design-critique/skills/heuristic-review.md).

**Produces:** a refined prototype and the change notes in `work/decisions.md`.

**Bar ("happy"):** no major issue on any critique lens; key tasks completed in testing without help (or a heuristic review if no testing was possible); the signature moment works.

**Ninja move:** test with someone in a difficult real situation (one hand busy, bright sun, tired, second language). Fixes for them make it better for everyone.

> **Checkpoint D: Prototype happy.** Erick signs off the prototype.

---

## Phase 5. Build and hand over

### Step 11. Editable Figma frames and/or prototype to dev

**Goal:** a hand-over engineers can build from without guessing.

**Moves**
- **Figma route:** run a preflight, then build frames from the library's components, binding every value to styles and variables; spec each micro-interaction (trigger, rules, feedback, duration and easing tokens, reduced-motion alternative).
- **Dev route:** share the prototype and its HTML with a hand-off spec: token names (not raw values), every state, copy, accessibility notes, analytics events and open questions with owners.
- Spec any new component once, so design and code share one definition.
- Walk engineers through it.

**Library:** [design-tool-sync](../05-ai-design-systems/skills/design-tool-sync.md), [component-spec](../05-ai-design-systems/skills/component-spec.md), [motion](../04-ui-design/skills/motion.md), [handoff-spec](../09-workflow-tooling/skills/handoff-spec.md).

**Produces:** Figma frames and/or `work/handoff.md` with the prototype link.

**Bar:** no raw values in Figma; every micro-interaction is specified; engineers have no unowned questions.

**Ninja move:** hand over the micro-interactions as specs, not just animations. They are what make it feel premium, and they are the first thing lost in build when left to interpretation.

---

## Phase 6. Check and polish

### Step 12. Check against the brief

**Goal:** prove the design answers every line of the refined brief, and that nothing extra slipped in.

**Library:** [brief-traceability](../06-design-critique/skills/brief-traceability.md) (lead).

**Produces:** `work/06-critique.md#brief-check`: a traceability table with evidence.

**Bar:** every brief line is met with a clickable link, or has a logged decision or a fix with an owner; every downstream ripple from step 2 has a designed answer or owner.

**Ninja move:** run the check in both directions. Anything designed that no brief line asks for either earns its place or goes.

### Step 13. Design critique

**Goal:** a sharp, criteria-based review of the screens, the flows and their coherence with everything decided underneath.

**Library:** [critique-screen](../06-design-critique/skills/critique-screen.md), [heuristic-review](../06-design-critique/skills/heuristic-review.md), [coherence-check](../06-design-critique/skills/coherence-check.md), [slop-check](../06-design-critique/skills/slop-check.md), [accessibility-audit](../07-qa-accessibility/skills/accessibility-audit.md), [critique-session](../06-design-critique/skills/critique-session.md) (with people).

**Produces:** `work/06-critique.md`.

**Bar:** every finding has an observation, a problem and a specific fix; deeper issues are routed back to the model or flows rather than patched on the surface.

**Ninja move:** run the AI critique before the human one. People then spend their time on judgement calls, not on spotting misaligned spacing.

### Step 14. Update the design from the critique

**Goal:** close every finding deliberately.

**Moves:** fix in priority order (blockers, accessibility, then polish); record each finding as accepted or rejected with a reason; re-check anything that changed against the brief check.

**Library:** [decision-log](../00-governance/skills/decision-log.md), [stage-gate](../00-governance/skills/stage-gate.md).

**Bar:** no open blocker; every finding has a recorded outcome.

### Step 15. Align to the design system in the company's Figma

**Goal:** every frame connected to the company's design system: copy styles, text styles, colour tokens, spacing, radius, effects and components.

**Moves**
- Preflight: confirm the connected libraries and inventory the styles, variables and components.
- Swap any detached or local element for the library component.
- Bind every value to a style or variable; report gaps instead of inventing values.
- Run a compliance scan (no raw values, no detached instances) and a contrast check in every theme.
- Log missing tokens or components as requests to the design system owners.

**Library:** [design-tool-sync](../05-ai-design-systems/skills/design-tool-sync.md) (lead), [design-qa](../07-qa-accessibility/skills/design-qa.md), [accessibility-audit](../07-qa-accessibility/skills/accessibility-audit.md), [audit-system](../05-ai-design-systems/skills/audit-system.md) (if many gaps), [system-governance](../05-ai-design-systems/skills/system-governance.md) (for requests).

**Produces:** system-aligned Figma frames and `work/05-system/sync-log.md`.

**Bar:** the compliance scan finds zero raw values and zero detached instances; gaps are logged with the system owner.

**Ninja move:** hand the client's design team a short list of the gaps the work uncovered in their system. It turns a delivery into a contribution to their system.

> **Checkpoint E: Ready to show.** Erick confirms the brief check, critique outcomes and system alignment.

---

## Phase 7. Present

### Step 16. Final presentation to the client

**Goal:** the client understands the thinking, trusts the decisions and makes a clear decision.

**Moves**
- Know the room and what each person cares about.
- Tell the story: their goal, the platform map and where this sits (with ripples handled), what was learned, the direction and why, a live walkthrough of one real user story including an error handled well and the signature moment, proof against the brief, and the one decision needed.
- Translate key decisions into the business metrics they move.
- Prepare answers to the three hardest questions; rehearse the demo on the real device.
- Send a one-page follow-up within a day.

**Library:** [client-presentation](../09-workflow-tooling/skills/client-presentation.md) (lead), [write-rationale](../09-workflow-tooling/skills/write-rationale.md).

**Produces:** the deck or walkthrough and `work/presentation.md`.

**Bar:** a clear client decision in the meeting; the follow-up is sent.

**Ninja move:** open with the platform map. Showing the client their whole business before showing a single screen is what makes them wonder how you did it.

> **Checkpoint F: Client decision.** Recorded with [decision-log](../00-governance/skills/decision-log.md).

---

## Encore (after launch)

Close the loop once real users arrive: read the analytics against the success metrics, run experiments where traffic allows, and report the impact. This turns one project into evidence for the next pitch.

**Library:** [read-analytics](../08-analysis/skills/read-analytics.md), [experiment-design](../08-analysis/skills/experiment-design.md), [ai-feature-evaluation](../08-analysis/skills/ai-feature-evaluation.md) (if AI), [impact-report](../08-analysis/skills/impact-report.md).

## Fast lanes

| Job | Run these steps |
|---|---|
| Small change to an existing feature | 2, 3, 8, 10, 12, 15 |
| New feature on a known platform | All, with step 1 as a quick refresh of the existing map |
| Concept or pitch only | 1 to 7, then 9 as a lightweight prototype, then 16 |
| Design review of someone else's work | 2, 12, 13 |

## Files a run produces

```
work/00-landscape.md   platform map and feature placement (steps 1-2)
work/00-brief.md       brief, refined at step 7
work/01-research.md    competitors, teardown, domain, findings, needs, personas
work/02-direction.md   problem, principles, concepts, decision, metrics
work/03-ux-spec.md     model, IA, flows, states, forms, copy, wireframes
work/04-ui-spec.md     direction, foundations, screens
work/05-system/        tokens, components, DESIGN.md, UX.md, sync log
work/06-critique.md    brief check and critique
work/handoff.md        hand-over to dev
work/presentation.md   client presentation and follow-up
work/decisions.md      every decision and checkpoint
```
