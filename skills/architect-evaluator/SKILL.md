---
name: architect-evaluator
description: >
  The rated-assessment skill of Archai — it applies a defined rubric to a specific subject and produces a structured, confidence-scored, neutral rating. Distinct from `architect-analyst`, which makes sense of a situation without a fixed rubric, and from `architect-governor`, which interprets a rating against organisational stakes rather than producing the rating itself. Use it when the need is to rate, score, or classify something specific — a technology, a deliverable's quality, a vendor, a pattern — against a defined set of dimensions, each with its own criteria and confidence, independent of what any particular organisation would make of the result. Trigger on "evaluate", "assess", "rate", "score this against our criteria", or "is this a good fit" when a structured rubric (not free-form judgement, and not a compliance verdict) is what's wanted. On its own this skill is a thin dispatcher: it holds the shared rating *shape* (an ordinal tier scale plus separately-tracked confidence) and process, and routes to whichever `architect-evaluator-<subject>` specialist holds the actual dimensions, criteria, and tier labels for the subject at hand — check the registry for what's built, since this skill never hardcodes the roster. `architect-governor` is this skill's primary downstream consumer, not a sibling doing the same job differently. Do NOT use to make sense of a situation without a rubric (that is `architect-analyst`), to decide what a rating means for a specific organisation's compliance posture (that is `architect-governor`, which consumes this skill's output), or when no specialist for the subject exists yet (name the gap and hand back to `architect`).
version: v1.0
---

# architect-evaluator — Rated Assessment

`architect-evaluator` applies a defined rubric to a specific subject and produces a structured, neutral rating. Its distinguishing feature against its neighbours: `architect-analyst` reasons about a situation without a fixed scoring scheme; `architect-evaluator` scores a subject on a named set of dimensions, each with explicit criteria, producing a rating that stays neutral even when scored against a specific organisation's own criteria; `architect-governor` takes that rating and reasons about what it means for *this* organisation's principles, standards, and stakes — a distinct, downstream step, not a parallel one.

It is deliberately thin. The rubric — the dimensions, their criteria, and the words on the rating scale — belongs to a specialist extension (`architect-evaluator-<subject>`); this skill holds only what is common across any rated assessment: the *shape* of a rating (an ordinal scale with a colour convention, and confidence tracked separately from it), the shape of the process, and where a specialist plugs in.

---

## When to use / when not to use

