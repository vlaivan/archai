---
name: architect-exporter-drawio
description: >
  The Draw.io serializer of the Archai export layer. Serializes structured architectural content into a valid Draw.io (diagrams.net) diagram — a `.drawio` / mxGraphModel XML file: one plain rectangle per element, one plain edge per relationship. Use it when the target deliverable is an editable diagram. Trigger on "export to Draw.io", "make a diagram", "create a .drawio", "diagram this", or when `architect-exporter` routes a Draw.io export here. It is deterministic: a bundled script emits and validates the XML from a node-and-edge graph (elements and relationships with ids). It renders any such graph as boxes and arrows; when an element carries a type, the box shows a «Type» stereotype, otherwise it is a plain box. Do NOT use for other output formats (route through `architect-exporter`), to extract or analyse, or to produce prose. Plain boxes and edges only — no semantic layout, nodes are placed on a simple grid so each is separable and the practitioner rearranges them.
version: v1.0
---

# architect-exporter-drawio — Draw.io Serializer

`architect-exporter-drawio` turns structured architectural content into an editable Draw.io diagram.

It is a **serializer, not a formatter**: the XML is produced by a bundled, deterministic script — `scripts/drawio_export.py` — not generated token by token. Like the ArchiMate serializer, the interpretation has already happened upstream, so this skill only serializes what it is given.

---

## When to use / when not to use

- **Use when** the deliverable is an editable diagram of architectural content — a `.drawio` file to open in diagrams.net / Draw.io.
- **Don't use when** the target is another output format (route through `architect-exporter`); when content still needs *extracting* or *analysing*; or when a data-exchange model (not a picture) is wanted — that is the ArchiMate serializer.

---

## Inputs

Draw.io needs only a **graph**: elements with a name (and an id), and relationships with a source and a target. It is metamodel-agnostic — any node-and-edge content renders as boxes and arrows, architectural or not.

When an element carries a `type`, it is shown as a stereotype — `«Type»` above the name — so an ArchiMate model displays its element types while plain, untyped input stays plain boxes. The type is rendered verbatim; nothing here validates it or consults the metamodel.

In the architecture flow the graph is the suite's shared model contract (typed elements and relationships from the extractor or another producer), documented with the ArchiMate serializer — `../architect-exporter-archimate/references/model-input.md`. Draw.io consumes that contract but does not require it: a bare `{elements, relationships}` graph is enough. Loose prose should be structured into a graph first before a diagram can be drawn from it.

---

## Method

1. **Confirm structured input.** Elements and relationships must be identified; if only loose content is available, structure it first (via the extractor). Normalise other producers onto the model contract.
2. **Run the serializer.** Pass the model (as JSON) to the script:

   ```
   python3 scripts/drawio_export.py INPUT.json -o DIAGRAM.drawio [--name "Diagram Name"]
   ```

   It creates one node per element (labelled with the element name, and a `«Type»` stereotype when the element carries a type) and one edge per relationship (labelled with the relationship type), places nodes on a grid, and wires edges by reference — deterministically.
3. **Read the script's report, then repair or relay.** The script validates its output (well-formedness, every edge endpoint resolves to a node, unique cell ids) and flags anything skipped (a relationship with a missing endpoint). If validation *fails* it exits non-zero and writes nothing. Relay the flags.
4. **Deliver the file and a short note.** Hand over the `.drawio` and tell the practitioner: open it in diagrams.net / Draw.io, drag the boxes into place, or use **Arrange ▸ Layout** for a one-click auto-arrange. Note that nodes arrive on a plain grid by design.

**Where the host cannot run code**, say so plainly and do not hand-write the XML. The script is dependency-free, so offer the structured model and the one-line command for the practitioner to run themselves, or route to a format the host can produce directly (Markdown).

---

## Outputs

A single valid `.drawio` (mxGraphModel) file — plain rectangles for elements, plain edges for relationships, on a grid — importable and fully editable in diagrams.net / Draw.io. Styling and colour are the practitioner's to apply.

---

## Layout

A diagram has no unplaced state — every node needs coordinates, or they stack at the origin and cannot be separated. This version therefore does the minimum a diagram requires: nodes on a plain grid, spaced so each is separable. The practitioner rearranges them, or applies Draw.io's **Arrange ▸ Layout**.

Semantic layout — grid-by-layer, swimlanes, dependency-aware arrangement — is out of scope at this level. This section is where it can be added through further skill extensions.

---

## References

- `scripts/drawio_export.py` — the deterministic serializer. Dependency-free (Python standard library only).
- `tests/test_drawio_export.py` — a re-runnable test harness that checks the output with an independent parser (`python3 tests/test_drawio_export.py`).
- `../architect-exporter-archimate/references/model-input.md` — the shared neutral model contract this serializer consumes.

---

## Design notes

- A serializer, not a formatter — the same rationale as the ArchiMate serializer: strict, structured output belongs to a deterministic, self-validating script.
- Metamodel-agnostic, type-opportunistic. The serializer needs only a graph and does no type validation or metamodel lookup. When an element carries a type it is shown as a `«Type»` stereotype — an ArchiMate model shows its types, a plain graph stays plain — but the type string is rendered verbatim, so nothing wires this skill to the metamodel.
- Shared contract. The neutral model contract is owned by the ArchiMate serializer (`model-input.md`) and referenced here; the two serializers share it, and the Markdown formatter does not use it — it is a serializer concern, not an export-layer one.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — deterministic serializer: a dependency-free script emits a valid Draw.io diagram from a node/edge graph — boxes and arrows on a grid, with a «Type» stereotype on elements that carry a type. Grid layout only; no semantic layout. |
