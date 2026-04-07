# Log

This log is the append-only chronological record of material wiki operations.
Each entry should use a heading in the form `## [YYYY-MM-DD] operation | title`
so later maintenance work can scan changes quickly.

## [2026-04-07] bootstrap | Initialize LLM wiki template

Created the minimal `llm-wiki` template bootstrap:

- added `AGENTS.md` as the schema and workflow contract
- created `raw/` with a tracked placeholder
- created typed wiki content directories under `wiki/`
- created `wiki/index.md`
- created `wiki/log.md`

## [2026-04-08] maintenance | Refresh index and log for updated repo contract

Updated the wiki navigation and operation surfaces to match the revised
instructions in `AGENTS.md` and `STYLE_GUIDE.md`:

- rewrote `wiki/index.md` so it acts as the first navigation surface and states
  the current empty-page status by category
- clarified `wiki/log.md` entry expectations while preserving the append-only
  history
