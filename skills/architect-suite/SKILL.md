---
name: architect-suite
description: >
  The meta-skill for building, maintaining, and evolving Archai — the architecture-practice skill suite. Use this skill whenever working ON the suite itself rather than WITH it: designing a new architect-* skill, refining an existing one, making structural decisions about the suite, checking a skill's alignment with the vision and conventions, reviewing a contribution, updating the skills registry, or onboarding a contributor. Trigger on: "add/create a skill", "refine/rework a skill", "review a skill", "update the skill registry", "is this consistent with the framework", "how do I contribute to the suite", or similar. Always consult this skill before creating or modifying any architect-* skill. Do NOT trigger for architecture practice work itself — that is the `architect` base skill and the functional architect-* skills.
version: v1.0
---

# Architect Suite — Meta-Skill

This skill governs the design and evolution of **Archai**, the architecture-practice skill suite. It is the builder-facing counterpart to `architect`, the practitioner entry point.

- Working *on* the suite → use this skill.
- Working *with* the suite → use `architect`.

Archai is explicitly designed to be extended by its community of contributors. Making that contribution safe, coherent, and easy is a large part of this skill's job.

---

## First step: read the vision

Before any suite work, read `references/vision.md`. It is the north star — the conceptual framework, the areas of concern, the naming convention, the metadata guidelines, the content guidelines, the design principles, and the roadmap. Every decision below is made in service of it.

---

## The layers

Archai has a base skill and two skill families beneath it, plus this meta-skill:

- **`architect`** — the base skill; the practitioner's entry point and router.
- **Foundation skills** — `architect-foundation` (generic) and `architect-foundation-<topic>` specialists: cross-cutting competencies and shared reference knowledge not tied to a value-cycle phase.
- **Functional skills** — `architect-<function>` (generic) and `architect-<function>-<specialisation>` specialists: competencies tied to value-cycle phases.
- **`architect-suite`** — this meta-skill.

Both families follow *generic before specialised*.

---

## Core responsibilities

### 1. Designing a new skill

Work through these questions before drafting:

- **Need** — is it rooted in a real practitioner experience, or speculative? Prefer real.
- **Position** — which value-cycle phase(s) and SECI quadrant(s) does it serve? Use this as a design lens to check scope and spot overlaps; it is not tracked per skill. (Foundation skills are cross-cutting rather than phase-bound.)
- **Layer** — base, foundation, functional, or a specialist under one of the two families?
- **Name** — apply the convention: `architect-foundation` / `architect-foundation-<topic>` for a foundation skill; `architect-<function>` for a functional skill; and `architect-<function>-<specialisation>` for a functional specialist. The plugin provides the namespace; never add a brand prefix.
- **Content** — write it to the vision's content guidelines: imperative instructions for Claude, only proven instruction (no slop), progressive disclosure, readable by AI and humans.

Give the skill appropriate, lightweight metadata: at least a `name`, a strong `description`, and a `version`. The `description` does the work — it is what triggers and routes the skill and what a human reads to understand it, so write it for both. The framework (value-cycle phase, SECI quadrant) is a conceptual lens for designing and reviewing skills, not metadata tracked per skill; chaining is likewise left to the model to interpret from descriptions and context.

Reference material that more than one skill needs does not live inside the skill — it lives in the `architect-foundation` family (see *Foundation skills* below). Point to it; do not copy it.

### 2. Refining an existing skill

- Preserve the skill's name and `description` intent — change only what genuinely improves.
- Decide whether a refinement belongs in the generic skill, or should break out as a specialist (a `-<topic>` foundation specialist or a `-<specialisation>` functional specialist).
- If the change affects how `architect` routes to the skill, update its `description` and the registry entry.
- Record significant design decisions in the skill's SKILL.md under a `## Design notes` heading.

### 3. Maintaining suite coherence

Review periodically:

- **Naming** — every skill follows the convention; the base skill is `architect`; `architect-suite` is the one deliberate in-family exception.
- **Descriptions** — each skill's `description` is third-person, clear, and triggers well.
- **Registry hygiene** — `references/skills-registry.md` is the single source of truth for what skills exist and their status; update it whenever a skill changes, and keep the roadmap and the table honest (only built skills in the table).
- **Foundation skills** — cross-cutting competencies and shared references live in the `architect-foundation` family, not duplicated across skills. When you spot duplication, consolidate it into a foundation skill (adding an `architect-foundation-<topic>` if needed).
- **Vision alignment** — new and revised skills honour the framework, the content guidelines, and the design principles.

### 4. Evolving the vision

The vision is a living reference. When accumulated experience suggests the framework itself should evolve:

- Propose the change explicitly before editing `references/vision.md`.
- Record what is changing and why — preserve the reasoning, not just the outcome.
- Consider which existing skills need updating to reflect the change.

### 5. Onboarding a contributor

Archai is built to be extended by its community of contributors. To add a skill:

1. Copy `skill-template/` (or the nearest existing skill) as a starting point.
2. Name it by the convention and give it appropriate metadata.
3. Write the body to the vision's content guidelines — imperative instructions for Claude, with progressive disclosure. Point shared references to the `architect-foundation` family.
4. Add an entry to `references/skills-registry.md`.
5. Open a pull request.

See `CONTRIBUTING.md` (repo root) for the full walkthrough and the quality checklist.

### 6. Reviewing a contribution

Before a skill merges or is promoted to **Active**, review it against the vision's content guidelines and the naming and coherence conventions, across the same three dimensions as the `CONTRIBUTING.md` checklist:

- **Content quality** — well-written and usable by both Claude and a human practitioner; only proven, evidence-backed instruction — no slop.
- **Structure** — convention-compliant name; appropriate metadata (a third-person description that triggers well); body follows the content guidelines and progressive disclosure.
- **Coherence with the suite** — correctly placed and scoped; shared material in the `architect-foundation` family, not duplicated; references resolve; registry updated.

Be diagnostic first — name what needs to change and why. Maintainers may request changes to keep the suite coherent.

---

## Foundation skills

Cross-cutting competencies and shared reference knowledge are organised as **foundation skills**, an extensible family rather than a single static module:

- `architect-foundation` — the generic foundation skill: a shared glossary and general foundational guidance many skills rely on.
- `architect-foundation-<topic>` — specialist foundation skills, each holding a specific body of knowledge (for example, a modelling-notation or framework-literacy foundation).

When building or refining a skill, point to the relevant foundation skill rather than copying its content; when you find duplicated reference material, consolidate it into a foundation skill, extending the family with a new `architect-foundation-<topic>` if warranted.

---

## Current suite state

The live inventory and status are maintained in the single source of truth:

📄 `references/skills-registry.md`

**Status legend:** 🔨 In progress · ✅ Active · 🔁 Under revision · ⚠️ Experimental

---

## Design principles (summary)

Full statements are in `references/vision.md`:

1. Composable by design
2. Generic before specialised
3. Context-aware
4. Self-documenting
5. Community-extensible
6. Practitioner-led evolution

---

## Reference files

| File | When to read |
|---|---|
| `references/vision.md` | Always — framework, naming, and the metadata & content guidelines |
| `references/skills-registry.md` | Single source of truth for what skills exist and their status |
| `CONTRIBUTING.md` (repo root) | When onboarding or reviewing a contribution |
| `skill-template/` (repo root) | When scaffolding a new skill |

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release of the Archai meta-skill. |
