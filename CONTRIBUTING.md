# Contributing to the Minds Codex Plugin

Thanks for your interest in improving the Minds plugin for Codex. This repo is MIT-licensed and open to contributions.

## Ways to contribute

- **Skills** — the plugin's capabilities live in `skills/*/SKILL.md`. Improvements to trigger descriptions, steps, or pitfalls are welcome.
- **Docs** — `README.md`, the `submission/` packet, and inline skill docs.
- **Bug reports & ideas** — open a GitHub issue at <https://github.com/minds-ai-co/codex-plugin/issues>.

## Ground rules

- **No secrets in the repo.** Never commit an API key, token, or `.env`. The plugin reads `MINDS_API_KEY` from Codex's secret store at runtime — it is never hardcoded. PRs are grep-checked for key patterns.
- **Skills are prompts, not code.** Each `SKILL.md` needs valid frontmatter (`name`, `description` naming the trigger) and a body with numbered steps and pitfalls. Keep them accurate to the live Minds tools.
- **Match existing style.** Follow the tone and structure of the surrounding files.

## Development

1. Fork and branch off `main`.
2. Make your change. For a new skill, add `skills/<name>/SKILL.md`.
3. Verify your Markdown renders and any referenced Minds tool actually exists on `getminds.ai/mcp`.
4. Open a Pull Request describing what changed and why.

## Pull requests

- Keep PRs focused and small where possible.
- PRs are reviewed before merge; a maintainer merges once review passes.
- By contributing you agree your work is licensed under the repo's [MIT License](./LICENSE).

## Security

Do **not** file security issues as public GitHub issues. Report vulnerabilities privately to **security@getminds.ai** — see [`submission/security-privacy.md`](./submission/security-privacy.md) for the disclosure process.

## Questions

Open an issue or reach the team at <https://getminds.ai>.
