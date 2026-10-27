---
id: S005
kind: symptom
summary: An agent acknowledges a specific correction and then repeats the corrected
  behavior under comparable conditions.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Correction without behavioral change
xml_source: symptoms/correction-without-behavioral-change.xml
---

# Correction without behavioral change

An agent acknowledges a specific correction and then repeats the corrected behavior under comparable conditions.

<a id="observations"></a>

## Observations

<a id="observations/repeated-violation"></a>

### Repeated violation

After receiving and acknowledging an applicable correction, the agent performs materially the same corrected action at least once more while that correction remains in force. The acknowledgment and later action are both observable in the episode or linked continuation.

<a id="how-to-recognize-it"></a>

## How to recognize it

In the transcript, pair the specific correction and acknowledgment with the next relevant tool call, edit, or answer. Use execution timestamps to distinguish a newly chosen action from one already in flight, and compare intervening instructions for a change in scope.

Inspect saved feedback files, memory loading records, and handoff summaries alongside the later input where available. These can show what was retained or omitted; compare actual later actions with the correction rather than treating an apology or memory write as proof of compliance.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/changed-context"></a>

### Changed context

The later action falls outside the correction’s stated scope. It therefore lacks the applicable correction required by [repeated violation](correction-without-behavioral-change.md#observations/repeated-violation).

<a id="benign-lookalikes/superseded-rule"></a>

### Superseded rule

A later applicable instruction changes the rule, or a higher-priority requirement displaces it. The original correction is no longer in force as required by [repeated violation](correction-without-behavioral-change.md#observations/repeated-violation).

<a id="benign-lookalikes/action-in-flight"></a>

### Action in flight

Execution logs show that the apparent recurrence was issued before the correction and acknowledgment. It is not a later action chosen after acknowledgment under [repeated violation](correction-without-behavioral-change.md#observations/repeated-violation).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model/harness versions, the correction’s exact text and scope, its delivery and acknowledgment times, and each subsequent opportunity to apply it. Preserve later actions, intervening instructions, memory artifacts, and effective input where available. Include recurrence counts relative to relevant opportunities, user correction turns, elapsed delay, damaged or redone work, and whether behavior eventually changed. Distinguish missing context evidence from a demonstrated loss of the correction.

<a id="examples"></a>

## Examples

<a id="examples/repeated-file"></a>

### Repeated file

Synthetic incident: after being told to edit a source template rather than generated output, the agent acknowledges the correction but makes the next fix in the generated file. Comparing the correction with the diff identifies the recurrence. The next build overwrites that fix, leaving one unresolved defect and ten minutes of rework.

<a id="examples/saved-feedback"></a>

### Saved feedback

Reported incident: [Claude Code issue #37847](https://github.com/anthropics/claude-code/issues/37847) lists eight shell-command recurrences after feedback was saved: four Python, two shell-loop, and two Node examples. The reporter compared saved memory and acknowledgments with later commands, describing repeated corrections and lost confidence in memory. Total time lost and the effective input to every invocation are not supplied.

<a id="examples/new-authorization"></a>

### New authorization

Synthetic comparison: after prohibiting edits to generated output, the user explicitly approves one emergency edit there. The transcript records that exception before the single edit, so the change does not violate a correction that remained in force for that action.
