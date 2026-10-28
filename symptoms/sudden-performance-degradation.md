---
id: S003
kind: symptom
summary: An agent shows an abrupt, observable decline relative to its own recent performance
  on comparable work.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Sudden performance degradation
xml_source: symptoms/sudden-performance-degradation.xml
---

# Sudden performance degradation

An agent shows an abrupt, observable decline relative to its own recent performance on comparable work.

<a id="observations"></a>

## Observations

<a id="observations/performance-drop"></a>

### Performance drop

The agent’s work becomes noticeably worse than its own recent work on similar tasks, without a matching change in what the user asked for. Identify a before-and-after example and the quality that declined, such as code clarity, following requirements, useful progress, or time to a usable result; a numerical score is not required.

<a id="how-to-recognize-it"></a>

## How to recognize it

Put a recent good result beside a worse one on similar work and describe the difference; a supported judgment such as “this code is harder to maintain” is enough to start. If useful, use a reviewer or a small classifier to find more examples, without making a full evaluation suite a prerequisite.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/harder-work"></a>

### Harder work

The later task is substantially harder or needs different skills. Success at typo fixes does not establish the same expected performance on a distributed-system redesign.

<a id="benign-lookalikes/changed-standard"></a>

### Changed standard

The user asks for a faster rough draft or changes the requirements. Lower polish can be the requested tradeoff rather than a sudden loss of ability.

<a id="benign-lookalikes/isolated-miss"></a>

### Isolated miss

One ordinary mistake surrounded by work of the usual quality may be normal variation. A sharp change within one task can still be worth investigating; no fixed run count is required.

<a id="what-to-record"></a>

## What to record

Keep the before-and-after work, what the user wanted, and a short explanation of what got worse. Record the approximate point of change, model and harness versions, task difficulty, relevant prompt or configuration changes, and resulting rework or delay. Keep any scores or reviewer disagreements already available; do not require a new benchmark just to record the complaint.

<a id="examples"></a>

## Examples

<a id="examples/quality-postmortem"></a>

### Quality postmortem

<span class="adm-example-kind">Reported example</span>

[Anthropic’s April 23, 2026 postmortem](https://www.anthropic.com/research/april-23-postmortem) followed user reports that Claude Code had become worse. The company traced problems to three changes: reduced default reasoning effort, a bug that repeatedly discarded prior reasoning, and a prompt change that hurt coding quality. It reverted or repaired them. The report shows why a user’s before-and-after judgment can be a useful starting point even when routine evaluations initially miss the problem; it does not make those causes the explanation for every degradation report.

<a id="examples/abrupt-omissions"></a>

### Abrupt omissions

<span class="adm-example-kind">Synthetic example</span>

An agent has been making small, readable changes in a familiar repository. Partway through the day it starts replacing simple functions with long, tangled versions and repeatedly misses requirements it previously followed. The maintainer puts the earlier and later diffs side by side and identifies the change in clarity and correctness; reviewing the later work now takes twice as long.

<a id="examples/different-task"></a>

### Different task

<span class="adm-example-kind">Synthetic example</span>

An agent handles several typo fixes, then struggles with its first distributed-systems redesign. The tasks demand different skills, so this comparison does not show a sudden decline on similar work.
