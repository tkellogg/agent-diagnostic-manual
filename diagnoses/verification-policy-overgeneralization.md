---
id: D003
kind: diagnosis
summary: "Instructions make the agent check more than the user\u2019s task needs,\
  \ often because several files repeat or contradict one another."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
unit: configured-agent-system
title: Overbroad verification instructions
xml_source: diagnoses/verification-policy-overgeneralization.xml
---

# Overbroad verification instructions

Instructions make the agent check more than the user’s task needs, often because several files repeat or contradict one another.

<a id="definition"></a>

## How this could happen

Verification instructions should reflect what the user wants to learn or deliver, what could go wrong, and how much checking is worthwhile. Rules such as “test after every change” can spread across skills and project files until even a quick prototype triggers a production-scale test process.

The agent may be following those instructions correctly. This diagnosis concerns instructions that are too broad, duplicated, or contradictory; it does not explain every case of excessive checking.

<a id="relations"></a>

## Symptoms and predicted effects

- [S001 — Repeated retrieval](../symptoms/repeated-retrieval.md)
- [S004 — Excessive verification](../symptoms/excessive-verification.md)

<a id="relations/I002"></a>
<a id="relations/I002/when"></a>

### Intervention: [I002 — Consolidate verification instructions with the user](../interventions/scope-verification-policy.md)

**Use this when:** The agent’s active instructions demand checks that do not fit the task, or several instructions keep restarting the same checks.

<a id="relations/I002/predictions"></a>

#### What to expect if this explanation is right

- <a id="relations/I002/predictions/expected-improvement"></a>**Expected improvement:** After consolidating the instructions, similar tasks should spend less time on unwanted checks and reach the user sooner.

- <a id="relations/I002/predictions/still-necessary"></a>**Still necessary:** Checks that the user needs for a release or a credible risk should still happen. The agent should respect when the user plans to do the remaining review.

- <a id="relations/I002/predictions/reason-to-reconsider"></a>**A reason to reconsider:** If excess checking continues under the simplified instructions, examine whether the agent understands the task and application.

- <a id="relations/I002/predictions/possible-harm"></a>**Possible harm:** Removing too much verification can let defects reach the user. If defects increase, restore the missing coverage without reinstating unrelated checks.

<a id="criteria"></a>

## What would support this explanation

<a id="criteria/operative-rule"></a>

### 1. The agent is using the instruction {#the-agent-is-using-the-instruction}

Find the actual instruction that leads to the extra checks, in the loaded skill, project guidance, or workflow. An unused file is not enough.

<a id="criteria/scope-mismatch"></a>

### 2. The instruction asks for too much {#the-instruction-asks-for-too-much}

Compare the rule with the user’s goal, intended review, and the application’s real failure risks. Explain which demanded checks do not help that work.

<a id="criteria/checking-consequence"></a>

### 3. Following it creates extra work {#following-it-creates-extra-work}

The instruction produces [excessive verification](../symptoms/excessive-verification.md). Repeated reads may also match [repeated retrieval](../symptoms/repeated-retrieval.md).

- [S004 — Excessive verification](../symptoms/excessive-verification.md)

<a id="exclusions"></a>

## When this explanation may not fit

<a id="exclusions/justified-check"></a>

### The task needs these checks

The user wants production readiness, or the proposed change presents a real risk that the check addresses. Extensive checking can be the right amount of work.

<a id="exclusions/execution-cost"></a>

### A useful check is slow

A useful check can be slow because its implementation is inefficient. That calls for improving the check, not necessarily removing its instruction.

<a id="differential"></a>

## Other explanations to consider

<a id="differential/state-loss"></a>

### The agent has forgotten a previous result

<a id="differential/state-loss/discriminator"></a>
If a passed result disappeared during compaction, consider [compaction loss](context-handoff-loss.md). The checking rule may already be reasonable.

<a id="differential/task-misunderstanding"></a>

### The agent misunderstands the goal

<a id="differential/task-misunderstanding/discriminator"></a>
If the instructions allow a quick prototype but the agent behaves as if it must certify a release, clarify the goal and the user’s review plans.

<a id="differential/app-misunderstanding"></a>

### The agent misunderstands what can fail

<a id="differential/app-misunderstanding/discriminator"></a>
Check the failure the agent says it is testing for. If the application cannot reach that state, improve its understanding of the application rather than adding more testing rules.

<a id="investigation"></a>

## Where to look next

Read the instructions actually loaded for one affected task. Mark duplicate demands, contradictions, and checks that do not help the user’s goal; review those findings with the person responsible for the workflow.
