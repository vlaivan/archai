# Archai — Vision & Framework

> An extendable suite of skills for AI-assisted architecture practice — enterprise, domain, and solution.

---

## 0. Identity

**Archai** is a Claude plugin: a suite of skills that support AI-assisted architecture practice. It is distributed as a Claude plugin and installs as `archai@vlaivan`. Its name comes from the Greek *arkhē*, reflecting its aim of giving a sound foundation for AI-assisted architecture work.

The suite is organised in an extendable (modular, composable) way — a single **`architect`** skill as the practitioner's entry point, a family of **`architect-foundation`** and **`architect-<function>`** skills for each facet of the work, and **`architect-suite`**, the meta-skill through which the community can build and evolve the suite itself further.

Archai's heritage is in systems thinking and the Enterprise Architecture (EA) discipline. Its framework draws on the theory around architecture value cycle, the SECI knowledge model and the ArchiMate metamodel — but its scope is the architect *role* at every altitude: **enterprise, domain, and solution**. The framework vocabulary below is stated in terms of "architecture" rather than "EA" to reflect that range, while remaining faithful to its EA lineage.

---

## 1. Purpose

Archai is a structured collection of skills designed to augment AI-assisted architecture practice. It is built to be genuinely useful from day one for individual practitioners, while being explicitly designed to scale — to architecture teams, Centres of Excellence, and coaching and consulting contexts.

The suite is not a collection of point solutions. It is a coherent system in which skills share a common conceptual foundation, a consistent design language, and clear relationships with one another. Skills are composable: the output of one becomes the input of the next, following the natural flow of architecture work and knowledge.

Two principles guide its growth. First, build from generalist skills towards specialist skills: the skill suite provides a framework usable for a wide range of generic architecture work, but can be optimised for more specific tasks through extension. Second, build to be extended by the community: the conventions, metadata, registry, and `architect-suite` meta-skill exist so that any practitioner can contribute a new skill that fits the whole.

---

## 2. Conceptual Foundation

The suite is grounded in two dimensions that shape how every skill is designed and how skills relate to one another.

### 2.1 Architecture Value Cycle

The architecture value cycle describes the activities that constitute architecture work, expressed as a sequence of practitioner-oriented phases. These are not strictly linear — real work moves fluidly across phases — but the cycle provides a shared vocabulary for describing what a skill does and where it sits in the flow of work.

| Phase | Description |
|---|---|
| Discovering | Identifying the architecture landscape — extracting, gathering and structuring understanding about the reality from various types of knowledge sources. |
| Analysing | Making sense of the architecture understanding that has been discovered — patterns, dependencies, gaps, scenarios and implications. |
| Designing | Shaping future architectures from principles towards blueprints and concrete delivery — goals, alternatives, constraints, solutions and transitions. |
| Planning & Implementing | Supporting the translation of architectural intent into reality through managed change — roadmaps, work packages and deliverables. |
| Enacting | Operating with and within the architecture on a daily basis in live real-life settings — using it, adapting it and sustaining it. |
| Governing | Maintaining architectural sustainability over time — setting direction, maintaining boundaries, ensuring compliance and supporting evolution. |

*Note: Some activities — such as modelling and communication — are cross-cutting practices that serve multiple phases rather than belonging exclusively to one. Skills that support these practices are designed accordingly.*

### 2.2 Knowledge Management Cycle (SECI)

The SECI model describes how knowledge moves through a practice — between tacit knowledge (held by people, embodied in experience) and explicit knowledge (documented, structured, shareable). It provides the epistemological backbone of the suite, shaping not just what each skill does, but how it handles knowledge.

| Quadrant | Description |
|---|---|
| Socialise | **Tacit → Tacit.** Sharing knowledge through interaction, dialogue and collaborative thinking. Example: structured sparring, workshop facilitation. |
| Externalise | **Tacit → Explicit.** Capturing implicit knowledge into structured, documented form. Example: transforming interview notes into architecture artefacts. |
| Combine | **Explicit → Explicit.** Synthesising and analysing structured knowledge. Example: gap analysis, capability assessment, roadmap synthesis. |
| Internalise | **Explicit → Tacit.** Making documented knowledge usable and actionable. Example: translating analysis into executive narratives or learning paths. |

