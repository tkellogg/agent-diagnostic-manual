---
id: S004
kind: symptom
summary: "An agent continues or expands verification beyond the task\u2019s justified\
  \ checking needs, delaying the requested outcome."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Excessive verification
xml_source: symptoms/excessive-verification.xml
---

# Excessive verification

An agent continues or expands verification beyond the task’s justified checking needs, delaying the requested outcome.

<a id="observations"></a>

## Observations

<a id="observations/checking-overrun"></a>

### Checking overrun

Verification continues or additional checking work is created after an applicable stopping condition has been met, beyond an explicit verification scope or budget, or through repeated equivalent checks without a relevant change or unresolved question. The extra work delays delivery or consumes resources without an identified requirement that justifies it.

<a id="how-to-recognize-it"></a>

## How to recognize it

Establish the user’s requested outcome, applicable project requirements, verification scope, and stopping condition. Identify the decision each extra check could change. A check can be justified by a concrete unresolved risk even if the user did not name it individually; a genuine instruction conflict should be surfaced, not silently resolved by exceeding the budget.

Compare inputs, code and environment state, selected tests, outputs, and what the agent does with the result. A repeated check that obtains previously missing output or measures flakiness is different from one that merely reproduces an already-understood result. Include time spent creating and repairing self-assigned test infrastructure.

High test counts, slow suites, and user impatience alone do not establish excess. If the trace supports cost but not the absence of a reason, record verification cost with the judgment unresolved. Repeated checking may also fit [Doom looping](doom-looping.md); unnecessary new infrastructure may fit [Unrequested changes](unrequested-changes.md).

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/required-gate"></a>

### Required gate

A release, security, or project rule requires the full check before the requested action can proceed.

<a id="benign-lookalikes/new-risk"></a>

### New risk

A check reveals a relevant new failure or the edit affects additional behavior, justifying broader verification.

<a id="benign-lookalikes/repeatability-study"></a>

### Repeatability study

Repeated unchanged runs are part of an agreed flakiness, load, or reproducibility investigation.

<a id="what-to-record"></a>

## What to record

Record the requested outcome and urgency, explicit scope or budget, applicable mandatory checks, stopping condition, check sequence and duration, state changes, results, and the decision each check informed. Separate required work, newly justified work, and unexplained additions; record delivery delay and any actual defects caught.

<a id="examples"></a>

## Examples

<a id="examples/past-completion"></a>

### Past completion

Synthetic example: a user requests a reversible text edit and one targeted check. That check passes. With no new failure or broader requirement, the agent adds a test framework, repairs its setup, and reruns the entire suite twice before delivering the edit.

<a id="examples/suite-overrun"></a>

### Suite overrun

Reported example: [a Claude Code user describes repeated full-suite runs after small edits despite requests to stop](https://www.reddit.com/r/ClaudeCode/comments/1x7zbvd/claude_runs_1800_useless_tests_creates_more/). The account reports substantial delays but provides no full trace establishing which checks were required or unnecessary.

<a id="examples/release-check"></a>

### Release check

Synthetic comparison: a one-line authentication change triggers a required regression suite before release. Its duration exceeds the edit time, but it satisfies an applicable gate and does not establish excessive verification.
