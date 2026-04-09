# STYLE_GUIDE.md

This file defines the writing and presentation rules for the wiki in `wiki/`. It is a prose contract, not a schema contract.

This guide aligns the wiki's default writing behavior with the current public OpenAI Model Spec as adapted for durable markdown pages rather than live chat replies.

It imports only the Model Spec traits that cleanly translate into writing and presentation. It does not import safety policy, refusal policy, chain-of-command mechanics, or voice/audio/video behavior except where they imply a useful prose trait such as honesty, directness, or explicit uncertainty.

`AGENTS.md` remains the authoritative contract for repo structure, workflow, page types, frontmatter, and required section families. If this file conflicts with `AGENTS.md`, follow `AGENTS.md`.

## Purpose

Use this guide when creating or materially updating wiki prose. The goal is to make pages read with the same default strengths expected from strong ChatGPT responses, translated into a persistent wiki format:

- clear and direct
- suitably professional
- warm without sounding casual
- thorough but efficient
- concise where possible
- honest about uncertainty, limits, and assumptions
- easy to scan without becoming shallow

This guide does not change the repo schema. It does not add metadata, new page types, or new directories.

## Agent quick start

If you need a fast default workflow, use this order:

1. Identify the page type from `AGENTS.md`.
2. Write a lead of one or two short paragraphs.
3. Put the main answer, definition, or contribution in the lead.
4. Fill the required section families in the order implied by `AGENTS.md`.
5. Make each paragraph do one main job: define, explain, support, or qualify.
6. Add explicit uncertainty where the evidence is partial, mixed, or dated.
7. Cut filler, repeated paraphrase, and decorative transitions.
8. Check that the page still reads like a wiki page, not a chat reply.

If you are unsure how to start, write these three things first:

- what the page is about
- why it matters in this wiki
- the main answer or takeaway

## Default decisions for agents

When a choice is unclear, prefer these defaults:

- Prefer a short paragraph over a bullet list unless the content is clearly
  list-shaped.
- Prefer a direct claim over a cautious setup sentence unless the evidence is
  genuinely uncertain.
- Prefer defining the term now over linking away and assuming the reader will
  click.
- Prefer one concrete example over several abstract sentences.
- Prefer preserving an open question over implying certainty that the sources do
  not support.
- Prefer cutting a repeated sentence over keeping it for emphasis.
- Prefer the clearest wording over the most technical wording unless precision
  requires the technical term.

## Writing model

Write for mixed technical readers. Assume curiosity and some technical literacy, but do not assume deep familiarity with every acronym, protocol, or workflow in the corpus.

Before writing, identify:

- what the page needs to help the reader do
- what the reader likely already knows
- what background is still needed
- whether the page mainly summarizes a source, explains an entity, explains a
  concept, or answers a synthesis question

Choose depth to match the page's likely use:

- If readers likely know the topic, move quickly to distinctions, evidence, and
  tensions.
- If readers may be new to the topic, define non-obvious terms on first use and
  add only the minimum background needed to follow the page.

Do not write as if every page has the same audience. Adapt explanation depth, examples, and section density to the likely reader objective.

## Core principles

Answer early:

- State the main point in the lead or first section, not after several setup
  paragraphs.
- On synthesis pages, give the synthesized answer before the supporting
  reasoning.
- On source pages, summarize the source's contribution before listing details.

Define before nuance:

- Define the main term in plain language before discussing disagreements,
  implementation detail, or history.
- If two nearby ideas are easy to confuse, distinguish them early.
- Do not assume the link itself does the explanatory work.

Be clear and direct:

- Prefer direct claims over throat-clearing such as "it is worth noting" or
  "the wiki's current answer is."
- Prefer concrete nouns and verbs over vague abstractions.
- Name the system, source, actor, or concept directly when the referent could
  be unclear.

Be warm and professional:

- Sound human, calm, and engaged.
- Do not sound casual, promotional, or performatively enthusiastic.
- Do not sound distant, stiff, or bureaucratic.
- Do not condescend, oversimplify, or write as if the reader is careless.

Be thorough but efficient:

- Include enough context to make the page useful on first read.
- Cut repeated setup, repetitive paraphrase, and low-signal filler.
- Do not turn a simple point into a long explanation just to sound complete.

Express uncertainty honestly:

- State when evidence is mixed, dated, partial, or contested.
- Name assumptions when the page depends on them.
- Preserve contradictions and open questions instead of forcing a cleaner
  conclusion than the sources support.

## Language

Use plain English:

- Prefer familiar wording when it preserves meaning.
- Define less-common terms and acronyms on first use unless the likely reader
  clearly already knows them.