Skills follow the SECI spiral: outputs from one quadrant naturally feed the next. Skills are not just individually useful — they chain together into coherent knowledge flows.

### 2.3 The Two-Dimensional Framework

Together, the architecture value cycle and the SECI model form the primary design space for the suite. Every skill is positioned within this space — describing both what it does (value cycle phase) and how it handles knowledge (SECI quadrant).

|  | Socialise | Externalise | Combine | Internalise |
|---|---|---|---|---|
| **Discovering** | | ● | | |
| **Analysing** | | ● | ● | |
| **Designing** | | ● | ● | ● |
| **Planning & Implementing** | | | ● | ● |
| **Enacting** | ● | | ● | ● |
| **Governing** | | ● | ● | ● |

*This matrix is illustrative. Many skills span multiple cells; positioning is refined as skills are built and used. Foundation skills are cross-cutting and are not confined to a single cell.*

---

## 3. Areas of Concern

Beyond these two dimensions, architecture work is always situated within a broader context. Three secondary areas of concern provide the scoping language for understanding where a skill applies and what it is working on. These do not structure the skills themselves, but inform how they are configured and applied.

### 3.1 Architecture Dimensions (Subject Matter)

The architectural subject matter in focus, aligned with and slightly adapting a layered model of architectural aspects made known and commonly applied by architecture frameworks (such as TOGAF and ArchiMate):

- **Motivation** — goals, drivers, principles, requirements
- **Strategy** — strategic direction, capabilities, value streams
- **Business** — processes, functions, roles, organisational structures
- **Information** — data, information structures, and semantics
- **Information Systems** — applications and the functions they support
- **Technology** — infrastructure, platforms, and technical components
- **Implementation & Migration** — transition architectures and change programmes

### 3.2 Management Levels

Architecture work occurs at different levels of organisational altitude. The same activity looks and feels different depending on the level:

- **Strategic** — long-horizon direction, enterprise-wide decisions, investment alignment
- **Tactical** — medium-term planning, domain-level design, programme architecture
- **Operational** — day-to-day architectural decisions, solution guidance, delivery support

### 3.3 Scoping Boundary

Architecture work is always bounded. The scope of a skill or engagement determines how broadly it needs to reason and what it can reasonably assume. Architecture work happens across all three levels — the architect role is the constant that spans them:

- **Enterprise** — the full organisation or a significant cross-cutting portion of it
- **Domain** — a defined business or technology domain within the enterprise
- **Solution** — a specific system, product, or initiative

---

## 4. Contextual Factors

A further set of tertiary contextual factors is noted here. These do not directly shape skill design at this stage, but become relevant as the suite matures — particularly as skills are adapted for different practitioners, organisations, and audiences. Examples of contextual factors include:

- **Subject Matter** — Domain-specific knowledge and conventions that shape how architectural concepts are interpreted and applied in a given industry or context.
- **Maturity Level** — The degree to which an organisation has developed its architecture capabilities, practices, and governance. A skill deployed in a nascent practice behaves differently than one operating within a mature Centre of Excellence.
- **Competence** — The skills, knowledge, and experience of the individuals using the suite. Distinct from organisational maturity — this is a practitioner-level factor.
- **Audience** — The intended recipient of architecture outputs. Role, background, and decision-making context all shape how knowledge should be framed and communicated.

---

## 5. Suite Architecture

The suite is built on a layered architecture: a single entry-point skill sits above two families of skills — foundation skills (cross-cutting) and functional skills (phase-based) — each of which may be extended by specialists as needs emerge. A meta-skill governs the design of the whole.

### 5.1 Layers

