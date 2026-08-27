# Structured Output Schema

The machine-readable form of an extraction, produced **on request** — when a downstream skill needs it, or the practitioner asks for it. It is the canonical hand-off representation when the extraction is passed to another skill.

It reuses the same element, relationship, and gap **IDs** as the human-readable tables (E001, R001, G001, …), so it is a re-serialisation of the one extraction, not a second version of it. Produce it consistently so it can be passed downstream without transformation.

Never emit it truncated: if it will not fit in one response, segment it (by layer or section) or write it to a file, and say which — a silently cut-off structured block is worse than none.

```json
{
  "extraction_metadata": {
    "source_description": "string",
    "scope": "enterprise | domain | solution | unclear",
    "management_level": "strategic | tactical | operational | mixed | unclear",
    "temporal_perspective": "current | target | transition | mixed | unclear",
    "material_quality": "high | moderate | low",
    "archimate_layers_covered": ["motivation", "strategy", "business", "..."]
  },
  "elements": [
    {
      "id": "E001",
      "name": "string",
      "archimate_type": "string — e.g. BusinessProcess, ApplicationComponent",
      "archimate_layer": "motivation | strategy | business | information | information_systems | technology | implementation_migration",
      "confidence": "confirmed | inferred | assumed",
      "source_reference": "string",
      "temporal_perspective": "current | target | transition | unclear | null",
      "description": "string — optional",
      "properties": {}
    }
  ],
  "relationships": [
    {
      "id": "R001",
      "source_element_id": "string",
      "target_element_id": "string",
      "archimate_relationship_type": "string — e.g. Association, Composition, Serving",
      "confidence": "confirmed | inferred | assumed",
      "source_reference": "string",
      "description": "string — especially for inferred relationships"
    }
  ],
  "gaps": [
    {
      "id": "G001",
      "type": "missing_element | missing_relationship | conflict | ambiguity",
      "description": "string",
      "priority": "high | medium | low",
      "clarification_needed": "string"
    }
  ],
  "assumptions": [
    {
      "id": "A001",
      "element_or_relationship_id": "string",
      "assumption_text": "string",
      "basis": "string"
    }
  ]
}
```

The `id` on each element and relationship is a handle local to the extraction: it keeps relationships wired to the right elements and gives a consumer an unambiguous reference. Keep it stable and unique within the extraction, and matching the ID in the human-readable tables. Whether a downstream consumer keeps these identifiers or re-maps them to its own scheme is its decision — the extractor guarantees a self-consistent extraction, not a final model identity.
