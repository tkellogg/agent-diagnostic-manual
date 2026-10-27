---
id: I003
kind: intervention
summary: Change the reusable QA workflow so acceptance checks exercise the required
  input-to-result path on the relevant artifact, while component checks retain their
  actual scope.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Verify through the required acceptance path
xml_source: interventions/verify-acceptance-path.xml
---

# Verify through the required acceptance path

Change the reusable QA workflow so acceptance checks exercise the required input-to-result path on the relevant artifact, while component checks retain their actual scope.

<a id="purpose"></a>

## Purpose

Make future verification cover the boundary that matters to the task. A component probe can help locate a defect without proving that a user's input, deployment path, or physical process reaches that component correctly.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/known-boundary"></a>

### Known boundary

Identify a required acceptance boundary omitted by the current QA workflow and the relevant artifact or destination.

<a id="preconditions/feasible-check"></a>

### Feasible check

The maintainer can change the QA skill, template, or harness, and the needed check is feasible within the task's access, cost, and authorization limits. Otherwise preserve the unresolved requirement rather than claiming verification.

<a id="procedure"></a>

## Procedure

<a id="procedure/define-path"></a>

### Define path

Update the reusable QA instructions to connect the relevant acceptance condition to its input, artifact version, and observable result. Select the smallest check that covers that path.

<a id="procedure/exercise-boundary"></a>

### Exercise boundary

Change the default acceptance procedure to use the required interface. For a user-input requirement, drive that input rather than calling its internal handler; for a delivered artifact, inspect the relevant destination. Wait for asynchronous completion using its observable result and an appropriate timeout.

<a id="procedure/retain-scope"></a>

### Retain scope

Keep component probes available for diagnosis, but label their results with what they exercised. Do not let a component success close a broader acceptance condition without matching evidence. Use existing check output; a new receipt format is not required.

<a id="procedure/review-outcomes"></a>

### Review outcomes

Confirm subsequent QA work follows the revised path and review both acceptance outcomes and the accuracy of claims based on them.

<a id="evaluation"></a>

## Evaluation

Predict which previously bypassed failures may become visible and which component-only tasks should remain unchanged. On future applicable work, inspect whether the required path was attempted, whether it worked, and whether the final statement matches the result. Record blocked or unavailable checks as unresolved.

Fewer overclaims with the required path still untested is only a reporting improvement. Newly detected defects may mean the check became more informative, not that implementation quality deteriorated. Persistent real-path failures require their own repair.

<a id="risks-and-confounders"></a>

## Risks and confounders

Full paths can be slow, flaky, or have external effects. Restrict the procedure to the task's actual acceptance boundary and authorized environment; do not require live deployment or physical fabrication for every component change.

<a id="stop-and-rollback"></a>

## Stop and rollback

Narrow or revert a check that introduces unauthorized effects, false blocking, or disproportionate delay. Keep the broader condition open when coverage is removed; rollback does not turn missing evidence into a pass.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This is an unvalidated workflow change. Better verification may reveal defects without fixing them, and a more accurate report alone does not establish better task completion.
