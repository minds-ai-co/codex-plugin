# Codex Plugin Directory — Submission Packet

This folder contains everything we hand to OpenAI Codex BD when pitching for inclusion in the curated **Plugin Directory** (the "Built by OpenAI" / featured tier shown in `Make Codex work your way`).

## Contents

| File | Purpose |
|---|---|
| `pitch-email.md` | Cold outreach email to OpenAI Codex partnerships. Send from alex@getminds.ai. |
| `one-pager.md` | Single-page partner brief — what Minds is, what the plugin does, traction numbers. Render to PDF before sending. |
| `demo-script.md` | 60-second screen-recorded demo walkthrough — what to show, what to say. |
| `security-privacy.md` | Data handling, auth model, content moderation, rate-limit attestation. The "boring but required" doc. |
| `screenshots/` | 3 reference screenshots: install flow, panel query, results synthesis. Capture before sending. |
| `compliance-checklist.md` | Self-attestation matching every published item in the Codex Apps SDK submission guidelines we could find. |

## Submission paths (ranked)

1. **Direct BD email** (`pitch-email.md`) — primary path. Address: `partnerships@openai.com`, cc `developers@openai.com`. There is no public submission form for the curated Plugin Directory as of 2026-06-05.
2. **Codex for Open Source program** — <https://developers.openai.com/codex/learn/programs/codex-for-open-source>. We qualify if we open-source the plugin repo (already MIT-licensed). Apply in parallel for additional surface area.
3. **OpenAI Cookbook PR** — submit a cookbook entry at <https://github.com/openai/openai-cookbook> showing "AI persona research from Codex via the Minds plugin". Cookbook curators are inside OpenAI; a merged cookbook entry is the warm intro.
4. **Codex Ambassadors / Discord** — get an ambassador to surface it internally. Lower priority; use only if (1) doesn't get a response in 2 weeks.

## Status (Sean to update)

- [ ] `pitch-email.md` reviewed by Sean
- [ ] `one-pager.md` reviewed + rendered to PDF
- [ ] 3 screenshots captured into `screenshots/`
- [ ] Demo recorded (loom or mp4) and URL added to `pitch-email.md`
- [ ] `security-privacy.md` reviewed by legal
- [ ] Plugin repo pushed public at `github.com/minds-ai-co/codex-plugin`
- [ ] Cookbook PR drafted (optional, parallel)
- [ ] Email sent to `partnerships@openai.com`
