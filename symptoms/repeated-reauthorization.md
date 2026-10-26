---
id: S008
kind: symptom
summary: An agent requests permission again for an action that remains covered by
  a clear, applicable authorization.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Repeated reauthorization
xml_source: symptoms/repeated-reauthorization.xml
---

# Repeated reauthorization

An agent requests permission again for an action that remains covered by a clear, applicable authorization.

<a id="observations"></a>

## Observations

<a id="observations/redundant-permission"></a>

### Redundant permission

After explicit authorization of an action, the agent asks the user to authorize materially the same action again without a changed target, scope, consequence, or applicable requirement that makes renewed approval necessary.

<a id="how-to-recognize-it"></a>

## How to recognize it

Match the requested action to the prior authorization: account, resource, operation, scope, and any conditions. A broad statement of intent may not authorize a particular consequential operation; a precise earlier approval is stronger evidence.

Determine whether the prompt came from the agent’s conversation or a tool/platform permission gate. Both can delay the task, but an agent may be required to relay a gate even when conversational permission already exists. Record such enforcement separately instead of attributing it to caution.

One redundant repeat after a clear approval is sufficient for this observation. Record later repeats and resulting delay. If the earlier permission disappeared from a continuation, [Lost task constraints](lost-task-constraints.md) may provide additional description.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/changed-action"></a>

### Changed action

The operation now affects a different account, recipient, resource, or materially broader scope.

<a id="benign-lookalikes/required-prompt"></a>

### Required prompt

The tool or governing instructions require a fresh approval at this stage or after authorization expires.

<a id="benign-lookalikes/conditional-consent"></a>

### Conditional consent

The earlier consent depended on a condition that has not been met or cannot yet be verified.

<a id="what-to-record"></a>

## What to record

Record the original approval, its scope and conditions, each later permission request, the action available at that point, and any changed circumstances. Include the origin of the prompt, relevant platform policies, expiry/session boundaries, and whether each answer led to execution or another request.

<a id="examples"></a>

## Examples

<a id="examples/same-click"></a>

### Same click

Synthetic example: the user explicitly approves clicking Continue on a named screen. With the same screen and no additional gate, the agent asks twice more whether it should click Continue.

<a id="examples/desktop-approval"></a>

### Desktop approval

Reported example: [Codex issue #48998](https://github.com/openai/codex/issues/48998) describes repeated demands for authorization of the same approved desktop action. The public report is not a complete audit of the governing tool policies.

<a id="examples/new-recipient"></a>

### New recipient

Synthetic comparison: the user authorizes sending a draft to one colleague. The next proposed action sends it to an entire mailing list, requiring a new scope decision.
