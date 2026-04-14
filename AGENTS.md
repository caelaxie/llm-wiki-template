# AGENTS.md

This repository follows an LLM wiki pattern inspired by Andrej Karpathy's `llm-wiki` gist and related agentic wiki workflows.

The goal is not one-off retrieval over `raw/`. The goal is to maintain a persistent, compounding markdown wiki that sits between the human and a curated collection of source material.

This file is the operating contract for that wiki. It defines how an LLM should orient itself, decide whether to create or update pages, keep navigation intact, and preserve uncertainty instead of flattening it away.

This repository intentionally uses a narrow structure: four wiki page types, markdown content only, and lightweight frontmatter.

`STYLE_GUIDE.md` is the companion writing guide for wiki prose and presentation. `AGENTS.md` remains authoritative for repo structure, workflow, page types, frontmatter, and required section families.

## Purpose

There are three layers in this repo:

1. `raw/` contains curated source documents. This is a human-curated source
   layer by default. The agent may read from it, cite it, and build wiki pages from it, but must not add, modify, rename, rewrite, or reorganize files in `raw/` unless the user explicitly asks. When the user does explicitly ask the agent to add material into `raw/`, any images that are part of that material must be downloaded automatically into `raw/assets/` and referenced with `[[raw/assets/...]]` wikilinks. For web material, this includes relevant source images exposed by the page or its image URLs, but excludes obvious site chrome, ads, avatars, tracking pixels, and unrelated decorative assets.
2. `wiki/` contains the persistent markdown wiki. This layer is generated and
   maintained by the LLM.
3. `AGENTS.md` is the schema and workflow contract for how the LLM operates on
   the wiki.

The wiki is a persistent artifact. New sources and valuable answers should be integrated into the wiki so knowledge accumulates over time.

`STYLE_GUIDE.md` supplements this contract with writing rules for audience, language, leads, heading style, and information flow. If the two files overlap, `AGENTS.md` wins on schema and workflow while `STYLE_GUIDE.md` governs writing style and presentation.

## Core principles

- Prefer updating existing wiki pages over creating near-duplicate pages.
- Treat `wiki/index.md` as the first navigation surface for queries and
  maintenance work.
- Record meaningful wiki operations in `wiki/log.md`.
- Keep wiki content in markdown.
- Preserve contradictions, uncertainty, and open questions instead of forcing
  premature reconciliation.
- Use bare `[[slug]]` wikilinks for wiki content pages whenever possible.
- Use `[[raw/...]]` wikilinks for raw-source references, including
  `[[raw/assets/...]]` for downloaded images stored in the raw corpus.
- Follow `STYLE_GUIDE.md` when writing or materially revising wiki prose.
- Keep the repo structure narrow. Do not introduce extra content directories,
  extra required metadata, or extra page classes unless the user explicitly asks.

## Session orientation

When working on an existing wiki, orient yourself before doing substantive work. Do this especially before ingest, broad maintenance, or creating new pages.

Minimum orientation pass:

1. Read `AGENTS.md`.
2. Read `STYLE_GUIDE.md` before creating or materially updating wiki prose.
3. Read `wiki/index.md`.
4. Scan the most recent relevant entries in `wiki/log.md`.
5. Read the most relevant existing wiki pages before creating anything new.

This prevents duplicate pages, missed cross-references, and edits that fight the current shape of the wiki.

If the wiki has grown enough that `wiki/index.md` is no longer sufficient on its own, run a targeted search across `wiki/` for relevant slugs, entities, concepts, and phrases before creating new pages.

## Repository layout

Required files:

- `AGENTS.md`
- `STYLE_GUIDE.md`
- `wiki/index.md`
- `wiki/log.md`

Required wiki content directories:

- `wiki/sources/`
- `wiki/entities/`
- `wiki/concepts/`
- `wiki/syntheses/`

Content pages must live only in those four typed directories.

## Markdown page conventions

Markdown source formatting is repo-wide by default:

- Store prose paragraphs as single logical lines separated by blank lines.
- Rely on editor soft wrap for reading.
- Do not manually wrap prose for visual width.
- Do not use trailing spaces or end-of-line backslashes for hard line breaks.
- Use explicit `<br>` only when a forced rendered line break is genuinely unavoidable.
- Preserve structural Markdown layout where line shape is part of the syntax or meaning, including YAML frontmatter, headings, lists, blockquotes, tables, and fenced code blocks.
- Apply this rule to repo Markdown by default, including wiki pages and Markdown test fixtures.
- Keep top-level `raw/` as protected corpus material, including `raw/assets/`;
  do not reformat it unless the user explicitly asks.

### Page types

