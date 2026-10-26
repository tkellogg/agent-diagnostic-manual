---
id: S010
kind: symptom
summary: An agent claims that requested work is complete while the delivered artifact
  or resulting state demonstrably lacks a required part.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: "Completion\u2013artifact mismatch"
xml_source: symptoms/completion-artifact-mismatch.xml
---

# Completion–artifact mismatch

An agent claims that requested work is complete while the delivered artifact or resulting state demonstrably lacks a required part.

<a id="observations"></a>

## Observations

<a id="observations/unsupported-completion"></a>

### Unsupported completion

A completion claim covers a stated deliverable or acceptance criterion, but inspection of the corresponding artifact or system state at that time contradicts the claim. The discrepancy is about delivered work, not merely confidence or phrasing.

<a id="how-to-recognize-it"></a>

## How to recognize it

Extract the exact completion claim and map it to the agreed scope. Inspect the actual destination, revision, branch, environment, or deployed state named by the claim. A missing file in a different worktree is not evidence that no file was written anywhere.

Check whether the work was created but not persisted, committed, transferred, or deployed as requested. These possibilities still matter to the completion claim, but differ from never performing the work. Compare contemporaneous state where possible; later deletion does not establish an earlier mismatch.

An explicit and accurate disclosure of incomplete work is not this symptom, although [Premature stopping](premature-stopping.md) may apply. A claim specifically about checks or evidence can also fit [Unsupported verification claims](unsupported-verification-claims.md). Do not infer intentional deception from the discrepancy alone.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/scoped-completion"></a>

### Scoped completion

The agent accurately says one stage is complete and clearly identifies the unfinished stages.

<a id="benign-lookalikes/wrong-location"></a>

### Wrong location

The reviewer inspects a different revision or destination from the one the agent correctly reported.

<a id="benign-lookalikes/later-change"></a>

### Later change

The artifact satisfied the claim when reported but was changed or removed afterward.

<a id="what-to-record"></a>

## What to record

Record acceptance criteria, exact completion language, claim time, artifact identity and revision, inspection method, and the missing or contradictory behavior. Preserve tool results and persistence/commit/deployment events. Record disclosed limitations, asynchronous state, and later modifications separately.

<a id="examples"></a>

## Examples

<a id="examples/missing-export"></a>

### Missing export

Synthetic example: the agent says the requested CSV export is implemented and ready. The delivered revision contains a button and success message but no export path, and exercising the named workflow produces no file.

<a id="examples/empty-worktree"></a>

### Empty worktree

Reported example: [Matthew Hawthorne’s February 2026 account](https://pushtoprod.substack.com/p/my-ai-agent-didnt-do-anything) describes a resumed agent reporting success after inheriting a nearly completed checklist and a clean worktree. Earlier work had occurred but was not committed into the resumed task’s branch.

<a id="examples/explicit-partial"></a>

### Explicit partial

Synthetic comparison: the agent states that the button is implemented but export generation remains unfinished. The delivery is incomplete, but the completion claim accurately describes its limited scope.
