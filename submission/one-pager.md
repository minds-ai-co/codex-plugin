# Minds for Codex — Partner Brief

**One-line.** AI persona panels inside Codex: query simulated customers, founders, and domain experts on any decision, without leaving your editor.

**Plugin.** `codex plugin marketplace add minds-ai-co/codex-plugin` · <https://github.com/minds-ai-co/codex-plugin>

---

## What developers get

| Workflow | Before | After (with Minds plugin) |
|---|---|---|
| Spec review | LLM gives one generic take | Spec gets reviewed by 12 simulated personas covering your real user mix |
| Persona-driven product decisions | Hallucinated "as a user, I would..." | Grounded answers from named, parameterized personas you control |
| Red-team UX | Manual checklist | Adversarial-persona panel that finds the abuse cases |
| Customer interview prep | Write the questions, hope for the best | Dry-run your interview script against synthetic customers first |

All four flows are one skill invocation away once installed.

## What's in the box

- **4 anchored skills** — `query-panel`, `create-mind`, `sort-group`, `clone-voice`
- **MCP server** wired to the Minds MCP tools (`list_minds`, `create_mind`, `query_panel`, `chat_with_mind`, …) — _exact tool count TBD (tool curation in progress)_
- **Auth flow** — ON_INSTALL, personal API key, local secret store
- **Public OSS, MIT-licensed**

## Why Minds

- **Built for research, not chat.** Minds is the only platform purpose-built for multi-persona inference at scale. Group-level panels, formation-based subgrouping, alignment scoring per persona.
- **Battle-tested in production.** Active enterprise contracts (incl. VW 1000-mind factory simulation), several YC-portfolio customers, ~XXXX active accounts.
- **Standards-first.** Streamable-HTTP MCP, Bearer auth, no custom protocols. Same endpoint powers our Claude Code skill and our own webapp.
- **Privacy by default.** No training on user content. Personal keys. Hosted on getminds.ai with SOC2 Type 1 in progress.

## Traction snapshot (Sean to fill in)

- Active users: XXXX
- Panels run / week: XXXX
- Minds created (lifetime): XXXX
- Enterprise contracts: VW + N more
- ChatGPT Apps SDK listing: live since XXXX

## Distribution alignment

Minds already ships:

- ChatGPT App in the App Marketplace (live)
- Claude Code skill (live in skill marketplace)
- Hermes native MCP integration (community)
- This Codex plugin (this submission)

The Codex plugin is the same MCP surface delivered through Codex's official extension model — zero new surface area for OpenAI to maintain.

## Asks

1. Plugin Directory consideration ("Built by OpenAI" / featured tier).
2. Compliance/review checklist for the curated tier.
3. Co-marketing opportunities (cookbook PR, blog post, video).

---

**Contact.** Alexander, Co-founder · alex@getminds.ai · <https://getminds.ai>
