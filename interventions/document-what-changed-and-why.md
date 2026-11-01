---
id: I007
kind: intervention
summary: Bring code and records into agreement with the intended state, explain important
  changes in brief dated comments, and update the agent's standing instructions to
  keep them consistent.
version: '1'
status: production
evidence: validated
updated: '2026-10-31'
title: Storybook consistent comments
xml_source: interventions/document-what-changed-and-why.xml
linked_pages:
- id: D005
  title: Failure to retire outdated memories
  kind: diagnosis
  url: diagnoses/failure-to-retire-outdated-memories.html
  direction: incoming, outgoing
- id: I006
  title: Move info outside session
  kind: intervention
  url: interventions/save-information-for-future-work.html
  direction: incoming, outgoing
---

# Storybook consistent comments

Bring code and records into agreement with the intended state, explain important changes in brief dated comments, and update the agent's standing instructions to keep them consistent.

<a id="purpose"></a>

## Purpose

The primary goal is consistent state: code, comments, docs, procedures, and saved facts should agree about what applies now. Update the places affected by a change, including assumptions built into the architecture. This can repair an existing inconsistency or accompany an ordinary change; no past mistake is required.

The short story is a backup for what you miss: “Do X'. We used to do X, but then we learned Y and Z matter.” When an old assumption turns up later, that history helps the next agent understand the intended state and unwind the assumption. It can also explain why today's implementation looks odd. A comment should explain the reason itself; a link can support it but cannot replace it.

This specializes [move info outside session](save-information-for-future-work.md) and adds repair of the existing state. History is useful provenance, not a substitute for updating known stale copies. Its benefit for [competing outdated memories](../diagnoses/failure-to-retire-outdated-memories.md) remains a working proposal, not a remedy tested by the cited paper.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/known-change"></a>

### The intended state can be established

Identify what now applies and what changed: architecture, behavior, a procedure, a person's role, or another consequential fact. Establish the reason from available evidence or the responsible person. If the reason is unknown, say so rather than inventing a story.

<a id="preconditions/editable-route"></a>

### Records and standing instructions can be changed

The maintainer can update the affected code or records and the project instructions or skills used by future agents. Identify which instructions those agents actually receive.

<a id="procedure"></a>

## Procedure

<a id="procedure/update-state"></a>

### Update existing state and explain what changed

Find where the former fact or approach still shapes current work. Update affected code, tests, comments, docs, procedures, and memories to match the intended state within the agreed scope. Look beyond literal mentions: an old assumption may be built into interfaces, data structures, or workflow ordering. Preserve accurate historical records as history. If part of the repair must wait, make that remaining mismatch explicit.

Beside the places future work will encounter, add a short, informal explanation of the current intent, the earlier approach, and why it changed. Include a date, preferably when the change took effect; distinguish that from when the comment was written if they differ. Explain scope when the older approach still applies elsewhere. Keep enough history to resolve a conflicting leftover without making every comment a design document.

**Coding example:** “2026-10-31: Check provider B's transaction status before retrying a timeout. We used to retry immediately, but B can now time out after charging, so that can charge twice. Provider A's idempotent retry path is unchanged.” Update the retry code and its tests too; the comment alone does not fix them.

**Non-coding example:** “As of 2026-10-15, send purchase approvals to Maya. Lee used to handle them; Maya took over when the teams merged.” Update the routing instructions and contact records, not just the note.

<a id="procedure/change-guidance"></a>

### Make this part of future work

Edit the existing AGENTS.md, project guidance, or relevant skill so future changes update affected state and leave brief dated explanations where the history helps. Tell agents to use those explanations when they encounter conflicting leftovers, check that the scope and authority match, and correct the stale copy. Verify that this guidance is loaded for the relevant work; merely saving the file is not enough.

**Example instruction:** “When a fact, procedure, or design changes, update the affected code and records so they agree. Where the reason will help later work, leave a brief dated comment: what applies now, what we used to do, and why it changed. Look for assumptions beyond exact text matches. If you cannot update a known dependency, record what remains inconsistent. Don't invent missing reasons or add a history note to every edit.”

<a id="evaluation"></a>

## Evaluation

Agree on who will review ordinary subsequent work and a check-in date, using an existing review job or reminder. Check whether agents keep affected state consistent, resolve missed old assumptions correctly, and avoid restoring superseded behavior. Include time spent updating and reading records. If no relevant work occurs, leave the outcome unresolved and choose another date.

Use [D005's predictions](../diagnoses/failure-to-retire-outdated-memories.md#relations/I007/predictions) when competing memories are the proposed cause. Correctly explaining the history is not enough if code or actions still contradict the intended state. If the guidance never reaches the agent, fix delivery; if it arrives but is ignored, reconsider the repair. Improvement does not isolate whether consistency repairs, history, or clearer instructions helped.

<a id="risks-and-confounders"></a>

## Risks and confounders

- An invented reason can make a bad decision harder to question. Keep unknown reasons unknown.
- Excessive history can bury current intent or make the old behavior more salient. Keep comments brief and useful.
- A newer date does not automatically win: records may differ in authority or apply to different people, versions, or environments.
- A broad consistency sweep can change valid behavior outside the intended scope. Distinguish a lasting requirement from an implementation that can improve.
- Historical explanations can themselves become stale. Update them when the underlying facts or constraints change.

<a id="stop-and-rollback"></a>

## Stop and rollback

- If the guidance causes excessive bookkeeping or incorrect changes, narrow or restore it and correct misleading comments while retaining accurate current intent.
- Review consequential code and actions changed on the basis of a faulty explanation. Removing the comment does not undo those changes.
