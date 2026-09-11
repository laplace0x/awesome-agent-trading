# Contributing to Awesome Agent Trading

Thank you for contributing! Here are the guidelines:

## Scope and Evidence

This directory covers tools for US equities and options, crypto and DeFi, and prediction markets such as Polymarket and Kalshi. Prioritize clear documentation, usable integrations, and a distinct role in research, strategy development, or execution.

For new entries, describe the actual role and supported modes: research, backtest, paper trading, dry-run, or live execution. Do not treat a roadmap as a shipped feature, a dry-run as a fill simulator, or an author's performance claim as an independently verified result. Label official versus community integrations, experimental projects, hosted services, and source-available licenses explicitly. Note account, venue, and data-access requirements where relevant.

Link to upstream documentation and a license source. If a license is only declared in a README or package manifest, say so; do not imply that a standalone license file was checked. Keep descriptions factual and avoid fixed strategy counts, unsourced returns, or universal position/leverage recommendations.

`data/projects.json` is a featured subset. Add new featured entries there and keep descriptions consistent with the README. Include `modes`, `origin`, `license`, `license_source`, `notes`, `last_verified`, `verification`, and `sources` when reviewed. Use `upstream-documentation` for documentation-only reviews; leave unknown values explicit. Update `llms.txt`, `docs/llms.txt`, and website copy when categories or featured resources change.

After editing the featured data, run `python3 scripts/build_directory.py` to regenerate the website's project list, category counts, and downloadable `docs/projects.json`. Commit the generated files together. CI checks that the public directory matches its source. Do not manually edit the generated sections in `docs/index.html`.

## Adding a New Entry

1. **Check if it already exists** — Search the README first
2. **Pick the right category** — Use existing sections
3. **Follow the table format** — Match the column structure of the section
4. **Keep descriptions concise** — One line, factual, no hype

## Format Guidelines

### For tools/platforms:
```
| [Name](URL) | Brief description | Key attribute |
```

### For agent skills:
```
| [Skill Name](URL) | Author | Brief description |
```

## What We Include

- ✅ Open-source projects with active maintenance
- ✅ APIs and SDKs accessible to autonomous agents
- ✅ Official hosted broker/exchange integrations, with account and access requirements
- ✅ Source-available tools when their license restrictions are clearly distinguished from open-source licenses
- ✅ Agent-native protocols and standards
- ✅ Well-documented tools with clear use cases
- ✅ Academic papers and research
- ✅ High-quality tutorials and guides

## What We Don't Include

- ❌ Opaque, invite-only tools without usable public documentation or access details
- ❌ Memecoins or specific token promotions
- ❌ Unverified or scam projects
- ❌ Unexplained paid-service promotions; disclose required subscriptions and data fees
- ❌ Archived or unavailable projects presented as active tools

For projects with no code activity in six months, investigate maintenance before recommending them as active. Stable libraries and published research may still be useful; label research or historical references separately. Stars and GitHub `updated_at` alone are not evidence of maintenance.

## Submission Process

1. Fork the repo
2. Add your entry to the appropriate section
3. Submit a PR with a clear description
4. One entry per PR preferred

## Questions?

Open an issue or reach out on [Twitter](https://x.com/agentLaplace).
