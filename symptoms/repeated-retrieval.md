---
id: S001
kind: symptom
summary: An agent repeatedly retrieves substantially the same information during an
  episode.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
title: Repeated retrieval
xml_source: symptoms/repeated-retrieval.xml
---

# Repeated retrieval

An agent repeatedly retrieves substantially the same information during an episode.

<a id="observations"></a>

## Observations

<a id="observations/multi-read"></a>

### Multi read

The agent makes multiple retrieval attempts for substantially the same information within a task episode. This includes rereading a file, repeating a search, or fetching the same document through different tools.

**This observation is neutral about usefulness and cause.** Repetition can be appropriate. The corresponding candidate diagnosis is [Unproductive repeated retrieval](../diagnoses/unproductive-repeated-retrieval.md).

<a id="how-to-recognize-it"></a>

## How to recognize it

Compare the question each call is trying to answer, the requested content or range, the source version, and the returned information. Identical tool arguments are a clue, not sufficient evidence. Different arguments can still retrieve the same information.

Track both exact repetition and semantically equivalent retrieval. Automated exact-match detectors can nominate cases for inspection; they cannot decide usefulness.

There is no diagnostic count threshold. “More than once” identifies repetition, not pathology.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/changed-source"></a>

### Changed source

A file changed after the previous read.

<a id="benign-lookalikes/different-content"></a>

### Different content

The new call obtains a different passage or field needed for the task.

<a id="benign-lookalikes/failed-delivery"></a>

### Failed delivery

Earlier output was truncated, empty, wrong, or not delivered.

<a id="benign-lookalikes/freshness-check"></a>

### Freshness check

A fresh result is required at a decision boundary.

<a id="benign-lookalikes/required-verification"></a>

### Required verification

A legitimate task explicitly requires checking a result again.

<a id="what-to-record"></a>

## What to record

Record task intent, call sequence, arguments, source identity/version, result content or permitted content hashes, and which result was actually delivered to the model. Preserve the relevant model input at the later decision point, including compaction boundaries and active instructions when available.

Also record what the agent did between reads and what changed after each read. Collect enough detail to assess progress and new information. Keep sensitive raw traces outside this repository unless their inclusion is deliberate and appropriate; link to an access-controlled evidence location where needed.

<a id="examples"></a>

## Examples

<a id="examples/stalled-edit"></a>

### Stalled edit

**Synthetic example — potentially unproductive.** An agent reads an unchanged configuration file, extracts the requested setting, then retrieves that same setting again before making the requested edit. Repetition continues without any edit or new question. This merits investigation; it does not reveal whether the previous result remained available to the model.

<a id="examples/verified-edit"></a>

### Verified edit

**Synthetic comparison — useful.** An agent reads a configuration file, edits it, then rereads the changed file to confirm the edit. The call may look identical while its purpose and source version differ. That is not evidence of the candidate diagnosis.
