---
id: S008
kind: symptom
summary: An agent requests permission again for an action that remains covered by
  a clear, applicable authorization.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Repeated reauthorization
xml_source: symptoms/repeated-reauthorization.xml
---

# Repeated reauthorization

An agent requests permission again for an action that remains covered by a clear, applicable authorization.

<a id="observations"></a>

## Observations

<a id="observations/redundant-permission"></a>

### Redundant permission

After explicit, applicable authorization of an action, the agent asks the user to authorize materially the same action at least once more. No changed target, scope, consequence, unmet consent condition, or governing requirement makes renewed approval necessary.

<a id="how-to-recognize-it"></a>

## How to recognize it

Match each new permission question to the earlier approval and the action proposed. Check whether scope, credentials, or platform permissions actually changed.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/changed-action"></a>

### Changed action

The operation now affects a different account, recipient, resource, or materially broader scope. It is not the same authorized action required by [redundant permission](repeated-reauthorization.md#observations/redundant-permission).

<a id="benign-lookalikes/required-prompt"></a>

### Required prompt

A governing instruction or tool gate requires fresh approval at this stage or after expiry. This is the renewed-approval requirement excluded by [redundant permission](repeated-reauthorization.md#observations/redundant-permission).

<a id="benign-lookalikes/conditional-consent"></a>

### Conditional consent

Earlier consent depended on an unmet or unverified condition. That consent is not yet applicable to the action, unlike the authorization in [redundant permission](repeated-reauthorization.md#observations/redundant-permission).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model/client and harness versions, original approval text, scope, conditions, and each later permission request. Preserve proposed actions, prompt origin, applicable gate policies, changed circumstances, and expiry or context boundaries. Include authorized actions attempted, redundant requests, user reply counts, approval-to-execution delay, unattended waiting time, and whether the task eventually ran or was abandoned.

<a id="examples"></a>

## Examples

<a id="examples/same-click"></a>

### Same click

<span class="adm-example-kind">Synthetic example</span>

The user approves clicking Continue on a named screen, but the agent asks twice more before clicking. The transcript, unchanged screen, and permission log show no new gate. Two extra replies are required and the click is delayed twelve minutes while the user is away.

<a id="examples/desktop-approval"></a>

### Desktop approval

<span class="adm-example-kind">Reported example</span>

[Codex issue #48998](https://github.com/openai/codex/issues/48998) describes a conversational request to click Continue after that same action had already been approved. The reporter identifies the repeat by comparing the approval with the later question and says authorized unattended work stopped for another reply. The issue does not include the full transcript or a complete policy audit; total blocked time is not quantified.

<a id="examples/new-recipient"></a>

### New recipient

<span class="adm-example-kind">Synthetic example</span>

The user approves sending a draft to one colleague, then a proposed action targets a mailing list. Comparing recipient lists exposes the changed scope. One new approval concerns a different action rather than repeating permission for the original send.
