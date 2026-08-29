# Archai Skills Registry

The single source of truth for the skills that currently exist in Archai. `architect` reads this to route, and `architect-suite` keeps it current. Only real, built skills appear in the table below — as each new skill is built, add its row. Intended-but-unbuilt skills live in the Roadmap, so the registry never points the router at something that isn't there.

## Skills

| Skill | Layer | Status | Handles |
|---|---|---|---|
| `architect-suite` | Meta | ✅ Active | Build, maintain, and evolve the suite: conventions, registry, contribution |
| `architect` | Base | ✅ Active | Practitioner entry point — interprets intent, holds context, routes to skills, names gaps |
| `architect-foundation` | Foundation | ✅ Active | Shared framework vocabulary and cross-cutting competencies; consulted by other skills |
| `architect-foundation-archimate` | Foundation (specialist) | ✅ Active | Shared ArchiMate 3.x metamodel reference; consulted by the extractor and export skills |
| `architect-sparring` | Functional | ✅ Active | Thinking companion — sharpens architectural thinking in dialogue; the suite's primary Socialise skill |
| `architect-extractor` | Functional | ✅ Active | Structures source material into ArchiMate-mapped understanding with confidence tiers; entry to the value chain |
| `architect-analyst` | Functional | ✅ Active | Analysis engine — turns architectural understanding into findings, a synthesis and prioritised recommendations, with an epistemic tier; current state oriented |
| `architect-designer` | Functional | ✅ Active | Design engine — turns architectural intent into an architectural model and grounded design decisions; target state oriented |
| `architect-exporter` | Functional | ✅ Active | Export layer entry point — determines the target format, secures the best input, and routes to the format specialist; prefers structured input, adapts to loose |
| `architect-exporter-md` | Functional (specialist) | ✅ Active | Markdown formatting specialist — maps document shapes (structure, narrative, records, groupings, relations, sequences, annotations) to Markdown constructs, faithfully and consistently |
| `architect-exporter-archimate` | Functional (specialist) | ✅ Active | ArchiMate serializer — a deterministic script emits and validates MEF XML (base model) from structured content |
| `architect-exporter-drawio` | Functional (specialist) | ✅ Active | Draw.io serializer — a deterministic script emits a valid `.drawio` diagram (plain boxes and edges on a grid) from structured content |

**Status legend:** 🔨 In progress · ✅ Active · 🔁 Under revision · ⚠️ Experimental

## Roadmap

Planned skills, added to the table above as each is built and validated:

- Functional skills — `architect-planner`, `architect-narrator`, `architect-governor`, `architect-evaluator`, `architect-researcher`
- Functional specialists — e.g. `architect-governor-quality`, `architect-evaluator-technology`; and further format specialists split out of `architect-exporter` as more output formats are added

Emergent candidates, to create only when a real, recurring need appears: further `architect-foundation-<topic>` and `architect-<function>-<specialisation>` extensions, etc.

## Adding a skill

See `../../../CONTRIBUTING.md`. When a new skill is built, add its row above; when its status changes, update it.
