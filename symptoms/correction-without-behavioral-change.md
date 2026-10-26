---
id: S005
kind: symptom
summary: An agent acknowledges a specific correction and then repeats the corrected
  behavior under comparable conditions.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Correction without behavioral change
xml_source: symptoms/correction-without-behavioral-change.xml
---

# Correction without behavioral change

An agent acknowledges a specific correction and then repeats the corrected behavior under comparable conditions.

<a id="observations"></a>

## Observations

<a id="observations/repeated-violation"></a>

### Repeated violation

After receiving and acknowledging an applicable correction, the agent performs materially the same corrected action again while the correction remains in force. The acknowledgment and later action are both observable in the episode or linked continuation.

<a id="how-to-recognize-it"></a>

## How to recognize it

Identify the exact correction, the agent’s acknowledgment, and the subsequent action. Compare the relevant conditions and any intervening instructions. An apology, promise, or saved memory demonstrates acknowledgment; it does not demonstrate that the later action complies.

A single clear recurrence after acknowledgment can establish this symptom; record additional recurrences rather than requiring an arbitrary count. If acknowledgment is absent, the episode may show an instruction violation but does not meet this narrower description.

Check whether the correction was available at the later decision. If a context transition removed it, [Lost task constraints](lost-task-constraints.md) may also apply. If availability cannot be established, leave that mechanism unresolved. Neither repetition nor an apology establishes deliberate disregard.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/changed-context"></a>

### Changed context

The later action occurs under materially different circumstances outside the correction’s scope.

<a id="benign-lookalikes/superseded-rule"></a>

### Superseded rule

A later applicable instruction changes the rule, or a higher-priority constraint requires another action.

<a id="benign-lookalikes/action-in-flight"></a>

### Action in flight

The apparently repeated action was already issued before the correction could be applied.

<a id="what-to-record"></a>

## What to record

Record the correction’s exact scope, delivery time, acknowledgment, later action, relevant context and authority, and any intervening changes. Preserve both the original instruction and the effective later input where available. Count distinct recurrences and record whether the correction affected any subsequent behavior.

<a id="examples"></a>

## Examples

<a id="examples/repeated-file"></a>

### Repeated file

Synthetic example: the user says not to edit a generated file, and the agent acknowledges that changes belong in its source template. On the next comparable fix it edits the generated file again without any changed instruction.

<a id="examples/saved-feedback"></a>

### Saved feedback

Reported example: [Claude Code issue #37847](https://github.com/anthropics/claude-code/issues/37847) describes specific feedback saved to memory followed by recurring actions contrary to that feedback. The report does not independently establish which memory content reached every later model invocation.

<a id="examples/new-authorization"></a>

### New authorization

Synthetic comparison: after saying never to edit generated output, the user explicitly requests a one-off emergency change to that output. Following the new instruction is not recurrence under the original unchanged constraint.