Use these page types for markdown content pages:

- `source`
- `entity`
- `concept`
- `synthesis`

### Frontmatter

All markdown content pages should begin with YAML frontmatter. This example shows the shared fields common to every page type:

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
- `sources` is a list of wiki-link strings pointing to the raw files and/or wiki
  pages that materially support the page.
- Use `[[raw/...]]` for raw-source references in `sources`, including
  `[[raw/assets/...]]` when an image asset is itself supporting source material.
- Use bare `[[slug]]` for wiki-page references in `sources`.
- All page types require `title`, `type`, `sources`, `created_at`, and
  `updated_at`.
- `created_at` is the page creation date in `YYYY-MM-DD` format.
- `updated_at` is the date of the last material edit in `YYYY-MM-DD` format.
- `source` pages must include `raw_sha256`, which stores the SHA-256 digest of
  the single canonical `[[raw/...]]` file that backs the page.
- Newly created `source` pages must include `raw_sha256` at creation time.
- The creator of a new `source` page must compute and set `raw_sha256`.
- The dedicated `refresh` workflow reconciles `raw_sha256` later and may
  bootstrap a missing value on an existing page during refresh.
- `raw_sha256` must not appear on `entity`, `concept`, or `synthesis` pages.
- If an image asset under `raw/assets/` is the single canonical raw backing
  file for a `source` page, it is still a normal `[[raw/...]]` reference and
  still requires `raw_sha256`.

Example non-source page frontmatter:

```yaml
---
title: "How Tailscale Builds a Mesh VPN"
type: "synthesis"
sources:
  - "[[tailscale-how-it-works]]"
  - "[[wireguard]]"
created_at: "2026-04-07"
updated_at: "2026-04-07"
---
```

Canonical `source` page frontmatter:

```yaml
---
title: "WireGuard Whitepaper"
type: "source"
sources:
  - "[[raw/wireguard-whitepaper.md]]"
raw_sha256: "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
created_at: "2026-04-07"
updated_at: "2026-04-07"
---
```

### Filenames and slugs

- Store source pages under `wiki/sources/`.
- Store entity pages under `wiki/entities/`.
- Store concept pages under `wiki/concepts/`.
- Store synthesis pages under `wiki/syntheses/`.
- Do not create additional content directories under `wiki/`.
- Do not create deeper nesting inside the four typed content directories.
- Use lowercase `kebab-case` filenames with a `.md` suffix.
- The canonical filename shape is `<slug>.md`.
- Keep slugs globally unique across all four typed content directories so bare
  `[[slug]]` links stay unambiguous.
- If two pages would otherwise share a slug, append a short stable qualifier.
- Prefer updating an existing canonical slug file over creating a near-duplicate
  alternate spelling.

### Create vs update

Default to updating an existing page when:

- the topic already has a canonical page
- the new source adds detail, evidence, dates, nuance, or contradictions
- the mention is important but not strong enough to justify a standalone page

Create a new page when:

- the topic is central to a source, not just a passing mention
- the topic recurs across sources and would otherwise be awkwardly buried
- a durable synthesis question deserves its own `synthesis` page

Do not create pages for fleeting mentions, weakly evidenced subtopics, or alternate phrasings of an existing page.

Before creating a page, search for likely existing slugs, synonyms, and related pages in the wiki.

### Body templates

Keep pages narrative and minimal. Do not add tags, scoring fields, status fields, or Dataview-specific structure unless the user asks.

The lists below define the baseline required section families for each page type. `STYLE_GUIDE.md` refines how those sections should be introduced, sequenced, and written.

Every content page must begin with a short unheaded lead immediately after frontmatter and before the first section heading. This lead is required structure for all page types, but it does not introduce an additional heading.

The required headings remain the section families listed below. Material such as scope limits, distinctions, implications, background, and notable absences should usually live inside those sections rather than expanding the schema with new required headings.

`source` pages should include:

- summary
- key takeaways
- evidence or notable details
- related pages
- open questions

For `source` pages, `## Summary` should begin with a short overall summary of the source's contribution and then include a required section map.

The section map stays inside `## Summary`; do not add a separate `## Section map` heading.

Use one bullet per section and subsection, with nested bullets indented by two spaces per level to show hierarchy.

Preserve the source's original section numbering when it exists.

Skip boilerplate headings such as acknowledgements, references, and author notes by default.

Include appendices only when they add substantive content relevant to the wiki.

Low-signal branches may be folded into the nearest meaningful parent bullet, but substantive analytical sections should remain explicit.

Recommended sentence-case headings for `source` pages:

- `## Summary`
- `## Key takeaways`
- `## Evidence or notable details`
- `## Related pages`
- `## Open questions`

