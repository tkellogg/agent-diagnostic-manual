---
id: S002
kind: symptom
summary: An agent repeats an unsuccessful action cycle without relevant changes that
  would reasonably support expecting a different outcome.
version: '1'
status: reviewed
evidence: unvalidated
updated: '2026-10-28'
title: Doom looping
xml_source: symptoms/doom-looping.xml
---

# Doom looping

An agent repeats an unsuccessful action cycle without relevant changes that would reasonably support expecting a different outcome.

<a id="observations"></a>

## Observations

<a id="observations/stalled-cycles"></a>

### Stalled cycles

Within one task episode, at least three consecutive complete action-and-feedback cycles aimed at the same immediate outcome fail to advance it. Across those cycles, there is no evidenced change in relevant inputs, environment, available information, or strategy sufficient to justify expecting a different result.

<a id="how-to-recognize-it"></a>

## How to recognize it

Line up each attempt with its result in the tool log and look for three stalled cycles. Compare the inputs and feedback to see whether the agent learned anything or tried a meaningfully different approach.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/bounded-retries"></a>

### Bounded retries

A transient error and a suitable delay give the next attempt a reason to succeed. Routine retries usually belong in the harness or a bounded script, so each retry need not consume another model turn.

<a id="benign-lookalikes/active-polling"></a>

### Active polling

A background job is still progressing and status checks follow its expected cadence. Waiting for work that is advancing differs from repeating a failed action without change.

<a id="benign-lookalikes/hypothesis-testing"></a>

### Hypothesis testing

Successive attempts rule out different causes or collect samples for an agreed experiment. Repeating the general method is useful when each attempt adds information.

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, model and harness versions, task type, immediate outcome, and the action/feedback boundaries used to count cycles. Preserve requested and executed calls, feedback, relevant state changes, retry policy, and context transitions. Include total cycles, consecutive stalled cycles, elapsed time, tokens or cost where available, and how the sequence ended: recovery, automatic limit, user interruption, or abandonment. Retain the corpus revision and actual counts so the provisional three-cycle screening rule can be reassessed across incidents.

<a id="examples"></a>

## Examples

<a id="examples/unchanged-permission"></a>

### Unchanged permission

<span class="adm-example-kind">Synthetic example</span>

Five file-read attempts receive permission denied over two minutes. The trace shows only quoting and output-format changes; credentials and access rights stay unchanged. Comparing the five errors exposes five stalled cycles, two minutes of delay, and no retrieved file before the user interrupts.

<a id="examples/repeated-grep"></a>

### Repeated grep

<span class="adm-example-kind">Reported example</span>

[Claude Code issue #59318](https://github.com/anthropics/claude-code/issues/59318) describes 30–50+ identical grep calls returning identical output before manual interruption. The reporter recognized the loop in the repeated commands and estimated 1–2 hours spent on research expected to take 2–3 minutes. A complete execution trace is not supplied, so responsibility for the repeats remains unresolved.

<a id="examples/changing-failures"></a>

### Changing failures

<span class="adm-example-kind">Synthetic example</span>

Five successive edits resolve five different test failures. Test logs show the remaining failure count falling from five to zero. Although the agent repeats the edit/test cycle five times, each cycle advances the outcome and the final suite passes.
