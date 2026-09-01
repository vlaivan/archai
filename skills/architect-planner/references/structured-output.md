# Structured Output Schema

The machine-readable form of a plan, produced **on request** — when a downstream skill needs it, or the practitioner asks for it. It is the canonical hand-off representation when the plan is passed to another skill.

It reuses the same **IDs** as the human-readable plan (TS1, W1, I1, PA1, …), so it is a re-serialisation of the one plan, not a second version of it.

Never emit it truncated: if it will not fit in one response, segment it or write it to a file, and say which — a silently cut-off structured block is worse than none.

```json
{
  "plan_metadata": {
    "planning_intent": "string — what this plan is designed to achieve",
    "scope": "enterprise | domain | solution",
    "management_level": "strategic | tactical | operational | mixed",
    "planning_horizon": "short | medium | long | mixed",
    "input_source": "design | analysis | direct_intent | mixed",
    "planning_foundation_quality": "high | moderate | low | absent",
    "hard_constraints": ["string"],
    "organisational_constraints": ["string"]
  },
  "transition_states": [
    {
      "id": "TS0",
      "name": "string",
      "description": "string — what the architecture looks like at this state",
      "value_delivered": "string — what the organisation gains by reaching this state",
      "is_current_state": true,
      "wave_id": "string — which wave delivers this state, null for current"
    }
  ],
  "waves": [
    {
      "id": "W1",
      "name": "string",
      "horizon": "string — e.g. 0-6 months",
      "purpose": "string",
      "transition_state_delivered_id": "TS1",
      "initiative_ids": ["I1"],
      "key_risks": ["string"],
      "organisational_constraint_notes": "string"
    }
  ],
  "initiatives": [
    {
      "id": "I1",
      "name": "string",
      "description": "string",
      "wave_id": "W1",
      "realises_design_decision_ids": ["DD1"],
      "depends_on_initiative_ids": ["string"],
      "enables_initiative_ids": ["string"],
      "indicative_scope": "small | medium | large",
      "constraint_type": "hard | organisational | assumption",
      "key_risks": ["string"],
      "planning_assumption_ids": ["PA1"]
    }
  ],
  "critical_path": {
    "description": "string — narrative of the critical path",
    "initiative_ids_in_order": ["I1", "I2"]
  },
  "planning_assumptions": [
    {
      "id": "PA1",
      "assumption": "string",
      "plan_dependency": "string — what part of the plan depends on this being true",
      "validation_priority": "high | medium | low",
      "impact_if_false": "string"
    }
  ],
  "open_planning_questions": [
    {
      "id": "PQ1",
      "question": "string",
      "impact_on_plan": "string",
      "priority": "high | medium | low"
    }
  ]
}
```

`realises_design_decision_ids` ties initiatives back to `architect-designer`'s `design_decisions` (DD-prefixed IDs), so a plan traces to the design it implements. Keep IDs stable and unique within the plan.