- **Base skill (`architect`)** — The single entry point for practitioners. It interprets intent, identifies the relevant value-cycle phase and SECI quadrant, and routes to the appropriate skill or skill chain. It also maintains context across interactions, enabling multi-step knowledge flows.
- **Foundation skills (`architect-foundation`, `architect-foundation-<topic>`)** — Cross-cutting architecture competencies and the shared reference knowledge many skills rely on, *not* tied to a single value-cycle phase: modelling notations, terminology, framework literacy, reference metamodels. `architect-foundation` is the generic foundation skill (shared glossary and general foundational guidance); `architect-foundation-<topic>` skills extend it with a specific body of knowledge. Foundation skills can be invoked directly, or consulted mid-flow by other skills, which point to them rather than copying their content.
- **Functional skills (`architect-<function>`)** — Skills that operate across the breadth of a value-cycle phase and all SECI quadrants. They are intentionally broad — designed to be immediately useful without requiring specialisation.
- **Functional specialists (`architect-<function>-<specialisation>`)** — Focused extensions of a functional skill, addressing specific subject matter areas, domains or methods. These emerge often from more specific practitioner needs and are layered underneath their parent.
- **Meta-skill (`architect-suite`)** — The builder-facing skill for creating, refining, and governing the suite itself. It sits deliberately within the `architect-` name family for immediate recognisability, but is scoped by its description to activate primarily when working *on* Archai itself.

Both the foundation and functional families follow *generic before specialised*: the generic skill comes first, and specialists (`-<topic>` or `-<specialisation>`) are added only when a real, recurring need is demonstrated.

### 5.2 Naming Convention

The plugin (`archai`) provides the namespace, so skills carry no brand prefix — they are invoked as `archai:<skill>`. Within that namespace, the **architect role** is the through-line:

| Layer | Pattern | Example |
|---|---|---|
| Base skill | `architect` | Entry point; routes to the skills below |
| Foundation generalist | `architect-foundation` | Cross-cutting competencies; shared glossary |
| Foundation specialist | `architect-foundation-<topic>` | `architect-foundation-archimate` |
| Functional generalist | `architect-<function>` | `architect-extractor`, `architect-analyst`, `architect-sparring` |
| Functional specialist | `architect-<function>-<specialisation>` | `architect-exporter-archimate`, `architect-governor-quality` |
| Meta-skill | `architect-suite` | Builder-facing; governs suite design (deliberate in-family exception) |

Rationale: the `architect-` stem is a *meaningful* discriminator (it signals the domain, which aids correct triggering) and it carries the full scope of the role — enterprise, domain, and solution — rather than narrowing to "EA". Two skill families sit under the base skill — foundation (cross-cutting) and functional (phase-based) — each with a generic form and optional specialists.

### 5.3 Metadata guidelines

Keep frontmatter light and write it well: good metadata serves two readers at once — a human scanning the suite, and the agent orchestrating it.

- **`name`** — the skill's identifier, following the naming convention.
- **`description`** — the field that matters most. Write it in the third person, stating what the skill does and when to use it, with concrete trigger phrases. It is what a person reads to understand the skill and what Claude reads to trigger and route to it, so make it fire when it should and stay quiet when it shouldn't.
- **`version`** — a simple `vMAJOR.MINOR` marker: bump MINOR for refinements that don't change the skill's essential behaviour or scope, MAJOR for a material change in what it does or how it behaves; `v0.x` is a draft, `v1.0` the first stable release once proven in practice.

Add other fields only where they genuinely earn their place — avoid metadata that is never exhaustive and quickly goes stale. A skill's **position** in the framework (value-cycle phase, SECI quadrant) is recorded once in the registry, not in each file; and **chaining** between skills is left to the model to interpret from descriptions and context rather than maintained as an explicit graph.

### 5.4 Foundation skills (`architect-foundation`)

Cross-cutting competencies and the reference knowledge shared across the suite are organised as **foundation skills** — an extensible family, not a single static module.

- `architect-foundation` — the generic foundation skill: shared terminology (a glossary of architecture and suite concepts) and general foundational guidance that many skills rely on.
- `architect-foundation-<topic>` — specialist foundation skills, each holding a specific body of knowledge or reference (for example, a modelling-notation or framework-literacy foundation).

Other skills **point to** the relevant foundation skill for this material instead of carrying private copies — giving contributors one canonical source to align to and keeping the suite free of duplication. Foundation skills can also be invoked directly when a practitioner needs that competency on its own.

