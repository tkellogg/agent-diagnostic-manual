---
id: S017
kind: symptom
summary: An agent answers or acts using information that no longer applies to the
  time or state the task concerns.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-31'
title: Using outdated information
xml_source: symptoms/using-outdated-information.xml
---

# Using outdated information

An agent answers or acts using information that no longer applies to the time or state the task concerns.

<a id="observations"></a>

## Observations

<a id="observations/outdated-basis"></a>

### Outdated basis

An answer or action relies on an earlier fact, instruction, or result as still applicable, despite an established change that makes it inapplicable to the task. Identify the old information, the relevant change, and the answer or action it affected; the update need not have reached the agent for the symptom to occur.

<a id="how-to-recognize-it"></a>

## How to recognize it

Compare the version or event time of the evidence with the state the task concerns. A recent retrieval or log-ingestion timestamp can conceal an older observation.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/historical-task"></a>

### Historical task

The task asks what was true before a change, and the agent uses evidence from that period. Old information is appropriate for that question.

<a id="benign-lookalikes/still-valid"></a>

### Still valid

The information is old but still applies. A newer document or commit does not invalidate every earlier fact, and a change in one environment need not apply to another.

<a id="benign-lookalikes/disclosed-limit"></a>

### Disclosed limit

The agent accurately limits its answer to the older state and leaves the current state unresolved. Mentioning an access problem does not suffice if the answer still presents an old finding as current.

<a id="benign-lookalikes/real-recurrence"></a>

### Real recurrence

Evidence from after a repair shows the problem recurring, or shows that the repair never reached the affected environment. A closed ticket alone does not make that evidence obsolete.

<a id="what-to-record"></a>

## What to record

Record the task's intended time and scope, exact claim or action, old source and version, and evidence establishing the change and where it applies. Preserve the model-visible input, retrieval results, dates, and any summary that might have changed their meaning. Distinguish an unavailable update from one delivered but not used. Record repeated work, incorrect changes, missed problems, and time lost; across comparable tasks count uses of outdated information alongside correct historical uses and current answers.

<a id="examples"></a>

## Examples

<a id="examples/old-review"></a>

### Old review

<span class="adm-example-kind">Reported example</span>


        [Codex issue #49083](https://github.com/openai/codex/issues/49083) reports a PR re-review using an old local checkout after remote reads failed. Two findings were already fixed in the newer head. The report supplies both revisions and command results; the user had to intervene to obtain the current version. The agent disclosed access trouble but still presented the obsolete defects as current findings.

<a id="examples/obsolete-answer"></a>

### Obsolete answer

<span class="adm-example-kind">Reported example</span>


        [When Retrieval Is Not Enough](https://arxiv.org/html/2610.36308v1) reports benchmark answers choosing an obsolete fact even with its replacement present. Adding the obsolete competitor produced 41 correct-to-stale flips for Qwen2.5 and nine for Qwen3. These are synthetic benchmark tasks, not measured production losses.

<a id="examples/restored-retry"></a>

### Restored retry

<span class="adm-example-kind">Synthetic example</span>

A coding agent restores automatic payment retries from an old design note. A later provider change made some failed responses ambiguous: the charge might already have succeeded. Comparing the proposed edit with the current requirement exposes the obsolete assumption; review blocks the change and the agent must redo it.

<a id="examples/past-policy"></a>

### Past policy

<span class="adm-example-kind">Synthetic example</span>

A support agent explains which refund policy applied to a purchase made last year, using the policy in force then. It separately identifies the current policy. The older rule answers the historical question without being presented as current guidance.
