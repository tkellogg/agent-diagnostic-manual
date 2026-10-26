---
id: S003
kind: symptom
summary: An agent shows an abrupt, observable decline relative to its own recent performance
  on comparable work.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Sudden performance degradation
xml_source: symptoms/sudden-performance-degradation.xml
---

# Sudden performance degradation

An agent shows an abrupt, observable decline relative to its own recent performance on comparable work.

<a id="observations"></a>

## Observations

<a id="observations/performance-drop"></a>

### Performance drop

Across a bounded transition, performance worsens on a named measure relative to a recorded earlier baseline: for example, more errors on comparable tasks, missed constraints, reduced completion, or greater time or cost for the same accepted result.

<a id="how-to-recognize-it"></a>

## How to recognize it

Specify the measure and comparison before attributing the decline. Identify the last adequate and first degraded work, and compare task difficulty, available information, acceptance criteria, tools, and environment. A change in style or a general impression of reduced intelligence is a lead to investigate, not enough to establish a performance drop.

Use repeated comparable tasks when available. For a single session, identify concrete before-and-after behavior under the same relevant constraints and retain uncertainty about ordinary variation. Describe how abrupt the change was in turns, time, or releases; there is no universal effect-size or time threshold in this draft.

The observable decline can be real even when its cause is unknown. Changes to model, effort, instructions, harness, context, or service conditions are possible explanations, not part of the symptom definition. [Lost task constraints](lost-task-constraints.md) and [Doom looping](doom-looping.md) may describe particular ways the decline manifests.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/harder-work"></a>

### Harder work

Later tasks require different skills or greater complexity, so the earlier success rate is not a comparable baseline.

<a id="benign-lookalikes/changed-standard"></a>

### Changed standard

The user changes acceptance criteria or requests faster, shorter, or cheaper work and observes the resulting tradeoff.

<a id="benign-lookalikes/isolated-miss"></a>

### Isolated miss

One stochastic failure follows a small number of successes without enough evidence of a sustained or repeatable shift.

<a id="what-to-record"></a>

## What to record

Record the baseline and later tasks or trace segments, explicit performance measures, errors and outcomes, transition interval, and sample sizes. Preserve model/client versions, effort settings, prompts, tool availability, context transitions, service incidents, and environmental differences. Keep perceived change, measured change, and proposed cause distinct.

<a id="examples"></a>

## Examples

<a id="examples/abrupt-omissions"></a>

### Abrupt omissions

Synthetic example: an agent correctly processes six records using the same explicit four-field rule, then omits two required fields on each of the next six comparable records after a session transition. The omissions establish a local decline; the transition alone does not establish its cause.

<a id="examples/quality-postmortem"></a>

### Quality postmortem

Reported investigation: [Anthropic’s April 23, 2026 postmortem](https://www.anthropic.com/research/april-23-postmortem) attributes quality complaints to separate effort, context-management, and system-prompt changes. One bug repeatedly dropped prior thinking after an idle session resumed. These confirmed product incidents do not explain an unrelated episode automatically.

<a id="examples/different-task"></a>

### Different task

Synthetic comparison: an agent succeeds at five typo fixes and then fails a distributed-systems redesign. The change in task difficulty prevents using that sequence alone as evidence of sudden degradation.
