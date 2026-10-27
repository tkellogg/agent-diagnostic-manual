---
id: D003
kind: diagnosis
summary: A standing checking policy applies beyond the risks or decisions it was meant
  to address, producing redundant verification even when the agent follows its instructions.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
unit: configured-agent-system
title: Verification policy overgeneralization
xml_source: diagnoses/verification-policy-overgeneralization.xml
---

# Verification policy overgeneralization

A standing checking policy applies beyond the risks or decisions it was meant to address, producing redundant verification even when the agent follows its instructions.

<a id="relations"></a>

## Relationships

Related symptom: [S001](../symptoms/repeated-retrieval.md)

Related symptom: [S004](../symptoms/excessive-verification.md)

<a id="relations/I002"></a>
<a id="relations/I002/when"></a>
[I002](../interventions/scope-verification-policy.md)

**When:** A specific editable instruction or workflow triggers checks without a relevant changed state, unresolved question, or still-unmet acceptance need.

<a id="relations/I002/predictions"></a>

#### Predictions

After narrowing that rule, verification overrun should decline for the affected class of work while required checks and defect detection remain intact. The reduction should occur at the rule's trigger points, not uniformly across unrelated tasks.

Continued extra checks after the revised rule reaches the agent favor another cause. Fewer checks with more missed defects suggest the scope was narrowed too far; slower delivery from another bottleneck may remain.

<a id="definition"></a>

## Definition

A verification policy should connect each required check to a decision, risk, or acceptance condition and define when enough evidence has been gathered. A broad or self-retriggering rule instead demands another check irrespective of whether the relevant state changed or the question was already answered.

The agent may be complying perfectly with that rule. The proposed pathology is in the configured checking policy, not an inference about caution, anxiety, or intent.

<a id="criteria"></a>

## Candidate criteria

<a id="criteria/operative-rule"></a>

### An operative rule triggers the work

Identify the actual instruction or workflow rule and the decision points where it caused the extra checks. Similar wording in an unused file is insufficient.

<a id="criteria/scope-mismatch"></a>

### The trigger exceeds the checking need

Establish that the rule covers a class of work whose relevant verification need is already satisfied or absent. Name the missing justification; elapsed time or passing results alone do not establish waste.

<a id="criteria/checking-consequence"></a>

### The policy produces excess checking

Following the rule produces [excessive verification](../symptoms/excessive-verification.md), with delay or resource use traceable to the extra checks. Equivalent rereads may also match [repeated retrieval](../symptoms/repeated-retrieval.md).

Related symptom: [S004](../symptoms/excessive-verification.md)

<a id="exclusions"></a>

## Exclusions

<a id="exclusions/justified-check"></a>

### Justified check

The checks address an unmet acceptance condition, relevant risk, new change, or an agreed repeatability study.

<a id="exclusions/execution-cost"></a>

### Execution cost

The chosen check is appropriate but expensive because of its implementation or environment. Slow execution alone does not establish an overgeneral policy.

<a id="differential"></a>

## Differential diagnosis

<a id="differential/state-loss"></a>

### The system loses evidence that checking finished

<a id="differential/state-loss/discriminator"></a>

#### Discriminator

Inspect whether the prior result reaches the later turn. Repetition after a transition may instead reflect [context handoff loss](context-handoff-loss.md).

<a id="differential/new-evidence"></a>

### New evidence warrants another check

<a id="differential/new-evidence/discriminator"></a>

#### Discriminator

Compare code, environment, and failures at each trigger. The later check may answer a genuinely new question.

<a id="differential/rule-independent"></a>

### Extra checking is not prescribed by the rule

<a id="differential/rule-independent/discriminator"></a>

#### Discriminator

Compare the instruction with the chosen action. If the rule already limits scope and the agent exceeds it, this policy explanation is incomplete.

<a id="investigation"></a>

## Investigation

Map extra checks to the rule and the question each result could answer. Include a healthy task where the same rule is useful. Inspect ordinary future work after a scoped policy change; a costly replay study is not a prerequisite.

<a id="interventions"></a>

## Interventions

[Give verification a scope and stopping condition](../interventions/scope-verification-policy.md) changes the offending policy. The maintainer must have authority to change it; an executing agent should not silently bypass a mandatory gate.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This is an unvalidated working model. An inefficient-looking check does not by itself establish a bad rule, and the entry provides no measured effect of changing one. Agreement about justified verification may vary with task risk.
