# Minds — Codex Plugin

**Query AI personas of real people — founders, customers, domain experts — without leaving Codex.**

Backed by [Minds AI](https://getminds.ai). Use it for spec review, persona-driven product decisions, UX research, and red-team panels right alongside your code.

---

## What you can do

| Skill | Trigger | Example |
|---|---|---|
| `query-panel` | "Ask my founders panel..." | `What would my customers panel think of this onboarding spec?` |
| `create-mind` | "Create a mind of..." | `Create a mind of Marc Andreessen, type: expert, keywords: VC, founder, contrarian` |
| `sort-group` | "Group my personas by..." | `Split my QA panel by seniority` |
| `clone-voice` | "Clone a voice onto..." | `Clone this audio sample onto my founder Mind` |

Plus slash commands:

- `/minds-panel <panel-name> <question>` — fire a panel question
- `/minds-create <name> <type> <keywords>` — spin up a new Mind

## Install

### Option 1 — One-line install (recommended)

```bash
codex plugin marketplace add minds-ai-co/codex-plugin
```

Then open Codex → **Plugins** → **Minds — AI Persona Panels** → install.

### Option 2 — Manual install

```bash
git clone https://github.com/minds-ai-co/codex-plugin.git ~/.codex/plugins/minds
mkdir -p ~/.agents/plugins
cp ~/.codex/plugins/minds/marketplace.json ~/.agents/plugins/marketplace.json
```

Restart Codex; the plugin appears in the Personal marketplace.

## Configure

You need a Minds API key.

1. Sign up at [getminds.ai](https://getminds.ai) (free tier available).
2. Open **Settings → API Keys → Personal**: <https://app.getminds.ai/?settings=api-keys&type=personal>
3. Click **Create key**, copy the `minds_…` value (shown ONCE).
4. Codex will prompt for `MINDS_API_KEY` on install — paste it there.

The key is stored locally by Codex's secret store; the plugin never reads it directly.

## Verify

After install:

```bash
codex plugin list
```

You should see `minds` listed with **4 skills**, **2 commands**, and **1 MCP server** (`https://app.getminds.ai/mcp`).

Then in a Codex session:

```
@minds list my panels
```

You should see your panels, or an empty list with a link to create one.

## Architecture

The plugin is a thin distribution wrapper around the Minds streamable-HTTP MCP server at `https://app.getminds.ai/mcp`. All 24 Minds MCP tools (`list_minds`, `create_mind`, `query_panel`, `chat_with_mind`, etc.) become available as native Codex MCP tools after install. The bundled skills add anchored prompts so the LLM doesn't reinvent the polling / synthesis shape for common workflows.

```
Codex (CLI / IDE / app)
   │
   ├── mcp config → https://app.getminds.ai/mcp  (Bearer auth, streamable-http)
   │       └── 24 MCP tools (list_minds, create_mind, query_panel, ...)
   │
   └── skills/ + commands/  (curated prompts for the 4 most common workflows)
```

No code runs locally beyond the plugin manifest. All inference and data live in the Minds webapp.

## Security & Privacy

- **Auth.** Personal API keys (`minds_…`). Keys are scoped to your Minds account.
- **Data.** Questions and answers traverse `app.getminds.ai`. Minds does not train on user content; see <https://getminds.ai/privacy>.
- **Local footprint.** The plugin ships skills (markdown) + a manifest. No binaries, no scripts, no telemetry from the plugin itself.
- **Revoke.** Delete the key in the webapp; the plugin loses access instantly.

Report security issues to **security@getminds.ai**.

## Support

- Docs: <https://docs.getminds.ai>
- Issues: <https://github.com/minds-ai-co/codex-plugin/issues>
- Email: <support@getminds.ai>

## License

MIT — see [LICENSE](./LICENSE).
