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
- In normal prose, cite `raw/` materials with Markdown footnotes when the
  prose depends directly on them.
- Treat footnotes as attribution and locator detail only, not as a place for
  side arguments, caveats, definitions, or extra explanation.
- Use a raw footnote when a claim is quoted, dated, numerical, source-
  specific, potentially disputed, surprising, or otherwise grounded directly in
  `raw/` material.
- A raw footnote is optional for broad orienting statements that are
  immediately followed by a cited supporting sentence or paragraph.
- A raw footnote is discouraged for generic setup sentences and repeated
  restatements of a claim already cited in the same short paragraph.
- On `source` pages, cite support-bearing paragraphs rather than trying to
  footnote every sentence mechanically.
- When adjacent sentences rely on the same raw source and the same locator or
  tight locator range, one footnote may cover them both. Split footnotes when
  the support shifts to a different section, page, source, or evidentiary
  strength.
- When a sentence is supported by both wiki pages and raw material, prefer an
  inline `[[slug]]` link plus a raw footnote.
- In raw-source footnotes, put the `[[raw/...]]` link first, then add the
  shortest useful locator detail, such as `p. 14`, `section "Protocol
  overview"`, or `under "Failure modes"`.

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
- In `## Summary`, state the source's main contribution early and plainly, then
  add a required nested section map.
- Keep the section map inside `## Summary`; do not add a separate `## Section
  map` heading.
- Structure the section map as short bullets, usually one sentence each.
- Use one bullet per section and subsection, with nested bullets indented by
  two spaces per level to show hierarchy.
- Preserve the source's original section numbering when it exists. If the
  source does not number sections, use titled nested bullets instead.
- Make each bullet say what that section or subsection does and why it matters.
  Add at most one notable claim when it materially helps navigation.
- Skip boilerplate headings such as acknowledgements, references, and author
  notes by default. Include appendices only when they add substantive content
  relevant to the wiki.
- On very long or mechanical outlines, fold low-signal branches into the
  nearest meaningful parent bullet rather than mirroring every minor heading.
- In `## Key takeaways`, favor distinct claims over paraphrased repetition.
- In `## Evidence or notable details`, highlight concrete examples, evidence,
  scope limits, and notable absences rather than rewriting the entire source or
  breaking them into separate required sections.
- Keep the nested section map navigational. Detailed interpretation still
  belongs in `## Key takeaways` and `## Evidence or notable details`.
- On `source` pages, cite most factual or interpretive claims in the body, but
  let nearby sentences share a footnote when they depend on the same raw source
  and the same locator range.
- Use a raw footnote on a `source` page when the prose narrows to a specific
  page, section, quote, heading, statistic, or other claim that needs precise
  grounding.
- In `## Open questions`, preserve what the source leaves unclear, weakly
  supports, or appears to contradict.

Example source-page template:

```md
---
title: "Example Paper Title"
type: "source"
sources:
  - "[[raw/example-paper.md]]"
raw_sha256: "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
created_at: "2026-04-10"
updated_at: "2026-04-10"
---

This page covers *Example Paper Title*, a paper about how a distributed system handles coordination and recovery. For this wiki, its main value is that it makes the paper's argument, evidence, and limits easy to scan before reading the full document.

## Summary

The paper argues that the proposed design improves recovery behavior by making failure handling explicit instead of treating it as a side effect of the normal path.[^1] Its main contribution to this wiki is a compact model for separating steady-state behavior from recovery behavior.

Section map:
- 1 Introduction: frames the problem, names the paper's core claim, and states why prior approaches are hard to reason about.[^1]
- 2 System model: defines the assumptions that bound the rest of the argument.[^2]
  - 2.1 Failure model: narrows which failures the design is meant to handle.[^2]
  - 2.2 Network assumptions: explains the timing and connectivity assumptions behind the evaluation.[^2]
- 3 Design: presents the mechanism and the main invariants the authors want the reader to carry into the evaluation.[^3]
  - 3.1 Coordination path: explains how the system behaves during normal operation.[^3]
  - 3.2 Recovery path: explains how the system handles failure and rejoin behavior.[^4]
    - 3.2.1 State transfer: shows how state is synchronized during recovery.[^4]
    - 3.2.2 Rejoin conditions: defines when a recovered node can safely participate again.[^4]
  - 3.3 Implementation details: covers storage layout, batching, and retry mechanics that matter less to the main argument, so those low-signal sub-branches are folded into this parent bullet.
- 4 Evaluation: reports steady-state and fault-injection results, then compares them against two baselines.[^5]
  - 4.1 Throughput results: measures normal-case performance.[^5]
  - 4.2 Fault-injection results: measures degradation and recovery under failure.[^6]
- 5 Limitations: narrows the claim to the conditions actually studied.[^7]
- Appendix A: details the benchmark harness used in the evaluation and is worth keeping because later wiki pages may need that methodology.[^8]

## Key takeaways

- The paper's main contribution is the separation between normal operation and recovery behavior.
- Its strongest evidence comes from evaluating both steady-state behavior and failure handling rather than only reporting best-case performance.
- The claims appear strongest in environments that match the stated failure and network assumptions.

## Evidence or notable details

The design section makes correctness depend on a bounded failure model and on explicit coordination points between replicas.[^3] That matters because the later performance claims only make sense if those coordination costs are accepted as part of the model.

The evaluation is also notable for separating steady-state benchmarks from fault-injection experiments.[^5] That makes it easier to see which improvements come from the design itself and which depend on favorable operating conditions.

## Related pages

- [[example-system]]
- [[failure-recovery]]
- [[coordination-under-partial-failure]]

## Open questions

- Does the paper's failure model match the environments this wiki cares about?
- Are the gains still convincing under noisier real-world conditions?
- Which parts of the design are durable concepts and which are paper-specific?

[^1]: [[raw/example-paper.md]], section "Introduction".
[^2]: [[raw/example-paper.md]], section "System model".
[^3]: [[raw/example-paper.md]], section "Design".
[^4]: [[raw/example-paper.md]], section "Recovery path".
[^5]: [[raw/example-paper.md]], section "Evaluation".
[^6]: [[raw/example-paper.md]], section "Fault-injection results".
[^7]: [[raw/example-paper.md]], section "Limitations".
[^8]: [[raw/example-paper.md]], appendix A.
```

### Entity pages

- Use the lead to say what the entity is and why it matters in this corpus.
- In `## Summary`, define the entity before describing debates around it.
- In `## Role or significance`, explain why the entity matters here, not only
  in the outside world.
- In `## Current understanding`, group related ideas together and move from the
  most important points to the qualifying detail. Put distinctions from nearby entities here when they help the reader.
- When a claim is grounded directly in `raw/` material rather than only in
  linked wiki pages, use a raw footnote in the same sentence or paragraph.
- When both support types matter, prefer the mixed pattern of inline `[[slug]]`
  plus a raw footnote.
- In `## Open questions or tensions`, name unresolved issues directly instead of
  burying them in surrounding explanation.

### Concept pages

- Use the lead to define the concept in plain language before expanding it.
- In `## Summary`, give the core idea in a way a new reader can follow.
- In `## Why it matters`, connect the concept to actual questions the wiki helps
  answer.
- In `## Current understanding`, distinguish the concept from nearby terms when
  that prevents confusion instead of introducing a separate required `Distinctions` section.
- When the prose depends directly on `raw/` evidence, use a raw footnote rather
  than leaving the claim unsupported or burying the support in a separate note.
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
- In the prose sections, use raw footnotes when a claim is tied directly to the
  source material instead of to another wiki page alone.
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

Good source-page paragraph with paragraph-level citation grouping:

```md
The document describes a control plane that helps peers discover each other and
exchange connection metadata. It also separates that coordination role from the
packet transport path.[^1]

[^1]: [[raw/tailscale-design.pdf]], p. 14.
```

Good source-page paragraph with split footnotes when support changes:

```md
The document says the coordination service handles peer discovery. A separate
section describes packet transport in WireGuard tunnels.[^1][^2]

[^1]: [[raw/tailscale-design.pdf]], p. 14.
[^2]: [[raw/tailscale-design.pdf]], section "Packet transport".
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

Bad raw footnote that explains instead of attributing:

```md
WireGuard minimizes protocol surface area.[^1]

[^1]: [[raw/wireguard-whitepaper.md]], section "Protocol overview". This is
important because it makes the system easier to reason about in practice.
```

Bad pattern with a redundant footnote on every sentence:

```md
The document describes a control plane.[^1] It also describes peer discovery.[^2]
It then separates transport from coordination.[^3]

[^1]: [[raw/tailscale-design.pdf]], p. 14.
[^2]: [[raw/tailscale-design.pdf]], p. 14.
[^3]: [[raw/tailscale-design.pdf]], p. 14.
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
- citation density matches the support instead of becoming mechanical
- footnotes carry attribution and locator detail, not side arguments
- the page still reads like durable wiki prose rather than a transient chat reply