`entity` pages should include:

- summary
- role or significance
- current understanding
- related pages
- open questions or tensions

Recommended sentence-case headings for `entity` pages:

- `## Summary`
- `## Role or significance`
- `## Current understanding`
- `## Related pages`
- `## Open questions or tensions`

`concept` pages should include:

- summary
- why it matters
- current understanding
- related pages
- open questions or tensions

Recommended sentence-case headings for `concept` pages:

- `## Summary`
- `## Why it matters`
- `## Current understanding`
- `## Related pages`
- `## Open questions or tensions`

`synthesis` pages should include:

- question or thesis
- synthesized answer
- citations or supporting pages
- unresolved points
- related pages

Recommended sentence-case headings for `synthesis` pages:

- `## Question or thesis`
- `## Synthesized answer`
- `## Citations or supporting pages`
- `## Unresolved points`
- `## Related pages`

### Citations and cross-links

- Footnotes are allowed on any page type.
- In normal prose, use bare `[[slug]]` links for wiki-page support.
- In normal prose, use Markdown footnotes for direct support from `raw/`.
- When referring to a downloaded image stored in the raw corpus, use a
  `[[raw/assets/...]]` wikilink rather than leaving a website image URL in
  place or using a plain relative Markdown path.
- When a sentence is supported by both wiki pages and raw material, prefer an
  inline bare `[[slug]]` link plus a raw-source footnote.
- Footnotes are for attribution and locator detail only, not for side
  arguments, caveats, definitions, or overflow explanation.
- Use a raw-source footnote when a claim is quoted, dated or time-bounded,
  numerical or otherwise specific, attributed to a particular source's framing
  or interpretation, or potentially disputed, surprising, or narrower than
  common background knowledge.
- A raw-source footnote is optional for high-level summary of a `source` page's
  own canonical raw document when the paragraph is clearly descriptive and
  non-quotational, and for broad orienting statements that are immediately
  followed by a cited supporting sentence or paragraph.
- A raw-source footnote is discouraged for generic setup sentences, repeated
  restatements of a claim already cited in the same short paragraph, and
  explanation that belongs in the body text.
- Use footnotes at paragraph scope when adjacent sentences rely on the same raw
  source and the same locator or tight locator range. Split footnotes when the
  support shifts to a different section, page, source, or evidentiary
  strength.
- In raw-source footnotes, put the direct `[[raw/...]]` link first, then add
  the shortest useful locator detail such as `p. 14`, `pp. 14-16`,
  `section "Protocol overview"`, `under "Failure modes"`, or `appendix A`.
- If no precise locator is available, the raw-source footnote may contain only
  the `[[raw/...]]` link or the link plus a brief note such as `general
  discussion`.
- If multiple raw sources support the same nearby claim, one footnote may list
  multiple `[[raw/...]]` links. Use separate footnotes when sources support
  different claims or need distinct locators for clarity.
- Definitions:
  - `normal prose` means leads and narrative body paragraphs.
  - `structural areas` means frontmatter, related-page lists, and synthesis
    citation inventories.
  - `locator range` means one page, a short page span, or one named section.
- These rules apply to normal prose only. They do not change frontmatter
  `sources`, `Related pages`, `wiki/index.md`, or other structural link areas,
  which continue using normal wiki links.
- On `source` pages, cite most factual or interpretive paragraphs. Paragraphs
  may share a single footnote when they use the same raw source and locator
  range, but a second footnote is required when the next sentence shifts to a
  different section, page, source, or evidentiary strength.
- In `synthesis` pages, the `## Citations or supporting pages` section is a
  plain link inventory, so list supporting `[[slug]]` and `[[raw/...]]` links
  inline rather than turning the section into footnoted prose.
- `synthesis` pages should cite the supporting wiki pages and source pages they
  rely on.
- These rules are editorial guidance, not lint or normalization requirements.
- New or materially updated pages should include meaningful links to the most
  relevant related pages whenever those relationships are known.
- Avoid isolated pages. If a page belongs in the wiki, it should usually connect
  to existing entities, concepts, or syntheses.

Examples:

Good source-page paragraph with paragraph-level citation grouping:

```md
WireGuard minimizes protocol surface area. It keeps the protocol surface small
enough to be auditable by design.[^1]

[^1]: [[raw/wireguard-whitepaper.md]], section "Protocol overview".
```

Good source-page paragraph with split footnotes when support changes:

```md
The coordination model in [[tailscale]] depends on metadata exchange rather
than a permanent hub-and-spoke data plane.[^1] The same source also frames the
control plane as separate from packet forwarding.[^2]

[^1]: [[raw/tailscale-design.pdf]], p. 14.
[^2]: [[raw/tailscale-design.pdf]], p. 15.
```

