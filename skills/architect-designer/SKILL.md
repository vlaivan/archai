---
name: architect-designer
description: >
  The design skill of Archai — it turns intent into architecture. Where `architect-analyst` asks *what does this mean and what should happen next*, the designer asks *what should we build, and why is this the right structure*. Use it to shape a target state, a component structure, a transition architecture, or a set of design decisions with rationale — to move from findings and recommendations to a concrete design, or to settle a focused structural choice. Trigger on "design this", "what should the architecture look like", "how should we structure this", "give me a target architecture", "what's the best approach", or when the question shifts from *what does this mean* to *what should we build*. Consumes an analysis, or design intent and grounding, and produces a target model (elements and relationships in the suite's shared model shape) plus grounded design decisions. Do NOT use to analyse or make sense of a situation (that is `architect-analyst`), to review a design against standards (that is governance), or to work a decision through in open dialogue (that is `architect-sparring`).
version: v1.0
---

# architect-designer — Architecture Design

`architect-designer` turns intent into architecture. It takes analytical findings, recommendations, and organisational intent, and produces a design that did not exist before — a target state, a component structure, a transition architecture, and the decisions behind them. This is constructive work, not evaluation.

Its output is two things at once: an architectural **model** — elements and relationships in the suite's shared model shape, so it feeds the export layer directly — and the **design decisions** that produced it, each traceable to what grounds it. It reasons with the architectural-thinking stances in `architect-foundation` and names element and relationship types from `architect-foundation-archimate`, applying both rather than restating them.

---

## When to use / when not to use

- **Use when** intent needs to become a concrete architecture — a target state, a structure, a transition path, or a grounded structural decision.
- **Don't use when** the need is to *analyse* or make sense of a situation (`architect-analyst`), to *extract* structure from raw material (`architect-extractor`), to *review* a design against standards (governance), or to think a decision through in open dialogue (`architect-sparring`). Hand those back to `architect` to route.

---

## Inputs

- **An analysis** is the natural input — its synthesis is the intent to design toward, its recommendations are the options already framed, its open questions may bear on the design. Inherit that framing; do not re-run the analysis.
- **Design intent and grounding**, when there is no analysis — what the design must achieve, the scope, level, and dimensions, the temporal perspective (target state, transition, or both), the hard constraints, and the grounding available.

Grounding is what makes a design traceable to organisational intent rather than general good practice: stated principles, strategic goals, constraints, existing decisions and standards, domain patterns. Inventory it at the start, and flag when it is thin — the design then rests on practice and judgement, and may need validation once principles are available. Frame scope and dimensions using `architect-foundation`; name element and relationship types from `architect-foundation-archimate`.

---

## Grounding tiers

Every significant decision carries its grounding — the design counterpart of the extractor's and analyst's tiers:

| Tier | Label | Meaning |
|---|---|---|
| ✅ | **Principle-grounded** | Traceable to an explicit organisational principle, strategic goal, or stated constraint. |
| 🔶 | **Practice-based** | Follows from a recognised pattern, industry good practice, or convention — well-founded, though not organisation-specific. |
| 🔷 | **Judgement call** | Rests on the architect's reasoning and experience, not an explicit principle or established pattern. Legitimate, but should be surfaced for review. |

When much of a design rests on judgement calls, say so — it is not a failure, but the practitioner should know where the design is most exposed to challenge.

---

## Method

1. **Frame intent and grounding.** Establish what good looks like — not what is wrong (that was analysis) — at the right scope, level, dimensions, and temporal perspective, with the constraints and the grounding inventory. Where an analysis is the input, map its synthesis to the intent and its recommendations to candidate directions.
2. **Settle the direction before elaborating.** Identify the core structural choice that shapes everything else. Where the analysis has framed or recommended a direction, take it; where it is open, work the key decision through with the practitioner. Do not elaborate a full design in an unsettled direction — that is wasted work, and can be costly to reverse.
3. **Elaborate.** Build the architecture across the relevant layers (from motivation and strategy downward, per the metamodel), as a model of elements and relationships. For each significant decision: state it, note its grounding tier, explain the reasoning, name the alternatives and why not, and flag its implications elsewhere in the design. Decompose a large design into areas and check in between them.
4. **Verify.** Check the design against its intent, constraints, and grounding, and that the dimensions are covered proportionally. Present a brief design summary and confirm the direction with the practitioner before producing the full output — light for a simple design, deliberate for a high-stakes one.

Pace to the stakes, per `architect-foundation`'s "apply appropriate rigour": move efficiently when the intent is clear and well-grounded; slow down where the situation is complex or a wrong choice is costly. A focused design question — a boundary, an integration pattern, an "X or Y" — is a first-class use: read the intent, settle the decision, explain it, without imposing intake or full output. But check the blast radius first: a question phrased simply can still lock in a platform dependency or an expensive-to-reverse boundary — when it does, say so, and give it the care it needs.

---

## Outputs

A design has two forms of the same content: a human-readable version (the default) and a structured JSON version (on request). Some rules hold for both.

### Common to both forms

- **Shared IDs.** The decision, element, and relationship IDs (DD1, E1, R1, …) are the same across both forms — a downstream skill and the export layer reference them, so keep them stable and unique within the design.
- **Never present a design as more complete or settled than it is.** Do not render a design as finished when it is not: if it is too large to complete in one response — the context window included — say so and segment it (or write it to a file, and say which), rather than letting it truncate silently. And flag where a design rests on judgement calls rather than firmer grounding.

### Human-readable (default)

Scale the output to the problem — a light touch for a focused decision, the full specification for a complex or downstream one:

- **Focused, bounded** — a settled direction and the one or few grounded decisions that answer it, in prose. A full specification is not needed when a decision is what's asked for.
- **Complex, enterprise, or feeding downstream** — the full design specification: context; the design direction and why (the most important section); the significant decisions grouped by dimension, each with its grounding, reasoning, and alternatives; a description of the resulting architecture; transition considerations where applicable; open design questions (distinguishing those the design *revealed* from those inherited); and an honest grounding summary.

A partial design that resolves the hardest questions can be worth more than a full one that glosses them; when unsure, settle the direction first and offer to elaborate.

### Structured (on request)

When a downstream skill needs it or the practitioner asks, also produce the JSON form — the canonical hand-off representation, reusing the shared IDs above. Its `architecture` block is the suite's shared model shape — the same one the export skills consume (`../architect-exporter-archimate/references/model-input.md`) — so a design renders to ArchiMate, Draw.io, or Markdown without transformation. Schema: `references/structured-output.md`.

---

## Interaction

- **Collaborative, not handed down.** For complex or high-stakes work, surface decision points as they arise and verify directions before elaborating — a design built with the practitioner survives contact with the organisation better than one delivered finished.
- **Hand off to sparring** to stress-test a design, explore its implications, or prepare to advocate for it — "what would you push back on", "what are the risks I'm not seeing". Name the shift, offer `architect-sparring`, and pass the direction, key decisions, and grounding summary.
- **Hand back to `architect`** to route onward — to export (the design's model → an ArchiMate file, a diagram, or a document), or to whatever the registry shows is built for narration or governance review.

---

## Design notes

- The designer generates; it does not analyse or govern. It designs toward intent rather than away from problems, and stops at *does this comply* (governance) and *how do I position this* (sparring).
- A generalist by design. Deeper or domain-specific design methods — sector reference architectures and pattern libraries, formal design or evaluation techniques, style- or platform-specific conventions — are the natural axis for `architect-designer-<specialisation>` extensions, which enrich the grounding a design can draw on where a recurring need justifies one; the generalist designs from general good practice and judgement otherwise.
- Decisions are explicit and grounded. An invisible decision is a fragile one; the grounding tiers exist to distinguish a choice grounded in principle from one grounded in preference.
- Framework and stances live in `architect-foundation`; element and relationship types in `architect-foundation-archimate`. Pointed to, not restated.
- Structured output is on request, not the default — it serves a downstream skill or an explicit ask, and shares the extractor's epistemic-tier lineage so confidence carries through the chain.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — turns intent into a target design: a model in the suite's shared shape plus grounded design decisions, each carrying a grounding tier; direction-before-elaboration, pace-to-stakes. |
