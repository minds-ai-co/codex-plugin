# Pressure-test API designs with a synthetic customer panel inside Codex

Run any product or API decision past a panel of AI personas — founders, customers, domain experts — without leaving your Codex session. This cookbook installs the open-source [Minds](https://getminds.ai) Codex plugin and walks through a real use case: pressure-testing a v2 pricing API design with a six-persona customer panel.

## Why this is useful

Codex is good at synthesizing one expert opinion. Product decisions need a *spread* of opinions — and historically that meant scheduling research interviews, recruiting users, transcribing, coding themes. With a synthetic panel you get the dissent surface in seconds, for cents instead of thousands, right where you're writing the spec. Synthetic panels don't replace real user research — but they're 10x faster at the "is this design even close to right?" stage, and they catch obvious failure modes before you bother humans.

## Prerequisites

- **Codex CLI or app** installed and signed in
- **A Minds account.** Sign up free at [getminds.ai](https://getminds.ai).
- **A Minds personal API key.** Create one at `Settings → API Keys → Personal` in the webapp. The key is shown ONCE — copy it before closing the dialog. Format: `minds_<64-char base62>`.

## Step 1 — Install the plugin

```bash
codex plugin marketplace add minds-ai-co/codex-plugin
codex plugin install minds
```

The CLI will prompt for `MINDS_API_KEY` on install. Paste your key. It's stored in Codex's secret store — the plugin never reads it directly.

Verify:

```bash
codex plugin list
# minds 0.1.0  (4 skills, 2 commands, 1 MCP server)
```

## Step 2 — Create or pick a panel

A **panel** is a group of Minds (personas) wired together so a single question fans out to all of them. You probably want to reuse an existing panel for repeated decisions. List what you have:

```
@minds list my panels
```

If you don't have one yet, create a 6-mind founders panel:

```
@minds create_mind type:user keywords:["solo founder","B2B SaaS","price-sensitive"] name:"Solo SaaS Sarah"
@minds create_mind type:user keywords:["scaling startup","series A","usage-based-pricing skeptic"] name:"Scaling Stage Mike"
@minds create_mind type:user keywords:["enterprise buyer","procurement-aware","predictable budget"] name:"Enterprise Eric"
@minds create_mind type:user keywords:["indie hacker","budget-conscious","monthly cap user"] name:"Indie Ivan"
@minds create_mind type:user keywords:["agency owner","reseller","multi-client billing"] name:"Agency Anna"
@minds create_mind type:user keywords:["AI-first startup","high-burn","scale-fast"] name:"AI-First Adi"

@minds create_group name:"v2 API customers" sparkIds:[...]
@minds create_panel groupIds:[<group-id>] name:"v2 pricing panel"
```

Each `create_mind` call returns instantly. Training happens in background but the Minds are usable immediately.

## Step 3 — Ask the panel a real question

```
/minds-panel "v2 pricing panel" Should we charge per-seat or per-usage for the v2 API?
```

The skill submits the question, polls status, and synthesizes the results. Illustrative response shape (real responses are richer — this is a synthesized excerpt):

```jsonc
{
  "question": "Should we charge per-seat or per-usage for the v2 API?",
  "panelId": "pnl_8f3a...",
  "status": "completed",
  "synthesis": {
    "consensus": "Per-usage with a free monthly cap.",
    "dissent": "Enterprise buyers strongly prefer per-seat for budget predictability."
  },
  "answers": [
    {
      "persona": "Solo SaaS Sarah",
      "sparkId": "spk_aaa",
      "stance": "per-usage",
      "quote": "Per-seat means I'm paying for my whole team to *maybe* use it. Per-usage with a free tier is the only way I'd start."
    },
    {
      "persona": "Enterprise Eric",
      "sparkId": "spk_bbb",
      "stance": "per-seat",
      "quote": "Procurement won't sign off on a usage bill that varies 5x month-to-month. Per-seat is the only line item I can defend."
    }
    // … 4 more
  ]
}
```

The synthesis surfaces the spread — not just an average. The dissent is the signal: if Enterprise Eric is your biggest segment, "consensus says per-usage" is the wrong takeaway.

## Step 4 — Iterate on the spec based on dissent

In the same Codex session, refine the question:

```
/minds-panel "v2 pricing panel" If we charged per-usage with a per-seat enterprise tier above 10 users, would that work?
```

You can chain this as many times as you need. Each panel run takes 5–30s. When you find a shape that resolves the dissent, write it into your spec.

## Production tips

- **Rate limits.** Default is 60 req/min, 1000 req/day on `getminds.ai`. Bigger panels burn budget faster; cap panel size at 12 for fast iteration.
- **Key rotation.** Rotate every 90 days. Revoke instantly in the webapp.
- **Don't put PII in persona context** unless you've reviewed the [Minds privacy policy](https://getminds.ai/privacy) and signed a DPA (available on request).
- **Security details.** See the plugin's [security & privacy doc](https://github.com/minds-ai-co/codex-plugin/blob/main/submission/security-privacy.md) for auth, data handling, moderation, and sub-processor list.

## Resources

- Plugin repo: <https://github.com/minds-ai-co/codex-plugin>
- Minds docs: <https://docs.getminds.ai>
- Minds MCP endpoint (24 tools): `https://getminds.ai/mcp`
- Codex plugin docs: <https://developers.openai.com/codex/plugins/build>
- Codex skills docs: <https://developers.openai.com/codex/skills>

Questions or feedback: `support@getminds.ai`.
