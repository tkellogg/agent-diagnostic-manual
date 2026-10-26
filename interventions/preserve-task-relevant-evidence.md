---
id: I001
kind: intervention
summary: Keep a bounded, versioned evidence record available across context transitions
  and compare task outcomes.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Preserve task-relevant evidence
xml_source: interventions/preserve-task-relevant-evidence.xml
---

# Preserve task-relevant evidence

Keep a bounded, versioned evidence record available across context transitions and compare task outcomes.

<a id="purpose"></a>

## Purpose

Test whether loss of task-relevant evidence from the active context contributes to repeated retrieval, and evaluate whether preserving that evidence improves the task outcome.

This is a **proposed protocol**, not a demonstrated remedy. A diagnosis's applicability link determines when it is worth considering; mere repetition does not justify it.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/missing-evidence"></a>

### Missing evidence

A prior retrieval delivered usable evidence, but the evidence appears absent from a later model input where it is needed.

<a id="preconditions/replayable-task"></a>

### Replayable task

The task and relevant source versions can be captured or replayed well enough for a meaningful comparison.

<a id="preconditions/persistent-record"></a>

### Persistent record

The harness allows a bounded record to remain available across context transitions.

<a id="preconditions/freshness-enforced"></a>

### Freshness enforced

Freshness requirements can still be enforced. Sensitive evidence remains within the system's existing access boundaries.

<a id="procedure"></a>

## Procedure

<a id="procedure/save-baseline"></a>

### Save baseline

Save a baseline checkpoint, configuration, and source versions. Define completion and correctness checks before inspecting the experimental outcome.

<a id="procedure/create-record"></a>

### Create record

Create a small evidence record containing the needed fact or excerpt, source identity/version, and its relationship to the pending task. Prefer source-grounded content over a new interpretive summary.

<a id="procedure/preserve-record"></a>

### Preserve record

Keep that record available across the context transition. Record exactly what is inserted, where, and how much context it consumes. This protocol preserves evidence; it does not prohibit further reads.

<a id="procedure/compare-runs"></a>

### Compare runs

Run a baseline and a modified condition from comparable checkpoints, with other conditions as similar as practical. Record unavoidable differences.

<a id="procedure/repeat-trials"></a>

### Repeat trials

Repeat trials to characterize variation. Where feasible, add a comparison retaining a similarly sized irrelevant record to help distinguish evidence availability from generic prompt or context changes.

<a id="procedure/review-outcome"></a>

### Review outcome

Review outcome and tradeoffs before retaining the change. Invalidate or refresh the record when its source version or task relevance changes.

<a id="evaluation"></a>

## Evaluation

Compare task completion and correctness first. Also record repeated retrievals, information gained, elapsed time, token/tool cost, and legitimate checks skipped.

A favorable result improves progress or resource use without unacceptable loss of correctness or necessary verification. Define acceptable tradeoffs for the task before running the experiment; this manual does not supply universal thresholds.

A null result is inconclusive when the manipulation failed to keep evidence visible. If evidence remained visible and repetition persisted, that weakens the simple evidence-loss hypothesis for this case. A positive result supports this intervention under these conditions; it does not uniquely establish the cause.

<a id="risks-and-confounders"></a>

## Risks and confounders

Preserved evidence can become stale, displace other useful context, change attention, or introduce additional instructions through its wording. Model sampling variation and changed source content can also explain differences.

Record these limitations. Avoid turning a new summary into an unquestioned authority. Preserve provenance and version checks.

<a id="stop-and-rollback"></a>

## Stop and rollback

Stop if the record becomes stale, correctness declines, necessary verification is skipped, or the comparison cannot maintain meaningful conditions. Remove the preservation policy and restore the prior context configuration. Retain the experimental record and failure outcome for review.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

**Unvalidated.** No baseline/modified comparison has been performed for this repository. The procedure is intended to make a hypothesis testable and a possible remedy reviewable.

Do not promote this entry's evidence label because a synthetic example sounds plausible.
