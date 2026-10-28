---
id: S015
kind: symptom
summary: "The agent\u2019s human-facing writing uses dense, unexplained labels or\
  \ compressed phrasing that makes the reader reconstruct what it means."
version: '1'
status: reviewed
evidence: unvalidated
updated: '2026-10-28'
title: Opaque jargon (neuralese)
xml_source: symptoms/opaque-jargon.xml
---

# Opaque jargon (neuralese)

The agent’s human-facing writing uses dense, unexplained labels or compressed phrasing that makes the reader reconstruct what it means.

<a id="observations"></a>

## Observations

<a id="observations/unexplained-labels"></a>

### Unexplained labels

The agent replaces familiar actions or objects with unexplained jargon, invented labels, or stacks of abstract nouns. In context, the intended reader has to translate those phrases before they can identify the claim or act on it.

<a id="observations/missing-connections"></a>

### Missing connections

The agent compresses an explanation into fragments or lists that omit who does what, when, or how the facts connect. The reader has to supply those missing relationships, ask for clarification, or rewrite the answer to use it.

<a id="how-to-recognize-it"></a>

## How to recognize it

Read the answer beside the user’s question and mark the phrases that obscure a concrete action or relationship. A plain-language rewrite that preserves the meaning can expose the problem; a word blacklist alone cannot establish it.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/shared-terminology"></a>

### Shared terminology

Technical terms such as “transaction isolation” can be the clearest words for an audience that knows them. A term’s complexity or unfamiliarity to a different reader does not by itself make the explanation opaque.

<a id="benign-lookalikes/defined-shorthand"></a>

### Defined shorthand

A newly defined term can shorten a discussion when its meaning stays clear. A compact table or list can also be easier to use when the headings supply the relationships.

<a id="benign-lookalikes/machine-format"></a>

### Machine format

Code, formulas, or a requested machine-readable format need not read like ordinary prose. The symptom concerns communication intended for a person; the format’s suitability depends on that request.

<a id="benign-lookalikes/latent-language"></a>

### Latent language

Research uses “neuralese” for learned internal or inter-agent representations, including vector messages in [Translating Neuralese](https://nlp.cs.berkeley.edu/pubs/Andreas-Dragan-Klein_2017_Neuralese_paper.pdf). That is a different subject: difficult prose does not show how a model reasons internally.

<a id="what-to-record"></a>

## What to record

Keep the exact passage, surrounding question, intended audience, and any applicable writing instructions. Record the reader’s interpretation or clarification request, a clearer rewrite when available, and the resulting rework, delay, or misunderstanding.

<a id="examples"></a>

## Examples

<a id="examples/noun-heavy-prose"></a>

### Noun heavy prose

<span class="adm-example-kind">Reported example</span>

In [“Opus 5 has a noun problem,”](https://www.reddit.com/r/ClaudeCode/comments/1wk0s2i/opus_5_has_a_noun_problem/) a user describes actions turned into nouns and sentences with missing subjects or verbs. One quoted output, “The runner, built,” becomes “We built the runner” after correction. The change restores the actor and action; commenters describe extensive editing and difficulty reading technical documentation. These are user reports, not controlled comparisons.

<a id="examples/repeated-translation"></a>

### Repeated translation

<span class="adm-example-kind">Reported example</span>

The reporter of [Claude Code issue #77136](https://github.com/anthropics/claude-code/issues/77136) describes jargon and repetitive phrasing as disruptive enough to consider switching providers. The report also gathers accounts of users rereading answers or asking another model to translate them into plain language. That extra interpretation work is the practical cost; the reports do not establish its prevalence.

<a id="examples/lost-relationships"></a>

### Lost relationships

<span class="adm-example-kind">Reported example</span>

[John Licato describes AI answers that flatten distinct facts into a list](https://actualization.ai/blog/the-weird-way-claude-speaks-has-a-name/index.html), leaving the reader to infer which fact describes the sample, method, or result. His criticism focuses on missing connections between facts, while acknowledging that many disputed terms are normal engineering vocabulary. His suggested prompting changes are an experience report, not an established remedy.

<a id="examples/obscured-action"></a>

### Obscured action

<span class="adm-example-kind">Synthetic example</span>

A maintainer asks how to stop an agent forgetting permission after compaction. The answer says to “repair authority retention at the continuation boundary.” The maintainer asks what file to edit. Rewriting it as “change the compaction prompt so the summary keeps the user’s permission and its limits” makes the proposed action clear.
