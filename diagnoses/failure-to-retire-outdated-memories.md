---
id: D005
kind: diagnosis
summary: The memory path keeps supplying superseded facts alongside their replacements,
  and the working agent uses the old version in later work.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-31'
unit: configured-agent-system
title: Failure to retire outdated memories
xml_source: diagnoses/failure-to-retire-outdated-memories.xml
---

# Failure to retire outdated memories

The memory path keeps supplying superseded facts alongside their replacements, and the working agent uses the old version in later work.

<a id="definition"></a>

## How this could happen

A memory system should preserve useful history while making clear which facts or requirements apply now. This diagnosis proposes that obsolete memories keep competing with their updates: the system supplies both, and the working agent does not reliably choose the applicable version. Retiring a memory means retiring its authority as current guidance, not necessarily deleting its history.

For example, an old instruction to retry failed payments and a later restriction may both be retrieved. An agent that chooses the familiar retry rule can undo a deliberate protection. A record explaining what changed and why may help it use the history correctly; that is the proposed repair, not a requirement to erase the earlier decision.


      [When Retrieval Is Not Enough](https://arxiv.org/html/2610.36308v1) isolates an obsolete competitor by replacing an unrelated statement while retaining the update, prompt, and four-statement context size. Accuracy fell from 100% to 44.6% and 87.8% on two Qwen models. The study supports interference from competing versions in that setting. It does not isolate a neural mechanism: old facts often matched familiar world knowledge, unlike their synthetic replacements. Generalization beyond that benchmark and the provenance intervention below remain unvalidated.

<a id="relations"></a>

## Symptoms and predicted effects

- [S017 — Using outdated information](../symptoms/using-outdated-information.md)

<a id="relations/I007"></a>
<a id="relations/I007/when"></a>

### Intervention: [I007 — Document what changed and why](../interventions/document-what-changed-and-why.md)

**Use this when:** Old and current records compete, and the maintainer can change how the transition and its reason are recorded and delivered to future work.

<a id="relations/I007/predictions"></a>

#### What to expect if this explanation is right

- <a id="relations/I007/predictions/expected-improvement"></a>**Expected improvement:** Future agents should follow the current requirement and make fewer changes that restore the old behavior. When apparently odd code protects a requirement introduced by a past change, they should preserve that requirement while still being able to improve the implementation.

- <a id="relations/I007/predictions/still-necessary"></a>**Still necessary:** Agents should still answer historical questions correctly, apply older rules where they remain valid, and revise current decisions when new evidence warrants it.

- <a id="relations/I007/predictions/reason-to-reconsider"></a>**A reason to reconsider:** If a clear, sourced transition reaches the working agent but it still follows the old rule, documenting provenance may be insufficient. If mistakes persist when only the applicable rule is present, competing memories are a weaker explanation. If the transition never arrives, investigate delivery before judging its usefulness.

- <a id="relations/I007/predictions/possible-harm"></a>**Possible harm:** A compelling but incorrect history can entrench a bad requirement. Longer notes can bury the current rule or make the obsolete one more salient.

<a id="criteria"></a>

## What would support this explanation

<a id="criteria/established-update"></a>

### 1. The old information has been superseded {#the-old-information-has-been-superseded}

Identify the fact or requirement, its replacement, and evidence that the replacement applies to this task. Recency alone does not establish authority or matching scope.

<a id="criteria/both-delivered"></a>

### 2. Both versions reached the agent {#both-versions-reached-the-agent}

The actual input contains the obsolete version and its applicable replacement. A newer fact stored in an unread file does not satisfy this criterion.

<a id="criteria/competing-use"></a>

### 3. The old version contributes to the mistake {#the-old-version-contributes-to-the-mistake}

The answer or action follows the obsolete record, producing [using outdated information](../symptoms/using-outdated-information.md). Trace the mistaken choice to that record; merely finding contradictory text in context or observing an unrelated wrong answer is insufficient.

- [S017 — Using outdated information](../symptoms/using-outdated-information.md)

<a id="exclusions"></a>

## When this explanation may not fit

<a id="exclusions/different-scopes"></a>

### Both versions remain valid

Different environments, customers, or historical periods can require different rules. Correctly selecting an older rule for its scope is not a failure to retire it.

<a id="exclusions/disputed-update"></a>

### Replacement is not established

A later guess or an untrusted instruction does not automatically supersede an authoritative record. Keep uncertainty about the current rule explicit.

<a id="differential"></a>

## Other explanations to consider

<a id="differential/missing-update"></a>

### The update never arrived

<a id="differential/missing-update/discriminator"></a>
Inspect the working input. If it contains only the older record, repair collection or retrieval rather than attributing the error to competition between delivered versions.

<a id="differential/compaction-loss"></a>

### Compaction removed the update

<a id="differential/compaction-loss/discriminator"></a>
If the update was present earlier but disappeared from the resumed input, investigate [incorrect compaction](context-handoff-loss.md). Preserve the update and its scope through that boundary.

<a id="differential/other-instruction"></a>

### Another instruction requires the old behavior

<a id="differential/other-instruction/discriminator"></a>
If an active rule explicitly directs the disputed action despite the update, resolve that instruction conflict. Rewriting factual memory alone may leave the rule intact.

<a id="differential/other-error"></a>

### The mistake does not depend on the old record

<a id="differential/other-error/discriminator"></a>
If ordinary traces show the same error with only the current information present, investigate misunderstanding, strong prior beliefs, or another failure to follow the supplied evidence. Do not infer competing memories from the wrong answer alone.

<a id="investigation"></a>

## Where to look next

Start with one consequential use of an obsolete rule. Follow both versions into the actual input and identify how the answer or action used the older one. Check whether the replacement's reason and scope survived delivery. Use ordinary future work to evaluate a repair; a replay or ablation is optional when it would resolve a worthwhile remaining uncertainty.
