---
id: S004
kind: symptom
summary: "An agent continues or expands verification beyond the task\u2019s justified\
  \ checking needs, delaying the requested outcome."
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Excessive verification
xml_source: symptoms/excessive-verification.xml
---

# Excessive verification

An agent continues or expands verification beyond the task’s justified checking needs, delaying the requested outcome.

<a id="observations"></a>

## Observations

<a id="observations/checking-overrun"></a>

### Checking overrun

Verification continues or additional checking work is created after an applicable stopping condition has been met, beyond an explicit verification scope or budget, or through repeated equivalent checks without a relevant change or unresolved question. The extra work delays delivery or consumes resources without an unmet acceptance need, relevant risk, or investigation question that justifies it; an overbroad standing rule can cause this behavior.

<a id="how-to-recognize-it"></a>

## How to recognize it

Start with the user request, project instructions, release rules, and any agreed checking budget or stopping condition. Build a timeline from test commands, CI runs, background jobs, and their results, marking when the requested checks were satisfied.

Compare later checks against code and environment changes, unresolved failures, and the decisions their results informed. Inspect diffs for newly created test infrastructure and job logs for setup or repair time. Distinguish a rule's existence from the acceptance need or risk it addresses; new failures, unmet coverage, and planned repeatability studies can justify further checking.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/required-gate"></a>

### Required gate

A release, security, or project check supplies coverage still needed for the requested action. That unmet acceptance need distinguishes it from [checking overrun](excessive-verification.md#observations/checking-overrun), even when the suite takes longer than the edit. A policy requiring equivalent checks after that need is met may itself warrant diagnosis.

<a id="benign-lookalikes/new-risk"></a>

### New risk

A check reveals a relevant new failure or an edit affects additional behavior. The new evidence justifies the broader checking, unlike the unexplained extra work in [checking overrun](excessive-verification.md#observations/checking-overrun).

<a id="benign-lookalikes/repeatability-study"></a>

### Repeatability study

Unchanged runs belong to an agreed flakiness, load, or reproducibility investigation. They answer its unresolved question and satisfy its checking scope, so repetition alone is not [checking overrun](excessive-verification.md#observations/checking-overrun).

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, requested outcome and urgency, explicit checking budget, mandatory gates, and stopping condition. Preserve check commands, selected tests, job timestamps, state changes, results, and the decision each check informed. Include required versus unexplained runs, infrastructure added, time after the stopping condition, tokens or cost where available, delivery delay, and defects actually caught. Record total tasks or checks reviewed when aggregating incidents, rather than treating a count of complaints as a rate.

<a id="examples"></a>

## Examples

<a id="examples/past-completion"></a>

### Past completion

Synthetic incident: a user requests a reversible text edit and one targeted check, which passes. With no new failure or broader requirement, the agent installs a test framework, repairs its setup, and runs the full suite twice. The command timeline shows twenty-four additional minutes before delivery and no further defect found.

<a id="examples/suite-overrun"></a>

### Suite overrun

Reported incident: [a Claude Code user reports repeated runs of more than 1,500 tests after small edits despite instructions to stop](https://www.reddit.com/r/ClaudeCode/comments/1x7zbvd/claude_runs_1800_useless_tests_creates_more/). The user recognized the activity by inspecting long-running background tasks and reports about two hours per run, with the project largely stalled for weeks. These are user estimates; the post does not supply a full trace establishing the applicable requirements for each run.

<a id="examples/release-check"></a>

### Release check

Synthetic comparison: a one-line authentication edit takes one minute and its mandatory regression suite takes twelve minutes. The release policy and CI log account for the longer check; the run satisfies a required gate rather than adding unexplained verification.
