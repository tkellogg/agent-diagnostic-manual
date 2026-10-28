---
id: D004
kind: diagnosis
summary: The workflow treats a passing component test as proof that the whole requested
  behavior works, even though the connections between components were never exercised.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
unit: configured-agent-system
title: Component checks mistaken for complete verification
xml_source: diagnoses/verification-scope-collapse.xml
---

# Component checks mistaken for complete verification

The workflow treats a passing component test as proof that the whole requested behavior works, even though the connections between components were never exercised.

<a id="definition"></a>

## How this could happen

A function can work while the application around it is broken. For example, directly calling a keyboard handler does not show that a real keypress reaches it. This diagnosis proposes that the testing or completion workflow treats those two checks as equivalent.

The failure is in how the system decides that verification is complete. A broad claim in the final answer may suggest this model, but it could also be a reporting mistake after an otherwise honest test process.

<a id="relations"></a>

## Symptoms and predicted effects

- [S011 — Unsupported verification claims](../symptoms/unsupported-verification-claims.md)

<a id="relations/I003"></a>
<a id="relations/I003/when"></a>

### Intervention: [I003 — Repair gaps between tests and real use](../interventions/verify-acceptance-path.md)

**Use this when:** The usual tests skip a connection required by the task, yet the workflow treats their success as verification of the whole behavior.

<a id="relations/I003/predictions"></a>

#### What to expect if this explanation is right

- <a id="relations/I003/predictions/expected-improvement"></a>**Expected improvement:** Tests should begin exercising the previously skipped connection. Existing bugs there may become visible, and claims that the whole feature was verified should have better support.

- <a id="relations/I003/predictions/still-necessary"></a>**Still necessary:** Small component changes should still use small tests when the broader workflow is outside the task’s scope.

- <a id="relations/I003/predictions/reason-to-reconsider"></a>**A reason to reconsider:** If the workflow records the missing coverage correctly but the final answer still claims everything passed, investigate reporting. More cautious wording alone does not fix a missing test.

- <a id="relations/I003/predictions/possible-harm"></a>**Possible harm:** Requiring a full workflow test for every small edit can slow routine work and introduce failures from unrelated services. Limit broader checks to the behavior and connections the task depends on.

<a id="criteria"></a>

## What would support this explanation

<a id="criteria/broader-requirement"></a>

### 1. The task needs more than the tested component {#the-task-needs-more-than-the-tested-component}

Name the requested behavior, such as a user pressing a key and seeing a result.

<a id="criteria/limited-probe"></a>

### 2. The check skips a needed connection {#the-check-skips-a-needed-connection}

The test calls or mocks an internal part instead of exercising that connection, and no other check covers it.

<a id="criteria/scope-promotion"></a>

### 3. The workflow treats the limited test as enough {#the-workflow-treats-the-limited-test-as-enough}

A test rule, result summary, or completion decision treats the component’s pass as proof of the whole behavior, producing [unsupported verification claims](../symptoms/unsupported-verification-claims.md). If only the final claim is visible, the cause remains uncertain.

- [S011 — Unsupported verification claims](../symptoms/unsupported-verification-claims.md)

<a id="exclusions"></a>

## When this explanation may not fit

<a id="exclusions/matching-evidence"></a>

### Another test covers the behavior

Another test may cover the missing connection. Check that before concluding it was never tested.

<a id="exclusions/scoped-task"></a>

### The user requested only a component change

The user may have asked only for a component change. A component test and a report limited to that change can be sufficient.

<a id="differential"></a>

## Other explanations to consider

<a id="differential/artifact-defect"></a>

### The full workflow was tested and failed

<a id="differential/artifact-defect/discriminator"></a>
A failed test has exposed a code defect. That does not establish this diagnosis unless the completion process ignores the failure and substitutes a narrower pass.

<a id="differential/stale-result"></a>

### The result belongs to an older build

<a id="differential/stale-result/discriminator"></a>
Compare the tested version with the delivered version. The test may cover the right behavior on the wrong code.

<a id="differential/reporting-error"></a>

### Only the final answer exaggerates the evidence

<a id="differential/reporting-error/discriminator"></a>
If the test process correctly records the broader behavior as untested, repair how the agent reports results rather than adding tests it already knows are missing.

<a id="investigation"></a>

## Where to look next

Choose one claimed success and trace it back to the test. Compare what the user does with what the test actually does, then find the instruction or decision that treated the smaller check as sufficient.
