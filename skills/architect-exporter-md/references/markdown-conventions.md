# Markdown Rendering Conventions

How content is rendered into Markdown across Archai — so every export reads as one system. This is a *formatting* reference, organised as the anatomy of a document: from its overall structure down to its finest markers. It knows document shapes, not content — it renders whatever the input holds, mapping each shape to the Markdown construct that fits, and never manufacturing what is not there.

The sections run from the most general (the document's skeleton) to the most marginal (the markers on individual items). A deliverable uses only the shapes its content actually has.

---

## Structure

The skeleton of the deliverable. Give it a single title (`#`), and section it with headings (`##`, `###`) that follow the content's own hierarchy — one heading level per level of nesting, no deeper than the content warrants. For a long deliverable, open with a table of contents: a linked list to the section anchors, so the reader can navigate. Keep sections short enough to scan; a wall of text under one heading is a structure that has given up.

## Narrative

Prose — to orient, summarise, or explain, not to carry data a construct would hold better. Lead with the point: a short summary before the detail, so a reader who stops early still leaves with the gist. Soft-wrap (one paragraph per line), a blank line between paragraphs, emphasis (`**bold**`, `*italic*`) used sparingly and only for genuine emphasis. Quote external or verbatim material in a blockquote (`>`) rather than blending it into your own words.

## Visualisations

Markdown is text, so visualisation is limited and host-dependent — be honest about that. Where a picture genuinely helps and the host supports it, embed a diagram as a fenced code block in a diagram language (for example a ` ```mermaid ` block); otherwise fall back to a linked image, or to a table used as a simple matrix. Never assume a diagram will render — offer it as an enhancement, and make sure the deliverable still reads without it.

## Records

A set of items that share fields → a table: one row per item, a header row, columns in a fixed order. Prefer a table whenever items are comparable on the same attributes. For a single item with many fields, a definition-style list (a bolded label per line) reads better than a one-row table. Keep column order consistent across deliverables so records stay comparable.

## Groupings

Items that bucket or nest → render the grouping explicitly rather than flattening it: a sub-heading per group with its records beneath, or nested lists for a shallow hierarchy. Order the groups consistently — the content's own order, or a stable convention — and name each so the reader sees the partition at a glance.

## Relations

Items linked to items — which Markdown has no native way to draw. Render a set of relations as a table (source · relation · target); render an individual cross-reference as a link to the target's anchor. Linearise honestly: a linked structure becomes a table plus anchors, and you say so, rather than pretending the page shows a graph.

## Sequence

Items with an order — steps, phases, a timeline → an ordered list (`1.`, `2.`) for a simple progression, or a table with an explicit order or step column when each item also carries fields. Let the order the reader's eye follows be the content's actual order; where an item depends on an earlier one, state the dependency rather than leaving it to position alone.

## Annotations

Markers attached to individual items — a status, a source, a confidence, a priority, whatever the content carries. Render each kind of annotation *one consistent way* throughout a deliverable — a dedicated column, or a compact inline tag or glyph — and, when a marker uses symbols, give a one-line legend the first time it appears. Render it faithfully whatever it means: the convention is about consistency, not about interpreting the marker.

---

## Fidelity and delivery

- **Render what is there, and only that.** Carry the content's markers through; never manufacture a field, a group, or an annotation the content does not have.
- **Never overstate.** A deliverable must not read as more complete or certain than its input; where the content carries markers of uncertainty, they are what keep it visible.
- **Flag what is missing.** Note content that was dropped, ambiguous, or absent, rather than rendering a clean surface over a partial input.
- **Never emit truncated.** If a deliverable will not fit in one response, segment it by section or — where the host can write files — write it to a `.md` file, and say which.
- **Delivery.** Render inline for a short deliverable read in place; for a large or reusable one, and where the host supports it, write a `.md` file and say which was done.
