---
id: S006
kind: symptom
summary: "A previously established task requirement or decision ceases to govern the\
  \ agent\u2019s later continuation."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Lost task constraints
xml_source: symptoms/lost-task-constraints.xml
---

# Lost task constraints

A previously established task requirement or decision ceases to govern the agent’s later continuation.

<a id="observations"></a>

## Observations

<a id="observations/constraint-loss"></a>

### Constraint loss

An explicit, still-applicable task constraint is represented or followed earlier, but a later continuation omits, contradicts, or replaces it and proceeds incompatibly with the original requirement.

<a id="how-to-recognize-it"></a>

## How to recognize it

Find the original requirement and the earlier plan, answer, or action that represented or followed it. Compare those records with later tool calls and artifact diffs to locate the first incompatible continuation.

Inspect compaction summaries, handoff messages, memory files, and replacement prompts around that point. Compare them with later user approvals or revisions, and inspect actual execution when a shortened summary leaves a requirement unstated.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/revised-request"></a>

### Revised request

The user changes or withdraws the earlier constraint before the later action. It is no longer the still-applicable requirement in [constraint loss](lost-task-constraints.md#observations/constraint-loss).

<a id="benign-lookalikes/concise-summary"></a>

### Concise summary

A shortened summary omits a detail, but later actions still honor it. The incompatible continuation required by [constraint loss](lost-task-constraints.md#observations/constraint-loss) is absent.

<a id="benign-lookalikes/resolved-conflict"></a>

### Resolved conflict

The agent obtains an authorized resolution to conflicting or infeasible instructions before acting. The later work follows the resolved requirement rather than contradicting a still-applicable one under [constraint loss](lost-task-constraints.md#observations/constraint-loss).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, original requirement and authority, and earlier evidence that it was represented or followed. Preserve later summaries, effective inputs, actions, and the first incompatible result, with compaction or handoff times and superseding instructions. Include the number of established constraints and affected constraints, unauthorized actions, user interruptions, rollback or rework time, and final outcome. Distinguish a missing representation from incompatible behavior when grouping incidents.

<a id="examples"></a>

## Examples

<a id="examples/review-gate"></a>

### Review gate

Synthetic incident: an initial migration plan requires review before execution; a handoff summary instead directs execution. Audit logs show three tables changed before any approval. Comparing the two plans and execution timestamps exposes the lost gate; the user interrupts and spends twelve minutes rolling back the migration.

<a id="examples/compacted-intent"></a>

### Compacted intent

Reported incident: [Claude Code issue #23776](https://github.com/anthropics/claude-code/issues/23776) compares a request to revise and present a plan with a compaction summary directing implementation. The agent reportedly made multiple file edits, added a test file, and ran builds before review. The user had to interrupt and restate the request; rollback was a possible consequence, not a confirmed outcome. No rework duration is reported.

<a id="examples/waived-review"></a>

### Waived review

Synthetic comparison: the user reviews a migration and approves execution before the agent runs it. The approval timestamp explains why the next summary omits the completed gate; one authorized migration proceeds without loss of the still-applicable requirements.