Good mixed wiki-link and raw-footnote citation:

```md
The control-plane claim in [[tailscale]] is consistent across the core
architecture documents.[^1]

[^1]: [[raw/tailscale-design.pdf]], p. 14; [[raw/tailscale-overview.md]],
section "Control plane".
```

Good synthesis citation inventory:

```md
## Citations or supporting pages

- [[tailscale]]
- [[wireguard]]
- [[raw/tailscale-design.pdf]]
```

Bad raw footnote that explains instead of attributing:

```md
The note explains the difference between control and data planes.[^1]

[^1]: The distinction is important because it clarifies why the design remains
simple.
```

Bad pattern with a redundant footnote on every sentence:

```md
WireGuard minimizes protocol surface area.[^1][^2]

[^1]: [[raw/wireguard-whitepaper.md]], section "Protocol overview".
[^2]: [[raw/wireguard-whitepaper.md]], section "Protocol overview".
```

## Operations

### Ingest

When the user asks to ingest a new source:

1. Ingest assumes the source has already been curated into `raw/`.
2. If the user provides a URL, PDF, or pasted text that is not yet in `raw/`,
   pause normal wiki ingest and ask whether to add that material to the corpus first. Only add it to `raw/` when the user explicitly instructs you to do so.
3. If the user explicitly asks to add new raw material and that material comes
   from the web, automatically download the relevant source images exposed by
   that material into `raw/assets/` and replace website image references with
   `[[raw/assets/<filename>]]` wikilinks. Skip obvious site chrome, ads,
   avatars, tracking pixels, and unrelated decorative assets.
4. Read `wiki/index.md`.
5. Read the source from `raw/`.
6. Extract the important claims, entities, concepts, evidence, and unresolved
   questions.
7. Check what already exists before creating anything new. Search for likely
   entities, concepts, syntheses, and alternate phrasings.
8. Create or update the corresponding `source` page in `wiki/sources/`. If the
   page is newly created, include `raw_sha256` in its frontmatter immediately.
9. Update the most relevant `entity`, `concept`, and `synthesis` pages when the
   source materially changes them.
10. Create new supporting pages only when they meet the create-vs-update rules
   above.
11. Add or refresh meaningful cross-links between the touched pages.
12. Update `wiki/index.md` so it remains a useful category-organized catalog of
   wiki pages.
13. Ensure each relevant index entry includes at least a link and a one-line
    summary.
14. Append an entry to `wiki/log.md` describing the ingest.
15. Update `updated_at` on every content page materially changed during ingest.
16. Set `created_at` and `updated_at` when creating a new content page.
17. When creating a new `source` page, compute and include `raw_sha256` in the
    initial frontmatter instead of relying on a later refresh to add it.

For batch ingest:

1. Read all incoming sources first.
2. Identify overlapping entities, concepts, and syntheses once.
3. Update the affected pages in one pass instead of repeatedly reopening the
   same topics source by source.
4. Update `wiki/index.md` once after the batch.
5. Append one batch-oriented log entry unless separate entries are genuinely
   clearer.

### Query

When the user asks a question:

1. Start from `wiki/index.md` to locate relevant wiki pages.
2. Read the most relevant wiki pages first.
3. Use `raw/` selectively when the wiki lacks needed detail, when a claim needs
   verification, or when a new source has not yet been integrated.
4. Synthesize the answer from the wiki instead of rediscovering everything from
   `raw/` by default.
5. Cite supporting wiki pages with inline bare `[[slug]]` links and use raw
   footnotes in normal prose when the answer depends directly on `raw/`
   material.
6. If the answer creates durable value for the knowledge base, file it back into
   the wiki as a `synthesis` page in `wiki/syntheses/`, then update `wiki/index.md` and `wiki/log.md`.
7. If the answer is trivial or one-off, answer directly without forcing a new
   page.

### Refresh

When the user asks for a refresh or raw-drift check:

1. Run the dedicated `refresh` command instead of `lint`.
2. `refresh` scans `source` pages and resolves each page's single canonical
   `[[raw/...]]` backing file.
3. `refresh` computes the SHA-256 of that raw file and ensures `raw_sha256` is
   present and current on the `source` page, bootstrapping a missing value when needed.
4. `refresh` identifies changed `source` pages and computes downstream
   dependency closures using only `sources` frontmatter links.
5. `refresh` prints a deterministic ordered report of the pages that should be
   refreshed next.
6. `refresh` must not rewrite dependent wiki pages, `wiki/index.md`, or
   `wiki/log.md`.
