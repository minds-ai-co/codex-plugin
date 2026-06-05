---
name: create-mind
description: Create a new AI persona ("Mind") from a name + a few keywords. Use when the user says "make a mind of [person]", "spin up a persona for [role]", or wants a synthetic respondent for a panel. Wraps Minds `create_mind` MCP tool with the right `type` enum and fastest training mode.
---

# Create a Mind

A "Mind" is an AI persona of a real or fictional person, grounded in public data (or supplied context). Creation is async — the ID returns instantly, training runs in the background.

## When to load

- "Create a mind of [person name]"
- "Make a persona for [role / archetype]"
- "Spin up a synthetic [customer / founder / expert] for testing"

## Steps

1. **Pick the `type`.** This is a strict enum: `creative | expert | user`. The schema lies and lists it as a free string — Minds rejects everything else.
   - `expert` — domain SMEs, advisors, real named professionals
   - `creative` — fictional characters, archetypes, brand mascots
   - `user` — generic personas, customer segments, user archetypes (default)
2. **Pick the `mode`.** Default to `keywords` — fastest, skips profile generation. Use `clone` only when the user supplies extensive source material.
3. **Call `create_mind`** with `{name, type, mode, keywords: [...]}`. The response contains the `sparkId` embedded in a markdown link in `content[0].text` — that one IS safe to regex.
4. **Report status.** Training takes 30-120s. Tell the user the Mind exists and link them to `https://getminds.ai/?sparkId=<id>`. If they want to chat immediately, `chat_with_mind` works even mid-training.
5. **Do NOT poll to "done" by default.** `idle` does NOT mean done — it means no status row exists yet. `completed` means trained. Only block for completion if the user explicitly asks to wait.

## Pitfalls

- `type: "persona"` returns `MCP error -32602`. Use `user` for general personas.
- Status `idle` ≠ ready. Don't tell the user "your Mind is ready" based on `idle`.
- Voice cloning is a separate pipeline (`clonedVoiceStatus` on the Spark). Don't conflate.
- Mind creation always returns an ID instantly — don't wait on the create call itself before responding.
