# Log

This log is the append-only chronological record of material wiki operations. Each entry should use a heading in the form `## [YYYY-MM-DD] operation | title` so later maintenance work can scan changes quickly.

## [2026-04-07] bootstrap | Initialize LLM wiki template

Created the minimal `llm-wiki` template bootstrap:

- added `AGENTS.md` as the schema and workflow contract
- created `raw/` with a tracked placeholder
- created typed wiki content directories under `wiki/`
- created `wiki/index.md`
- created `wiki/log.md`

## [2026-04-08] maintenance | Refresh index and log for updated repo contract

Updated the wiki navigation and operation surfaces to match the revised instructions in `AGENTS.md` and `STYLE_GUIDE.md`:

- rewrote `wiki/index.md` so it acts as the first navigation surface and states
  the current empty-page status by category
- clarified `wiki/log.md` entry expectations while preserving the append-only
  history

## [2026-04-08] maintenance | Rewrite style guide around ChatGPT-style prose

Replaced the prior writing guide with a full rewrite aligned to the current public OpenAI Model Spec's writing defaults, adapted for persistent wiki pages:

- removed the prior MediaWiki-inspired framing
- rewrote the guide around answer-first, direct, warm, professional, and
  concise prose
- tightened formatting rules for leads, paragraphs, headings, and list usage
- rewrote page-type guidance from scratch
- added anti-patterns and short good/bad examples to make the style operational

## [2026-04-08] maintenance | Make style guide easier for agents to apply

Tightened the rewritten style guide so agents can execute it with less interpretation:

- added a quick-start workflow for drafting and revising pages
- added default decision rules for common writing tradeoffs
- added a default page-writing sequence shared across page types
- expanded the final checks to verify the guide is operational for agents
