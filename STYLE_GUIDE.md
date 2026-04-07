# STYLE_GUIDE.md

This file defines the writing and presentation rules for the wiki in `wiki/`.
It is inspired by the MediaWiki documentation style guide, especially its
guidance on audience and content, language, and structuring pages.

`AGENTS.md` remains the authoritative contract for repo structure, workflow,
page types, frontmatter, and required section families. If this file conflicts
with `AGENTS.md`, follow `AGENTS.md`.

## Purpose

Use this guide when creating or materially updating wiki prose. The goal is to
make the wiki clearer, easier to scan, and easier to understand for readers
with different technical and cultural backgrounds.

This guide does not change the repo schema. It does not add metadata, new page
types, or new directories.

## Before writing

Write for mixed technical readers. Assume curiosity and some technical
literacy, but do not assume the reader already knows every acronym, protocol,
or workflow pattern.

Before writing, identify:

- who the page is for
- what the reader is trying to learn, understand, or verify
- what the reader likely already knows
- what background the reader still needs
- whether the page mainly summarizes a source, explains an entity, explains a
  concept, or answers a synthesis question

Choose depth based on the page's likely audience:

- If the page targets readers familiar with the topic, skip basic explanation
  and move quickly to the key distinctions.
- If the page may be read by newcomers to the topic, define non-obvious terms
  on first use and add a short amount of scaffolding before using jargon
  heavily.

Reduce hidden background assumptions:

- Do not assume the reader knows the local jargon of one field unless the page
  clearly targets that field.
- If the page expects prior knowledge of networking, Kubernetes,
  cryptography, or agent-runtime concepts, say so in the lead.
- Introduce one unfamiliar idea at a time instead of stacking several new
  concepts into the same paragraph.

## Core writing rules

State the page's purpose early. A reader should understand within the opening
lines what the page covers and why it exists.

Define before discussing:

- Define the main term in one plain sentence before discussing nuance,
  disagreements, or implementation details.
- If readers are likely to confuse nearby terms, explain the distinction early.
- On concept and entity pages, define the thing before expanding into tensions,
  history, or comparison.

Lead with the takeaway:

- State the main answer or summary early enough that a skimming reader can
  follow the page without reading every section.
- On synthesis pages, answer the question before expanding the reasoning.
- On source pages, summarize the source before listing evidence.

Use examples when abstraction alone would be hard to follow:

- When a concept is hard to picture, include one short example before or
  alongside the general explanation.
- Use examples to make unfamiliar terms legible, not to add side topics.
- Prefer simple examples that match the page's actual subject matter.

Explain links, do not hide explanation inside them:

- Do not rely on a link to carry the explanation.
- A sentence should still make sense if the reader does not open the linked
  page.

Preserve uncertainty:

- When the evidence is mixed, dated, or incomplete, say so directly.
- Keep tensions explicit instead of burying them inside dense explanation.
- Do not force a cleaner conclusion than the sources support.

## Language

Use plain English:

- Prefer concrete nouns and verbs over abstract framing.
- Prefer direct claims over throat-clearing such as "the wiki's current answer
  is" or "it can be argued that" when a simpler sentence is accurate.
- Define less-common acronyms and terms on first use unless the intended reader
  would clearly already know them.

Use active, professional, inclusive language:

- Prefer active voice when it keeps responsibility clear.
- Keep the tone professional, calm, and direct.
- Use inclusive language.

Avoid wording that adds friction without adding meaning:

- Avoid vague abstractions and filler.
- Avoid colloquialisms, jokes, and region-specific turns of phrase.
- Avoid saying a task or idea is "easy", "simple", or "obvious".
- Avoid unnecessary negative phrasing when a direct positive instruction or
  statement is clearer.

Prefer stable and concrete references:

- Prefer absolute dates over relative time words such as "recently" or
  "currently" when timing matters.
- Name the specific system, source, or concept instead of using vague pronouns
  such as "this" or "it" when the referent could be unclear.

Control sentence and paragraph shape:

- Prefer short to medium paragraphs.
- Split paragraphs that carry more than one major idea.
- If a paragraph is hard to skim, rewrite it.
- If a section introduces three or more mechanisms, phases, or takeaways,
  prefer a list over a dense paragraph.

## Structuring pages

Every content page should begin with a short lead immediately after frontmatter
and before the first section heading.

The lead should usually:

- explain what the page covers
- signal who the page is most useful for
- mention any prerequisite context the reader should have
- state the main takeaway early

Use sentence-case headings. Keep headings descriptive and consistent.

- Do not put a heading before the lead.
- Do not put links inside headings.
- Keep heading text functional rather than decorative.
- Treat the section families in `AGENTS.md` as content requirements, not as
  fixed title-case heading text.

Keep information flow predictable:

- Start with orientation, then move into detail.
- Define before discussing.
- Contrast easily confused ideas before assuming the reader sees the boundary.
- Establish significance before diving into nuance.

When possible, arrange sections so a reader can scan from:

1. what this page is for
2. the main answer or summary
3. the supporting detail
4. open questions and related pages

## Page-type guidance

The required page types and baseline section families are defined in
`AGENTS.md`. Use the guidance below as a writing overlay, not as a replacement
for the contract.

### Source pages

- Use the lead to identify the source, what kind of document it is, and why it
  matters to this wiki.
- In the summary section, state the source's main argument or contribution
  early.
- In the key takeaways section, favor distinct claims over repetitive
  restatements.
- In the evidence or notable details section, highlight concrete examples,
  evidence, and limitations rather than rewriting the whole source.

### Entity pages

- Use the lead to orient the reader to the entity and why it matters here.
- In the summary section, say what the entity is before describing debates
  around it.
- In the role or significance section, explain why the entity matters in the
  corpus, not only in the outside world.
- In the current understanding section, group related ideas together.
- Keep tensions explicit instead of burying them inside dense explanation.

### Concept pages

- Use the lead to define the concept in plain terms before expanding it.
- In the why it matters section, connect the concept to actual questions the
  wiki helps answer.
- In the current understanding section, define boundaries and distinguish the
  concept from nearby ideas when that helps avoid confusion.

### Synthesis pages

- Use the lead to restate the question and tell the reader what kind of answer
  the page gives.
- In the question or thesis section, phrase the question clearly and
  concretely.
- In the synthesized answer section, give the answer early, then support it.
- Keep supporting reasoning ordered and easy to scan.
- Use the unresolved points section to preserve what the wiki still does not
  know.

## Practical checks

Before finishing a material writing pass, check:

- the lead exists and orients the reader before the first heading
- the page purpose is clear within the opening lines
- the page states any important prerequisite background instead of assuming it
- the first screen contains the main takeaway, not only setup
- non-obvious terms are introduced with enough context
- nearby terms are distinguished when confusion is likely
- examples are used where abstraction alone would be hard to follow
- headings are in sentence case
- the main answer or summary appears before deep detail
- the prose is direct and free of filler
