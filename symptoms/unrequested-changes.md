---
id: S009
kind: symptom
summary: An agent modifies artifacts or system state beyond the authorized task scope
  without an established dependency that requires the change.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Unrequested changes
xml_source: symptoms/unrequested-changes.xml
---

# Unrequested changes

An agent modifies artifacts or system state beyond the authorized task scope without an established dependency that requires the change.

<a id="observations"></a>

## Observations

<a id="observations/scope-expansion"></a>

### Scope expansion

The agent makes a material change to an artifact or system state that is outside the requested or otherwise authorized scope and is not supported as necessary to complete the task. This includes reverting unrelated work, unsolicited rewrites, and additional infrastructure.

<a id="how-to-recognize-it"></a>

## How to recognize it

Compare the user’s request with the actual diff or audit log. Separate unrelated changes from edits needed to make the requested behavior work.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/necessary-dependency"></a>

### Necessary dependency

The requested behavior requires a supporting schema, interface, or configuration change within the granted authority. This is the necessary dependency excluded by [scope expansion](unrequested-changes.md#observations/scope-expansion).

<a id="benign-lookalikes/authorized-refactor"></a>

### Authorized refactor

The user grants refactoring or cleanup scope that includes the affected components. The change is not outside the authorized boundary in [scope expansion](unrequested-changes.md#observations/scope-expansion).

<a id="benign-lookalikes/display-noise"></a>

### Display noise

A viewer renders an apparent rewrite, but the underlying artifact and behavior are unchanged. There is no material change under [scope expansion](unrequested-changes.md#observations/scope-expansion); actual unsolicited formatting changes still require a scope assessment.

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, request and standing authority, baseline revision, and before-and-after artifacts. Preserve semantic diffs, commands and execution times, claimed dependencies, concurrent-edit ownership, and whether each change was proposed or applied. Include total and out-of-scope files or resources changed, lost work, rollback success, recovery time, downstream failures, and the final task outcome.

<a id="examples"></a>

## Examples

<a id="examples/unrelated-reset"></a>

### Unrelated reset

<span class="adm-example-kind">Synthetic example</span>

While fixing a parser, the agent restores an unrelated documentation file to HEAD, deleting eighty uncommitted lines written by the user. The pre-run snapshot and reset command identify the deleted work and its lack of connection to the parser. The user spends twenty-five minutes recovering and reapplying the edits.

<a id="examples/concurrent-edits"></a>

### Concurrent edits

<span class="adm-example-kind">Reported example</span>

[Codex issue #6187](https://github.com/openai/codex/issues/6187) describes unrelated concurrent edits disappearing during the agent’s unexpected-changes check despite instructions to preserve them. The reporter recognizes the resets by comparing work in other files before and after the task and says some incidents erased hours of uncommitted work. Exact recovery time and an independently reproduced trace are not provided.

<a id="examples/required-interface"></a>

### Required interface

<span class="adm-example-kind">Synthetic example</span>

An authorized API field requires edits to a handler, serializer, and schema. Comparing the three-file diff with the API contract explains all three changes, including two files not named in the request; no unrelated work is altered.
