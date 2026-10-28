---
id: I001
kind: intervention
summary: Save enough evidence to see what compaction forgets, change the compaction
  prompt or algorithm, and review the next few days of ordinary work with the user.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Fix compaction so important information survives
xml_source: interventions/preserve-task-relevant-evidence.xml
---

# Fix compaction so important information survives

Save enough evidence to see what compaction forgets, change the compaction prompt or algorithm, and review the next few days of ordinary work with the user.

<a id="purpose"></a>

## Purpose

Improve what the compactor keeps and discards so critical information is not forgotten. Keep what unfinished work is likely to need; remove irrelevant history so the summary still saves space.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/identified-omission"></a>

### Important information was lost

Important information disappears during compaction, as proposed in [compaction loss](../diagnoses/context-handoff-loss.md). [Repeated retrieval](../symptoms/repeated-retrieval.md), [lost constraints](../symptoms/lost-task-constraints.md), or [repeated permission requests](../symptoms/repeated-reauthorization.md) can point you toward an incident to inspect.

<a id="preconditions/editable-transition"></a>

### Access to compaction

You can edit the compaction prompt or algorithm and inspect its summaries. If compaction is controlled by a provider, identify the configurable part before promising a repair.

<a id="procedure"></a>

## Procedure

<a id="procedure/locate-boundary"></a>

### Inspect the compaction prompt

Find the compaction prompt or algorithm and save its current version. Compare a recent summary with the conversation before it; identify useful facts it lost and irrelevant details it retained.

<a id="procedure/preserve-evidence"></a>

### Save before-and-after conversations

Check whether the harness already saves the conversation before compaction and the resulting summary. If it does not, add a pre-compaction hook to save them privately; agree with the user where they go, who can access them, and how long to keep them.

<a id="procedure/create-record"></a>

### Change what compaction keeps

Edit the compaction prompt or algorithm to keep unfinished goals, decisions, current constraints, permission limits, and findings needed for the next likely steps. Tell it to discard completed detours and repetitive output. Include one short example of an important fact the old version lost.

<a id="procedure/confirm-delivery"></a>

### Check what survived

Inspect the next summary and, where accessible, the context used after compaction. Confirm the important facts survived in usable form; a saved full transcript alone does not show what the agent retained.

<a id="procedure/review-work"></a>

### Review occasional samples

Set up an occasional background review of saved before/after conversations and subsequent work. Reuse an existing job or add an async hook that samples compactions; do not add another model call to every working turn.

<a id="procedure/agree-followup"></a>

### Agree on a check-in date

Agree with the user on a check-in date, who will review the samples, and a reminder or scheduled job. For example, review in three workdays if normal use should produce several compactions; if too few occur, report that and choose another date.

<a id="evaluation"></a>

## Evaluation

- Before applying the change, record which lost facts should now survive and which later mistakes should decline. Use the predictions in [D001](../diagnoses/context-handoff-loss.md#relations/I001/predictions) when that explanation fits.
- At the agreed check-in, compare saved summaries with the next work. Did requirements survive? Did the agent repeat less work? Did the summary still omit irrelevant material?
- If the facts survive but mistakes continue, reconsider the explanation. If summaries were not captured or no relevant compaction occurred, say that the review is inconclusive.

<a id="risks-and-confounders"></a>

## Risks and confounders

- Keeping too much can fill the context; keeping outdated facts can cause bad decisions. A summary can also preserve permission while dropping its limits.
- Saved conversations can contain private data. Keep collection limited to the agreed location and retention period. A model or task change can make comparisons harder.

<a id="stop-and-rollback"></a>

## Stop and rollback

- Restore the previous compaction prompt or algorithm if the change causes stale decisions, lost permission limits, or excessive context use.
- Correct affected summaries and repair any resulting work. Reverting the prompt does not undo actions already taken.
- Remove temporary capture or review hooks when the agreed review ends, unless the user chooses to keep them.
