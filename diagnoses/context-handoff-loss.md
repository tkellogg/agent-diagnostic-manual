---
id: D001
kind: diagnosis
summary: A compaction or handoff drops still-needed task state from the receiving
  agent's input, causing it to repeat discovery, lose constraints, or ask again for
  existing authorization.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
unit: configured-agent-system
title: Context handoff loss
xml_source: diagnoses/context-handoff-loss.xml
---

# Context handoff loss

A compaction or handoff drops still-needed task state from the receiving agent's input, causing it to repeat discovery, lose constraints, or ask again for existing authorization.

<a id="relations"></a>

## Relationships

Related symptom: [S001](../symptoms/repeated-retrieval.md)

Related symptom: [S006](../symptoms/lost-task-constraints.md)

Related symptom: [S008](../symptoms/repeated-reauthorization.md)

<a id="relations/I001"></a>
<a id="relations/I001/when"></a>
[I001](../interventions/preserve-task-relevant-evidence.md)

**When:** Task state was available before a context transition and omitted from the continuation that needed it; the maintainer can change the transition policy.

<a id="relations/I001/predictions"></a>

#### Predictions

On future continuations that receive the preserved state, redundant retrieval, constraint violations, and repeated authorization requests attributable to that omission should decline. Legitimate source refreshes and requests for expanded authority should remain.

Failures before any transition should not improve through this mechanism. Persistence despite confirmed delivery weakens the omission explanation; acting beyond preserved permission suggests that the intervention lost its scope restrictions.

<a id="definition"></a>

## Definition

The context-management system should carry forward the information needed for unfinished work. Its selection or delivery policy instead omits still-applicable evidence, constraints, or authorization at compaction or delegation. A later decision must reconstruct that state or proceeds without it.

This is a proposed explanation of the configured system. [Repeated retrieval](../symptoms/repeated-retrieval.md) alone does not establish it, and a transcript retaining information does not establish that the receiving model had it.

<a id="criteria"></a>

## Candidate criteria

<a id="criteria/prior-state"></a>

### Previously available task state

Identify a specific fact, constraint, or authorization that was available before the transition and remained applicable to the later decision.

<a id="criteria/delivery-loss"></a>

### Loss at the transition

The transition output and effective receiving input show the needed state omitted or materially altered, with no equivalent representation available at that decision. Inaccessible model inputs leave this criterion unknown.

<a id="criteria/linked-disruption"></a>

### A disruption the missing state explains

The continuation unnecessarily retrieves the same evidence, violates the omitted constraint, or requests authorization already granted. Identify the connection to the particular missing state rather than relying on timing alone.

Related symptom: [S001](../symptoms/repeated-retrieval.md)

Related symptom: [S006](../symptoms/lost-task-constraints.md)

Related symptom: [S008](../symptoms/repeated-reauthorization.md)

<a id="exclusions"></a>

## Exclusions

<a id="exclusions/expired-state"></a>

### Expired state

Information legitimately expired or the user changed the requirement or authorization before continuation.

<a id="exclusions/equivalent-context"></a>

### Equivalent context

The receiving input contains an adequate equivalent of the necessary state. Poor use of visible information requires another explanation.

<a id="differential"></a>

## Differential diagnosis

<a id="differential/initial-delivery"></a>

### Information was never delivered

<a id="differential/initial-delivery/discriminator"></a>

#### Discriminator

Compare the original usable result with actual model input before the transition. Backend success or a saved file alone cannot establish prior delivery.

<a id="differential/policy-conflict"></a>

### A standing rule demands the behavior

<a id="differential/policy-conflict/discriminator"></a>

#### Discriminator

Check whether a fresh-consent or repeated-check rule still requires the action when the state is visible. For excessive checking, consider [verification policy overgeneralization](verification-policy-overgeneralization.md).

<a id="differential/visible-state"></a>

### The agent acts against visible state

<a id="differential/visible-state/discriminator"></a>

#### Discriminator

If the relevant state is present and clear at the decision, investigate competing instructions and action selection. Do not infer internal forgetting from incompatible behavior.

<a id="investigation"></a>

## Investigation

Inspect the affected transition and the next decision using existing input captures where available. Compare which state survived with what the pending work needed. Look for ordinary continuations under the same policy that preserved the state and proceeded correctly; no replay of the incident is required.

<a id="interventions"></a>

## Interventions

[Preserve task state across context transitions](../interventions/preserve-task-relevant-evidence.md) changes future handoffs and compactions. A one-time reminder may rescue an episode but does not repair the transition policy.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This is an unvalidated working model. The entry supplies neither an adjudicated public case establishing the mechanism nor evidence that the intervention is effective. Evidence for an omission, its contribution to behavior, and benefit from changing the policy are separate claims.
