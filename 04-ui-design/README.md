# UI design

How it looks: direction, layout, type, colour and motion first; then hierarchy, charts and finished screens on top of the design system.

**Position in the line:** step 4 and 6 of `playbooks/run-brief.md`.  
**Writes:** work/04-ui-spec.md and screens  
**Gate:** G4 Look, G6 Taste

Runs in two parts: foundations before the design system, screens after it.

## Running this stage alone

Foundations need the brief and brand files. Screens need wireframes or a clear description, and the design system if one exists.

## Skills, in running order

| # | Skill | Step | Use when |
|---|---|---|---|
| 1 | [Set the visual direction](skills/visual-direction.md) | 4 | A new product, page or redesign needs a look; "what style should this be", "art direct this", "it looks generic"; before any screens are composed. |
| 2 | [Set layout, grid and spacing](skills/layout-and-spacing.md) | 4 | Defining page structure, grids, breakpoints or spacing; "it feels cramped", "make it responsive", "what grid should we use". |
| 3 | [Set typography](skills/typography.md) | 4 | Choosing typefaces, sizes or text styles; "the text hierarchy is off", "set up the type scale". |
| 4 | [Build the colour system](skills/colour.md) | 4 | Choosing a palette, adding dark mode, or fixing contrast; "pick colours", "it fails contrast", "add a dark theme". |
| 5 | [Compose visual hierarchy](skills/visual-hierarchy.md) | 6 | Laying out a screen so the important thing is seen first; "nothing stands out", "everything shouts", "what should people notice first". |
| 6 | [Design motion](skills/motion.md) | 4 | Adding transitions, micro-interactions or animation; "make it feel alive", "spec the animation"; defining motion tokens. |
| 7 | [Design data visualisation](skills/data-visualisation.md) | 6 | The product shows charts, dashboards or metrics; "which chart should we use", "design the dashboard". |
| 8 | [Compose a screen](skills/compose-screen.md) | 6 | Building a high-fidelity screen or page from the spec and the system; "design this screen", "build the page". |

## Gate checklist: G4 Look (UI foundations)

- [ ] A person chose the visual direction
- [ ] Every colour pairing passes contrast in both themes
- [ ] Type survives 200 per cent text size

## Gate checklist: G6 Taste (Screens)

- [ ] Screens use system tokens and components only
- [ ] Every state built
- [ ] Pre-delivery check passed
- [ ] Taste pass done by a person

## Posts and articles that informed this stage

- S01: [designer-skills (repo)](https://github.com/Owl-Listener/designer-skills) by Owl-Listener (repo, read: partial)
- S05: [getdesign.md](https://getdesign.md/) by VoltAgent team (site); format from Google Labs (site, read: read)
- S12: [Claude Code is terrible at design: a 9-step workflow](https://www.linkedin.com/posts/charlie-hills_claude-code-is-terrible-at-design-the-9-share-7472226424129736704-iC5A) by Charlie Hills (post, read: partial)
- S24: [UI redesign as art direction (Codex skill)](https://www.linkedin.com/posts/timothynice_codex-productdesign-genai-share-7488387102556983296-y74B) by Timothy Nice (post, read: read)

## More skills in the original repositories

Not rewritten here, either because a consolidated skill covers most of it or because it is specialist. Use them directly when you need the depth.

- [designer-skills / illustration-style](https://github.com/Owl-Listener/designer-skills/blob/main/ui-design/skills/illustration-style/SKILL.md): Define an illustration style guide: visual language, colour usage, and application rules. Use when commissioning or standardising illustration. For icons, use `icon-system` (design-systems).
- [inclusive-design-skills / information-density](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/information-density/SKILL.md): Design interfaces where information density can be adjusted to suit different cognitive needs and preferences. Use when designing dashboards, data tables, feeds, inboxes, settings panels, or any interface with variable a
- [inclusive-design-skills / preference-audit](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/preference-audit/SKILL.md): Audit an existing interface for respect of user preferences including motion, contrast, colour scheme, and text scaling. Chains: user-preference-respect, responsive-accessibility, colour-independence. Use when reviewing 
- [inclusive-design-skills / responsive-accessibility](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/responsive-accessibility/SKILL.md): Design responsive layouts that maintain accessibility across screen sizes, zoom levels, and orientations. Use when designing responsive interfaces, testing zoom behaviour, or reviewing layouts across devices. Triggers on
- [inclusive-design-skills / simplified-views](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/simplified-views/SKILL.md): Design simplified and reduced-complexity views of interfaces for users who need less visual noise and fewer options. Use when designing settings, dashboards, complex tools, or any interface that could benefit from a simp
- [inclusive-design-skills / specify](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/specify/SKILL.md): Specify adaptive behaviour for an interface. Chains: user-preference-respect, responsive-accessibility, flexible-typography, colour-independence, simplified-views, information-density. Use when designing a new interface 
- [inclusive-design-skills / user-preference-respect](https://github.com/Owl-Listener/inclusive-design-skills/blob/main/adaptive-interfaces/skills/user-preference-respect/SKILL.md): Design interfaces that detect and respond to system-level user preferences. Use when implementing dark mode, reduced motion, high contrast, text scaling, or any user preference that affects how the interface renders. Tri
- [ui-ux-pro-max-skill / banner-design](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/banner-design/SKILL.md): Design banners for social media, ads, website heroes, creative assets, and print. Multiple art direction options with optional generated or supplied visuals. Actions: design, create, generate banner. Platforms: Facebook,
- [ui-ux-pro-max-skill / brand](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/brand/SKILL.md): Brand voice, visual identity, messaging frameworks, asset management, brand consistency. Activate for branded content, tone of voice, marketing assets, brand compliance, style guides.
- [ui-ux-pro-max-skill / slides](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/blob/main/.claude/skills/slides/SKILL.md): Create strategic HTML presentations with Chart.js, design tokens, responsive layouts, copywriting formulas, and contextual slide strategies.

Back to the [index](../README.md).
