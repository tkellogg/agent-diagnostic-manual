---
schema_version: 1
id: S001
kind: symptom
title: Repeated retrieval
summary: An agent repeatedly retrieves substantially the same information during an episode.
status: draft
evidence: unvalidated
updated: "2026-10-26"
tags: [retrieval, context, repetition]
---
# Repeated retrieval

## Observation

The agent makes multiple retrieval attempts for substantially the same information within a task episode. This includes rereading a file, repeating a search, or fetching the same document through different tools.

**This observation is neutral about usefulness and cause.** Repetition can be appropriate. The corresponding candidate diagnosis is [Unproductive repeated retrieval](../diagnoses/unproductive-repeated-retrieval.md).

## How to recognize it

Compare the question each call is trying to answer, the requested content or range, the source version, and the returned information. Identical tool arguments are a clue, not sufficient evidence. Different arguments can still retrieve the same information.

Track both exact repetition and semantically equivalent retrieval. Automated exact-match detectors can nominate cases for inspection; they cannot decide usefulness.

There is no diagnostic count threshold. “More than once” identifies repetition, not pathology.

## Benign lookalikes

- A file changed after the previous read.
- The new call obtains a different passage or field needed for the task.
- Earlier output was truncated, empty, wrong, or not delivered.
- A fresh result is required at a decision boundary.
- A legitimate task explicitly requires checking a result again.

## What to record

Record task intent, call sequence, arguments, source identity/version, result content or permitted content hashes, and which result was actually delivered to the model. Preserve the relevant model input at the later decision point, including compaction boundaries and active instructions when available.

Also record what the agent did between reads and what changed after each read. Collect enough detail to assess progress and new information. Keep sensitive raw traces outside this repository unless their inclusion is deliberate and appropriate; link to an access-controlled evidence location where needed.

## Examples

**Synthetic example — potentially unproductive.** An agent reads an unchanged configuration file, extracts the requested setting, then retrieves that same setting again before making the requested edit. Repetition continues without any edit or new question. This merits investigation; it does not reveal whether the previous result remained available to the model.

**Synthetic comparison — useful.** An agent reads a configuration file, edits it, then rereads the changed file to confirm the edit. The call may look identical while its purpose and source version differ. That is not evidence of the candidate diagnosis.

These are explanatory examples, not observed cases or validation data.
