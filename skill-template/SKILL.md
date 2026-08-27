---
name: architect-<name> # architect-foundation-<topic> | architect-<function> | architect-<function>-<specialisation>
description: >
  <One paragraph, third person. State what the skill does and WHEN to use it, and name concrete trigger phrases a user would actually say. Write it to fire when it should and stay quiet when it shouldn't. This description is what triggers and routes the skill, and what a human reads to understand it — write it well for both.>
version: v1.0
---

<!--
This is a scaffold, not a conformance spec. The sections below suit a transform-style skill (Inputs → Method → Outputs); a behavioural or dialogue skill legitimately differs in structure — adapt the shape to the skill's nature. What is binding is the content guidelines, not this layout.

Write to the vision's content guidelines (../skills/architect-suite/references/vision.md): instructions for Claude (imperative), only proven instruction (no slop), progressive disclosure (lean body, detail in references/), readable by both AI and human practitioners. Give the skill appropriate metadata — the `description` is the field that matters most. A skill's position (value-cycle phase, SECI quadrant) lives in the skills registry, not here.
-->

# <Skill title>

<One or two sentences: the skill's job, in the practitioner's terms.>

## When to use / when not to use

- Use when: <...>
- Don't use when: <hand off to which sibling skill instead>

## Inputs

<What it accepts — direct practitioner input, or output from which upstream skill(s).>

## Method

<The steps Claude follows. Imperative ("Parse…", "Identify…", "Produce…"). Keep this SKILL.md lean; put long reference material in `references/`, and point shared reference content to the `architect-foundation` family rather than copying it.>

## Outputs

<What it produces, and which downstream skill(s) can consume it.>

## References

<Optional. Files under `references/`, and/or a pointer into the `architect-foundation` family.>

## Design notes

<Optional. Significant design decisions and the reasoning behind them.>

## Version history

<Newest first, one row per notable change. Use vMAJOR.MINOR — bump MINOR for refinements that don't change the skill's essential behaviour or scope, MAJOR for a material change in what it does or how it behaves. v0.x = draft; v1.0 = first stable release once proven in practice.>

| Version | Date | Summary |
|---|---|---|
| <Version number.> | <Date of change.> | <Summary of key changes.> |