- **Use when** a specific subject needs to be scored against a defined rubric — dimensions with named criteria, not open-ended reasoning, and not yet filtered through a specific organisation's stakes.
- **Don't use when** the need is to make sense of a situation without a fixed rubric (`architect-analyst`), to decide what a rating means for a specific organisation's compliance posture or governance process (`architect-governor` — hand this skill's output to it), or when the subject has no specialist rubric built yet. In that last case, name the gap rather than approximating a rubric that doesn't exist — hand back to `architect`.

---

## The rating shape

This skill mandates a *shape*, not a vocabulary. What every specialist shares:

- **An ordinal tier scale**, coloured 🟢 (best standing) → 🟡 (mixed) → 🔴 (worst standing), applied per dimension and overall. Three tiers is the default; a specialist may use more where its subject genuinely needs finer gradation, provided the colour convention still reads low-to-high.
- **The tier labels are the specialist's to choose**, fitted to what is actually being rated. What "good" looks like differs by subject — an adoption decision (Use / Consider / Avoid), a conformance-flavoured scale (Strong / Partial / Weak), a maturity scale (Advanced / Developing / Initial), or something else entirely. Pick words that describe the dimension's standing in terms native to the subject; do not force a specialist's vocabulary to fit an adoption frame it doesn't have. State the chosen labels and their meaning once, up front, in the specialist's own SKILL.md.
- **Confidence, tracked separately from the tier, always using the same three levels regardless of specialist:**

  | Confidence | Meaning |
  |---|---|
  | **High** | Grounded in documented evidence — public sources with citations, or internal records and formal decisions. |
  | **Medium** | Grounded in a credible but less certain basis — an informed stakeholder's considered view, a public source of moderate authority. |
  | **Low** | Grounded in limited, informal, or unverified input. A signal worth tracking, not a basis for the rating alone. |

A low-confidence rating at the best tier is more actionable than a high-confidence one presented without its basis — confidence is reported, never hidden inside the tier.

---

## Criteria basis

A rubric's dimensions and criteria default to general good practice for the subject — a specialist's own, subject-matter judgement of what "good" looks like, independent of any one organisation. This is the fallback, never a hardcoded assumption about any specific organisation's standards.

A specialist may also accept an organisation's own criteria as an override — a named standard, a re-weighting of the dimensions, a stricter threshold on one of them — supplied by the practitioner or drawn from organisation-specific documentation. This is a parameter to the method, not a different method: the dimensions, the tier shape, and the evidence-and-confidence discipline stay exactly as rigorous either way.

Whichever basis is used, state it plainly as part of the rating — "scored against general good practice" or "scored against [named organisational criteria]" — so a reader never mistakes one for the other. A rating scored against organisation-specific criteria is not governance's job done early: it is still a neutral score against a stated basis, and still needs `architect-governor`'s interpretive step to say what meeting or missing that basis means for this engagement, this stage, these stakes.

---

## Method

1. **Confirm the subject and its granularity.** The rubric must apply to something specific enough to be assessable and significant enough to be worth assessing — the specialist defines what "right-sized" means for its subject type; validate against it before proceeding.
2. **Load the specialist.** Check the registry for an `architect-evaluator-<subject>` specialist that holds the dimensions, criteria, and tier labels for this kind of subject — this skill never assumes or hardcodes which specialists exist, since the suite grows independently of this dispatcher's own release cycle. If none exists, say so plainly — this skill does not improvise a rubric or invent labels on the fly.
3. **Confirm the criteria basis.** Establish whether the rating scores against general good practice or against organisation-supplied criteria (see Criteria basis above); ask rather than assume if it's ambiguous.
4. **Apply the rubric.** The specialist owns dimension-by-dimension scoring, its tier labels, its evidence model, and how separate evidence lanes (e.g. public versus internal) combine. This skill's role is to hold the process shape consistent: scope first, evidence gathered and rated, dimensions synthesised into an overall rating with its logic made explicit.
5. **Synthesise and expose the logic.** An overall rating is a function of its dimension ratings — state that function (e.g. "any worst-tier rating on a hard-constraint dimension forces an overall worst-tier rating") rather than asserting a verdict. An undocumented override of the stated logic is a hunch, not a rating.

---

## Outputs

A rated assessment: the criteria basis it was scored against (general good practice, or named organisational criteria), dimension-by-dimension ratings (in the specialist's own tier labels) with confidence, an overall rating with its synthesis logic stated, key risks and highlights (each with why it's surfaced), and evidence gaps (what's missing, at what confidence, what would resolve it). The specialist defines the exact shape of the output and its tier vocabulary; this skill's contribution is that every specialist's output follows the same ordinal-scale-plus-confidence structure and states its criteria basis plainly, so a reader who knows one evaluator can orient quickly in another even when the words differ.

**Never present a rating as more complete or certain than it is.** If the subject has enough material that the full rated assessment will not fit in one response — the context window included — say so and segment it (or write it to a file, and say which), rather than letting it truncate silently.

---

## Interaction

- **Hand off to `architect-governor`** whenever the real question shifts from *how does this score* to *what does this mean for us*. Pass the full rating — dimension-by-dimension, with confidence, the stated synthesis logic, and the criteria basis — rather than just the overall tier, so governance has the evidence to reason from.
- **Hand back to `architect`** when no specialist exists for the subject, or to route a rating onward to whichever skill the practitioner's next need calls for.

---

## Design notes

- Deliberately thin. The rubric — dimensions, criteria, tier labels — is subject-matter expertise that belongs to a specialist, not to a router. This skill holds only what's genuinely common across any rated assessment: the shape of a rating, plus confidence.
- Shape, not vocabulary. The parent mandates an ordinal, colour-coded tier scale and a separately-tracked confidence axis. It deliberately does not mandate tier labels — different specialists want different words for what "good" looks like on their scale (an adoption decision, a conformance scale, a maturity scale), and forcing one vocabulary suite-wide would fit later specialists poorly.
- No specialist is named here. This skill discovers what's built by checking the registry each time it's invoked. Adding an `architect-evaluator-<subject>` extension should never require editing this dispatcher.
- Criteria are a parameter, not a hardcoded assumption. The generic rubric shape and good-practice default exist so this skill works for any organisation out of the box; an organisation's own criteria can override the default without becoming a different method, provided the basis is always stated plainly (see Criteria basis).
- Evaluation versus governance is a pipeline, not a fork. Evaluation produces a rating that is neutral — the same regardless of which organisation asked, even when scored against that organisation's own criteria. Governance is what happens next: translating the rating into what it means given a specific organisation's principles and stakes. Keeping the two separate means a rating stays reusable and trustworthy as a baseline, and governance's real work doesn't get hidden behind a rating that only looks neutral.
- The distinction from `architect-analyst` is load-bearing: analysis has no fixed rubric; evaluation scores a subject against dimensions with stated criteria and tier labels.
- Confidence as a first-class, separately-tracked signal, never folded into the tier, is the one piece of vocabulary this skill does fix suite-wide — it is genuinely subject-agnostic in a way tier labels are not.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — thin dispatcher holding a shared rating *shape* (ordinal, colour-coded tiers plus separately-tracked confidence) across `architect-evaluator-<subject>` specialists, discovered via the registry rather than named here; tier labels left to each specialist, a criteria basis (general good practice by default, organisation-supplied criteria as a stated override) left open to each; evaluation and governance framed as a pipeline, not parallel activities. |
