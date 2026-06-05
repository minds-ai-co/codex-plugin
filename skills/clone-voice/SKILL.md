---
name: clone-voice
description: Clone a voice onto an existing Mind so panel answers can be played back in that voice. Use when the user uploads an audio sample or asks "make [Mind] sound like [person]". Wraps the voice-cloning pipeline on top of `chat_with_mind`.
---

# Clone a voice onto a Mind

Voice cloning is a parallel pipeline to training — it runs separately and writes `clonedVoiceStatus` on the Spark row.

## When to load

- "Clone [person]'s voice onto [Mind name]"
- "Make [Mind] sound like this audio"
- "Add voice to my [Mind]"

## Steps

1. **Verify the Mind exists** via `list_minds`. Grab the `sparkId`.
2. **Direct the user to the webapp for the upload step.** Voice samples are uploaded via the Mind detail page at `https://getminds.ai/?sparkId=<id>` — there's no MCP tool for uploading audio yet (P2 work). Give them the deep link.
3. **Poll `clonedVoiceStatus`** by calling `get_mind_status(sparkId)` — the response includes voice status as a separate field. `completed` means the voice is usable.
4. **Test it.** After completion, `chat_with_mind(sparkId, "say hello", { voice: true })` returns an audio URL.

## Pitfalls

- Voice and training status are independent. A Mind can be trained-not-voiced or voiced-not-trained.
- No MCP upload tool yet — direct users to the webapp. Don't promise CLI-only voice cloning until P2 ships.
- Voice cloning has a different consent surface than training. The webapp UI handles consent prompts; the MCP path does not.
