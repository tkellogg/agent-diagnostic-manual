---
id: S009
kind: symptom
summary: An agent modifies artifacts or system state beyond the authorized task scope
  without an established dependency that requires the change.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
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

Compare the actual change with the task boundary and standing authorization. Scope can be defined by intended behavior rather than a literal file list; a necessary supporting change may be in an unmentioned file. Require an explanation grounded in dependencies, not just the agent’s preference for cleanup.

Inspect semantic changes and actual execution. A large diff can reflect line endings or formatting, and a proposed rewrite may never have been applied. Distinguish changed files from deleted work, and recoverable intermediate edits from lasting output.

Record unrelated concurrent or preexisting work separately from the agent’s own changes. Unrequested test infrastructure can overlap with [Excessive verification](excessive-verification.md); the same episode can have both scope and resource consequences.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/necessary-dependency"></a>

### Necessary dependency

The requested behavior requires a supporting schema, interface, or configuration change within the granted authority.

<a id="benign-lookalikes/authorized-refactor"></a>

### Authorized refactor

The user grants broad refactoring or cleanup scope that includes the affected components.

<a id="benign-lookalikes/display-noise"></a>

### Display noise

The apparent rewrite is a diff-display, formatting, or line-ending effect without the alleged semantic change.

<a id="what-to-record"></a>

## What to record

Record the request and standing scope, before-and-after artifacts, semantic diff, actual commands, dependencies, and stated rationale. Identify ownership and timing of unrelated edits, whether changes were proposed or applied, and any recovery. Preserve enough baseline state to distinguish the agent’s work from concurrent changes.

<a id="examples"></a>

## Examples

<a id="examples/unrelated-reset"></a>

### Unrelated reset

Synthetic example: while fixing a parser, the agent discovers uncommitted documentation edits made by the user and restores them to HEAD as cleanup. The edits have no bearing on the parser fix and were outside its authority.

<a id="examples/concurrent-edits"></a>

### Concurrent edits

Reported example: [Codex issue #6187](https://github.com/openai/codex/issues/6187) describes unrelated concurrent edits being reset during a check for unexpected changes despite an instruction to preserve them. The account does not provide an independently reproduced incident.

<a id="examples/required-interface"></a>

### Required interface

Synthetic comparison: implementing an authorized API field requires updating its serializer and schema as well as the initially mentioned handler. The supporting edits are necessary to the requested behavior.
