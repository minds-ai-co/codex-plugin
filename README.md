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

Invoke a skill in plain language, or call the Minds MCP tools directly (e.g. `@minds query_panel ...`).

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
2. Open **Settings → API Keys → Personal**: <https://getminds.ai/?settings=api-keys&type=personal>
3. Click **Create key**, copy the `minds_…` value (shown ONCE).
4. Provide it as the `MINDS_API_KEY` environment variable. The plugin's MCP config
   (`.mcp.json`) reads the bearer token from `MINDS_API_KEY` (`bearer_token_env_var`).
   Because the marketplace entry uses `authentication: ON_INSTALL`, Codex prompts for
   it at install where supported; otherwise export it in your shell before launching
   Codex (`export MINDS_API_KEY=minds_…`).

The key lives in your environment / Codex secret store; the plugin never reads or
persists it — Codex injects it into the MCP `Authorization` header.

## Verify

After install:

```bash
codex plugin list
```

You should see `minds` listed with **4 skills** and **1 MCP server** (`https://getminds.ai/mcp`).

> **Smoke-test the auth path, not just registration.** `tools/list` is public on
> `getminds.ai/mcp`, so tools can appear even if the key isn't wired. Confirm a real
> authenticated call succeeds (below) — that is the check that proves `MINDS_API_KEY`
> is actually injected.

Then in a Codex session:

```
@minds list my panels
```

You should see your panels, or an empty list with a link to create one.

## Architecture

The plugin is a thin distribution wrapper around the Minds streamable-HTTP MCP server at `https://getminds.ai/mcp`. The Minds MCP tools (`list_minds`, `create_mind`, `query_panel`, `chat_with_mind`, etc.) become available as native Codex MCP tools after install. The bundled skills add anchored prompts so the LLM doesn't reinvent the polling / synthesis shape for common workflows.

```
Codex (CLI / IDE / app)
   │
   ├── .mcp.json → https://getminds.ai/mcp  (Bearer auth, streamable-http)
   │       └── Minds MCP tools (list_minds, create_mind, query_panel, ...)
   │
   └── skills/  (curated prompts for the 4 most common workflows)
```

No code runs locally beyond the plugin manifest. All inference and data live in the Minds webapp.

## Security & Privacy

- **Auth.** Personal API keys (`minds_…`). Keys are scoped to your Minds account.
- **Data.** Questions and answers traverse `getminds.ai`. Minds does not train on user content; see <https://getminds.ai/privacy>.
- **Local footprint.** The plugin ships skills (markdown) + a manifest. No binaries, no scripts, no telemetry from the plugin itself.
- **Revoke.** Delete the key in the webapp; the plugin loses access instantly.

Report security issues to **security@getminds.ai**.

## Support

- Docs: <https://docs.getminds.ai>
- Issues: <https://github.com/minds-ai-co/codex-plugin/issues>
- Email: <support@getminds.ai>

## License

MIT — see [LICENSE](./LICENSE).
