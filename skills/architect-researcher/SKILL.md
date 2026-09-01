---
name: architect-researcher
description: >
  The external-evidence skill of Archai — it grounds architecture work in what the world knows: standards, reference architectures, industry patterns, frameworks, benchmarks, peer practice. Use it whenever architecture work needs external grounding rather than internal understanding. Trigger on "what does industry practice look like", "are we aligned with the standard", "what do others do", "is there a reference architecture for...", "benchmark this against...", or "research this for me". Also useful mid-flow from another skill — analysis filling an evidence gap, design seeking reference patterns, governance checking conformance against a named standard, sparring grounding a challenge. Works standalone or as a service callable by any skill. Produces a research brief with sourced, tiered findings, ready to use directly or pass to another skill. Do NOT use to make sense of internal material (that is `architect-extractor` or `architect-analyst`), to design or govern from the evidence once gathered (their own skills), or to think a problem through in dialogue (`architect-sparring`).
version: v1.0
---

# architect-researcher — External Architecture Evidence

`architect-researcher` grounds architecture work in external evidence. Where `architect-extractor` asks *what do we know internally*, this skill asks *what does the world know — and what does it mean for this problem?*

Its core job is turning distributed, often implicit external knowledge — standards bodies, reference frameworks, analyst reports, academic literature, peer practice — into a structured, explicitly sourced research brief that other skills can consume directly. It is as much a service skill as a standalone one: invoked to build an evidence base at the start of a piece of work, or called mid-flow from another skill when a specific external question needs answering before that work can continue.

---

## When to use / when not to use

- **Use when** architecture work needs grounding in external evidence — a standard, a reference architecture, industry pattern, benchmark, or peer practice.
- **Don't use when** the need is to make sense of *internal* material (`architect-extractor`, `architect-analyst`), to design, plan, or govern from evidence once it's gathered (their own skills), or to think a problem through in dialogue (`architect-sparring`). Hand those back to `architect` to route, or return control to the calling skill if invoked mid-flow.

---

## Inputs

- **A standalone research request** — a question the practitioner wants grounded in external evidence.
- **A mid-flow call from another skill** — the research question typically arrives pre-framed (e.g. "find reference patterns for event-driven integration in financial services"). Accept the framing, but verify what kind of question it actually is: what exists (reference patterns), what is recommended (best practice), what is required (standards conformance), or what is emerging (technology assessment) — these need different sources.

Frame dimensions using `architect-foundation`; name element and relationship types from `architect-foundation-archimate` where a finding bears on the metamodel.

---

## Source taxonomy

Every finding is tagged with a source type, which sets its epistemic weight:

| Type | Label | Description | Weight |
|---|---|---|---|
| Standard | 🏛️ | Normative standards: ISO, IEEE, NIST, W3C, OMG, etc. | Highest — defines conformance baselines |
| Framework | 📐 | Established frameworks and methodologies: TOGAF, ArchiMate, ITIL, COBIT, Zachman, SAFe, etc. | High — widely adopted reference practice |
| Analyst | 📊 | Research and advisory publications: Gartner, Forrester, IDC, McKinsey, etc. | Moderate-high — curated but commercially positioned |
| Vendor | 🏢 | Reference architectures, whitepapers, technical documentation from technology vendors | Moderate — authoritative on their own products; interest-affected on broader claims |
| Academic | 🎓 | Peer-reviewed research, conference papers, journal articles | Moderate-high for theoretical claims; variable for applied practice |
| Case study | 📋 | Published peer practice: organisation case studies, implementation reports | Moderate — specific context may limit transferability |
| Community | 💬 | Practitioner forums, open-source documentation, widely-cited posts from recognised practitioners | Low-moderate — useful for emerging practice; uneven quality |

Where a finding rests on multiple source types, note the combination — convergence across independent types significantly strengthens a finding.

## Confidence model

Every finding carries an epistemic status, mirroring the confidence models used across the suite:

| Tier | Label | Meaning |
|---|---|---|
| ✅ | **Established** | Consistently supported by high-weight sources (standards or frameworks), or strong convergence across multiple independent source types. |
| 🔶 | **Emerging** | Supported by credible sources but lacking the depth, breadth, or maturity of established practice — evolving standards, nascent patterns, analyst projections. |
| ❓ | **Indicative** | Based on limited, low-weight, or dated sources. A signal, not a foundation — should not anchor significant decisions without further validation. |

