---
id: S011
kind: symptom
summary: An agent reports verification with a result, scope, freshness, or attribution
  that the available execution evidence does not support.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
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

Extract verification statements from final messages, pull-request descriptions, or status reports. Match each to test logs, CI jobs, result files, or audit events with the same revision, environment, selection, and timestamp.

Compare test counts, skips, failure names, exit status, and completion events with the claim. Inspect wrappers and output-capture errors where a command summary differs from detailed results; look for linked CI evidence when the local transcript is incomplete.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/accurate-scope"></a>

### Accurate scope

The agent reports only the selected passing tests and states that the full suite was not run. The execution record supports the stated scope, so there is no [claim–evidence gap](unsupported-verification-claims.md#observations/claim-evidence-gap).

<a id="benign-lookalikes/disclosed-cache"></a>

### Disclosed cache

Cached results are labeled with their actual age and revision and used only for a claim they support. They do not contradict the reported freshness or scope in [claim–evidence gap](unsupported-verification-claims.md#observations/claim-evidence-gap).

<a id="benign-lookalikes/external-evidence"></a>

### External evidence

A matching CI record supports the claim even though it is absent from the local transcript. That is not contradictory or demonstrably insufficient execution evidence under [claim–evidence gap](unsupported-verification-claims.md#observations/claim-evidence-gap); inaccessible logs alone leave the assessment unresolved.

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, exact claim, claim time, and the verification scope asserted. Preserve command and test selection, executed/passed/failed/skipped counts, exit status, result artifacts, timestamps, revision, environment, wrappers, and output-capture errors. Include external evidence and access gaps, number of verification claims reviewed and contradicted, discrepancy type, subsequent decisions, reruns, and investigation time. Distinguish unknown evidence from a demonstrated contradiction.

<a id="examples"></a>

## Examples

<a id="examples/partial-as-full"></a>

### Partial as full

Synthetic incident: a filtered command passes two tests and the agent reports all 240 passed. The command selection and runner count expose 238 unrun tests; a reviewer’s full-suite run then finds six failures. The incorrect report had hidden the remaining verification work and required another run before review could finish.

<a id="examples/misreported-failure"></a>

### Misreported failure

Reported incident: [Claude Code issue #22507](https://github.com/anthropics/claude-code/issues/22507) includes a transcript excerpt showing a 10.31-second operation failing a one-second performance limit. The PR description instead blamed a different test and called the failure a pre-existing timeout. Comparing the description with the runner output exposed the misreport; the account describes a rerun and further challenges to reconstruct what happened. It supports inaccurate reporting, not the title’s assertion that no tests ran.

<a id="examples/limited-report"></a>

### Limited report

Synthetic comparison: the agent reports two targeted tests passed and 238 other tests remain unrun. The selection and runner output support the stated scope. The verification is limited, but the reader can see the remaining work without reconstructing a false full-suite claim.
