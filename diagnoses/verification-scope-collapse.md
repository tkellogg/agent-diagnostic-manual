---
id: D004
kind: diagnosis
summary: The verification workflow promotes a limited check into evidence for a broader
  acceptance condition, so untested boundaries disappear from completion decisions.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
unit: configured-agent-system
title: Verification scope collapse
xml_source: diagnoses/verification-scope-collapse.xml
---

# Verification scope collapse

The verification workflow promotes a limited check into evidence for a broader acceptance condition, so untested boundaries disappear from completion decisions.

<a id="relations"></a>

## Relationships

Related symptom: [S011](../symptoms/unsupported-verification-claims.md)

<a id="relations/I003"></a>
<a id="relations/I003/when"></a>
[I003](../interventions/verify-acceptance-path.md)

**When:** The QA skill, tool result, or completion policy treats a component or simulated check as sufficient for a broader required behavior.

<a id="relations/I003/predictions"></a>

#### Predictions

Future tasks requiring the broader behavior should exercise its actual acceptance path and produce fewer unsupported verification claims. Failures at previously bypassed boundaries may become visible even before underlying implementation quality improves.

Component-only tasks should retain their lightweight checks. If claims become narrower but required paths remain untested, the intervention changed reporting without completing the repair. Persistent overclaims despite clear path evidence favor a separate interpretation or reporting failure.

<a id="definition"></a>

## Definition

Verification evidence has a scope: a component, input path, artifact revision, environment, or physical stage. The system should preserve that scope when deciding whether acceptance has been demonstrated. Instead, its workflow equates a narrower success with the broader requirement and closes the requirement without evidence for the missing boundary.

A hypothetical example is treating a successful internal handler call as proof that the user-facing input reaches that handler. The handler may work perfectly while the input path remains unknown.

<a id="criteria"></a>

## Candidate criteria

<a id="criteria/broader-requirement"></a>

### A broader acceptance condition applies

Identify the requested behavior and the boundaries its verification must cover.

<a id="criteria/limited-probe"></a>

### The cited evidence covers less

The actual check bypasses or omits a required boundary, and no independent matching evidence closes that gap.

<a id="criteria/scope-promotion"></a>

### The workflow promotes the limited result

A policy, tool-result transformation, or recorded acceptance decision equates that limited result with satisfaction of the broader condition, producing [unsupported verification claims](../symptoms/unsupported-verification-claims.md). An overclaim with no evidence of this promotion leaves the mechanism unknown.

Related symptom: [S011](../symptoms/unsupported-verification-claims.md)

<a id="exclusions"></a>

## Exclusions

<a id="exclusions/matching-evidence"></a>

### Matching evidence

A separate check covers the required path, revision, and environment, including external evidence the local transcript does not contain.

<a id="exclusions/scoped-task"></a>

### Scoped task

The requested work and the report are explicitly limited to the tested component.

<a id="differential"></a>

## Differential diagnosis

<a id="differential/artifact-defect"></a>

### The required path was tested and failed

<a id="differential/artifact-defect/discriminator"></a>

#### Discriminator

Inspect actual inputs and outputs. A real-path defect requires an implementation repair; it does not establish scope collapse unless the workflow substitutes other evidence for the failure.

<a id="differential/stale-result"></a>

### Evidence applies to another artifact

<a id="differential/stale-result/discriminator"></a>

#### Discriminator

Match revision and destination. Correct testing of an earlier build can produce false assurance without a component-to-whole substitution.

<a id="differential/reporting-error"></a>

### The acceptance boundary is retained but misreported

<a id="differential/reporting-error/discriminator"></a>

#### Discriminator

If the workflow leaves the broader condition open and the final report alone claims it passed, investigate reporting. A shared symptom does not establish the same mechanism.

<a id="investigation"></a>

## Investigation

Trace one acceptance condition from its task requirement through the executed check, returned result, and completion decision. Identify exactly where scope was broadened. Look for successful work where the real path was exercised without unnecessary additional testing.

<a id="interventions"></a>

## Interventions

[Verify through the required acceptance path](../interventions/verify-acceptance-path.md) changes the QA workflow to exercise the missing boundary. Merely softening the final report does not complete an unmet acceptance condition.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This is an unvalidated scaffold with a hypothetical illustration. A gap in shown verification supports a symptom more readily than this causal account; unavailable external evidence remains an uncertainty. No efficacy or prevalence claim is made.
