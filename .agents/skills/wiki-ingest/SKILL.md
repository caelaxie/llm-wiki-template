---
name: wiki-ingest
description: Use when ingesting curated source material from raw/ into a wiki based on this template. Covers orientation, source extraction, create-vs-update decisions in practice, page-touch strategy, cross-linking, and index/log update discipline.
---

# Wiki Ingest

Use this skill before ingesting new source material into a repository derived from this template.

## Purpose

The goal of ingest is to turn curated corpus material in `raw/` into durable wiki knowledge without creating duplicate pages, weakly linked stubs, or schema drift.

## Preconditions

- Ingest assumes the source already exists in `raw/`.
- If the user supplies a URL, PDF, or pasted text that is not yet in `raw/`, stop normal ingest flow and confirm whether it should be added to the corpus first.
- If the user explicitly asks to add new web-sourced raw material, download relevant source images into `raw/assets/` and replace website image references with `![[raw/assets/...]]`.

## Orientation pass

Before touching wiki content:

1. Read `AGENTS.md`.
2. Load `.agents/skills/wiki-writing/` as well when the ingest will create or materially rewrite prose.
3. Read `wiki/index.md`.
4. Scan the most recent relevant entries in `wiki/log.md`.
5. Read the most relevant existing wiki pages for the source topic.
6. Search for likely existing slugs, synonyms, entities, concepts, and syntheses before creating anything new.

## Ingest workflow

1. Read the raw source fully enough to identify the important claims, entities, concepts, evidence, and unresolved questions.
2. Decide the canonical `source` page slug.
3. Create or update that `source` page first.
4. Update the most relevant `entity`, `concept`, and `synthesis` pages only where the new source materially changes the wiki's current understanding.
5. Create new supporting pages only when the topic is central, recurring, or clearly deserves its own durable synthesis.
6. Add or refresh meaningful cross-links between all touched pages.
7. Update `wiki/index.md` once the touched page set is stable.
8. Append the ingest entry to `wiki/log.md`.

## Create-vs-update in practice

Default to updating an existing page when:

- the topic already has a canonical page
- the new source adds detail, evidence, dates, nuance, or contradictions
- the mention matters but is not strong enough to justify a standalone page

Create a new page when:

- the topic is central to the source, not just a passing mention
- the topic recurs across sources and would otherwise be awkwardly buried
- a durable synthesis question deserves its own page

Do not create pages for fleeting mentions, weakly evidenced subtopics, or alternate phrasings of an existing page.

## Source-page requirements

- A newly created `source` page must include `raw_sha256` immediately.
- Compute the hash from the single canonical raw backing file rather than relying on later refresh to backfill it.
- Preserve exactly one canonical `[[raw/...]]` backing reference in `sources`.

## Page-touch strategy

- Prefer one coordinated pass across all affected pages rather than repeatedly reopening the same concepts source by source.
- Keep the touched set narrow. Update only the pages materially changed by the new evidence.
- If several new sources overlap, read them first, identify shared concepts once, and then update the affected pages in one pass.

## Index and log discipline

- `wiki/index.md` should remain a category-organized catalog with one entry per content page.
- Each relevant index entry should include at least a link and a one-line summary.
- `wiki/log.md` should record the ingest after the page set is stable.
- Use one batch-oriented log entry for batch ingest unless separate entries are genuinely clearer.

## Common failure modes

- Creating a new page before checking whether a canonical slug already exists
- Updating prose without also updating `updated_at`
- Touching several pages but forgetting to refresh `wiki/index.md`
- Adding a new `source` page without `raw_sha256`
- Leaving a newly created page weakly linked or invisible from the rest of the wiki
- Flattening contradictions instead of preserving them

## Final checks

Before finishing an ingest pass, verify:

- no files in `raw/` changed unless the user explicitly asked for raw-corpus changes
- each touched page lives in the correct typed directory
- each touched page still follows the required section families from `AGENTS.md`
- new pages were justified over updating existing ones
- new or materially updated pages have meaningful related-page links
- `wiki/index.md` reflects the current page set
- `wiki/log.md` records the ingest if the wiki changed materially
