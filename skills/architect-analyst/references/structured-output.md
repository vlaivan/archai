# Structured Output Schema

The machine-readable form of an analysis, produced **on request** — when a downstream skill needs it, or the practitioner asks for it. It is the canonical hand-off representation when the analysis is passed to another skill.

It reuses the same finding, recommendation, and open-question **IDs** as the human-readable output (F1, R1, Q1, …), so it is a re-serialisation of the one analysis, not a second version of it. Produce it consistently so it can be passed downstream without transformation.

Never emit it truncated: if it will not fit in one response, segment it or write it to a file, and say which — a silently cut-off structured block is worse than none.

```json
{
  "analysis_metadata": {
    "analytical_question": "string — the restated problem",
    "scope": "enterprise | domain | solution | unclear",
    "management_level": "strategic | tactical | operational | mixed | unclear",
    "temporal_perspective": "current | target | gap | transition | mixed",
    "dimensions": ["motivation", "strategy", "business", "..."],
    "patterns_used": ["gap_analysis", "capability_assessment", "..."],
    "input_quality": "high | moderate | low | mixed",
    "overall_confidence": "high | moderate | low"
  },
  "inputs": [
    {
      "id": "I1",
      "type": "extractor_output | document | direct_input | inferred",
      "description": "string",
      "quality": "high | moderate | low"
    }
  ],
  "findings": [
    {
      "id": "F1",
      "statement": "string — a concise finding",
      "dimension": "string",
      "pattern": "string — the analytical pattern that produced it",
      "tier": "evidence_based | reasoned | conjectured",
      "significance": "high | medium | low",
      "basis": "string — the evidence or the reasoning steps",
      "related_input_ids": ["I1"],
      "related_finding_ids": ["F2"]
    }
  ],
  "synthesis": {
    "themes": [
      {"id": "T1", "theme": "string", "related_finding_ids": ["F1", "F3"], "implication": "string"}
    ],
    "answer": "string — the narrative answer to the analytical question"
  },
  "recommendations": [
    {
      "id": "R1",
      "recommendation": "string",
      "addresses_finding_ids": ["F1"],
      "confidence": "high | moderate | low",
      "rationale": "string"
    }
  ],
  "open_questions": [
    {
      "id": "Q1",
      "question": "string",
      "impact": "string — what would change if it were resolved",
      "priority": "high | medium | low"
    }
  ]
}
```

The `id` on each finding, recommendation, and open question is a handle local to the analysis: keep it stable and unique, and matching the ID in the human-readable output. A recommendation's confidence is capped by the weakest finding it rests on.
