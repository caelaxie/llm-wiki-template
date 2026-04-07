# AGENTS.md

This repository follows an LLM wiki pattern inspired by the `llm-wiki` gist:
https://gist.githubusercontent.com/karpathy/442a6bf555914893e9891c11519de94f/raw/ac46de1ad27f92b28ac95459c782c07f6b8c964a/llm-wiki.md

## Purpose

The goal is to maintain a persistent, compounding markdown wiki that sits between
the human and a curated collection of raw source material.

There are three layers in this repo:

1. `raw/` contains curated source documents. This layer is immutable from the
   LLM's perspective. Read from it, but do not modify, rewrite, or reorganize
   files in it unless the user explicitly asks.
2. `wiki/` contains the persistent markdown wiki. This layer is generated and
   maintained by the LLM.
3. `AGENTS.md` is the schema and workflow contract for how the LLM operates on
   the wiki.

The wiki is a persistent artifact. Do not treat this repo like one-off RAG over
raw files. New sources and valuable answers should be integrated into the wiki
so knowledge accumulates over time.

This file defines default conventions for this template repo. Downstream repos
may adapt them to fit their domain.

## General Rules

- Prefer updating existing wiki pages over creating near-duplicate pages.
- Maintain links between related wiki pages using Obsidian-style wikilinks.
- Treat `wiki/index.md` as the first navigation surface when answering questions about the corpus.
- Record meaningful wiki operations in `wiki/log.md`.
- Keep wiki content in markdown.
- Preserve contradictions, uncertainty, and open questions instead of flattening them away.
- Use bare `[[slug]]` wikilinks for wiki content pages whenever possible.
- Use `[[raw/...]]` wikilinks for raw-source references.
- Other output forms such as slide decks, charts, and canvases remain possible when useful, but they are outside this markdown page schema.

## Repository Layout

Required files:

- `AGENTS.md`
- `wiki/index.md`
- `wiki/log.md`

Required wiki content directories:

- `wiki/sources/`
- `wiki/entities/`
- `wiki/concepts/`
- `wiki/syntheses/`

Content pages must live only in those four typed directories.

## Markdown Page Conventions

### Page Types

Use these page types for markdown content pages:

- `source`
- `entity`
- `concept`
- `synthesis`

### Frontmatter

All markdown content pages should begin with this minimal YAML frontmatter:

```yaml
---
title: "Page Title"
type: "source|entity|concept|synthesis"
sources:
  - "[[raw/source-file.md]]"
created_at: "YYYY-MM-DD"
updated_at: "YYYY-MM-DD"
---
```

Rules:

- `title` is the canonical human-readable page title.
- `type` must be one of `source`, `entity`, `concept`, or `synthesis`.
- `sources` is a list of wiki-link strings pointing to the raw files and/or wiki pages that materially support the page.
- Use `[[raw/...]]` for raw-source references in `sources`.
- Use bare `[[slug]]` for wiki-page references in `sources`.
- `created_at` is the page creation date in `YYYY-MM-DD` format.
- `updated_at` is the date of the last material edit in `YYYY-MM-DD` format.

### Filenames And Slugs

- Store source pages under `wiki/sources/`.
- Store entity pages under `wiki/entities/`.
- Store concept pages under `wiki/concepts/`.
- Store synthesis pages under `wiki/syntheses/`.
- Do not create additional content directories under `wiki/`.
- Do not create deeper nesting inside the four typed content directories.
- Use lowercase `kebab-case` filenames with a `.md` suffix.
- The canonical filename shape is `<slug>.md`.
- Keep slugs globally unique across all four typed content directories so bare `[[slug]]` links stay unambiguous.
- If two pages would otherwise share a slug, append a short stable qualifier.
- Prefer updating an existing canonical slug file over creating a near-duplicate alternate spelling.

### Body Templates

Keep pages narrative and minimal. Do not add tags, scoring, status fields, or
Dataview-specific structure unless the user asks.

