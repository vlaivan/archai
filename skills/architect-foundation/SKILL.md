---
name: architect-foundation
description: >
  The generic foundation skill of Archai — the shared architecture vocabulary and cross-cutting competencies the rest of the suite builds on. Use it, or consult it from another skill, when work needs foundational grounding rather than a specific value-cycle activity: orienting within the architecture framework (the value cycle, the SECI quadrants, the areas of concern), the meaning of core architecture concepts and terms, or general principles of sound architectural reasoning not tied to any one phase. Other architect-* skills point here for shared terminology and concepts rather than restating them. Specialist bodies of knowledge (for example an ArchiMate reference) live in architect-foundation-<topic> extensions. Do NOT use for phase-specific work (that is the functional architect-* skills) or for building the suite itself (that is architect-suite).
version: v1.0
---

# architect-foundation — Shared Architecture Foundation

`architect-foundation` is the suite's shared foundation: the vocabulary and cross-cutting competencies every other skill assumes. It is generic and cross-cutting — not tied to a value-cycle phase — and it holds *applied* knowledge (how to think architecturally), distinct from `architect-suite`, which governs how skills are built.

It is used two ways:

- **Consulted** by other skills — they point here for shared terms and concepts rather than restating them.
- **Invoked directly** when a practitioner needs grounding: framework orientation, what a term means, or the fundamentals behind a piece of work.

It is extended by `architect-foundation-<topic>` skills, each holding a specific body of knowledge (for example, an ArchiMate metamodel reference).

---

## The framework (quick reference)

The suite is organised around two dimensions, set in a broader context. The canonical definitions and rationale live in the vision (`../architect-suite/references/vision.md`); this is the working shorthand.

**Architecture value cycle** — the phases of architecture work:

- **Discovering** — identifying the landscape and current-state reality.
- **Analysing** — making sense of it: patterns, dependencies, gaps, implications.
- **Designing** — shaping target architectures, from principles to blueprints.
- **Planning & Implementing** — turning architectural intent into reality through managed change.
- **Enacting** — operating with and within the architecture day to day.
- **Governing** — sustaining coherence, compliance, and evolution over time.

**SECI knowledge quadrants** — how knowledge moves: **Socialise** (tacit→tacit) · **Externalise** (tacit→explicit) · **Combine** (explicit→explicit) · **Internalise** (explicit→tacit).

**Areas of concern** — the context a piece of work sits in:

- **Dimensions** (subject matter) — Motivation · Strategy · Business · Information · Information Systems · Technology · Implementation & Migration.
- **Management level** — Strategic · Tactical · Operational.
- **Scoping boundary** — Enterprise · Domain · Solution.

**Contextual factors** — the conditions that shape how work is framed and adapted, rather than what it is about: **subject matter**, **maturity**, **competence**, and **audience**.

Use these to locate a piece of work — its phase, its knowledge mode, and its dimensions, level, and scope — the same orientation `architect` performs when routing.

---

## Architectural thinking

A cross-cutting starter pack of stances for sound architectural reasoning, independent of phase — the thinking every skill in the suite draws on. Apply them as a baseline; specific methods and rigour come from the functional skills. Individual stances may grow into their own `architect-foundation-<topic>` when they warrant real depth.

- **Keep the whole in view.** Architecture is structure and relationships, not isolated parts. Situate a piece of work in its wider context — the surrounding systems, the layers above and below it, the decisions it depends on and the ones it constrains — while still reasoning at the right level. Zoom out before you zoom in.
- **Decompose and draw clear boundaries.** Break a complex whole into parts and be explicit about the boundaries — aiming for loose coupling, high cohesion, and cuts placed where responsibility and change naturally divide.
- **Maintain traceability.** Connect architectural inferences to their sources; connect architectural decisions to their reasons and rationale; connect architectural designs to their intents. Every piece of understanding should trace back to the evidence; every recommendation should trace back to the goal or driver behind it; every solution on business, information, systems and technology layers should trace back to the motivation and strategy that guide it.
- **Understand current, target and transition states.** Distinguish where the architecture is now, where it could or should go — including alternative scenarios — and the path between; be explicit about which you are working on, and treat architecture as evolving rather than a static snapshot.
- **Ground in evidence.** Anchor architectural reasoning in the actual situation and its artefacts; separate what's known from what's assumed, and how confident you are in each; prefer real inputs over abstraction.
- **Surface options and trade-offs.** Architecture is choosing and making decisions under constraints. Hold viable alternatives open and name what each gains and gives up — against the drivers and qualities that matter — before converging on one.
- **Apply a whole-lifecycle view.** Consider the whole lifecycle in architectural decision-making. Weigh the cost and consequences of building, running, and changing architectural solutions across their lifetime, not just the up-front build.
- **Focus on the significant decisions.** Architecture is the decisions that are hard or costly to reverse; weight the costly, hard-to-reverse ones most; keep cheap and reversible choices open; and make commitments deliberately, weighing economics and constraints.
- **Design for qualities, not just function.** Much of architecture is driven by desirable quality attributes — identify which matter most in each situation and which should take priority, make them explicit and weigh how they trade off.
- **Reuse before reinventing.** Reach for proven architectural patterns, reference architectures, and architecture standards — consistency across the estate usually beats local novelty.
- **Adjust approach to context, not dogma.** The right architectural approach often depends on the situation; adapt patterns and "best practice" to the actual goals, constraints, and maturity rather than applying them by rote.
- **Apply appropriate rigour.** Apply just enough architecture: proportion effort, formality, and detail to what the architectural decision needs. A model or artefact earns its place only by improving understanding or a decision — it is a means, not an end.
- **Assume capability and value orientation.** Frame architectural issues in business terms — capabilities and the value delivered — with no architecture jargon. Architecture has no intrinsic value; it is about enabling the business to do what it needs to do.
- **Understand stakeholder needs.** Architecture serves understanding and decisions — shape what you surface, and how, tailored to the stakeholders who must act on it.

---

## Design notes

- Generic by design: deep or domain-specific bodies of knowledge belong in `architect-foundation-<topic>` extensions, not here.
- Reference over duplication: the framework's canonical definitions stay in the vision; this skill carries a working quick-reference plus the architectural-thinking stances the vision doesn't cover.
- Suite terminology is defined where it is introduced: the framework terminology in the suite vision, the skill-specific terminology in the skills, and standard architecture terminology as a fallback. A shared glossary under `references/` can be added when skills introduce terms specific enough to be worth collecting in one place.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — framework quick-reference and a starter set of cross-cutting architectural-thinking stances. |
