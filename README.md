# Archai

A Claude plugin for AI-assisted architecture practice — an extendable (modular, composable) suite of skills for enterprise, domain and solution architects. It covers foundational architecture competencies together with competencies tied to specific phases of the architecture value cycle (incl. discovery, analysis, design, planning & implementation, enactment and governance) as well as a meta-skill (`architect-suite`) for extending the suite.

This repository is a **single-plugin marketplace**: it *is* the `archai` plugin, and it also declares itself a Claude marketplace so it can be installed directly.

## Install

Archai is distributed as a single-plugin marketplace on GitHub (`vlaivan/archai`). Install it in whichever Claude surface you use — it is skills-only, so there is nothing to configure afterwards.

### Claude Code (CLI)

```
/plugin marketplace add vlaivan/archai
/plugin install archai@vlaivan
```

### Claude Desktop / claude.ai (UI)

1. Open the plugin settings and choose **Add marketplace**.
2. In the URL field, enter the repository — `vlaivan/archai`, or the full URL `https://github.com/vlaivan/archai` — and click **Sync**.
3. Once the `vlaivan` marketplace is added, install the **archai** plugin from it.

## Layout

```
.claude-plugin/
  marketplace.json          # marketplace 'vlaivan' → this plugin (source "./")
  plugin.json               # plugin 'archai'
skills/
  architect/                # base skill — practitioner entry point
  architect-foundation/     # shared set of foundational skills
  architect-*/              # extendable set of functional skills
  architect-suite/          # meta-skill — suite vision and principles
skill-template/             # copy this to start a new skill
CONTRIBUTING.md             # how to add a skill
LICENSE
```

## Contributing

Archai is designed to be extended. Start from `skill-template/`, follow `CONTRIBUTING.md`, and use the `architect-suite` skill to keep your contribution aligned with the framework. The framework itself is documented in `skills/architect-suite/references/vision.md`.

## License

See [LICENSE](LICENSE).
