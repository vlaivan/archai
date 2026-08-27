---
name: architect-exporter-md
description: >
  The Markdown formatting specialist of the Archai export layer — the conventions for rendering architectural content into clean, faithful, consistent Markdown. Use it when the target output format is Markdown: "as a document", "as a report", "write this up in Markdown", "produce a Markdown inventory / gap table / roadmap", or similar, and when `architect-exporter` routes a Markdown export here. It renders whatever architectural content it is given — a structured model or loose prose — preserving whatever the content carries and inventing nothing it does not. Do NOT use for other output formats (route through `architect-exporter`), and do NOT use it to decide what a document should say or which document to produce — that is the request's job, or narration's. This skill formats; it does not author.
version: v1.0
---

# architect-exporter-md — Markdown Formatting

`architect-exporter-md` renders architectural content into Markdown. It is a **formatting guide**, not a content guide: it governs *how* architectural content is laid out in Markdown — faithfully and consistently — not *what* the content is or what it should say.

Its value is consistent rendering discipline. Anyone can format Markdown; the point here is that every shape the content takes — its structure, narrative, records, groupings, relations, sequences, and the annotations on them — maps to the Markdown construct that fits, the same way every time, so deliverables stay faithful to their source and comparable with one another. It renders what is there and never manufactures what is not.

---

## When to use / when not to use

- **Use when** architectural content needs to be rendered into Markdown — a document, inventory, table, roadmap, or summary.
- **Don't use when** the target is another output format (route through `architect-exporter`); or when the task is to *decide what to say* or *which document to produce* — choosing the message and framing for an audience is narration, drawing conclusions is analysis. This skill renders; it does not author.

---

## Inputs

Architectural content, structured or loose:

- **Structured** — content already organised into records, relations, and groupings, however annotated (an extractor structured-output block is one example: `../architect-extractor/references/structured-output.md`). Render each shape with the construct that fits.
- **Loose** — prose, tables, or a described model. Render as faithfully as the content allows, without inventing structure it does not have.

For correct ArchiMate element and relationship naming when rendering model content, use the metamodel foundation: `../architect-foundation-archimate/references/metamodel.md`.

---

## Method

1. **Confirm the deliverable and scope.** Establish what is being rendered and, for anything non-trivial, propose a short rendering spec — which content, which tables, what is included and excluded — and confirm it before rendering in full. This scopes the render; it does not decide the message.
2. **Render by the conventions.** Produce the Markdown following `references/markdown-conventions.md` — mapping each shape the content takes (structure, narrative, records, groupings, relations, sequences, annotations) to the Markdown construct that fits, and applying the fidelity rules. Preserve everything the content carries.
3. **Flag what could not be rendered.** Note anything dropped, ambiguous, or absent; never render a clean surface over a partial input.

Never emit a deliverable truncated: if it will not fit in one response, segment it or (where the host can write files) write it to a `.md` file, and say which.

---

## References

- `references/markdown-conventions.md` — the rendering conventions: core rules, table layouts, common rendering patterns, fidelity rules, and delivery. This is the substance of the skill.
- `../architect-foundation-archimate/references/metamodel.md` — ArchiMate element and relationship names, for rendering model content correctly.
- `../architect-extractor/references/structured-output.md` — one example of a structured input this skill renders.

---

## Design notes

- A formatting guide, not a content guide. The skill owns *how* architectural content becomes Markdown — the conventions that keep every export faithful and consistent — and nothing about *what* the content says. Deciding the message and which document to make is the request's or narration's job; that boundary is what keeps this skill a rendering layer rather than a second author.
- The value is consistent shape-to-construct rendering, not generic Markdown: the same content shape becomes the same Markdown construct every time, so the output carries the fidelity of its source.
- The conventions are organised as document anatomy — structure, narrative, visualisations, records, groupings, relations, sequences, annotations — a closed set of shapes rather than an open list of content types. Any document is a combination of these; the skill names shapes, never architectural content.
- Metamodel naming is delegated to `architect-foundation-archimate`, not restated here.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — the Markdown formatting specialist: renders content into faithful, consistent Markdown by mapping document shapes to the constructs that fit. |
