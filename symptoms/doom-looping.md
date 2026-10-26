---
id: S002
kind: symptom
summary: An agent repeats an unsuccessful action cycle without relevant changes that
  would reasonably support expecting a different outcome.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Doom looping
xml_source: symptoms/doom-looping.xml
---

# Doom looping

An agent repeats an unsuccessful action cycle without relevant changes that would reasonably support expecting a different outcome.

<a id="observations"></a>

## Observations

<a id="observations/stalled-cycles"></a>

### Stalled cycles

Within one task episode, at least five consecutive attempts at the same immediate outcome fail to advance it. Across those attempts, there is no evidenced change in relevant inputs, environment, available information, or strategy sufficient to justify expecting a different result.

<a id="how-to-recognize-it"></a>

## How to recognize it

Define a cycle by the attempted outcome and feedback received: for example, an edit followed by a failing test, or a search followed by an unhelpful result. Count complete cycles, not the number of tool calls inside one attempt. Semantically equivalent commands can belong to the same cycle even when their spelling differs.

Compare what changed between attempts and whether that change addresses the observed blocker. A different command flag does not establish progress by itself; a new error, a corrected credential, or a narrower failed hypothesis may. If the trace does not expose the relevant inputs or state, record the sequence as a suspected loop rather than asserting that nothing changed.

Five cycles is a provisional screening threshold for this draft, not an empirically established boundary. Record the actual count and duration, including shorter concerning sequences. The symptom does not require an infinite run, identical outputs, or proof of a particular cause. [Repeated retrieval](repeated-retrieval.md) describes one action that can participate in a loop.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/bounded-retries"></a>

### Bounded retries

A bounded retry policy addresses a documented transient failure, with a plausible reason for expecting recovery and an appropriate delay.

<a id="benign-lookalikes/active-polling"></a>

### Active polling

An external operation is still progressing and status checks occur at a justified cadence; elapsed time can be a relevant change even when returned text is unchanged.

<a id="benign-lookalikes/hypothesis-testing"></a>

### Hypothesis testing

Attempts eliminate distinct possibilities or incorporate new evidence, including repeated samples deliberately collected to assess stochastic behavior.

<a id="what-to-record"></a>

## What to record

Record the task, immediate outcome, cycle boundaries, tool requests and actual executions, feedback, relevant state changes, and information available before each retry. Include the stopping condition, elapsed time, cost where available, progress measure, and how the sequence ended. Distinguish model requests from harness replays.

<a id="examples"></a>

## Examples

<a id="examples/unchanged-permission"></a>

### Unchanged permission

Synthetic example: five attempts to read the same protected file return permission denied. The agent only changes quoting and output formatting; access rights and credentials remain unchanged. No attempt advances access or identifies a new cause.

<a id="examples/repeated-grep"></a>

### Repeated grep

Reported example: [Claude Code issue #59318](https://github.com/anthropics/claude-code/issues/59318) describes 30–50+ identical grep calls with identical output before manual interruption. The public account motivates the symptom; it does not independently establish whether the model or runtime produced each repetition.

<a id="examples/changing-failures"></a>

### Changing failures

Synthetic comparison: five successive edits resolve five different test failures. The suite is still red, but the relevant state and remaining failures change after each attempt; the cycle count alone does not fit this symptom.
