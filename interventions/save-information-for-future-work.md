---
id: I006
kind: intervention
summary: Change the agent's prompts or skills so it saves useful decisions, constraints,
  and findings outside the conversation, updates them when they change, and reads
  them when later work needs them.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-31'
title: Save information for future work
xml_source: interventions/save-information-for-future-work.xml
---

# Save information for future work

Change the agent's prompts or skills so it saves useful decisions, constraints, and findings outside the conversation, updates them when they change, and reads them when later work needs them.

<a id="purpose"></a>

## Purpose

Make useful information survive through deliberate recording during ordinary work. [Fix compaction](preserve-task-relevant-evidence.md) changes what a summarizer keeps; this intervention changes what the working agent writes down before the conversation is lost. The two can complement each other.

A file that nobody finds does not provide memory. The repair needs both a rule for saving information and a reliable way for future work to find and read it. Preserve information because it will help later decisions, not because it appeared in the conversation.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/reuse-needed"></a>

### Later work needs information from earlier work

Past incidents show useful information being lost, rediscovered, or repeatedly requested. [Incorrect compaction](../diagnoses/context-handoff-loss.md) is one possible explanation, but information may also be missing when a new session or another agent takes over.

<a id="preconditions/accessible-records"></a>

### Instructions and persistent records can be changed

The maintainer can edit the working agent's prompts or skills. The relevant agents can write and read records in a location appropriate for that project's data. Identify what those agents actually load; do not assume a folder or memory feature is automatically consulted.

<a id="procedure"></a>

## Procedure

<a id="procedure/find-loss"></a>

### Identify what was worth saving

Inspect a past incident and the existing instructions. Find the decision, constraint, or finding later work needed, and whether it was never saved, saved somewhere inaccessible, or saved but not read. Fix the missing part of the existing arrangement before adding another store.

<a id="procedure/choose-home"></a>

### Choose where the information belongs

Use the place future work already consults. A design decision may belong in a design document; a reason for surprising code may belong beside that code; an unfinished task may belong in its ticket. Research notes, project docs, and an agent's persistent memory are other options. Choose a home for the information rather than copying it into every location.

Keep the source or reason, the scope where it applies, and any condition that makes it stale. A permission record must retain its limits and expiry; it does not authorize unrelated future work. Keep temporary task state separate from lasting project guidance.

<a id="procedure/change-writing"></a>

### Change when and what the agent saves

Edit the relevant prompt or skill to update those records when a useful decision or finding becomes established, or when an existing constraint changes. Save before the information depends on surviving compaction or session closure. Replace stale guidance instead of appending contradictory instructions. Useful history can remain: [document what changed and why](document-what-changed-and-why.md) connects the former rule to its replacement without presenting both as current instructions. Do not require a note for every tool call.

**Example instruction:** When you settle a decision that later work will depend on, update the project's existing design note with the decision, its reason, and when to revisit it. Keep task-specific constraints and permission limits in the task's ticket. Update the existing record if the decision changes; do not create a second competing copy.

<a id="procedure/change-reading"></a>

### Make later work find the record

Put the route to the records in instructions that future sessions receive, such as the project's startup instructions or the relevant skill. Link each task to its own records. Tell the agent when to read them: when resuming that task or starting work affected by the recorded decision. Do not rely on a pointer that exists only in the conversation that may be lost, or load every saved note on every turn.

Instruct the reader to check the record's scope and recheck facts whose freshness matters. A research observation should remain an observation; saving it must not turn it into an instruction or an established fact.

<a id="procedure/check-route"></a>

### Check the route from saving to use

Confirm the revised instructions reach both the writer and the later reader. Follow one relevant record through a subsequent session or resumption: was it saved, could the agent find it, did it read the needed content, and did its work use it correctly? Reuse existing traces. A file's existence alone does not show that this route works.

<a id="procedure/arrange-review"></a>

### Review future use at an agreed date

Agree with the user which repeated work or lost constraints should decline, who will review a few ordinary subsequent tasks, and a check-in date. Arrange a reminder or existing background review. Include work different from the incident that motivated the change. If no task needed the saved information, report that the result is still unknown and choose another date.

<a id="evaluation"></a>

## Evaluation

- Look for fewer repeated investigations, missed constraints, and unnecessary requests for information already provided. Use the predictions in [D001](../diagnoses/context-handoff-loss.md#relations/I006/predictions) when compaction loss is the proposed cause.
- Check whether the agent applies current records within their scope, still verifies changeable facts, and completes useful work. Count time spent writing and reading notes as a cost; more saved text is not itself an improvement.
- If information was not saved or read, revise that part of the procedure. If the right information was read but the same mistakes continue, reconsider the explanation instead of adding more reminders to save it.
- Improvement can justify keeping the change without proving why the information was previously missing. Distinguish the benefit of a reusable record from memorizing the answer to the incident used to design the rule.

<a id="risks-and-confounders"></a>

## Risks and confounders

- Incorrect or obsolete notes can mislead many future sessions. Duplicate records can disagree, and general memory can accidentally spread task-specific assumptions or permissions.
- Saving too much creates writing overhead, harder searches, and extra context consumption. Requiring a note before every action can stall useful work.
- Moving conversation content into shared docs or tickets can expose private information. Use the agreed audience and location; do not copy entire transcripts merely to avoid choosing what matters.

<a id="stop-and-rollback"></a>

## Stop and rollback

- Revise or restore the previous instructions if recordkeeping costs exceed the benefit, or if future agents repeatedly act on stale or out-of-scope information.
- Correct or retire misleading records and their links. Reverting a prompt does not remove records already written or undo work based on them; keep accurate records that remain useful.
- Remove temporary observation hooks after the agreed review unless the user chooses to keep them.