`source` pages should include:

- summary
- key takeaways
- evidence or notable details
- related pages
- open questions

`entity` pages should include:

- summary
- role or significance
- current understanding
- related pages
- open questions or tensions

`concept` pages should include:

- summary
- why it matters
- current understanding
- related pages
- open questions or tensions

`synthesis` pages should include:

- question or thesis
- synthesized answer
- citations or supporting pages
- unresolved points
- related pages

### Citations

- Use inline Obsidian-style wiki links for citations in page bodies.
- Use bare `[[slug]]` links for wiki page citations.
- Use `[[raw/...]]` links for raw-source citations.
- `synthesis` pages should cite the supporting wiki pages and source pages they rely on.

## Operations

### Ingest

When the user asks to ingest a new source:

1. Read `wiki/index.md`.
2. Read the source from `raw/`.
3. Extract the important claims, entities, concepts, evidence, and unresolved questions.
4. Create or update the corresponding `source` page in `wiki/sources/`.
5. Update the most relevant `entity`, `concept`, and `synthesis` pages in their typed directories when the source materially changes them.
6. Integrate that material into the wiki by creating new pages only when needed and otherwise updating the most relevant existing pages.
7. Update `wiki/index.md` so it remains a useful category-organized catalog of wiki pages.
8. Ensure each relevant index entry includes at least a link and a one-line summary.
9. Append an entry to `wiki/log.md` describing the ingest.
10. Update `updated_at` on every content page materially changed during ingest.
11. Set `created_at` and `updated_at` when creating a new content page.

### Query

When the user asks a question:

1. Start from `wiki/index.md` to locate relevant wiki pages.
2. Read the most relevant wiki pages first.
3. Synthesize the answer from the wiki instead of rediscovering everything from `raw/` by default.
4. Cite supporting wiki pages and source pages with inline wiki links.
5. If the answer creates durable value for the knowledge base, file it back into the wiki as a `synthesis` page in `wiki/syntheses/`, then update `wiki/index.md` and `wiki/log.md`.

### Lint

When the user asks for a lint or health check:

1. Inspect the wiki for contradictions between pages.
2. Look for stale claims that newer sources may have superseded.
3. Identify orphan pages or missing cross-references.
4. Identify important concepts or entities that are mentioned but not yet well integrated.
5. Identify research gaps or follow-up questions that would improve the wiki.
6. Identify markdown content pages with missing or malformed frontmatter.
7. Identify `created_at` or `updated_at` values that are not in `YYYY-MM-DD` format.
8. Identify filenames that violate lowercase `kebab-case`.
9. Identify content pages stored outside the four typed content directories.
10. Identify near-duplicate pages caused by slug drift or weak disambiguation.
11. Identify slug collisions that would make bare `[[slug]]` links ambiguous.
12. Identify `wiki/index.md` entries missing category placement, links, or one-line summaries.
13. Record the lint pass in `wiki/log.md` if it materially affects the wiki or future work.

## Index And Log

- `wiki/index.md` is the content-oriented catalog of the wiki.
- Read `wiki/index.md` first for queries and maintenance work.
- Organize `wiki/index.md` by category using sections for `Sources`, `Entities`, `Concepts`, and `Syntheses`.
- Include one entry per content page, with at least a link and a one-line summary.
- `wiki/log.md` is the chronological, append-only record of wiki activity.
- Start each log entry with a heading in this format: `## [YYYY-MM-DD] operation | title`

## Completion Checklist

Before finishing any wiki-changing task, verify that:

- no files in `raw/` were modified
- every touched content page lives in the correct typed directory
- wiki-page links use bare `[[slug]]` wherever possible
- raw-source references use `[[raw/...]]`
- no content-page slug collides with another content-page slug
- `wiki/index.md` reflects the current page set
- `wiki/log.md` has a new entry if the wiki changed materially
- contradictions, weak evidence, and open questions remain explicit
- the wiki is more useful and navigable than it was before the pass
