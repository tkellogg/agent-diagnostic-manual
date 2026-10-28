---
id: D001
kind: diagnosis
summary: The compaction prompt or algorithm drops information that later work still
  needs, so the agent repeats work, misses a requirement, or asks for permission again.
version: '1'
status: reviewed
evidence: unvalidated
updated: '2026-10-28'
unit: configured-agent-system
title: Incorrect compaction
xml_source: diagnoses/context-handoff-loss.xml
---

# Incorrect compaction

The compaction prompt or algorithm drops information that later work still needs, so the agent repeats work, misses a requirement, or asks for permission again.

<a id="definition"></a>

## How this could happen

Compaction makes room by forgetting most of a conversation. It has to predict what will matter next: keep the decisions, constraints, permissions, and findings needed for unfinished work, and discard irrelevant history. This diagnosis proposes that the compactor is making that choice badly.

For example, it may preserve a long account of completed edits but drop the user’s instruction to leave a particular file alone. The agent then resumes without that restriction. The same visible mistake has a different explanation if the restriction survived in the context.

<a id="relations"></a>

## Symptoms and predicted effects

- [S001 — Repeated retrieval](../symptoms/repeated-retrieval.md)
- [S006 — Lost task constraints](../symptoms/lost-task-constraints.md)
- [S008 — Repeated reauthorization](../symptoms/repeated-reauthorization.md)

<a id="relations/I001"></a>
<a id="relations/I001/when"></a>

### Intervention: [I001 — Fix compaction](../interventions/preserve-task-relevant-evidence.md)

**Use this when:** A compaction summary has lost important information, and you can change the compaction prompt or algorithm.

<a id="relations/I001/predictions"></a>

#### What to expect if this explanation is right

- <a id="relations/I001/predictions/expected-improvement"></a>**Expected improvement:** After compaction, the agent should reread fewer unchanged sources, follow the saved requirements, and stop asking again for permission already given.

- <a id="relations/I001/predictions/still-necessary"></a>**Still necessary:** It should check sources that may have changed and ask permission for work outside the original scope. The summary should still discard irrelevant history.

- <a id="relations/I001/predictions/reason-to-reconsider"></a>**A reason to reconsider:** If the important information survives but the same mistakes continue, investigate how the agent uses it. Problems that start before compaction need another explanation.

- <a id="relations/I001/predictions/possible-harm"></a>**Possible harm:** Keeping too much can crowd out useful context. Keeping a permission but losing its limits can lead to unauthorized work.

<a id="relations/I006"></a>
<a id="relations/I006/when"></a>

### Intervention: [I006 — Save information for future work](../interventions/save-information-for-future-work.md)

**Use this when:** Important information is available before compaction, and you can change the working agent's instructions for saving it outside the conversation and finding it later.

<a id="relations/I006/predictions"></a>

#### What to expect if this explanation is right

- <a id="relations/I006/predictions/expected-improvement"></a>**Expected improvement:** After compaction, the agent should recover the saved decisions, requirements, and permission limits from their records. It should repeat less investigation, miss fewer constraints, and ask less often for permission already given, even if the compactor still drops those details.

- <a id="relations/I006/predictions/still-necessary"></a>**Still necessary:** The agent should still recheck facts that may have changed and seek permission for new scope. Reading a relevant saved note is useful retrieval, not a recurrence of the redundant work this change aims to reduce.

- <a id="relations/I006/predictions/reason-to-reconsider"></a>**A reason to reconsider:** If the right information is saved and present in the resumed agent's context but the mistakes continue, investigate conflicting instructions or failures to follow it. If the record is never read, repair that route before judging the explanation. Improvement alone does not establish incorrect compaction: saved records can also help with omissions unrelated to compaction.

- <a id="relations/I006/predictions/possible-harm"></a>**Possible harm:** Stale or overly broad records can spread a mistake across future sessions. Excessive note-taking and rereading can replace the original repeated work with a new source of overhead.

<a id="criteria"></a>

## What would support this explanation

<a id="criteria/prior-state"></a>

### 1. The information mattered {#the-information-mattered}

Identify a fact, requirement, or permission that was in the conversation before compaction and was needed afterward.

<a id="criteria/delivery-loss"></a>

### 2. Compaction dropped it {#compaction-dropped-it}

The summary or the model’s context after compaction omits or changes that information. If you cannot inspect either, keep information loss as a hypothesis.

<a id="criteria/linked-disruption"></a>

### 3. The omission explains the mistake {#the-omission-explains-the-mistake}

The next work shows [repeated retrieval](../symptoms/repeated-retrieval.md), breaks the missing requirement, or asks for the lost permission. Show which missing fact would have helped; timing alone is not enough.

- [S001 — Repeated retrieval](../symptoms/repeated-retrieval.md)
- [S006 — Lost task constraints](../symptoms/lost-task-constraints.md)
- [S008 — Repeated reauthorization](../symptoms/repeated-reauthorization.md)

<a id="exclusions"></a>

## When this explanation may not fit

<a id="exclusions/expired-state"></a>

### Information no longer needed

Forgetting is useful when a fact is obsolete, a task is finished, or permission has expired. Keeping everything would defeat compaction.

<a id="exclusions/equivalent-context"></a>

### The meaning survived

A shorter wording may preserve the same meaning. If the relevant information is still clear, there may be a problem with following it, but it was not lost during compaction.

<a id="differential"></a>

## Other explanations to consider

<a id="differential/initial-delivery"></a>

### The agent never had the information

<a id="differential/initial-delivery/discriminator"></a>
Check the conversation before compaction. A fact in an unread file was never available to summarize; improve how the agent finds or records it.

<a id="differential/policy-conflict"></a>

### Another instruction demands the repeated work

<a id="differential/policy-conflict/discriminator"></a>
If the summary retains a passed test but a standing rule requires another run anyway, changing compaction will not remove that rule. Consider [overbroad verification instructions](verification-policy-overgeneralization.md).

<a id="differential/visible-state"></a>

### The agent has the information but does not use it

<a id="differential/visible-state/discriminator"></a>
If the needed fact is clear in the current context, look for conflicting instructions or a failure to follow it. Rewriting the summary may not help.

<a id="investigation"></a>

## Where to look next

Compare the conversation just before compaction with its summary and the next mistake. Look for something the compactor discarded that the unfinished task was likely to need, and for less useful material it kept instead.
