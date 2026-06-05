---
name: query-panel
description: Ask a panel of AI personas a single question and synthesize their answers. Use when the user wants "what would X think", "run this past my customers", "get the founder panel's take", or any multi-persona reaction. Wraps the Minds `query_panel` + `get_panel_results` MCP tools with the right polling shape so the LLM doesn't return early.
---

# Query a Minds panel

When the user wants a panel reaction, use this exact shape — don't reinvent the polling.

## When to load

- "What would [persona group] think about [thing]?"
- "Ask my [founders / customers / experts] panel: [question]"
- "Get a persona panel on this spec"
- Any product-decision moment where multi-perspective input would add signal

If the user wants to talk to ONE persona, use `chat_with_mind` directly via MCP — don't use this skill (it's for the multi-persona case).

## Steps

1. **Resolve the panel.** If the user named a panel ("founders panel", "qa panel"), call `list_panels` and match by name. If no panel exists yet, stop and tell the user — panel creation is a separate workflow (`/minds-create-panel`).
2. **Submit the question.** Call `query_panel(panelId, question)`. This is fire-and-forget — it returns "Question submitted..." instantly. Do NOT treat that as the answer.
3. **Poll for results.** Call `get_panel_status(panelId)` every 5s. Stop when status is `completed` (max 60s wait). If it's still running at 60s, surface that to the user and ask whether to keep polling.
4. **Pull and synthesize.** Call `get_panel_results(panelId)` once status is complete. Each persona returns an answer + alignment scores. Group by sentiment, surface dissenters, and quote the strongest 1-2 voices verbatim. Do NOT just paste the full JSON — synthesize.
5. **Cite the personas.** Use the format `— [Persona name](https://getminds.ai/?sparkId=...)`. The link is in `structuredContent.answers[].sparkId`.

## Pitfalls

- `query_panel` is fire-and-forget. Don't return its response as the answer — that's just the receipt.
- `get_panel_status` may return "Status check timed out. Use ... to retry." That's the tool's hint, not an error. Poll again.
- Don't average alignment scores into a single number — the dissent is the signal. Show the spread.
- IDs live in `structuredContent`, not the human-readable `text` block. Regexing UUIDs out of `text` will grab the wrong one.
