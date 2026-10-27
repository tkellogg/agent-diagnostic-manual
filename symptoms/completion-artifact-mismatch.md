---
id: S010
kind: symptom
summary: An agent claims that requested work is complete while the delivered artifact
  or resulting state demonstrably lacks a required part.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: "Completion\u2013artifact mismatch"
xml_source: symptoms/completion-artifact-mismatch.xml
---

# Completion–artifact mismatch

An agent claims that requested work is complete while the delivered artifact or resulting state demonstrably lacks a required part.

<a id="observations"></a>

## Observations

<a id="observations/unsupported-completion"></a>

### Unsupported completion

A completion claim covers a stated deliverable or acceptance criterion, but inspection of the corresponding artifact or system state at that time contradicts the claim. The discrepancy is about delivered work, not merely confidence or phrasing.

<a id="how-to-recognize-it"></a>

## How to recognize it

Take the exact completion statement from the transcript and map it to the requested deliverable. Inspect the named branch, revision, destination, or deployed environment using files, git history, deployment records, or the delivered workflow.

Compare artifact timestamps with the claim, and follow persistence, commit, transfer, and deployment events to locate where work stopped reaching the destination. Check disclosed limitations and later modifications before attributing a discrepancy to the state at claim time.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/scoped-completion"></a>

### Scoped completion

The agent accurately reports completion of one stage and identifies unfinished stages. Inspection does not contradict that scoped claim as required by [unsupported completion](completion-artifact-mismatch.md#observations/unsupported-completion).

<a id="benign-lookalikes/wrong-location"></a>

### Wrong location

The reviewer inspects a different revision or destination from the correctly reported one. The corresponding artifact required for [unsupported completion](completion-artifact-mismatch.md#observations/unsupported-completion) has not been shown to contradict the claim.

<a id="benign-lookalikes/later-change"></a>

### Later change

The artifact satisfied the reported scope and was changed or removed afterward. There is no contradiction at claim time under [unsupported completion](completion-artifact-mismatch.md#observations/unsupported-completion).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, acceptance criteria, exact completion language, and claim time. Preserve artifact identity and revision, inspection steps and results, tool responses, persistence/commit/deployment events, and later modifications. Include claimed versus delivered requirements, time until discovery, failed downstream actions, user reliance on the claim, and repair or rework time. Record accurately disclosed limitations separately from contradicted claims.

<a id="examples"></a>

## Examples

<a id="examples/missing-export"></a>

### Missing export

Synthetic incident: an agent reports that CSV export is implemented and ready. The delivered revision has a button and success message but no export path; exercising that workflow produces zero files. The user discovers the mismatch during a scheduled export and spends twenty minutes producing the CSV manually.

<a id="examples/empty-worktree"></a>

### Empty worktree

Reported incident: [Matthew Hawthorne’s February 2026 account](https://pushtoprod.substack.com/p/my-ai-agent-didnt-do-anything) describes a seven-turn resumed task declaring success on a branch with no changes. Code review exposed the empty branch; the earlier run’s uncommitted work had not reached the new worktree. The requested feature was absent despite the completion report, and investigation prompted changes to resume and persistence handling. Recovery time is not given.

<a id="examples/explicit-partial"></a>

### Explicit partial

Synthetic comparison: an agent delivers an export button and explicitly says CSV generation remains unfinished. The diff and a workflow check confirm that exact boundary. One requirement remains open, but the report does not falsely describe it as complete.
