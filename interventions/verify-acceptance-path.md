---
id: I003
kind: intervention
summary: "Audit where existing tests bypass connections that users rely on, then change\
  \ the project\u2019s test setup and QA instructions to cover those gaps on relevant\
  \ future work."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Repair gaps between tests and real use
xml_source: interventions/verify-acceptance-path.xml
---

# Repair gaps between tests and real use

Audit where existing tests bypass connections that users rely on, then change the project’s test setup and QA instructions to cover those gaps on relevant future work.

<a id="purpose"></a>

## Purpose

Make the software factory test the behavior it claims to have checked. The repository’s tests and the instructions for choosing them are part of that factory; adding an isolated test without changing future verification can leave the same mistake in place.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/known-boundary"></a>

### A gap in existing verification

[Unsupported verification claims](../symptoms/unsupported-verification-claims.md) or [component checks mistaken for complete verification](../diagnoses/verification-scope-collapse.md) point to a gap: individual parts pass, but their connection is untested. A confirmed diagnosis is not required to repair a demonstrated coverage gap.

<a id="preconditions/feasible-check"></a>

### Access to the test setup

You can change the project’s test setup and QA guidance, and exercise the relevant behavior within the user’s access, cost, and safety limits.

<a id="procedure"></a>

## Procedure

<a id="procedure/find-gaps"></a>

### Find what the tests skip

Take a recent claim that a feature works and inspect the tests behind it. Compare the user’s steps with the test’s steps. Look for mocked services, directly called handlers, skipped serialization, or deployment differences that hide a connection the user depends on.

<a id="procedure/choose-coverage"></a>

### Choose the useful checks

Review the consequential gaps with the user or maintainer. Select the smallest tests that exercise those connections; keep fast component tests for the problems they already catch.

<a id="procedure/exercise-boundary"></a>

### Exercise the missing connections

Repair the test setup and fixtures so those checks use the relevant interfaces. For a keyboard feature, send a keypress through the UI rather than calling the handler directly. Use a safe test environment for workflows with external effects.

<a id="procedure/update-workflow"></a>

### Change the recurring QA workflow

Update the QA skill, project instructions, and relevant CI job so agents routinely choose the repaired checks when that behavior changes. Remove any rule that treats a component pass as proof that the entire workflow works.

<a id="procedure/review-outcomes"></a>

### Review later work

At an agreed check-in, inspect a few ordinary changes involving those connections. Check whether the intended tests ran, what they found, and whether the final report describes the evidence accurately.

<a id="evaluation"></a>

## Evaluation

- Expect previously hidden integration bugs to become visible. Finding them can be progress even before the code has been repaired.
- Check that unsupported verification claims decline because relevant testing improved. A cautious final answer with the same missing coverage is only a reporting improvement.
- Component-only work should remain cheap. If every change now triggers a large end-to-end suite, narrow the selection rule.

<a id="risks-and-confounders"></a>

## Risks and confounders

- Broader tests can be slow, flaky, or affect external systems. Match them to the actual task and use an authorized test environment.
- A new test may share the implementation’s mistaken assumptions. Compare its steps with real use, not just the code it tests.

<a id="stop-and-rollback"></a>

## Stop and rollback

- Narrow or revert a check that introduces unauthorized effects, false failures, or disproportionate delay.
- Keep any removed coverage marked as untested until a suitable replacement exists.
