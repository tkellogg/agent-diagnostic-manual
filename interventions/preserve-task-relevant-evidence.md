---
id: I001
kind: intervention
summary: Reinsert a previously delivered, still-current source excerpt into the next
  model input when a context transition has removed information needed for the pending
  action.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Restore missing evidence to active context
xml_source: interventions/preserve-task-relevant-evidence.xml
---

# Restore missing evidence to active context

Reinsert a previously delivered, still-current source excerpt into the next model input when a context transition has removed information needed for the pending action.

<a id="purpose"></a>

## Purpose

Restore the missing information so the agent can resume the pending task action. Apply this at an affected decision point after compaction, truncation, or a handoff. The same action can test whether evidence loss contributes to [repeated retrieval](../symptoms/repeated-retrieval.md); a diagnosis is not required to try it when the preconditions below hold.

**Principle:** information retained in a transcript or memory file is only useful at a decision point if it reaches the model's input. Restore the smallest sufficient source excerpt with its provenance, rather than relying on a new interpretation of what the agent should remember.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/missing-evidence"></a>

### Missing evidence

A prior retrieval delivered usable evidence, but it appears absent from the active context after a transition. Identify the recoverable source excerpt and the pending task action that needs it. Repetition alone does not establish that evidence is missing.

<a id="preconditions/persistent-record"></a>

### Persistent record

The operator or harness can include a bounded evidence block in the next model input after the transition, without it immediately being removed by the same context policy.

<a id="preconditions/freshness-enforced"></a>

### Freshness enforced

The excerpt's source version remains applicable to the task, and using it respects the task's freshness requirements. If a fresh read is required, perform that read instead. The excerpt can be supplied within the system's existing access boundaries.

<a id="procedure"></a>

## Procedure

<a id="procedure/save-baseline"></a>

### Save baseline

Capture the pending action, the transition that lost the evidence, the input before restoration where accessible, and the relevant source version. Record what successful progress and correctness would look like at the next decision point.

<a id="procedure/create-record"></a>

### Create record

Copy the smallest sufficient fact or excerpt from the earlier tool result into a labeled evidence block. Include the source path or identifier, version or retrieval time, and the pending action it informs. Keep the source text distinct from the operator's explanation of its relevance.

<a id="procedure/preserve-record"></a>

### Preserve record

Insert that block into the next model input after the transition, using the harness's task-context or tool-result mechanism. Treat the excerpt as source data under its original trust level. Keep task instructions and tool permissions unchanged, including permission to retrieve information when needed. Record the block's location and size.

<a id="procedure/verify-input"></a>

### Verify input

Inspect the assembled model input or delivery trace to confirm the block actually survived truncation and was supplied. Writing it to a memory file alone does not establish delivery. If the effective input is inaccessible, record delivery as unverified and limit conclusions accordingly.

<a id="procedure/resume-task"></a>

### Resume task

Resume the pending task without adding a separate instruction to stop rereading. At the next decision point, record whether the agent uses the restored evidence, retrieves it again, or takes another action, and whether that action advances the task correctly.

<a id="procedure/review-outcome"></a>

### Review outcome

Check the resulting task state against the recorded success conditions. Remove the block when the pending need ends or its source changes. If another context transition loses still-needed evidence, recheck the preconditions before reinserting it; do not accumulate duplicate blocks.

<a id="evaluation"></a>

## Evaluation

**For this episode:** assess the next decision and the eventual task outcome. The prediction is that the agent can use the restored excerpt to advance the pending action with fewer redundant retrievals. Record correctness, completion, repeated reads of that source, elapsed time, added context tokens, tool cost, and any necessary checks skipped. Fewer reads without correct progress is not a successful remedy.

**For a controlled evaluation:** save a checkpoint immediately before the affected decision and compare continuation with and without the evidence block. Keep the task, source versions, model, instructions, and tool configuration the same where practical; record differences. Repeat matched trials when assessing a general preservation policy. A similarly sized irrelevant block can provide an additional control for generic context changes, but is not required to restore evidence in one episode.

**Interpretation:** failure to deliver the block leaves the intervention untested. If the excerpt is confirmed present but the same retrieval loop persists, that weakens the hypothesis that absence of this evidence is sufficient to explain the loop. Correct progress after restoration is useful case evidence, but a single continuation cannot separate the effect from sampling variation, and even a controlled improvement does not uniquely establish the cause.

<a id="risks-and-confounders"></a>

## Risks and confounders

The excerpt can become stale or displace other needed context. Reinsertion changes placement and attention as well as availability, so a benefit may depend on presentation. Added instructions, a newly written summary, changed source content, and model sampling variation can also explain differences.

Source text may contain instructions that should remain untrusted data. Preserve its provenance and trust boundary; do not promote it into system instructions or treat the agent's claim to remember it as evidence that it was delivered.

<a id="stop-and-rollback"></a>

## Stop and rollback

Stop reinserting the block if its source becomes stale, it displaces necessary context, correctness declines, or required checks are skipped. Remove the block from subsequent inputs and disable any reinsertion hook added for this intervention. Retain the before/after inputs and outcome for review. Removing the block does not undo completed tool actions; inspect any resulting changes before continuing the task.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

**Unvalidated.** No inspected outcome or controlled comparison supports this procedure in the repository. It is a proposed action with a testable prediction; its effectiveness across tasks, models, and context policies remains unknown.
