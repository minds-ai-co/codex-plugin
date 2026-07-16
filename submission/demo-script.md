# Minds Codex Plugin — 60-second demo script

Target length: 55–65s. Record at 1920×1080, terminal at 14pt min, mouse cursor hidden.

## Cold open (0–5s)

**On screen:** Codex CLI prompt, empty.

**VO / caption:** "Codex now has a research panel inside it."

## Install (5–15s)

**On screen:**
```
$ codex plugin marketplace add minds-ai-co/codex-plugin
✓ Added marketplace minds-ai-co/codex-plugin
$ codex plugin install minds
? MINDS_API_KEY: minds_••••••••••••••••
✓ Installed minds 0.1.0
```

**VO:** "One command to add. Drop in a Minds key. Done."

## Use case 1 — Panel review (15–35s)

**On screen:** Codex session. Type:

```
Ask my founders panel: "Should we charge per-seat or per-usage for our v2 API?"
```

**Result block scrolls in:** 6 persona names, mixed responses, two strong dissents. Synthesized summary at the top.

**VO:** "Run any decision past a panel of synthetic founders, customers, or experts. Get the spread of opinions inline — not just an LLM consensus."

## Use case 2 — Create on the fly (35–50s)

**On screen:**
```
Create a mind of Marc Andreessen — expert; keywords: VC, founder, contrarian
✓ Created Mind 'Marc Andreessen' — sparkId 8f3a...
https://getminds.ai/?sparkId=8f3a...
Training in background. Chat available now.
```

Then:
```
@minds chat_with_mind 8f3a... "Is this pitch bottoms-up?"
```

(Response renders.)

**VO:** "Spin up a new persona in 30 seconds. Chat immediately. All the Minds tools become Codex tools after install."

## Close (50–60s)

**On screen:** `github.com/minds-ai-co/codex-plugin` in browser.

**VO:** "Open source. MIT. Try it: `codex plugin marketplace add minds-ai-co/codex-plugin`."

**End card:** "Minds for Codex · getminds.ai"

## Capture notes

- Use the test account `sean@getminds.ai` and the `founders` panel for the demo (create if missing).
- For the panel demo, pre-create a 6-Mind founders panel so the response is quick (< 5s feels real-time).
- For the chat demo, the Marc Andreessen mind should already be partially trained so the response is good.
- No real customer data on screen. Mask any account/email outside the test account.