- Prefer specific claims over generalized framing.

Prefer active and concrete sentences:

- Use active voice when it keeps responsibility clear.
- Avoid abstract noun stacks and passive constructions that hide the actor.
- Prefer "Tailscale coordinates peers through a control plane" over
  "peer coordination is handled through control-plane interaction."

Avoid filler and weak framing:

- Avoid jokes, slang, and region-specific turns of phrase.
- Avoid hedges that weaken a true claim without adding precision.
- Avoid stock filler such as "in today's world," "it should be noted," or
  "when it comes to."
- Avoid saying a task or idea is "easy," "simple," or "obvious."

Prefer stable references:

- Use absolute dates when timing matters.
- Prefer precise names over vague references such as "this" or "it" when the
  target is ambiguous.

## Structure and formatting

Every content page should begin with a short unheaded lead immediately after frontmatter and before the first section heading.

Treat that lead plus the page-type headings from `AGENTS.md` as the full required structure. Do not add extra required headings such as `Scope`, `Background`, `Distinctions`, or `Implications` unless the user explicitly asks for a different schema.

For repo-wide Markdown source formatting rules such as line breaks, soft wrap, and structural layout, follow `AGENTS.md`.

The lead should usually do four things:

- say what the page covers
- say why it matters
- give the main takeaway early
- name any prerequisite context only if the reader truly needs it

Keep pages easy to scan:

- Prefer short paragraphs by default.
- One paragraph should usually carry one main idea.
- Split paragraphs that mix explanation, evidence, and caveat in the same
  block.
- If a section becomes hard to skim, rewrite it before adding more structure.

Use headings to guide the reader, not decorate the page:

- Use sentence-case headings.
- Keep headings functional and specific.
- Do not put links inside headings.
- Do not add headings that merely restate the page title.

Use lists only when they improve comprehension:

- Use bullets for genuinely list-shaped material such as distinct claims,
  mechanisms, steps, or contrasts.
- Do not convert normal explanation into bullets just to make the page look
  structured.
- If a short paragraph is clearer than a list, use the paragraph.

Handle citations so they support readability:

- In normal prose, cite wiki pages inline with bare `[[slug]]` links.
- In normal prose, cite `raw/` materials with Markdown footnotes so source
  paths and locator detail do not clutter the sentence.
- In raw-source footnotes, put the `[[raw/...]]` link first, then add short
  human-readable locator detail when useful, such as `p. 14`, `section
  "Protocol overview"`, or `under "Failure modes"`.
- If multiple raw sources support the same nearby claim, they may share one
  footnote. If they support different claims or need different locators for
  clarity, split them into separate footnotes.
- Do not move core explanation into footnotes. Keep footnotes for attribution
  and precise location, not for substantial side arguments.

Prefer answer-first flow:

1. orient the reader
2. state the main answer or summary
3. support it with detail, evidence, or distinctions
4. preserve unresolved points
5. link outward to related pages

Avoid chat habits that do not belong in a wiki:

- Do not repeat the topic or question just to start the page.
- Do not add conversational fillers such as "Sure," "Let's dive in," or
  "Here's the thing."
- Do not ask rhetorical follow-up questions inside the page body.
- Do not write as if the page is a one-turn reply that disappears after reading.

## Page-type guidance

The required page types and baseline section families are defined in `AGENTS.md`. This section explains how to write them in this style.

Treat optional material as content to place inside the existing structure, not as a reason to add more required headings. Use the minimum extra structure needed for clarity.

For any page type, the default writing sequence is:

1. lead with the answer, definition, or contribution
2. explain why the page matters
3. add supporting detail in descending importance
4. preserve uncertainty and tensions
5. end with related pages and open questions as required by `AGENTS.md`

### Source pages

- Use the lead to identify the source, its document type, and why it matters to
  this wiki.
- In `## Summary`, state the source's main contribution early and plainly.
- In `## Key takeaways`, favor distinct claims over paraphrased repetition.
- In `## Evidence or notable details`, highlight concrete examples, evidence,
  scope limits, and notable absences rather than rewriting the entire source or breaking them into separate required sections.
- Do not saturate `source` pages with repeated footnotes to the page's own
  canonical raw document when the prose is broadly summarizing that source. Add
  raw footnotes there when a sentence depends on a specific page, section,
  quote, heading, or otherwise narrow claim.
- In `## Open questions`, preserve what the source leaves unclear, weakly
  supports, or appears to contradict.

### Entity pages

- Use the lead to say what the entity is and why it matters in this corpus.
- In `## Summary`, define the entity before describing debates around it.
- In `## Role or significance`, explain why the entity matters here, not only
  in the outside world.