7. After `refresh`, the agent may rewrite the reported pages, update
   `updated_at` only for material content changes, then update `wiki/index.md` and `wiki/log.md` if the wiki changed materially.

For dependency resolution during `refresh`:

- If page `A` lists `[[B]]` in `sources`, `A` depends on `B`.
- Body wikilinks remain navigational and do not create refresh dependencies.
- `source` pages must contain exactly one canonical `[[raw/...]]` reference in
  `sources`.
- `source` pages must carry `raw_sha256`; `refresh` can backfill a missing hash
  on an existing page without failing fast.

### Lint

When the user asks for a lint or health check:

1. Inspect the wiki for contradictions between pages.
2. Look for stale claims that newer sources may have superseded.
3. Identify orphan pages or pages with weak integration into the rest of the
   wiki.
4. Identify broken or ambiguous wikilinks.
5. Identify important concepts or entities that are mentioned but not yet well
   integrated.
6. Identify research gaps or follow-up questions that would improve the wiki.
7. Identify markdown content pages with missing or malformed frontmatter.
8. Identify `source` pages with missing or malformed `raw_sha256`.
9. Identify `created_at` or `updated_at` values that are not in `YYYY-MM-DD`
   format.
10. Identify filenames that violate lowercase `kebab-case`.
11. Identify content pages stored outside the four typed content directories.
12. Identify near-duplicate pages caused by slug drift or weak disambiguation.
13. Identify slug collisions that would make bare `[[slug]]` links ambiguous.
14. Identify `wiki/index.md` entries missing category placement, links, or
    one-line summaries.
15. Record the lint pass in `wiki/log.md` if it materially affects the wiki or
    future work.

`lint` remains a health check. It should not be repurposed to perform raw-drift refresh or cascading page rewrites.

For larger wikis, prefer programmatic scans for link graphs, frontmatter shape, and index completeness instead of relying on manual inspection alone.

## Index and log

- `wiki/index.md` is the content-oriented catalog of the wiki.
- Read `wiki/index.md` first for queries and maintenance work.
- Organize `wiki/index.md` by category using sections for `Sources`,
  `Entities`, `Concepts`, and `Syntheses`.
- Include one entry per content page, with at least a link and a one-line
  summary.
- `wiki/log.md` is the chronological, append-only record of wiki activity.
- Start each log entry with a heading in this format:
  `## [YYYY-MM-DD] operation | title`

Examples:

```md
- [[wireguard]] - Entity page for WireGuard as a minimal, public-key-based VPN design.
```

```md
## [2026-04-07] ingest | Tailscale architecture source
```

## Pitfalls

- Never modify files in `raw/` unless the user explicitly asks.
- Do not store downloaded images ad hoc elsewhere in `raw/`; place them under
  `raw/assets/` and reference them as `[[raw/assets/...]]`.
- Do not leave relevant website image URLs in place when the corresponding raw
  material is being added to the corpus; download those images into
  `raw/assets/` unless they are obvious site chrome or unrelated assets.
- Do not skip orientation on an existing wiki before major ingest or synthesis
  work.
- Do not create pages for passing mentions just because a name appears once.
- Do not create alternate pages when an existing canonical slug already covers
  the topic.
- Do not update content pages without also considering whether `wiki/index.md`
  or `wiki/log.md` should change.
- Do not flatten contradictions away when the evidence is mixed or dated.
- Do not leave newly created pages weakly linked or invisible from the rest of
  the wiki.

## Completion checklist

Before finishing any wiki-changing task, verify that:

- no files in `raw/` were modified unless the user explicitly asked to add or
  update source material there
- any downloaded images added to the raw corpus were stored under `raw/assets/`
  rather than elsewhere in `raw/`
- relevant images from web-sourced raw material were downloaded locally into
  `raw/assets/` instead of being left as website image URLs
- every touched content page lives in the correct typed directory
- every touched content page begins with a short unheaded lead immediately after
  frontmatter
- wiki-page links use bare `[[slug]]` wherever possible
- raw-source references use `[[raw/...]]` in frontmatter, footnotes, or other
  structural citation inventories as appropriate
- downloaded image references use `[[raw/assets/...]]` rather than external
  URLs or plain relative Markdown paths
- every touched `source` page includes `raw_sha256`, and non-`source` pages do
  not include it
- no content-page slug collides with another content-page slug
- new pages were created only when they were justified over updating an existing
  page
- `wiki/index.md` reflects the current page set
- `wiki/log.md` has a new entry if the wiki changed materially
- contradictions, weak evidence, and open questions remain explicit
- the wiki is more useful and navigable than it was before the pass