When much of a brief is Indicative, say so prominently — the evidence base is thin, and the practitioner should factor that into how they use the findings.

---

## Method

1. **Frame the question.** State the specific question the research answers — not necessarily the practitioner's original words, but the underlying question the right evidence would resolve. For a mid-flow request, verify which kind of question it actually is (what exists / what is recommended / what is required / what is emerging) before searching. Scope it: which dimensions it bears on, domain-specific or domain-agnostic, established/emerging/forward-looking, any standards the practitioner already works to, and the depth needed. State the plan briefly before searching — what you intend to look for and where — so the practitioner can redirect before effort is spent.
2. **Search with discipline.** Prefer highest-weight sources first — standards and frameworks before analyst reports, before vendor content, before community sources — except where the question type calls for a different order (emerging-practice questions often surface fastest in community and case-study sources; weight them accordingly but flag the limits). Prefer primary sources over secondary summaries. Search iteratively: after each search, assess whether it answers, partially answers, or redirects the question, and adjust. Define what "good enough" looks like and stop there rather than searching exhaustively.
3. **Extract findings.** For each source: the specific finding relevant to the question, the source (name, type, date), the epistemic tier, and the direct implication for the practitioner's problem — kept explicitly separate from what the source itself says, since most sources do not speak directly to the specific problem and the inference bridging that gap should be visible and owned. Keep findings atomic — one claim each.
4. **Synthesise.** Identify convergences (where independent sources agree — the strongest findings), divergences (where they conflict, often signalling genuine complexity or an evolving field), and gaps (where the evidence is thin or silent). Assess overall evidence strength: strong enough to act on, or directional only.

---

## Outputs

A research brief, always produced (unlike the conversational skills, research is a deliverable by default):

- **Research question** — the specific question addressed, confirming any reframing from the original request.
- **Scope and approach** — dimensions, domain context, temporal frame, source priority: brief.
- **Findings** — a table (finding, implication for this problem, source, type, tier), with narrative beneath for any finding whose implication is non-obvious.
- **Synthesis** — convergences, divergences, and an overall strength assessment.
- **Evidence gaps** — what wasn't found, or found only weakly; prioritised, not exhaustive.
- **Recommended use** — which findings are strong enough to anchor decisions, which are directional signals, which need further validation.

Never present a brief as more conclusive than the evidence supports — a thin evidence base presented with false confidence is worse than an honest gap.

---

## Interaction

- **Mid-flow invocation.** Confirm the specific question before searching, scope narrowly to what's needed (don't expand into a general survey unless asked), return findings in a form the calling skill can use immediately, and return control once done. If something significant surfaces that reframes the calling skill's work, flag it — that's a signal to surface, not suppress — but otherwise stay within the ask.
- **Iterative research.** For broad or multi-part questions, answer one part, present it, confirm direction, then continue — this avoids wasted effort if early findings reframe what's actually needed.
- **Hand off downstream.** A substantial brief is a natural input to analysis (as an evidence source), design (as reference patterns), governance (as a baseline), or sparring (as ammunition for a position). Name the natural next move and pass the brief's findings directly.
- **Hand back to `architect`** when the practitioner's need turns out not to be research at all.

---

## Design notes

- The researcher externalises; it does not analyse, design, or govern from what it finds — those steps belong to the receiving skill.
- Source type and epistemic tier are tracked separately and both matter: a single Standard-tier source can outweigh several Community-tier ones, but convergence across independent types is itself evidence.
- The implication gap is the skill's distinctive contribution: a finding without a stated implication for the practitioner's specific problem is half the job — search is how you get the material, the bridge from source to problem is the job.
- Output-by-default (rather than conversational-by-default, as in the analytical skills) reflects that research produces a deliverable meant for reuse, not a dialogue that converges toward one.
- No structured hand-off form. Unlike the extractor/analyst/planner chain, nothing downstream references a research finding by ID — it's read and reasoned from, not indexed into. A structured form is worth adding if a real consumer with an ID-based need for one emerges.
- Framework and stances live in `architect-foundation`; element and relationship types in `architect-foundation-archimate`. Pointed to, not restated.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — grounds architecture work in external evidence: seven-type source taxonomy with explicit epistemic weight, three-tier confidence model (Established / Emerging / Indicative), source-to-implication bridging as the skill's distinctive act, callable standalone or mid-flow from any skill; output-by-default, prose only — no structured hand-off form, as nothing downstream references a finding by ID. |
