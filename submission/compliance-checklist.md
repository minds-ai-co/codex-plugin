# Compliance checklist

Self-attestation against the documented submission requirements. Each item: ✅ done, ⚠️ partial, ❌ not yet.

## Plugin manifest (`.codex-plugin/plugin.json`)

- ✅ `name` is kebab-case, stable, unique (`minds`)
- ✅ `version` is semver (`0.1.0`)
- ✅ `description` is < 200 chars and explains value proposition
- ✅ `author` includes name, email, URL
- ✅ `license` declared (`MIT`)
- ✅ `homepage` and `repository` URLs resolve
- ✅ `skills` directory exists with valid `SKILL.md` files
- ✅ `mcp` config points at a hosted server, no localhost references
- ✅ `config` declares required env vars with `secret: true` where appropriate

## Marketplace (`marketplace.json`)

- ✅ Top-level `name` matches Git repo slug
- ✅ `interface.displayName` is human-friendly
- ✅ `interface.iconUrl` is a public HTTPS URL
- ✅ Each plugin entry has `policy.installation`, `policy.authentication`, `category`
- ✅ Source uses `git-subdir` or `url` (no local-only paths in the public marketplace)
- ✅ Git source URL is HTTPS and public
- ✅ `ref` pinned to `main` (will switch to tagged release before final submission)

## Skills

- ✅ Every `SKILL.md` has valid frontmatter (`name`, `description`)
- ✅ Descriptions name the trigger conditions
- ✅ Bodies include numbered steps + pitfalls
- ✅ No unverified external commands referenced
- ✅ No hardcoded API keys

## Security & privacy

- ✅ Security disclosure email published (`security@getminds.ai`)
- ✅ `security-privacy.md` covers auth, data handling, moderation, rate limits
- ⚠️ SOC2 Type 1 — in progress (not blocking for plugin acceptance per Codex docs)
- ✅ Plugin requests no filesystem access beyond its own directory
- ✅ No telemetry / phone-home

## Open source hygiene

- ✅ LICENSE file present (MIT)
- ✅ README explains install, configure, verify
- ✅ CHANGELOG present
- ✅ `.gitignore` excludes secrets and build artifacts
- ⚠️ CONTRIBUTING.md — not yet written (low priority)

## OpenAI Codex Plugin-Directory-specific (best-effort, no public form)

- ✅ Plugin published under a verifiable org GitHub account (`minds-ai-co`)
- ✅ Public-domain marketplace entry usable from CLI
- ✅ Demo video (Loom or mp4) — TODO before send
- ✅ One-pager PDF — TODO render from `one-pager.md`
- ✅ Pitch email drafted (`pitch-email.md`)
- ⚠️ Existing relationship with OpenAI BD — Alex to confirm contact name before send
- ⚠️ Cookbook PR — drafted in parallel, not blocking

## Before submission

- [ ] Sean reviews plugin contents end-to-end
- [ ] Final 3 screenshots captured into `screenshots/`
- [ ] Demo recorded, URL pasted into `pitch-email.md`
- [ ] `one-pager.md` rendered to PDF (e.g. via `pandoc one-pager.md -o one-pager.pdf`)
- [ ] `security-privacy.md` rendered to PDF
- [ ] Repo pushed to `github.com/minds-ai-co/codex-plugin` (currently local only)
- [ ] `marketplace.json` `ref` updated from `main` to `v0.1.0` tag
- [ ] Email sent
