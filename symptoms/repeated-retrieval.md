---
id: S001
kind: symptom
summary: An agent retrieves already-delivered information again without a new content,
  freshness, or verification need.
version: '1'
status: reviewed
evidence: unvalidated
updated: '2026-10-28'
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

Group reads of the same source in the tool log and compare what they returned. Check whether a change, freshness need, or unresolved question explains each reread.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/changed-source"></a>

### Changed source

A reread after an edit obtains a changed setting needed for the next decision. The new information makes this useful work.

<a id="benign-lookalikes/different-content"></a>

### Different content

A second read obtains a different passage or field needed for the task. It is not a repeat of information already obtained.

<a id="benign-lookalikes/failed-delivery"></a>

### Failed delivery

The earlier result was empty, wrong, or cut off before the needed content. A retry can obtain missing information; repeated unsuccessful retries may still become [doom looping](doom-looping.md).

<a id="benign-lookalikes/freshness-check"></a>

### Freshness check

A file or service may have changed since the last read. Checking a version number, timestamp, diff, or other reliable change signal can establish whether a full reread is needed; an unchanged result can still answer a real freshness question.

<a id="benign-lookalikes/required-verification"></a>

### Required verification

An independent second source can answer an unresolved reliability question. Repeating equivalent checks after that question is settled does not add the same value.

<a id="what-to-record"></a>

## What to record

Record the episode identifier and date, task type, model and harness versions, retrieval tools, and relevant instructions. Preserve call timestamps, arguments, source versions, returned passages or permitted hashes, delivery status, and the earlier result associated with each repeat. Include total retrievals and repeat counts, output volume, elapsed time, tokens or cost where available, context transitions, intervening edits, and the eventual task outcome. Record user interruptions and recovery work so incident frequency and impact can be compared across runs.

<a id="examples"></a>

## Examples

<a id="examples/stalled-edit"></a>

### Stalled edit

<span class="adm-example-kind">Synthetic example</span>

An agent reads a 200-line configuration file, extracts the requested setting, and rereads the unchanged file twice without making the edit or encountering a new requirement. The tool log and file hash identify two redundant retrievals: 400 additional lines enter the transcript while the edit remains unstarted.

<a id="examples/verified-edit"></a>

### Verified edit

<span class="adm-example-kind">Synthetic example</span>

An agent reads a configuration file, edits one setting, and rereads it once. The diff and returned value show that the second read verifies the changed state; two reads support one completed edit and reveal no redundant retrieval under this definition.

<a id="examples/repeated-grep"></a>

### Repeated grep

<span class="adm-example-kind">Reported example</span>

[Claude Code issue #59318](https://github.com/anthropics/claude-code/issues/59318) describes recognizing 30–50+ consecutive grep calls with identical arguments and output during codebase research. The reporter says tasks expected to take 2–3 minutes instead occupied 1–2 hours and required manual interruption. The account supplies repetition and impact estimates, but not a complete trace separating model requests from runtime replays.
