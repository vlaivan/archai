# Archai Skills Registry

The single source of truth for the skills that currently exist in Archai. `architect` reads this to route, and `architect-suite` keeps it current. Only real, built skills appear in the table below — as each new skill is built, add its row. Intended-but-unbuilt skills live in the Roadmap, so the registry never points the router at something that isn't there.

## Skills

| Skill | Layer | Status | Handles |
|---|---|---|---|
| `architect-suite` | Meta | ✅ Active | Build, maintain, and evolve the suite: conventions, registry, contribution |

**Status legend:** 🔨 In progress · ✅ Active · 🔁 Under revision · ⚠️ Experimental

## Roadmap

Planned skills, added to the table above as each is built and validated:

- `architect` — base skill: the practitioner's entry point and router
- `architect-foundation` (and `-<topic>` extensions) — cross-cutting foundational competencies and shared references
- Functional skills — `architect-extractor`, `architect-analyst`, `architect-designer`, `architect-planner`, `architect-narrator`, `architect-governor`, `architect-researcher`, `architect-sparring`
- Functional specialists — e.g. `architect-governor-quality`, `architect-exporter` (with `-archimate` / `-drawio` / `-md`), `architect-evaluator-technology`

Emergent candidates, to create only when a real, recurring need appears: a generic `architect-evaluator` parent; further `architect-foundation-<topic>` skills.

## Adding a skill

See `CONTRIBUTING.md`. When a new skill is built, add its row above; when its status changes, update it.
