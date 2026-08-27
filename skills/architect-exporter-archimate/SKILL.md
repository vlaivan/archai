---
name: architect-exporter-archimate
description: >
  The ArchiMate serializer of the Archai export layer. Serializes structured architectural content into ArchiMate Model Exchange Format (MEF) XML — the Open Group's interchange standard, importable into Archi, BiZZdesign, and Sparx EA. Use it when the target deliverable is an ArchiMate model file. Trigger on "export to ArchiMate", "generate an ArchiMate model", "make a MEF file", "make this importable into Archi", or when `architect-exporter` routes an ArchiMate export here. It is deterministic: a bundled script emits and validates the XML, so it needs structured, typed content (elements and relationships carrying ArchiMate types) — loose content must be structured first. Do NOT use for other output formats (route through `architect-exporter`), to extract or analyse, or to render diagrams or prose. Base model only — elements, relationships, properties, and documentation; it does not produce diagram views or layout.
version: v1.0
---

# architect-exporter-archimate — ArchiMate MEF Serializer

`architect-exporter-archimate` turns structured architectural content into valid ArchiMate Model Exchange Format (MEF) XML, importable into ArchiMate-conformant tools.

It is a **serializer, not a formatter**: the XML is produced by a bundled, deterministic script — `scripts/mef_export.py` — not generated token by token. MEF has a strict schema (namespaces, a fixed child order, typed `xsi:type` values, and source/target references that must resolve), and hand-writing that risks subtly invalid output that will not import. A script gets it right every time, the same way, at any scale, and can *validate its own output* — which is the whole reason to prefer determinism here.

By the time content reaches export, the architectural interpretation has already happened upstream (the extractor and its siblings typed the elements and relationships). So this skill does no interpreting: it serializes what it is given.

---

## When to use / when not to use

- **Use when** the deliverable is an ArchiMate model file (MEF XML) for import into a modelling tool.
- **Don't use when** the target is another output format (route through `architect-exporter`); when content still needs *extracting* or *analysing*; or when the practitioner wants a rendered diagram (MEF is a data-exchange format, not a picture).

---

## Inputs

A structured, typed model — this is a serializer, so it needs structure it can encode. The script consumes a **neutral model contract of its own** — elements and relationships with types and ids — documented in `references/model-input.md`. It is not tied to any one producer's schema.

- **Its own contract, many producers.** The extractor's structured-output maps directly (its field names are accepted as aliases). Other producers — a design skill's components, a planning skill's plateaus and work packages — are *normalised onto the contract by this skill* before the script runs (see Method). The serializer keeps one strict contract; the skill absorbs the variety.
- **Loose content must be structured first.** A serializer cannot honestly guess types — that is the extractor's job. When only loose content is available, get it structured before serializing rather than inventing a model. For this format, structured input is effectively a precondition, not a preference — the point at which the export router's "prefer structured, structure first" ladder matters most.

The MEF *encoding* (the `xsi:type` spellings, the file structure) lives in this skill and its script. The *metamodel* — what the types mean — is defined in the foundation: `../architect-foundation-archimate/references/metamodel.md`. Consult it to resolve or sanity-check a type before serializing.

---

## Method

1. **Confirm structured, typed input — and normalise it onto the contract.** If the content is loose, structure it first (via the extractor) — do not hand a serializer un-typed content and let it default everything. If it comes from a producer other than the extractor, map its shape onto the model contract in `references/model-input.md` (components become elements; plateaus become `Plateau` elements and work packages `WorkPackage` elements, with sequence expressed as relationships; and so on). This normalisation is the skill's judgment; the script does none of it.
2. **Run the serializer.** Pass the model (as JSON) to the script:

   ```
   python3 scripts/mef_export.py INPUT.json -o MODEL.xml [--name "Model Name"] [--xsd schema/archimate3_Model.xsd]
   ```

   It maps each element and relationship type to its MEF `xsi:type`, generates stable identifiers, wires relationships by reference, carries documentation and properties (including confidence, temporal, and source markers) through, and emits the file in the schema-required order — deterministically.
3. **Read the script's report, then repair or relay.** The script always runs structural checks (well-formedness, every relationship endpoint resolves to a declared element, every type valid, identifiers unique) and, when a MEF XSD is available to it, validates against the official schema as well — the summary line states which level ran. It flags anything it defaulted or skipped (an unrecognised type, a relationship with a missing endpoint). If validation *fails* it exits non-zero and writes nothing; fix the input and re-run rather than shipping a broken file. Relay the flags.
4. **Deliver the file and a short note.** Hand over the `.xml` with counts, the validation level reached, any defaults or skips reported, and import instructions (Archi: *File > Import > Open Exchange File Format*). Do not summarise the model content — the practitioner inspects it in their tool.

**Where the host cannot run code**, say so plainly and do not fake the XML — a hand-written MEF file cannot be trusted to import. The script is dependency-free, so offer the structured model and the one-line command for the practitioner to run themselves, or route to a format the host can produce directly (Markdown).

---

## Outputs

A single valid MEF XML file — elements, relationships, properties, and documentation — importable into Archi, BiZZdesign, or Sparx EA.

---

## Layout

This version produces the model only, not diagram views. On import, the modelling tool holds the elements unplaced — Archi arranges them automatically — and the practitioner composes and lays out views in the tool.

View generation and diagram layout are out of scope at this level. This section is where they can be added through further skill extensions.

---

## References

- `references/model-input.md` — the neutral model contract the script consumes, its accepted aliases, and how to normalise other producers onto it.
- `scripts/mef_export.py` — the deterministic serializer. Dependency-free; uses `lxml` for XSD validation when both the library and a schema are present.
- `tests/test_mef_export.py` — a re-runnable test harness that serializes synthetic models and checks the output with an independent parser (`python3 tests/test_mef_export.py`).
- `../architect-foundation-archimate/references/metamodel.md` — the ArchiMate metamodel; consult to resolve or sanity-check a type before serializing.
- `../architect-extractor/references/structured-output.md` — one producer whose output maps directly onto the contract.

To enable authoritative validation, place the official ArchiMate MEF XSD (`archimate3_Model.xsd`) in a `schema/` folder beside the skill, or pass `--xsd`. It is not bundled (it is not redistributable); download it from The Open Group.

---

## Design notes

- A serializer, not a formatter. Strict, schema-validated output belongs to a deterministic script, not to token-by-token generation; that is the difference between this skill and the Markdown formatter. The script also validates its own output, which hand-written XML cannot.
- One strict contract, many producers. The script consumes a single neutral model contract; the skill normalises whatever produced the content onto it. That keeps the serializer strict and single-input while the export layer as a whole still assumes no single upstream schema.
- Interpretation and normalisation are the skill's; serialization is the script's. Typing content is upstream's job and mapping a producer's shape onto the contract is this skill's; by the time the script runs there is nothing to interpret.
- The MEF encoding lives here; the metamodel lives in the foundation. The `xsi:type` spellings and file structure are MEF-specific and belong to the serializer; what the types *mean* is `architect-foundation-archimate`'s, pointed to, not copied.
- Validation is layered and honest. Structural checks always run; authoritative XSD validation runs when the schema is available, and the output states which level was reached — it never claims schema-validity it did not perform.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — deterministic serializer: a dependency-free script emits ArchiMate MEF XML (elements, relationships, properties, documentation) from a neutral model contract, with layered validation (structural always; XSD when a schema is present). Base model only; no views or layout. |
