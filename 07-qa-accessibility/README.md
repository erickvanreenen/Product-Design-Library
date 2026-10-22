# QA and accessibility

Does it work for everyone, as specified, within the law.

**Position in the line:** step 8 of `playbooks/run-brief.md`.  
**Writes:** work/07-qa-report.md  
**Gate:** G8 Ship

## Running this stage alone

Needs the design or build. Accessibility and design QA can run on any existing product.

## Skills, in running order

| # | Skill | Step | Use when |
|---|---|---|---|
| 1 | [Audit accessibility](skills/accessibility-audit.md) | 8 | A design or build needs an accessibility check; "is this accessible", "run a WCAG audit", "check contrast and keyboard"; before release. |
| 2 | [Check cognitive load](skills/cognitive-load-check.md) | 8 | Flows feel heavy or people drop out; "is this too complicated", "simplify this flow"; before release of any multi-step task. |
| 3 | [Check legal accessibility requirements](skills/compliance-check.md) | 8 | Planning or releasing a product; "which accessibility laws apply", "do we need to meet WCAG"; entering a new market. |
| 4 | [Plan a usability test](skills/usability-test-plan.md) | 8 | A prototype or build needs testing with users; "plan a usability test", "write test tasks", "test with assistive technology users". |
| 5 | [Check the build against the design](skills/design-qa.md) | 8 | Something has been built; "QA this build", "does it match the design", "check for drift"; before release; on a schedule. |

## Gate checklist: G8 Ship (QA and accessibility)

- [ ] No open critical accessibility issues
- [ ] No high-severity design QA issues
- [ ] Legal applicability checked

## Posts and articles that informed this stage

- S25: [Autonomous design-ops audits](https://www.linkedin.com/posts/stanislau_claudecode-productdesign-designops-share-7484931629862477824-4Fsv) by Stanislau (post, read: partial)
- S26: [Digital accessibility laws for UX designers](https://www.uxdesigninstitute.com/blog/digital-accessibility-laws-for-ux/) by UX Design Institute (post, read: partial)

## More skills in the original repositories

Not rewritten here, either because a consolidated skill covers most of it or because it is specialist. Use them directly when you need the depth.

- [designer-skills / click-test-plan](https://github.com/Owl-Listener/designer-skills/blob/main/prototyping-testing/skills/click-test-plan/SKILL.md): Design first-click and click tests for findability and navigation. Use when testing whether people can locate something. For full task-based observation, use `test-scenario`.
- [inclusive-design-skills / accessibility-debt-tracking](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/accessibility-debt-tracking/SKILL.md): Track and manage accessibility debt: known accessibility issues that have been deferred. Use when managing a backlog of accessibility issues, planning remediation, or when accessibility problems are accumulating faster 
- [inclusive-design-skills / accessibility-testing-strategy](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/accessibility-testing-strategy/SKILL.md): Plan what to test, how to test, and who should test for accessibility. Use when defining a testing approach, planning QA, setting up automated and manual testing, or deciding what level of accessibility testing a project
- [inclusive-design-skills / document](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/document/SKILL.md): Document accessibility decisions and tradeoffs for a feature. Chains: decision-documentation, tradeoff-analysis, compliance-mapping. Use when a feature is being designed or shipped and accessibility decisions need to be 
- [inclusive-design-skills / review](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/review/SKILL.md): Review and surface undocumented accessibility assumptions in an existing feature or product. Chains: decision-documentation, tradeoff-analysis, compliance-mapping, accessibility-debt-tracking. Use when inheriting a produ
- [inclusive-design-skills / stakeholder-communication](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/stakeholder-communication/SKILL.md): Communicate accessibility decisions, requirements, and value to stakeholders who aren't accessibility specialists. Use when presenting accessibility work to leadership, product managers, engineers, or anyone who needs to
- [inclusive-design-skills / tradeoff-analysis](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/accessibility-decisions/skills/tradeoff-analysis/SKILL.md): Analyse accessibility tradeoffs when a design decision improves accessibility for one group but may affect another, or when accessibility competes with other requirements. Use when facing conflicting accessibility needs,
- [inclusive-design-skills / adaptive-personalisation](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/adaptive-personalisation/SKILL.md): Design help systems and support patterns that work for people with cognitive disabilities. Use when designing help content, tooltips, onboarding, FAQs, support flows, documentation, or any context where users need guidan
- [inclusive-design-skills / assess-load](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/assess-load/SKILL.md): Assess cognitive load across a complete multi-step process and produce a load map. Chains: cognitive-load-assessment, memory-load-reduction, wayfinding-navigation. Use when evaluating a checkout flow, onboarding sequence
- [inclusive-design-skills / contextual-help-design](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/contextual-help-design/SKILL.md): Design help systems and support patterns that work for people with cognitive disabilities. Use when designing help content, tooltips, onboarding, FAQs, support flows, documentation, or any context where users need guidan
- [inclusive-design-skills / review](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/review/SKILL.md): Run a full cognitive accessibility review of a flow, screen, or interface. Chains: cognitive-load-assessment, plain-language-design, wayfinding-navigation, error-prevention-recovery, focus-attention-design, memory-load-r
- [inclusive-design-skills / simplify](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/cognitive-accessibility/skills/simplify/SKILL.md): Simplify content and interactions to reduce cognitive load. Chains: plain-language-design, cognitive-load-assessment, focus-attention-design. Use when given content, a flow, or an interface that needs to be made more acc

Back to the [index](../README.md).
