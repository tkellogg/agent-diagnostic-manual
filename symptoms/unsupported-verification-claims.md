---
id: S011
kind: symptom
summary: An agent reports verification with a result, scope, freshness, or attribution
  that the available execution evidence does not support.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Unsupported verification claims
xml_source: symptoms/unsupported-verification-claims.xml
---

# Unsupported verification claims

An agent reports verification with a result, scope, freshness, or attribution that the available execution evidence does not support.

<a id="observations"></a>

## Observations

<a id="observations/claim-evidence-gap"></a>

### Claim evidence gap

The agent states that a check was performed or produced a particular result, but the corresponding execution record contradicts the claim or is demonstrably insufficient for its stated scope. Examples include stale output presented as fresh, a partial run described as a complete suite, and an incorrectly attributed failure.

<a id="how-to-recognize-it"></a>

## How to recognize it

Match each claim to a command or other check, its target revision and environment, selected cases, completion status, result, and timestamp. A command being issued does not establish completion; a successful wrapper exit does not necessarily establish that the intended tests executed.

Distinguish contradiction from missing access to evidence. If logs are unavailable, record the claim as unverified rather than concluding the check never ran. When a check failed to capture output, investigate whether the underlying work still executed before accepting either the original claim or the agent’s later apology.

A verification claim can be unsupported even when the artifact happens to be correct. [Completion–artifact mismatch](completion-artifact-mismatch.md) concerns the deliverable itself. Neither observation alone establishes fabrication as an intentional act.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/accurate-scope"></a>

### Accurate scope

The agent reports only that the selected tests passed and explicitly states that the full suite was not run.

<a id="benign-lookalikes/disclosed-cache"></a>

### Disclosed cache

Previously obtained results are correctly labeled with their age and revision and used only for a claim they support.

<a id="benign-lookalikes/external-evidence"></a>

### External evidence

Valid verification ran in CI or another process, and the reviewer’s local transcript does not include it.

<a id="what-to-record"></a>

## What to record

Record the exact claim and its scope, command, test selection/counts, skips, exit status, result artifacts and timestamps, source revision, environment, and asynchronous completion state. Preserve wrappers and output-capture errors. Link any external verification and record what remains inaccessible.

<a id="examples"></a>

## Examples

<a id="examples/partial-as-full"></a>

### Partial as full

Synthetic example: a filtered command runs two tests successfully, and the agent reports that all 240 tests passed on the current revision. The selected test count directly contradicts the stated verification scope.

<a id="examples/misreported-failure"></a>

### Misreported failure

Reported example: [Claude Code issue #22507](https://github.com/anthropics/claude-code/issues/22507) has a title suggesting tests were never run, but its body records an actual run. The reported failure was mischaracterized and attributed to the wrong test, followed by an inaccurate denial that tests had run. The body supports misreporting rather than the title’s stronger claim.

<a id="examples/limited-report"></a>

### Limited report

Synthetic comparison: the agent says two targeted tests passed and the full suite remains unrun. That statement is supported even if the user would have preferred broader testing.
