# Serializer Input Contract — the model JSON

The neutral shape the MEF serializer (`scripts/mef_export.py`) consumes. It is the serializer's *own* contract — elements and relationships with types and ids — not any one producer's schema. Whatever produced the content, the skill normalises it onto this before the script runs.

```json
{
  "name": "Model name",
  "documentation": "Optional model-level documentation.",
  "elements": [
    {
      "id": "E1",
      "name": "Order Management System",
      "type": "ApplicationComponent",
      "documentation": "Optional element documentation.",
      "properties": {"Owner": "Sales IT"}
    }
  ],
  "relationships": [
    {
      "id": "R1",
      "source": "E1",
      "target": "E2",
      "type": "Serving",
      "name": "Optional label",
      "documentation": "Optional relationship documentation."
    }
  ]
}
```

**Required:** each element needs `id` (unique in the model), `name`, and `type`; each relationship needs `source` and `target` (matching element ids) and `type`. Everything else is optional. Types are ArchiMate element and relationship types — see the metamodel foundation for the set.

**How the script treats it:**

- Unknown element types default to `ApplicationComponent`, unknown relationship types to `Association` — both flagged, never silently.
- A relationship whose `source` or `target` does not resolve to an element is skipped and flagged, rather than emitted as a dangling reference that would break import.
- `properties` become MEF string properties; `documentation` becomes MEF documentation.

**Accepted aliases (direct extractor output maps with no rewriting):** element `archimate_type` → `type`, `description` → `documentation`; relationship `source_element_id` → `source`, `target_element_id` → `target`, `archimate_relationship_type` → `type`. The extractor's `confidence`, `temporal_perspective`, and `source_reference` are carried through as properties (Confidence, Temporal, Source), so provenance survives into the tool.

**Normalising other producers onto the contract** (the skill's job, before the script runs):

- A design skill's *components* → elements; design decisions or rationale → element `documentation` or `properties`.
- A planning skill's *plateaus* → `Plateau` elements and *work packages* → `WorkPackage` elements; sequence and dependency → relationships (`Triggering`, `Flow`, or `Association`).
- Any producer's per-item markers → `properties`.

The rule is constant: the serializer keeps one strict contract; the skill maps each producer onto it.
