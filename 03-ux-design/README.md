# UX design

How it works: the model, structure, flows, states, forms, words and AI behaviour.

**Position in the line:** step 3 of `playbooks/run-brief.md`.  
**Writes:** work/03-ux-spec.md  
**Gate:** G3 Spec

## Running this stage alone

Needs the job story and the chosen direction. For a small change, start at `user-flows` and `states-and-errors`.

## Skills, in running order

| # | Skill | Step | Use when |
|---|---|---|---|
| 1 | [Define the conceptual model](skills/conceptual-model.md) | 3 | Before flows or screens; "what are the objects", "what do we call this"; naming arguments; a redesign where the product feels inconsistent. |
| 2 | [Structure the information architecture](skills/information-architecture.md) | 3 | Organising content or features; designing navigation; "where does this live", "users cannot find X"; content volume is growing. |
| 3 | [Map user flows](skills/user-flows.md) | 3 | Designing how a user completes a job; "map the flow", "what are the steps", "what happens if it fails"; before wireframes. |
| 4 | [Design states, feedback and errors](skills/states-and-errors.md) | 3 | Any flow or component is specified; "what does it show while loading", "write the error states", "what if it fails"; before handoff. |
| 5 | [Design forms](skills/form-design.md) | 3 | Any form, sign-up, checkout or data entry; "people drop out of this form", "design the form". |
| 6 | [Write interface copy](skills/ux-writing.md) | 3 | Labels, buttons, errors, empty states, onboarding or help text are needed; "write the copy", "what should this button say", "review this microcopy". |
| 7 | [Design the AI experience](skills/ai-experience.md) | 3 | The product has an AI feature (assistant, generation, recommendations, agents); "design the AI feature", "how should the AI behave", "what happens when it is wrong". |
| 8 | [Specify wireframes](skills/wireframe-spec.md) | 3 | Flows and states are settled and layout must be decided; "wireframe this", "lay out the screen"; also first-run and onboarding screens. |

## Gate checklist: G3 Spec (UX design)

- [ ] Every flow lists empty, loading, error, success and edge states
- [ ] Copy written in the agreed vocabulary
- [ ] AI behaviour defined where relevant
- [ ] Works without a mouse

## Posts and articles that informed this stage

