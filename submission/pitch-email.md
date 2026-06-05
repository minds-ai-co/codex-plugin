Subject: Minds — AI persona panels for Codex (plugin shipped, requesting Plugin Directory consideration)

Hi Codex team,

I'm Alexander, co-founder of Minds (getminds.ai). We've built a Codex plugin that lets developers query AI personas of real people — founders, customers, domain experts — directly from a Codex session, and I'd love your team's eyes on it for the Plugin Directory.

**The plugin (live now):** <https://github.com/minds-ai-co/codex-plugin>

```
codex plugin marketplace add minds-ai-co/codex-plugin
```

**60-second demo:** <LOOM URL — TODO before send>

**What it does.** Wraps our existing MCP server (24 tools) so Codex users can:

- `/minds-panel founders What do you think of this onboarding spec?` — run a real-time panel of synthetic personas across a question, get the spread of opinions inline
- `/minds-create "Marc Andreessen" expert VC,founder,contrarian` — spin up a persona in 30s
- Ask follow-ups conversationally — all 24 MCP tools (`list_minds`, `chat_with_mind`, `query_panel`, etc.) become native Codex tools after install

**Why it belongs in the Plugin Directory.**

1. **Net-new capability for Codex.** Today Codex users can spec-review with an LLM. With Minds they can spec-review against simulated customer / domain-expert reactions — closer to a real research signal, an order of magnitude cheaper than recruiting human research panels.
2. **Already battle-tested.** Minds powers panel research for VW (1000-mind factory simulation contract), several YC companies, and ~XXXX active users today. The MCP endpoint has been live and stable for 6+ months.
3. **Clean fit with the existing Codex affordances.** We use the official `.codex-plugin/plugin.json` manifest, ship 4 anchored skills, register through streamable-HTTP MCP, and follow the existing Codex auth surface (`policy.authentication: ON_INSTALL` + `secret: true` config). No custom protocol, no out-of-band binaries.
4. **Open source.** MIT-licensed, code is in the public repo, security policy is in `submission/security-privacy.md`.

**What we'd love from you.**

- Inclusion in the curated `Built by OpenAI` / featured shelf of the Plugin Directory, or guidance on what's missing for that consideration.
- Any compliance / review checklist we should run against — happy to fill in whatever's needed.
- If a cookbook entry would help, we have a draft ready: <COOKBOOK PR URL — TODO once opened>.

Attached:
- `one-pager.pdf` — partner brief, traction numbers, screenshots
- `security-privacy.pdf` — data handling, auth model, moderation, rate limits

Happy to jump on a 15-min call any time next week. Looking forward to hearing your thoughts.

Best,
Alexander
Co-founder, Minds
alex@getminds.ai
<https://getminds.ai>
