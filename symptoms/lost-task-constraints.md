---
id: S006
kind: symptom
summary: "A previously established task requirement or decision ceases to govern the\
  \ agent\u2019s later continuation."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
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

Identify the original constraint and evidence that it was initially represented or followed. Compare it with a later task summary, plan, stated understanding, or action. A missing mention in an abbreviated summary alone is insufficient if the agent still acts consistently with the constraint.

A visible summary that changes the requirement provides stronger evidence of representational loss than action alone. If the instruction remains visible but the agent violates it, describe lost adherence without claiming literal memory erasure. Record compaction or handoff timing without assuming it caused the change.

Distinguish a lost requirement from a newly introduced one and from a forgotten fact that does not constrain the task. [Correction without behavioral change](correction-without-behavioral-change.md) additionally requires an acknowledged correction; it can overlap with this symptom.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/revised-request"></a>

### Revised request

The user explicitly changes or withdraws the earlier constraint.

<a id="benign-lookalikes/concise-summary"></a>

### Concise summary

A summary omits a detail for brevity, but the complete instruction remains available and subsequent actions honor it.

<a id="benign-lookalikes/resolved-conflict"></a>

### Resolved conflict

The agent identifies an instruction conflict or infeasible constraint and obtains an appropriate resolution before proceeding.

<a id="what-to-record"></a>

## What to record

Record the original requirement and its authority, earlier compliant behavior or representation, later summaries and actions, and the exact discrepancy. Preserve compaction/handoff boundaries, replacement context, active instructions, and any superseding user messages. Note whether the evidence shows missing representation, incompatible action, or both.

<a id="examples"></a>

## Examples

<a id="examples/review-gate"></a>

### Review gate

Synthetic example: the agent’s plan says to present a migration for review before running it. After a handoff, the replacement plan says to run the migration, and the agent does so without the requested review.

<a id="examples/compacted-intent"></a>

### Compacted intent

Reported example: [Claude Code issue #23776](https://github.com/anthropics/claude-code/issues/23776) describes a request to revise and present a plan for review being transformed during compaction into an instruction to implement changes. Technical details reportedly survived while the review requirement did not.

<a id="examples/waived-review"></a>

### Waived review

Synthetic comparison: the user reviews the plan and explicitly approves execution. A subsequent summary omits the completed review gate and the agent proceeds; the constraint has been satisfied rather than lost.
