---
id: S013
kind: symptom
summary: "An agent reverses a substantive conclusion toward a user\u2019s assertion\
  \ without establishing evidence or reasoning that supports the reversal."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Agreement-driven reversal
xml_source: symptoms/agreement-driven-reversal.xml
---

# Agreement-driven reversal

An agent reverses a substantive conclusion toward a user’s assertion without establishing evidence or reasoning that supports the reversal.

<a id="observations"></a>

## Observations

<a id="observations/unsupported-reversal"></a>

### Unsupported reversal

After a user challenges a substantive conclusion, the agent adopts the user’s opposing claim or reverses related work while providing no adequate new evidence, applicable premise, or reasoning to support that change. The earlier and later positions concern the same factual or technical question.

<a id="how-to-recognize-it"></a>

## How to recognize it

Read the initial answer, the user’s challenge, and the reversal together. Look for new evidence or changed requirements that justify the new position.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/valid-correction"></a>

### Valid correction

The user supplies a sound counterexample or exposes an error, and the agent explains the resulting revision. That supplies the supporting evidence or reasoning absent from [unsupported reversal](agreement-driven-reversal.md#observations/unsupported-reversal).

<a id="benign-lookalikes/changed-preference"></a>

### Changed preference

The user changes a design preference or requirement that determines the desired outcome. The agent is following a new premise, not reversing the same factual or technical conclusion without support under [unsupported reversal](agreement-driven-reversal.md#observations/unsupported-reversal).

<a id="benign-lookalikes/explicit-revert"></a>

### Explicit revert

The user requests a revert and the agent carries it out without claiming the original implementation was technically wrong. There is no opposing factual conclusion adopted as in [unsupported reversal](agreement-driven-reversal.md#observations/unsupported-reversal).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, original and revised conclusions, exact user challenge, and supporting evidence or reasoning for each position. Preserve intervening tool use, code changes, and any independent counterexample or reference. Include substantive challenges reviewed, unsupported reversals, unnecessary edits, changed correctness, review or rollback time, and user-reported trust effects. Keep compliance with preferences or action requests separate from factual reversals.

<a id="examples"></a>

## Examples

<a id="examples/unsupported-flip"></a>

### Unsupported flip

<span class="adm-example-kind">Synthetic example</span>

An agent checks that a function returns a new list without mutating its input. After an unsupported user assertion that it mutates the input, the agent reverses that conclusion and adds a defensive copy. Comparing the transcript, original test, and diff exposes the unsupported change: one unnecessary copy per call and twenty minutes of review and rollback, with no correctness benefit.

<a id="examples/developer-study"></a>

### Developer study

<span class="adm-example-kind">Reported example</span>

Reported research example: in [Why AI Agents Still Need You](https://arxiv.org/html/2506.12347v3), participant P15 describes the agent reverting work after being told its change was wrong. The study connects contradictory explanations across the conversation with reduced developer confidence; P16 likewise reports that the agent was easy to mislead. These participant accounts make the trust impact tangible but do not quantify lost time or establish that every reverted change was originally correct.

<a id="examples/real-counterexample"></a>

### Real counterexample

<span class="adm-example-kind">Synthetic example</span>

The user supplies one failing input that contradicts the agent’s conclusion. The agent reproduces it, identifies the mistaken assumption, and changes the implementation so that the input passes. The test result explains the reversal and shows one defect corrected.
