# Structured Output Schema

The machine-readable form of a design, produced **on request** — when a downstream skill needs it, or the practitioner asks for it. It is the canonical hand-off representation when the design is passed to another skill.

It reuses the same decision and element/relationship **IDs** as the human-readable design (DD1, E1, R1, …), so it is a re-serialisation of the one design, not a second version of it. Its `architecture` block is the suite's shared model shape, so the design renders to any export format without transformation.

Never emit it truncated: if it will not fit in one response, segment it or write it to a file, and say which — a silently cut-off structured block is worse than none.

```json
{
  "design_metadata": {
    "design_intent": "string — the purpose this design serves",
    "scope": "enterprise | domain | solution",
    "management_level": "strategic | tactical | operational | mixed",
    "temporal_perspective": "target_state | transition | both",
    "dimensions_in_scope": ["motivation", "strategy", "business", "..."],
    "grounding_quality": "high | moderate | low | absent",
    "input_source": "analysis | direct_intent | mixed",
    "overall_grounding": "principle-grounded | practice-based | judgement-heavy | mixed"
  },
  "design_direction": {
    "statement": "string — the core structural stance",
    "rationale": "string — why this direction",
    "alternatives_considered": [
      {"alternative": "string", "reason_not_chosen": "string"}
    ]
  },
  "design_decisions": [
    {
      "id": "DD1",
      "decision": "string — what was decided",
      "dimension": "string",
      "grounding_tier": "principle-grounded | practice-based | judgement-call",
      "grounding_basis": "string — the principle, pattern, or reasoning that grounds it",
      "rationale": "string",
      "alternatives_considered": ["string"],
      "implications": "string — what it constrains or enables elsewhere",
      "related_decision_ids": ["DD2"]
    }
  ],
  "architecture": {
    "_note": "elements and relationships in the suite's shared model shape (the export model contract). role_in_design and related_decision_ids tie each element back to the decisions that produced it.",
    "elements": [
      {
        "id": "E1",
        "name": "string",
        "type": "string — an ArchiMate element type",
        "temporal": "target | transition | both",
        "role_in_design": "string — why this element exists in this design",
        "related_decision_ids": ["DD1"]
      }
    ],
    "relationships": [
      {
        "id": "R1",
        "source": "E1",
        "target": "E2",
        "type": "string — an ArchiMate relationship type",
        "description": "string"
      }
    ]
  },
  "transition": {
    "applicable": true,
    "phases": [
      {
        "id": "TP1",
        "name": "string",
        "description": "string",
        "key_changes": ["string"],
        "dependencies": ["string"],
        "risks": ["string"]
      }
    ]
  },
  "open_design_questions": [
    {
      "id": "DQ1",
      "question": "string",
      "origin": "design_revealed | inherited",
      "impact": "string — what would change if it were resolved",
      "priority": "high | medium | low"
    }
  ]
}
```

The `architecture` block uses `id` / `name` / `type` / `source` / `target` — the export model contract's fields — so it feeds the serializers directly, no transformation. Keep ids stable and unique within the design.
