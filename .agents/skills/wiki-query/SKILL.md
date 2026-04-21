---
name: wiki-query
description: Use when answering questions from a wiki based on this template. Covers wiki-first retrieval, selective raw-source verification, answer synthesis, citation behavior, and when a durable answer should be filed back into the wiki as a synthesis page.
---

# Wiki Query

Use this skill before answering questions from a repository derived from this template.

## Purpose

The goal of query work is to answer from the accumulated wiki first, use `raw/` only when needed, and file durable answers back into the wiki when doing so improves the knowledge base.

## Query workflow

1. Start from `wiki/index.md` to locate the relevant parts of the wiki.
2. Read the most relevant wiki pages first.
3. Use `raw/` selectively when the wiki lacks needed detail, when a claim needs verification, or when a new source has not yet been integrated.
4. Synthesize from the wiki instead of rediscovering everything from `raw/` by default.
5. Cite supporting wiki pages inline with bare `[[slug]]` links.
6. Use raw-source footnotes in normal prose when the answer depends directly on `raw/` material.

## When to open raw sources

Go to `raw/` when:

- the wiki does not contain the needed detail
- the answer depends on a time-bounded, numerical, quoted, disputed, or source-specific claim
- the wiki appears stale relative to a source already present in the corpus
- the user is asking about material that has not yet been integrated

Do not default to `raw/` when the wiki already contains a good answer.

## How to answer

- Give the answer early rather than rebuilding the topic from scratch.
- Write in plain language with a professional tone, and define non-obvious terms when the answer would otherwise assume field familiarity.
- Use the wiki's own page structure and terminology where that helps the answer stay aligned with the repo.
- Make uncertainty explicit if the wiki or sources are mixed, partial, or dated.
- If the answer depends on both wiki pages and raw material, prefer inline `[[slug]]` links plus raw footnotes rather than replacing everything with raw citations.

## Durable vs one-off answers

Create or update a `synthesis` page when:

- the answer resolves a reusable question the wiki is likely to face again
- the answer combines multiple existing pages into a durable conclusion
- the answer would make the wiki materially easier to navigate later

Answer directly without creating a page when:

- the answer is trivial or one-off
- the answer does not improve the long-term usefulness of the wiki
- creating a page would mostly duplicate what already exists

## Filing back into the wiki

When an answer deserves to become durable wiki content:

1. Create or update the synthesis page under `wiki/syntheses/`.
2. Use the synthesis lead to state the answer in plain language, define any non-obvious key term the reader needs immediately, and add a short scope note when the conclusion is materially bounded.
3. Add the relevant supporting pages and raw sources under `## Evidence base`, using claim-led bullets rather than a flat link dump.
4. Keep contradictions or unresolved conflicts visible in `## Unresolved points` even when the synthesis privileges one interpretation.
5. Update `wiki/index.md` so the new or revised synthesis is discoverable.
6. Append the operation to `wiki/log.md`.

## Common failure modes

- Answering from `raw/` even though the wiki already has the needed synthesis
- Writing the answer in expert-only shorthand that a careful newcomer cannot follow
- Quoting raw material directly without integrating it into the wiki's existing concepts
- Creating a new synthesis page for a trivial answer
- Leaving a durable answer out of `wiki/index.md`
- Flattening mixed evidence into a false certainty
