---
id: S001
kind: symptom
summary: An agent retrieves already-delivered information again without a new content,
  freshness, or verification need.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Repeated retrieval
xml_source: symptoms/repeated-retrieval.xml
---

# Repeated retrieval

An agent retrieves already-delivered information again without a new content, freshness, or verification need.

<a id="observations"></a>

## Observations

<a id="observations/multi-read"></a>

### Multi read

Within one task episode, the agent retrieves substantially the same information again after an earlier usable result was delivered, for at least two retrievals in total. The later retrieval supplies no needed new content or source state and addresses no unmet freshness or verification need; a standing instruction to reread does not by itself establish such a need.

<a id="how-to-recognize-it"></a>

## How to recognize it

In the session transcript or tool audit log, group retrievals by the question answered, source, and returned passage or field. Compare result bodies or hashes, delivery status, and file versions or timestamps; identical commands can return changed content, while different commands can return the same content.

Check task requirements, source-change risks, and intervening edits for a new content need, freshness condition, or unresolved verification question. Pair each candidate repeat with the earlier delivered result, and use context snapshots or compaction summaries to investigate whether that result remained available at the later call. A rule can explain a redundant read without making it useful; record that rule for investigation.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/changed-source"></a>

### Changed source

A reread after an edit returns the changed setting needed for the next decision. Unlike [multi-read](repeated-retrieval.md#observations/multi-read), it supplies a needed new source state.

<a id="benign-lookalikes/different-content"></a>

### Different content

A second call obtains a different passage or field needed for the task. It does not retrieve substantially the same information as [multi-read](repeated-retrieval.md#observations/multi-read).

<a id="benign-lookalikes/failed-delivery"></a>

### Failed delivery

A retry obtains information whose earlier result was empty, wrong, truncated before the needed content, or not delivered. The earlier usable delivery required by [multi-read](repeated-retrieval.md#observations/multi-read) is absent. This excludes this symptom, not a delivery fault or [doom looping](doom-looping.md) if repeated unsuccessful retries meet its definition.

<a id="benign-lookalikes/freshness-check"></a>

### Freshness check

A reading at a decision boundary establishes freshness needed for a decision about mutable state, even if the value is unchanged. It answers an unmet freshness need, unlike [multi-read](repeated-retrieval.md#observations/multi-read); a generic reread instruction alone is insufficient.

<a id="benign-lookalikes/required-verification"></a>

### Required verification

An independent second retrieval checks a still-unresolved reliability question, and the agent performs that check. It supplies verification evidence missing from [multi-read](repeated-retrieval.md#observations/multi-read); equivalent repetitions after the question is settled are not excluded merely because a rule demands them.

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, retrieval tools, and relevant instructions. Preserve call timestamps, arguments, source versions, returned passages or permitted hashes, delivery status, and the earlier result associated with each repeat. Include total retrievals and repeat counts, output volume, elapsed time, tokens or cost where available, context transitions, intervening edits, and the eventual task outcome. Record user interruptions and recovery work so incident frequency and impact can be compared across runs.

<a id="examples"></a>

## Examples

<a id="examples/stalled-edit"></a>

### Stalled edit

Synthetic incident: an agent reads a 200-line configuration file, extracts the requested setting, and rereads the unchanged file twice without making the edit or encountering a new requirement. The tool log and file hash identify two redundant retrievals: 400 additional lines enter the transcript while the edit remains unstarted.

<a id="examples/verified-edit"></a>

### Verified edit

Synthetic comparison: an agent reads a configuration file, edits one setting, and rereads it once. The diff and returned value show that the second read verifies the changed state; two reads support one completed edit and reveal no redundant retrieval under this definition.

<a id="examples/repeated-grep"></a>

### Repeated grep

Reported incident: [Claude Code issue #59318](https://github.com/anthropics/claude-code/issues/59318) describes recognizing 30–50+ consecutive grep calls with identical arguments and output during codebase research. The reporter says tasks expected to take 2–3 minutes instead occupied 1–2 hours and required manual interruption. The account supplies repetition and impact estimates, but not a complete trace separating model requests from runtime replays.
