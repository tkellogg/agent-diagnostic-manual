---
id: I001
kind: intervention
summary: Change the compaction or handoff policy to carry still-needed evidence, constraints,
  and scoped authorization into future receiving inputs.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Preserve task state across context transitions
xml_source: interventions/preserve-task-relevant-evidence.xml
---

# Preserve task state across context transitions

Change the compaction or handoff policy to carry still-needed evidence, constraints, and scoped authorization into future receiving inputs.

<a id="purpose"></a>

## Purpose

Repair continuity across context transitions so future agents can use established task state. The intervention changes the transition mechanism or reusable handoff instructions, rather than adding a reminder to one completed incident.

Information stored in a transcript or memory file helps only when the receiving agent can use it. Preserve the smallest sufficient state with its source and scope; an excerpt of untrusted data must not become a new instruction.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/identified-omission"></a>

### Identified omission

Identify still-needed state that the current transition policy omits, and the class of later decisions it affects. Repetition alone does not establish an omission.

<a id="preconditions/editable-transition"></a>

### Editable transition

The maintainer can change the compaction, delegation, or context-loading policy and has authority to supply the relevant information to the receiving agent.

<a id="procedure"></a>

## Procedure

<a id="procedure/locate-boundary"></a>

### Locate boundary

Locate the shared policy that selects and delivers state at the affected transition. Record its current version and the decision-relevant omission.

<a id="procedure/create-record"></a>

### Create record

Modify that policy to retain pending decisions, still-applicable constraints, authorization with its limits, and the minimum evidence needed for the next work. Keep source identifiers and freshness conditions; omit completed or irrelevant history.

<a id="procedure/preserve-record"></a>

### Preserve record

Wire the selected state into the receiving input through the normal handoff or context-loading path. Preserve instruction precedence and source trust. Invalidate evidence when its source changes, and never broaden permissions while summarizing them.

<a id="procedure/confirm-delivery"></a>

### Confirm delivery

Inspect a representative subsequent transition to check that the selected state reaches the receiving input without immediate truncation. If effective input is inaccessible, record delivery as unconfirmed.

<a id="procedure/review-work"></a>

### Review work

Observe later tasks with the affected transition. Compare their relevant decisions with the predictions recorded before applying the policy change.

<a id="evaluation"></a>

## Evaluation

Choose a review point with actual opportunities for the omitted state to matter. Track avoidable rediscovery, constraint adherence, and appropriate authorization decisions alongside completion, correctness, and context cost. Compare similar transitions using existing logs; a replay study is optional.

Improvement after confirmed delivery supports the relevant diagnosis-dependent prediction. Persistence despite delivery weakens a simple omission account; missing delivery leaves the change untested. Fewer rereads accompanied by stale decisions or fewer permission questions accompanied by unauthorized actions are harmful outcomes.

<a id="risks-and-confounders"></a>

## Risks and confounders

Retained state can become stale, displace useful context, strip permission limits, or promote source text into authority. Changes in task mix, source freshness, and model behavior can also change the symptom rate.

<a id="stop-and-rollback"></a>

## Stop and rollback

Narrow or revert the retention policy if it introduces stale decisions, authorization errors, or excessive context cost. Restore the previous transition configuration and correct affected retained state; reverting cannot undo actions already taken.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This is a proposed system change with no efficacy result established here. Successful storage, successful delivery, and improved decisions are separate claims.
