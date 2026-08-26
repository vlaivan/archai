# Contributing to Archai

Archai is built to be extended. A new skill should feel like part of the whole — the same conventions, the same metadata, the same way of chaining with its neighbours. This is the short version; the `architect-suite` skill is the full, authoritative guide (it reads the vision and helps you design a skill that fits).

## Before you start

- Read `skills/architect-suite/references/vision.md` — the framework, the naming convention, and the design principles.
- Skim `skills/architect-suite/references/skills-registry.md` — the live inventory, so you know what already exists and where a genuine gap sits.
- Prefer extending an existing skill over adding a narrow new one — *generic before specialised*.

## Add a skill

1. Copy `skill-template/` to `skills/<your-skill-name>/`.
2. Name it by the convention (the plugin provides the namespace, so **no brand prefix**):
   - foundational generalist skill → `architect-foundation`
   - foundational specialist skill extension → `architect-foundation-<topic>`
   - functional generalist skill → `architect-<function>`
   - functional specialist skill extension → `architect-<function>-<specialisation>`
3. Give it appropriate metadata (see the template and vision).
4. Write the body as instructions *for Claude* — imperative, lean, with longer material in `references/`. Point shared reference content to `architect-foundation` rather than copying it, or extend the foundational skills if necessary.
5. Add a row for your skill to `skills/architect-suite/references/skills-registry.md`.
6. Open a pull request.

## Quality checklist

### Skill content quality
- [ ] Skill is generally well-written and useful in real-life architecture practice.
- [ ] Skill is readable and presented in a form usable by both AI and human users — any architecture practitioner could benefit from the skill, be it a human architect or an AI agent performing an architecture task.
- [ ] Skill has a theoretical grounding while considering practical usability.
- [ ] Skill contains only concepts and instructions proven in practice and validated by concrete results and deliverables — no slop.

### Skill structure
- [ ] Skill name follows the suite convention.
- [ ] Skill has appropriate metadata as guided by the suite convention.
- [ ] Skill description is written third-person, describes clearly what the skill does and supports appropriate triggering.
- [ ] Skill follows the content guidelines of the suite.


### Skill coherence with suite
- [ ] Skill is scoped and positioned appropriately in relation to the overall suite framework — not too generic and not too specific for its purpose.
- [ ] Skill is structurally coherent — shared reference material lives in `architect-foundation` or its extensions, it is not duplicated across skills — skill is under correct `architect-*` functional skill or its extensions.
- [ ] Skill's references to other skills are correct and written relative to the skill's own directory (`../<skill>/…`) — no broken links, no repo-root-relative paths.
- [ ] Skill is synced with `architect-suite` and skill registry is updated.

## Review

Use the `architect-suite` skill to check a contribution against the conventions before it merges. Maintainers may request changes to keep the suite coherent.

## License

By contributing, you agree that your contributions are licensed under the repository's [LICENSE](LICENSE).
