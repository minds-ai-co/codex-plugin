# Minds Codex/ChatGPT Plugin

The `minds` plugin: skills + an MCP server config that let a host (ChatGPT/Codex desktop app, Claude Desktop) call Minds and render panel results as a rich in-conversation widget. This repo owns the **plugin packaging, marketplace submission readiness, and render-verification** — not the widget's server emission (that lives in `minds-ai-co/webapp`).

## Language

**Response Widget**:
The native, in-conversation widget that renders when Minds is installed as a plugin and a tool returns results. Server-emitted from `minds-ai-co/webapp` as a `ui://` HTML resource wired to the tool output; the host fetches and paints it. This is what "the widget" means.
_Avoid_: "the artifact", "scorecard artifact" (that's a different, rejected thing — see below).

**Claude artifact**:
A skill-driven scorecard drawn by Claude into its side-panel artifact surface (the abandoned "Path B", issue #3). **Explicitly NOT the deliverable** — the MCP must have nothing to do with it.
_Avoid_: using "widget" to mean this.

**Desktop app**:
The OpenAI desktop application. Codex and the ChatGPT desktop app are now **merged into one**; we call it "the ChatGPT/Codex desktop app". One of the two target hosts (with Claude Desktop).
_Avoid_: treating "Codex CLI" and "the desktop app" as the same surface — the CLI has no widget surface.

**Render-verification**:
Confirming the *current* webapp-emitted Response Widget actually renders in a target host — as opposed to *building* the widget. This workspace verifies; it does not build the server side.

## Minds domain terms (as seen in tool output)

**Panel**:
A multi-Mind research conversation. Contains `groups[]`, each with `sparks[]`. Results come from `get_panel_results`.
_Avoid_: study, survey, focus group (user-facing synonyms; canonical term is Panel).

**Mind / Spark**:
A Mind is a synthetic persona. In panel-results shape, personas appear as `sparks` (`{id, name, discipline}`) grouped under `groups`.
