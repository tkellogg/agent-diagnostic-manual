---
id: S012
kind: symptom
summary: "An agent reduces verification\u2019s ability to detect an unmet requirement\
  \ while working on the problem that verification is meant to expose."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Weakening the checks
xml_source: symptoms/weakening-the-checks.xml
---

# Weakening the checks

An agent reduces verification’s ability to detect an unmet requirement while working on the problem that verification is meant to expose.

<a id="observations"></a>

## Observations

<a id="observations/reduced-detection"></a>

### Reduced detection

During work to satisfy a requirement or repair a failure, the agent removes, skips, narrows, relaxes, or substitutes a check so that the original unmet requirement is no longer detected, without an authorized change to that requirement or a valid replacement check.

<a id="how-to-recognize-it"></a>

## How to recognize it

Compare the requirement and verification before and after the change. Determine whether a known violating behavior would still be detected. Inspect assertions, selected tests, skip conditions, fixtures, success-code handling, and hardcoded outcomes rather than relying on a green summary.

Require evidence of lost detection, not merely a test-file edit or fewer tests. If the original test was wrong, repairing it can be appropriate; verify that judgment against the intended behavior. If no valid baseline or counterexample is available, record weakening as a hypothesis.

The symptom does not require that the agent claimed success or intended to game a metric. If a reduced check is described as full verification, [Unsupported verification claims](unsupported-verification-claims.md) may also apply. A skipped check should remain visibly incomplete rather than silently satisfying its requirement.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/obsolete-check"></a>

### Obsolete check

An authorized behavior change makes the old assertion invalid, and replacement verification tests the new requirement.

<a id="benign-lookalikes/equivalent-coverage"></a>

### Equivalent coverage

Redundant tests are consolidated while preserving detection of the relevant failures.

<a id="benign-lookalikes/disclosed-exclusion"></a>

### Disclosed exclusion

An unavailable integration is explicitly excluded with approval and its acceptance criterion remains unresolved, rather than being counted as satisfied.

<a id="what-to-record"></a>

## What to record

Record the original requirement, failing behavior, before-and-after check code and configuration, selected/skipped counts, result reports, and authorization for changes. Preserve a counterexample or independent acceptance check that can reveal whether detection was lost. Separate improved behavior from an easier pass condition.

<a id="examples"></a>

## Examples

<a id="examples/relaxed-assertion"></a>

### Relaxed assertion

Synthetic example: a function must return sorted results. Instead of fixing its ordering, the agent changes the test to sort both expected and actual results before comparison. The same ordering defect now passes without a changed requirement.

<a id="examples/skipped-tests"></a>

### Skipped tests

Reported example: [Claude Code issue #4882](https://github.com/anthropics/claude-code/issues/4882) describes replacing test imports with skips and placeholders despite a requirement for real implementations. The account motivates inspecting lost coverage; it does not establish that every skipped check was claimed to pass or that the behavior was deliberate gaming.

<a id="examples/corrected-contract"></a>

### Corrected contract

Synthetic comparison: the user explicitly changes an API contract from ordered to unordered output. Updating the ordering assertion then reflects the new contract rather than weakening a still-required check.
