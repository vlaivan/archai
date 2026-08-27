---
name: architect-foundation-archimate
description: >
  The ArchiMate metamodel foundation for Archai — the shared reference for ArchiMate 3.x layers, aspects, element types, and relationships. Consult it, or point to it from another skill, whenever architecture work needs to be grounded in the ArchiMate metamodel: classifying content into element types, choosing a relationship, or checking what a given ArchiMate concept means. Other skills (for example `architect-extractor` and the export skills) rely on it for the metamodel rather than carrying their own copies. Use directly when a practitioner asks what an ArchiMate element or relationship is, or how something should be classified. Do NOT use for method or output-format specifics — those live in the consuming skill; this foundation defines the metamodel, not how any one skill applies it.
version: v1.0
---

# architect-foundation-archimate — ArchiMate Metamodel Foundation

`architect-foundation-archimate` is the suite's shared knowledge of the ArchiMate 3.x metamodel. It is a foundation specialist: a single, canonical reference that other skills point to instead of each carrying — and restating, and drifting — their own copy of the element types and relationships.

It holds the metamodel itself — *what* the layers, aspects, elements, and relationships are. It deliberately does not hold usage-specific guidance — how to recognise an element in a messy transcript, or how to serialise one to a file format. That belongs to the consuming skill, which points here for the definitions and adds its own application on top.

---

## The metamodel

The full working reference — layers and aspects, element types by layer, and the common relationships with their notation — is in:

📄 `references/metamodel.md`

Read it when work spans multiple architectural dimensions, or when a classification is not obvious. The essentials below are enough to orient; the reference is the detail.

---

## How to use this foundation

- **Resolve the aspect, then the layer.** The active / behaviour / passive distinction — something that *acts*, something it *does*, something it *acts upon* — is the backbone of the core layers. Settle which aspect an element is before arguing about which layer.
- **Distinguish behaviour from structure.** A "service" is behaviour; the component that provides it is active structure. A named "system" is structure; what it *does* is a function.
- **Place information correctly.** A conceptual information entity is a Business Object; its concrete realisation processed by applications is a Data Object.
- **Prefer specificity, but never force it.** Where the correct type is genuinely unclear, use the most general honest type — Association for an untyped relationship, for instance — and record the ambiguity, rather than committing to precision the evidence does not support. Honest approximation over confident misclassification.
- **Cross-layer relationships are normal.** An Application Component serving a Business Process, a Business Process realising a Business Service — these are valid and expected.
- **When something falls outside this reference, say so.** It is selective, not exhaustive. Fall back to standard ArchiMate 3.x knowledge for any element, relationship, or rule it does not cover — flagging that you have gone beyond the reference — and treat the Open Group ArchiMate 3.x specification as the authority for anything that must be exact.

---

## Design notes

- Scope is the metamodel only. Extraction signals, export serialisation, and diagramming conventions are usage-specific and live in the skills that consume this foundation, so this reference stays neutral and reusable across all of them.
- The reference is selective by design — the elements most encountered in practice — with a note that the full ArchiMate set remains available. Breadth is added when a consuming skill demonstrates a real need for it.

---

## Version history

| Version | Date | Summary |
|---|---|---|
| v1.0 | 2026-08 | Initial release — ArchiMate 3.x layers, aspects, element types, and common relationships as a shared, usage-neutral reference for the suite. |
