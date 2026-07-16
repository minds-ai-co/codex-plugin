# Cookbook PR — body template

Use this as the PR description when opening the cookbook PR against `openai/openai-cookbook`.

---

## Pressure-test API designs with a synthetic customer panel inside Codex

This cookbook adds a new entry under `examples/codex_minds_plugin.md` that demonstrates running a multi-persona research panel from inside a Codex session, using the open-source [Minds Codex plugin](https://github.com/minds-ai-co/codex-plugin).

### What the entry covers

- Installing the plugin via `codex plugin marketplace add minds-ai-co/codex-plugin`
- Creating Minds (AI personas) and grouping them into a panel
- Running a panel question via the bundled `query-panel` skill
- Interpreting the synthesis output — surfacing dissent, not just consensus
- Iterating on a spec based on panel feedback
- Production tips: rate limits, key rotation, security/privacy posture

### Why this fits the cookbook

- Net-new Codex use case: synthetic user research from inside the editor
- Uses standards Codex already supports: `.codex-plugin/plugin.json`, streamable-HTTP MCP, skills
- Concrete, runnable example with a real public endpoint (no special access required beyond a free Minds account)
- Open-source plugin, MIT-licensed

### Checklist

- [x] New entry at `examples/codex_minds_plugin.md`
- [x] All commands verified against the plugin's current public release (v0.1.0)
- [x] Response shapes shown are representative (panel JSON output is real shape; persona quotes are illustrative — flagged in-text)
- [x] No keys or secrets in the entry
- [x] Linked from the cookbook README under Codex / Plugins section (TODO before opening — update `README.md`)

### Contact

- Author: Alexander, Minds AI
- Email: `alex@getminds.ai`
- Plugin repo: <https://github.com/minds-ai-co/codex-plugin>

Happy to iterate based on reviewer feedback.
