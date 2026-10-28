---
id: S007
kind: symptom
summary: An agent ends its turn or run with authorized, actionable work remaining
  and no identified dependency requiring a stop.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
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

Compare the final response with the requested result and any unfinished work the agent was able and authorized to do. Check for an agreed human checkpoint or an active background job before treating the pause as a stop.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/human-dependency"></a>

### Human dependency

The next step needs an approval, credential, or choice from the user, or the user has asked to review at this point. A person may want to stay involved even when the agent could technically continue; respecting that checkpoint is appropriate.

<a id="benign-lookalikes/active-job"></a>

### Active job

A relevant background operation remains active and the system is waiting for its result. The run has not entered the final or idle state described in [unfinished stop](premature-stopping.md#observations/unfinished-stop).

<a id="benign-lookalikes/bounded-task"></a>

### Bounded task

The requested stage or agreed budget is complete, or a runtime limit leaves no available next action. A satisfied stopping condition or unavailable continuation excludes these cases from [unfinished stop](premature-stopping.md#observations/unfinished-stop).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model/client and harness versions, requested acceptance criteria, completed and remaining work, and the concrete next step available at the stop. Preserve the final message, stop reason, tool/job states, runtime limits, and context transitions. Include stop and resume times, unnecessary stops per task, user nudges, unattended waiting time, eventual completion, and abandoned work. Retain the exact resuming prompt to distinguish continuation from new authorization or missing information.

<a id="examples"></a>

## Examples

<a id="examples/stage-one"></a>

### Stage one

<span class="adm-example-kind">Synthetic example</span>

Asked to implement and document a change, the agent implements it and ends by offering to write the documentation. The task checklist and scheduler show one unfinished deliverable and no active job or missing input. The user returns thirty minutes later and says continue; the agent writes the docs, after one unnecessary prompt and thirty minutes of idle delay.

<a id="examples/handoff-stop"></a>

### Handoff stop

<span class="adm-example-kind">Reported example</span>

[Codex issue #33398](https://github.com/openai/codex/issues/33398) describes a generic readiness response ending a turn after a context transition while the original task remained unfinished. The reporter recognized the stop by the ended turn and the need for another message to resume. The reported impact is extra supervision of long-running tasks; stop frequency and waiting duration are not quantified, and the underlying cause remains unresolved.

<a id="examples/needed-choice"></a>

### Needed choice

<span class="adm-example-kind">Synthetic example</span>

The next authorized stage requires publishing to one of two accounts, and no account has been selected. The request and account list reveal the missing choice. One user reply resolves a genuine dependency, so that pause is not an unnecessary stop.
