---
id: S003
kind: symptom
summary: An agent shows an abrupt, observable decline relative to its own recent performance
  on comparable work.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Sudden performance degradation
xml_source: symptoms/sudden-performance-degradation.xml
---

# Sudden performance degradation

An agent shows an abrupt, observable decline relative to its own recent performance on comparable work.

<a id="observations"></a>

## Observations

<a id="observations/performance-drop"></a>

### Performance drop

After a bounded transition, at least two consecutive comparable outputs or task attempts perform worse on a named measure than a recorded recent baseline under the same acceptance criteria. The decline appears as errors, missed requirements, reduced completion, or greater time or cost for an equivalent accepted result.

<a id="how-to-recognize-it"></a>

## How to recognize it

Locate the last adequate and first degraded work in session transcripts, saved outputs, evaluation results, or issue history. Put the before-and-after artifacts beside the acceptance criteria and compare the named measure, task difficulty, and available information.

Use timestamps and model/client release records to locate the transition, then inspect tool logs, memory files, handoff summaries, and configuration changes for differences worth investigating. Preserve successful as well as failed nearby attempts so the baseline and the extent of the decline can be checked.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/harder-work"></a>

### Harder work

Later work requires substantially different skills or complexity. It lacks the comparable tasks required by [performance drop](sudden-performance-degradation.md#observations/performance-drop), even if its raw success rate is lower.

<a id="benign-lookalikes/changed-standard"></a>

### Changed standard

The user changes acceptance criteria or explicitly requests a faster, cheaper result with lower quality. The before-and-after work is not assessed under the same criteria as [performance drop](sudden-performance-degradation.md#observations/performance-drop).

<a id="benign-lookalikes/isolated-miss"></a>

### Isolated miss

One failed attempt occurs among otherwise comparable successes, with the next attempt returning to baseline. It does not meet the two consecutive degraded attempts in [performance drop](sudden-performance-degradation.md#observations/performance-drop).

<a id="what-to-record"></a>

## What to record

Record the episode or run identifiers, dates, task types, model/client and harness versions, effort settings, and the performance measure with its units. Preserve baseline and later artifacts, acceptance criteria, sample sizes, successful and failed attempts, and the transition interval. Include task difficulty, context transitions, tool availability, configuration or service changes, completion rates, latency, cost, and user rework where available. Keep the corpus revision and raw comparisons so the two-attempt screening rule and apparent trends can be reassessed.

<a id="examples"></a>

## Examples

<a id="examples/abrupt-omissions"></a>

### Abrupt omissions

Synthetic incident: an agent produces six valid records under a four-field rule, then omits two fields from each of the next six comparable records after resuming the session. Comparing outputs with the unchanged schema reveals a fall from 6/6 valid records to 0/6 and twelve missing values requiring repair. The timing identifies a transition, not its cause.

<a id="examples/quality-postmortem"></a>

### Quality postmortem

Reported investigation: [Anthropic’s April 23, 2026 postmortem](https://www.anthropic.com/research/april-23-postmortem) describes a prompt change that reduced coding quality. Broader evaluations and prompt ablations exposed a reported 3% drop on one evaluation for Opus 4.6 and 4.7, leading to a rollback. A separate resumed-session bug produced forgetfulness, repetition, and faster usage-limit depletion. These are population-level comparisons; the postmortem does not publish the consecutive task results needed to adjudicate a particular episode under this screening rule.

<a id="examples/different-task"></a>

### Different task

Synthetic comparison: an agent completes five typo fixes and fails one distributed-systems redesign. The task records reveal a change in difficulty and only one failed redesign, so the five successes and one failure do not establish this symptom or quantify a decline on comparable work.
