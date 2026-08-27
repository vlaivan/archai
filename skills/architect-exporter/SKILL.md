---
name: architect-exporter
description: >
  The export layer's entry point. Use it whenever architectural content needs to become a concrete deliverable in a particular output format: it determines the target format, secures the best available input, and routes to the specialist that renders that format. Trigger on "export", "render", "produce a deliverable", "write this up as <a format>", "turn this into a document / model / diagram", or similar. It prefers structured architectural content from an upstream skill, and can arrange for structuring or fall back to loose content when needed. Do NOT use to extract or structure raw source material, to analyse or recommend, or to shape audience-tailored messaging (that is narration) — and do NOT render a format here; each format has its own renderer.
version: v1.0
---

# architect-exporter — Architecture Export Router

`architect-exporter` is the entry point to the export layer. It takes architectural content, determines which output format the deliverable must be in, secures the best available input, and routes the work to the specialist that renders that format. It does not render anything itself — rendering belongs to the format specialists.

Keeping the router separate from the renderers gives one predictable entry point for every export, one place that settles format and input quality, and format-specific rendering isolated in the skill that owns each format.

---

## When to use / when not to use

- **Use when** architectural content needs to become a deliverable in a specific output format.
- **Don't use when** the need is to *extract* structure from raw source, to *analyse* or recommend, or to shape audience-tailored messaging. This skill routes an export to the right renderer; it does not decide what to say, draw conclusions, or render a format itself.

---

## Inputs

Architectural content from upstream. Output fidelity follows the input, so prefer structure where you can get it:

1. **Prefer structured content.** Structured architectural output from an upstream producing skill — the extractor's structured-output block is one such form (`../architect-extractor/references/structured-output.md`), and other producing skills yield their own. Pass it through to the renderer: it already carries elements, relationships, tiers, and IDs.
2. **Structure it first when that is warranted.** When only loose content is available but a structured form would clearly give a better result, offer to have it structured first — turning raw material into structured understanding is the extractor's job — before routing.
3. **Fall back to loose content.** When structuring is not warranted or not wanted, route the loose content as given, and be explicit that the deliverable will inherit its looseness.

Accept structured content from whichever skill produced it; assume no single upstream schema.

---

## Method

1. **Determine the target format.** Establish which output format the deliverable must be in, and what it is for.
2. **Secure the best available input.** Apply the input ladder above — prefer structured, arrange structuring when warranted, or take the loose content as given.
3. **Route to the format's specialist.** Hand the content to the specialist that renders the target format. The export specialists and the formats they render are listed in the registry; Markdown deliverables are produced by `architect-exporter-md`.

---

## Outputs

A deliverable in the requested format, produced by that format's specialist. This skill's own output is the routing: the target format determined, the best input secured, and the work handed to the right renderer.

---

## References

- `../architect-extractor/references/structured-output.md` — one example of a structured input this skill can secure and pass through; other producing skills provide their own structured forms.

---

## Design notes

- A router, not a renderer. The skill's whole job is to determine the format, secure the best input, and dispatch. Format-specific rendering lives in the specialists, so the entry point stays thin and every format is handled the same way.
- Input fidelity is a preference, not a contract. Structured content gives the best result, so the skill seeks it — using it when present, arranging structuring when warranted, and passing loose content through as an honest fallback. It assumes no single upstream schema, since many skills produce content worth exporting.
- Rendering, narration, and analysis are elsewhere. Deciding what to say for an audience is narration; drawing conclusions is analysis; producing the bytes of a format is the specialist's job. The router does none of these.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — the export layer's entry point: determines the target format, secures the best available input, and routes to the format's specialist. |
