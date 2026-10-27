---
id: S002
kind: symptom
summary: An agent repeats an unsuccessful action cycle without relevant changes that
  would reasonably support expecting a different outcome.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
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

Use the session transcript and tool execution log to pair attempts with their feedback, such as an edit with its test result or a search with its returned matches. Group cycles by the immediate outcome; this helps separate several tool calls within one attempt from successive attempts.

Compare command arguments, outputs, file diffs, service status, and timestamps between cycles. Look for evidence that a retry addresses the blocker: a corrected credential, new error, eliminated hypothesis, or documented recovery interval. Mark gaps in the recorded state rather than filling them with an assumption that nothing changed.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/bounded-retries"></a>

### Bounded retries

Retries follow a documented transient failure and a recovery interval that gives the next attempt a reason to succeed. That changed recovery state differs from [stalled cycles](doom-looping.md#observations/stalled-cycles); a retry limit alone would not explain unchanged failures.

<a id="benign-lookalikes/active-polling"></a>

### Active polling

Status checks follow an active external job at its expected cadence, and job telemetry shows progress or a documented completion window. The evolving job state supplies the relevant change missing from [stalled cycles](doom-looping.md#observations/stalled-cycles).

<a id="benign-lookalikes/hypothesis-testing"></a>

### Hypothesis testing

Successive attempts eliminate distinct hypotheses or add samples to a planned stochastic estimate. They advance the immediate investigation or add relevant information, unlike [stalled cycles](doom-looping.md#observations/stalled-cycles).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, model and harness versions, task type, immediate outcome, and the action/feedback boundaries used to count cycles. Preserve requested and executed calls, feedback, relevant state changes, retry policy, and context transitions. Include total cycles, consecutive stalled cycles, elapsed time, tokens or cost where available, and how the sequence ended: recovery, automatic limit, user interruption, or abandonment. Retain the corpus revision and actual counts so the provisional three-cycle screening rule can be reassessed across incidents.

<a id="examples"></a>

## Examples

<a id="examples/unchanged-permission"></a>

### Unchanged permission

Synthetic incident: five file-read attempts receive permission denied over two minutes. The trace shows only quoting and output-format changes; credentials and access rights stay unchanged. Comparing the five errors exposes five stalled cycles, two minutes of delay, and no retrieved file before the user interrupts.

<a id="examples/repeated-grep"></a>

### Repeated grep

Reported incident: [Claude Code issue #59318](https://github.com/anthropics/claude-code/issues/59318) describes 30–50+ identical grep calls returning identical output before manual interruption. The reporter recognized the loop in the repeated commands and estimated 1–2 hours spent on research expected to take 2–3 minutes. A complete execution trace is not supplied, so responsibility for the repeats remains unresolved.

<a id="examples/changing-failures"></a>

### Changing failures

Synthetic comparison: five successive edits resolve five different test failures. Test logs show the remaining failure count falling from five to zero. Although the agent repeats the edit/test cycle five times, each cycle advances the outcome and the final suite passes.