The framework and design rationale in *this* document remain owned by `architect-suite`, since they are builder-facing.

### 5.5 Content guidelines

Write every skill to a common standard, so the suite reads as one system and is usable by both Claude and human practitioners:

- **Voice** — write the body as instructions for Claude: imperative and verb-first ("Parse…", "Identify…", "Produce…"), not documentation addressed to a user.
- **Substance** — include only concepts and instructions proven in practice and validated by concrete results — no slop. Every instruction should change what Claude does or produces.
- **Dual audience** — primarily Claude executing the skill, but also a human architecture practitioner reading it; any practitioner should be able to learn from it.
- **Progressive disclosure** — keep the SKILL.md lean; put long reference material, tables, and worked examples in `references/`, and shared references in the `architect-foundation` family (point to them, never copy).
- **Reference paths** — write every path relative to the skill's own directory, so it resolves both in the repository and in the installed plugin: `references/<file>.md` for a file in the same skill, `../<skill>/references/<file>.md` for a sibling skill's file, `../<skill>/` for the skill itself, and `../../<file>` for a repo-root file such as CONTRIBUTING.md (one `../` per level — from `references/` it is `../../../`). Never write a repo-root-relative path (`skills/…`) — it breaks once installed, because `skills/` sits at the plugin root.
- **Formatting** — write Markdown in soft-wrap style: one paragraph per line (no hard line breaks mid-paragraph), a blank line between paragraphs, and code blocks, tables, and YAML frontmatter left intact. Let the editor wrap long lines.

---

## 6. Design Principles

- **Composable by design** — Skills chain together, the output of one feeding the next. Chaining is interpreted from descriptions and context rather than hard-wired in metadata.
- **Generic before specialised** — Breadth before depth, in both families. Generic foundation and functional skills come first; specialists emerge when a genuine, recurring need has been demonstrated.
- **Context-aware** — Skills adapt to the areas of concern and contextual factors in play. The same skill may behave differently by audience, maturity level, or dimension.
- **Self-documenting** — A clear description plus the registry keep every skill legible — what it does, when to use it and where it sits — without heavy per-skill metadata.
- **Community-extensible** — The suite is designed to be extended by its community of contributors. Conventions, metadata, the registry and `architect-suite` exist so a new contribution fits the whole rather than fragmenting it.
- **Practitioner-led evolution** — Beyond the foundational skills, the roadmap is driven by practitioner experience and the natural pull of the value cycle and the SECI spiral — not upfront planning.

---

## 7. Current State & Roadmap

The suite has moved well beyond its founding skills; the live inventory, status, and routing detail are maintained in the single source of truth:

📄 `skills-registry.md`

The **base skill** (`architect`), a set of **foundation skills** (`architect-foundation` and its `-<topic>` extensions), and a full set of **functional skills** (`architect-<function>` and its `-<specialisation>` extensions) together cover cross-cutting competencies and every value-cycle phase across all four SECI quadrants. The roadmap is a **contribution backlog** rather than a plan — candidates emerge from real use.

---

## Appendix: Framework at a Glance

**Primary Dimensions**
- Architecture Value Cycle: Discovering · Analysing · Designing · Planning & Implementing · Enacting · Governing
- Knowledge Management Cycle (SECI): Socialise · Externalise · Combine · Internalise

**Secondary Areas of Concern**
- Architecture Dimensions: Motivation · Strategy · Business · Information · Information Systems · Technology · Implementation & Migration
- Management Levels: Strategic · Tactical · Operational
- Scoping Boundary: Enterprise · Domain · Solution

**Tertiary Contextual Factors**
- Subject Matter · Maturity Level · Competence · Audience

**Naming Convention**
- Plugin namespace: `archai` — skills invoked as `archai:<skill>`
- Base skill: `architect`
- Foundation: `architect-foundation` · `architect-foundation-<topic>` — e.g. `architect-foundation-archimate`
- Functional: `architect-<function>` — e.g. `architect-extractor` · `architect-analyst` · `architect-sparring`
- Functional specialist: `architect-<function>-<specialisation>` — e.g. `architect-exporter-archimate`
- Meta-skill: `architect-suite`
