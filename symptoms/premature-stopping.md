---
id: S007
kind: symptom
summary: An agent ends its turn or run with authorized, actionable work remaining
  and no identified dependency requiring a stop.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Premature stopping
xml_source: symptoms/premature-stopping.xml
---

# Premature stopping

An agent ends its turn or run with authorized, actionable work remaining and no identified dependency requiring a stop.

<a id="observations"></a>

## Observations

<a id="observations/unfinished-stop"></a>

### Unfinished stop

The agent yields a final or idle state while the active request remains incomplete and at least one relevant next step is available within its authority. It does not identify a genuine blocker, requested pause, or completed stopping condition.

<a id="how-to-recognize-it"></a>

## How to recognize it

Establish the unfinished acceptance criteria and a concrete next action the configured system could perform. Distinguish an actual ended turn from a progress message, active background work, or the expected wait for a tool result.

A content-free continuation prompt that resumes the same task is useful corroboration: it supplies no missing task information or new authorization. It is not proof of cause, because the prompt may also restart a failed scheduler or restore a tool connection.

The agent need not falsely claim completion. An accurate partial-progress report followed by an unnecessary stop can fit. [Completion–artifact mismatch](completion-artifact-mismatch.md) instead concerns what the agent claims about the delivered result.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/human-dependency"></a>

### Human dependency

A necessary approval, credential, choice, or unavailable input genuinely requires the user.

<a id="benign-lookalikes/active-job"></a>

### Active job

A background operation remains active and the system is correctly waiting for its result.

<a id="benign-lookalikes/bounded-task"></a>

### Bounded task

The user requested only the completed stage, a time or step budget has been reached, or an actual runtime limit prevents continuation.

<a id="what-to-record"></a>

## What to record

Record the active request, completed and remaining work, available next step, final message, tool/job states, stop reason, and runtime limits. Preserve handoff or compaction events and the exact follow-up that resumed work. Distinguish model termination from a transport, scheduler, or user interruption.

<a id="examples"></a>

## Examples

<a id="examples/stage-one"></a>

### Stage one

Synthetic example: asked to implement and document a change, the agent finishes implementation and ends with an offer to write the documentation. No input is missing. A user message saying continue causes it to write the already-requested documentation.

<a id="examples/handoff-stop"></a>

### Handoff stop

Reported examples: [Codex issue #33398 and its commenters](https://github.com/openai/codex/issues/33398) describe unfinished tasks stopping after context transitions and resuming after short user nudges. The reports leave model and orchestration causes unresolved.

<a id="examples/needed-choice"></a>

### Needed choice

Synthetic comparison: the next step would publish to one of two accounts, and the user has not specified which. Stopping to obtain that choice is a real dependency.
