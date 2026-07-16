# Compliance checklist

Self-attestation against the documented submission requirements. Each item: ✅ done, ⚠️ partial, ❌ not yet / blocked.

**Re-attested 2026-07-16** against current reality (issues #9, #11, #12). This packet is **NOT submit-ready** — it is gated on the open manifest blocker **#12** (see "Blockers & gated items" below). Do not read any ✅ as "ready to publish".

## Plugin manifest (`.codex-plugin/plugin.json`)

- ✅ `name` is kebab-case, stable, unique (`minds`)
- ✅ `version` is semver (`0.1.0`)
- ❌ `description` ≤ 200 chars — currently 206; trim tracked in **#12**
- ✅ `author` includes name, email, URL
- ✅ `license` declared (`MIT`)
- ✅ `homepage` and `repository` URLs resolve (verified in #10/#12)
- ✅ `skills` directory exists with valid `SKILL.md` files
- ❌ **MCP server registers on install — BLOCKED (#12).** The manifest does not currently register the Minds MCP server in Codex, so tools + the Response Widget do not load. Format fix is tracked in **#12** (open); empirical `codex plugin install` proof is Sean-gated. Do not attest this ✅ until #12 lands and is re-verified.
- ⚠️ Secret/config declaration — restructuring under **#12**; not attested pending that fix.

## Marketplace (`marketplace.json`)

- ✅ Top-level `name` (`minds-marketplace`) is a valid free identifier — Codex does **not** require the marketplace `name` to match the repo slug (`codex-plugin`), per the #10 spec review (do not rename)
- ✅ `interface.displayName` is human-friendly
- ⚠️ Plugin `interface` / icon fields — Codex `interface` shape is being corrected under **#12** (the previous `iconUrl` attestation was against the wrong schema); not re-attested here pending #12.
- ✅ Each plugin entry has `policy.installation`, `policy.authentication`, `category`
- ✅ Source uses `url` (root-located plugin) — validated clean in #10/#12
- ✅ Git source URL is HTTPS and public
- ⚠️ `ref` pinned to `main` — switch to a tagged release (`v0.1.0`) is a **Sean-gated finalizer**, out of scope here

## Skills

- ✅ Every `SKILL.md` has valid frontmatter (`name`, `description`) — 4 skills, validated in #12
- ✅ Descriptions name the trigger conditions
- ✅ Bodies include numbered steps + pitfalls
- ✅ No unverified external commands referenced
- ✅ No hardcoded API keys — repo-wide grep clean (#12)

## Security & privacy

- ✅ Security disclosure email published (`security@getminds.ai`)
- ✅ `security-privacy.md` covers auth, data handling, moderation, rate limits
- ✅ Widget is served vendor-inlined with no external CDN/script loads (verified live on `getminds.ai/mcp`, #11) — no third-party origin runs in the host sandbox (one residual: Iconify may attempt runtime icon fetches; cosmetic, tracked as a webapp report-item)
- ⚠️ SOC2 Type 1 — in progress, target Q3 2026 (not blocking for plugin acceptance per Codex docs)
- ✅ Plugin requests no filesystem access beyond its own directory
- ✅ No telemetry / phone-home

## Open source hygiene

- ✅ LICENSE file present (MIT)
- ✅ README explains install, configure, verify
- ✅ CHANGELOG present
- ✅ `.gitignore` excludes secrets and build artifacts
- ✅ CONTRIBUTING.md present (added under #9)

## Repository & distribution

- ✅ Repo is **PUBLIC** at github.com/minds-ai-co/codex-plugin (the earlier "currently local only" line was stale — corrected 2026-07-16)
- ✅ Plugin published under a verifiable org GitHub account (`minds-ai-co`)
- ✅ Public-domain marketplace entry usable from CLI
- ✅ One-pager PDF — rendered from `one-pager.md`, committed under `submission/` (#9)
- ✅ Security-privacy PDF — rendered from `security-privacy.md`, committed under `submission/` (#9)
- ✅ Pitch email drafted (`pitch-email.md`)
- ❌ Demo video (Loom or mp4) — **render-gated** (depends on #3 render path + Sean capture)
- ❌ 3 reference screenshots in `screenshots/` — **render-gated / Sean-gated capture**
- ⚠️ Existing relationship with OpenAI BD — Sean/Alex to confirm contact before send
- ⚠️ Cookbook PR — drafted in parallel (`cookbook-draft.md`), not blocking

## Per-host widget render status (folded from #11, 2026-07-16)

The native Response Widget bundle is **production-ready** (bridge-adaptive + vendor-inlined, live on `getminds.ai/mcp`). Remaining render gates are host/connector config or upstream, **not our code** — see `submission/README.md` for the full matrix. Summary: ChatGPT/Codex desktop = renders once the client is updated + flags enabled (openai/codex #21019); Claude Desktop = blocked on upstream ext-apps #671 + server-side `_meta` gaps; chatgpt.com web = renders once the Minds connector is re-enabled.

## Blockers & gated items (explicit — these are OUT of scope for #9)

**#12 publish-blocker (must clear before any submit-ready claim):**
- Manifest does not register the MCP server → plugin is inert on the current `widgets` base. Format fix is done in **PR #14 (reviewed-clean, pending merge)**; empirical `codex plugin install` smoke test is Sean-gated.
- `description` ≤200 trim, `interface`/icon schema, commands removal, secret/config placement — all restructured in PR #14.
- The slash-command pitch (`/minds-panel`, `/minds-create`) has been **removed** from `one-pager.md` / `pitch-email.md` / `demo-script.md` / the cookbook docs now that #12 confirmed Codex has no commands concept. The exact MCP tool count is left as a **TODO placeholder** (pending the in-flight tool curation — not ours to finalize).

**Render-gated (depend on #3 render path; Sean captures):**
- 3 screenshots (install flow, panel query, results synthesis)
- 60-second demo recording

**Sean-gated finalizers (not this task):**
- `marketplace.json` `ref` `main` → `v0.1.0` tag
- Pitch email send
- Sean end-to-end review of plugin contents