- S14: [AI Designer Playbook](https://www.linkedin.com/posts/antivirusakash_ux-uxdesign-aidesign-share-7464923833121271808-p4zB) by Akash Solanki (post, read: partial)
- S17: [10 AI skills product designers should understand](https://www.linkedin.com/posts/imen-mlika_ux-ui-uxdesign-share-7498120402737582080-MQek) by Imen Mlika (post, read: partial)

## More skills in the original repositories

Not rewritten here, either because a consolidated skill covers most of it or because it is specialist. Use them directly when you need the depth.

- [ai-design-skills / bias-detection-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/bias-detection-design/SKILL.md): Designing review workflows to surface and mitigate bias in AI outputs.
- [ai-design-skills / consent-and-agency](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/consent-and-agency/SKILL.md): Designing for informed user consent, opt-out, and human override.
- [ai-design-skills / guardrail-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/guardrail-design/SKILL.md): Defining behavioral boundaries: what the AI should and shouldn't do.
- [ai-design-skills / value-specification](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/ai-alignment-reasoning/value-specification/SKILL.md): Translating organisational values and user expectations into system constraints.
- [ai-design-skills / agent-role-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/design-agent-orchestration/agent-role-design/SKILL.md): Defining what each agent does, knows, and owns in a multi-agent system.
- [ai-design-skills / handoff-protocols](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/design-agent-orchestration/handoff-protocols/SKILL.md): Designing smooth transitions between agents and between AI and humans.
- [ai-design-skills / observability-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/design-agent-orchestration/observability-design/SKILL.md): Making multi-agent workflows visible and debuggable for designers and developers.
- [ai-design-skills / state-management](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/design-agent-orchestration/state-management/SKILL.md): Managing shared context, memory, and state across multiple agents.
- [ai-design-skills / task-decomposition](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/design-agent-orchestration/task-decomposition/SKILL.md): Breaking complex user goals into subtasks that agents can handle.
- [ai-design-skills / context-window-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/context-window-design/SKILL.md): Designing around token limits, memory, and conversation persistence.
- [ai-design-skills / conversation-patterns](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/conversation-patterns/SKILL.md): Turn-taking, repair sequences, grounding, and dialogue structure for human-AI interaction.
- [ai-design-skills / feedback-loops](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/feedback-loops/SKILL.md): User correction, thumbs up/down, inline editing, and reinforcement signals.
- [ai-design-skills / frustration-detection](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/frustration-detection/SKILL.md): Reading user emotional state from text signals: caps, punctuation density, repetition, latency: and adapting before the user disengages.
- [ai-design-skills / multimodal-orchestration](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/multimodal-orchestration/SKILL.md): Coordinating text, image, voice, and tool-use modalities in a single interaction.
- [ai-design-skills / progressive-disclosure](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/model-interaction-design/progressive-disclosure/SKILL.md): Revealing AI capability gradually to match user mental models.
- [ai-design-skills / chain-of-thought-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/prompt-architecture/chain-of-thought-design/SKILL.md): Designing reasoning chains that produce better outputs.
- [ai-design-skills / few-shot-patterns](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/prompt-architecture/few-shot-patterns/SKILL.md): Crafting examples that steer AI behavior effectively.
- [ai-design-skills / prompt-versioning](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/prompt-architecture/prompt-versioning/SKILL.md): Managing prompt iterations, testing changes, and tracking what works.
- [ai-design-skills / system-prompt-structure](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/prompt-architecture/system-prompt-structure/SKILL.md): Anatomy of effective system prompts: role, context, constraints, format.
- [ai-design-skills / template-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/prompt-architecture/template-design/SKILL.md): Creating reusable, parameterised prompt templates for consistent outputs.
- [ai-design-skills / behavioral-consistency](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/system-behavior-shaping/behavioral-consistency/SKILL.md): Ensuring the AI behaves predictably across sessions, edge cases, and modalities.
- [ai-design-skills / cultural-adaptation](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/system-behavior-shaping/cultural-adaptation/SKILL.md): Adapting AI behavior for different cultural contexts, languages, and norms.
- [ai-design-skills / domain-voice](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/system-behavior-shaping/domain-voice/SKILL.md): Tailoring AI behavior for specific professional domains.
- [ai-design-skills / emotional-design](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/system-behavior-shaping/emotional-design/SKILL.md): How the AI responds to user frustration, confusion, delight, and distress.
- [ai-design-skills / error-personality](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/system-behavior-shaping/error-personality/SKILL.md): How the AI communicates mistakes, uncertainty, and limitations gracefully.
- [ai-design-skills / persona-architecture](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/system-behavior-shaping/persona-architecture/SKILL.md): Defining AI character, voice, and personality traits.
- [ai-design-skills / tone-calibration](https://github.com/Owl-Listener/ai-design-skills/blob/main/skills/system-behavior-shaping/tone-calibration/SKILL.md): Adjusting formality, warmth, confidence, and style per context.
- [designer-skills / conversational-ux](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/conversational-ux/SKILL.md): Design voice and conversational interfaces: dialog flows, error recovery, and persona. Use when the interface speaks and listens rather than being tapped. For graphical input collection, use `form-design`.
- [designer-skills / gesture-patterns](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/gesture-patterns/SKILL.md): Design gesture interactions for touch and pointer: swipe, drag, long-press, and their discoverability. Use when input is gestural. For OS-standard gestures on iOS and Android, use `platform-conventions` (ui-design).
- [designer-skills / interfaces-that-feel](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/interfaces-that-feel/SKILL.md): Apply an emotional resonance lens to a UI that is technically correct but flat, prescribing changes at the copy, motion, and interaction layer. Use when a design tests fine but lands cold. For the polish-perception argum
- [designer-skills / search-ux](https://github.com/Owl-Listener/designer-skills/blob/main/interaction-design/skills/search-ux/SKILL.md): Design search: query input, zero results, refinement, and result presentation. Use when users retrieve rather than browse. For browse structure, use `navigation-patterns`.
- [inclusive-design-skills / multimedia-accessibility](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/multimedia-accessibility/SKILL.md): Design accessible video, audio, and multimedia content with captions, transcripts, and audio descriptions. Use when creating or reviewing video, audio, podcasts, webinars, animations, or any time-based media. Triggers on
- [inclusive-design-skills / readable-content](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/readable-content/SKILL.md): Write and structure content for diverse reading abilities and cognitive styles. Use when writing long-form content, help documentation, product descriptions, policies, terms, or any content that needs to be understood by
- [inclusive-design-skills / review](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/review/SKILL.md): Review content for accessibility across cognitive and literacy levels. Chains: readable-content, alt-text-design, heading-structure, link-text-design, table-accessibility, form-labelling, multimedia-accessibility. Use wh
- [inclusive-design-skills / rewrite](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/rewrite/SKILL.md): Rewrite content in plain language while preserving meaning. Chains: readable-content, link-text-design. Use when given content that is too complex, jargon-heavy, or inaccessible for the target audience.
- [inclusive-design-skills / structure](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/structure/SKILL.md): Structure content for screen reader and assistive technology use. Chains: heading-structure, alt-text-design, table-accessibility, form-labelling. Use when building a new page, document, or content template and you want 
- [inclusive-design-skills / table-accessibility](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessible-content/skills/table-accessibility/SKILL.md): Design data tables that work for screen readers and cognitive accessibility. Use when creating or reviewing tables, data grids, comparison tables, pricing tables, or any tabular data. Triggers on: table, data table, grid
- [inclusive-design-skills / audit](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/audit/SKILL.md): Audit an interface for multi-modal interaction support. Chains: keyboard-navigation, touch-target-design, multi-modal-input, gesture-alternatives, feedback-and-status, motion-sensitivity. Use when reviewing an existing i
- [inclusive-design-skills / feedback-and-status](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/feedback-and-status/SKILL.md): Design feedback and status communication that works across senses: visual, auditory, and haptic. Use when designing loading states, success messages, progress indicators, notifications, alerts, or any system response to
- [inclusive-design-skills / gesture-alternatives](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/gesture-alternatives/SKILL.md): Design alternatives to gesture-based and motion-based interactions. Use when designing swipe actions, pinch-to-zoom, shake-to-undo, tilt controls, multi-finger gestures, or any interaction that requires specific physical
- [inclusive-design-skills / keyboard-review](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/keyboard-review/SKILL.md): Review keyboard navigation and focus management in an existing interface. Chains: keyboard-navigation, feedback-and-status. Use when testing or reviewing keyboard accessibility specifically, before a release, or when use
- [inclusive-design-skills / multi-modal-input](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/multi-modal-input/SKILL.md): Design interfaces that offer multiple input methods so users can choose what works for their abilities and context. Use when designing any interactive system where users provide input: forms, search, editors, creative t
- [inclusive-design-skills / voice-interaction](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/inclusive-interaction/skills/voice-interaction/SKILL.md): Design voice interactions and speech interfaces that work for people with diverse speech patterns, accents, and communication styles. Use when designing voice commands, voice search, dictation, voice assistants, or any i

Back to the [index](../README.md).