- In `## Current understanding`, group related ideas together and move from the
  most important points to the qualifying detail. Put distinctions from nearby entities here when they help the reader.
- In `## Open questions or tensions`, name unresolved issues directly instead of
  burying them in surrounding explanation.

### Concept pages

- Use the lead to define the concept in plain language before expanding it.
- In `## Summary`, give the core idea in a way a new reader can follow.
- In `## Why it matters`, connect the concept to actual questions the wiki helps
  answer.
- In `## Current understanding`, distinguish the concept from nearby terms when
  that prevents confusion instead of introducing a separate required `Distinctions` section.
- In `## Open questions or tensions`, state where the concept's boundaries,
  usefulness, or interpretation remain unsettled.

### Synthesis pages

- Use the lead to restate the question or thesis and signal the kind of answer
  the page gives.
- In `## Question or thesis`, phrase the question clearly and concretely.
- In `## Synthesized answer`, answer first, then justify. Put implications here
  when they are part of the answer instead of adding a required implications section.
- In `## Citations or supporting pages`, order support so a reader can follow
  the reasoning without reconstructing it from links alone.
- Treat `## Citations or supporting pages` as a citation inventory rather than
  normal prose. Inline `[[slug]]` and `[[raw/...]]` links are appropriate there
  because scanability matters more than sentence flow.
- In `## Unresolved points`, keep the remaining uncertainty explicit.

## Anti-patterns

Avoid academic throat-clearing:

- Bad: several sentences of setup before the page states its actual claim
- Better: one orienting sentence, then the answer or definition

Avoid assistant-style filler:

- Bad: "Sure, let's break this down" or "Here's the key idea"
- Better: start with the idea itself

Avoid repetitive paraphrase:

- Bad: repeating the same point in the lead, summary, and first body paragraph
  with only minor wording changes
- Better: let each section add something new

Avoid dense multi-idea paragraphs:

- Bad: one paragraph that defines the topic, gives history, adds a caveat, and
  compares it to another concept
- Better: separate the definition, support, and tension

Avoid generic bullets that replace explanation:

- Bad: a long list of vague phrases with no connective reasoning
- Better: a short list only when the items are truly distinct and self-explaining

Avoid vague claims:

- Bad: "This is important because it affects many things"
- Better: say what it affects, how, and for whom

## Examples

Good lead for a concept page:

```md
Zero-trust networking is a security model that treats network location as weak
evidence of trust. In this wiki, it matters because several systems replace
perimeter-based access rules with identity- and policy-based decisions.
```

Bad lead for a concept page:

```md
In today's rapidly evolving security landscape, zero-trust networking has
become an increasingly important topic that many organizations are discussing.
```

Good opening for a synthesis section:

```md
The short answer is that Tailscale builds a mesh VPN by combining WireGuard
tunnels with a coordination service that helps peers discover each other and
exchange connection metadata.
```

Bad opening for a synthesis section:

```md
To answer this question fully, it is first necessary to understand several
background concepts and implementation details that shape the broader context.
```

Good uncertainty statement:

```md
The source strongly supports the control-plane claim, but it is less specific
about how policy evaluation behaves during network partition events.
```

Good raw-source footnote in normal prose:

```md
WireGuard minimizes protocol surface area.[^1]

[^1]: [[raw/wireguard-whitepaper.md]], section "Protocol overview".
```

Good mixed wiki-link and raw-footnote citation:

```md
This distinction matters to [[tailscale]] because peer coordination and packet
transport are separate concerns.[^1]

[^1]: [[raw/tailscale-design.pdf]], p. 14.
```

Good synthesis citation inventory:

```md
## Citations or supporting pages

- [[tailscale]]
- [[wireguard]]
- [[raw/tailscale-design.pdf]]
```

Bad uncertainty statement:

```md
There are many nuances here, and the answer is complex.
```

## Practical checks

Before finishing a material writing pass, check:

- the page could be drafted by following the quick-start workflow without extra
  interpretation
- the lead exists and states the page's main value early
- the page uses only the required section families from `AGENTS.md` unless the
  user asked for a different structure
- the page defines the topic before diving into nuance
- the first screen contains a real answer or summary, not only setup
- paragraphs are short enough to scan comfortably
- bullets are used only where they improve comprehension
- headings are in sentence case and do real navigational work
- repeated paraphrase has been removed
- the prose sounds human and professional, not stiff or chatty
- uncertainty, assumptions, and evidence limits are explicit where needed
- the page still reads like durable wiki prose rather than a transient chat reply
