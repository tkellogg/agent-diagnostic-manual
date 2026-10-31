---
id: I007
kind: intervention
summary: Change the agent's writing and reading instructions so important updates
  preserve the previous rule, what prompted the change, and the current requirement
  in one connected record.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-31'
title: Document what changed and why
xml_source: interventions/document-what-changed-and-why.xml
---

# Document what changed and why

Change the agent's writing and reading instructions so important updates preserve the previous rule, what prompted the change, and the current requirement in one connected record.

<a id="purpose"></a>

## Purpose

Make requirements tangible through their history: we used to do X; then Y happened; now we do X-prime because of Y. This can explain why a design looks unusual and prevent later work from undoing a deliberate fix. The old rule remains useful history, clearly distinguished from current guidance.

This specializes [save information for future work](save-information-for-future-work.md). Saving only the latest rule loses its rationale; appending a contradictory note leaves the reader to reconstruct the transition. Keep the transition together where future work will encounter it. Its benefit for [competing outdated memories](../diagnoses/failure-to-retire-outdated-memories.md) is a working proposal, not a remedy tested by the cited paper.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/known-change"></a>

### The change and its basis can be established

Identify a consequential change in a fact, requirement, or decision. Use source records or the responsible person's account; if the reason is unknown, record that rather than inventing a convincing history.

<a id="preconditions/editable-route"></a>

### The recording and reading path can be changed

The maintainer can edit the relevant prompts, skills, project guidance, or memory handling, and can identify which records later agents actually read.

<a id="procedure"></a>

## Procedure

<a id="procedure/locate-transition"></a>

### Find the transition that later work misses

Inspect a past mistake and the records used. Find the old rule, the event or evidence that prompted its replacement, the current requirement, and where each applies. Distinguish a requirement from one implementation of it.

<a id="procedure/write-history"></a>

### Connect the old rule to the current one

Update the existing authoritative note, code comment, or task record. State the current requirement prominently, then explain the prior approach, what changed, and why the new approach follows. Include a source or decision link, effective date or version where relevant, scope, and any condition for revisiting the decision. Keep only history that explains the requirement.


        **Example:** For provider B, an ambiguous payment timeout must go to reconciliation before another charge is attempted. We used to retry every timeout. After provider B stopped guaranteeing that a timeout meant no charge occurred, retries could charge twice. We now check transaction status first. Provider A still supports retries with its idempotency key. See the provider-change ticket for the effective version and supporting evidence.

<a id="procedure/change-writer"></a>

### Make future updates preserve the reason

Edit the relevant reusable writing instruction: when a decision or requirement changes, revise its existing record to explain what used to apply, what changed, and what applies now. Mark the former rule as historical. Link or correct competing copies rather than leaving separate current-looking instructions. Do not require a history note for every edit.

<a id="procedure/deliver-together"></a>

### Keep the transition together when read

Change the relevant reading instructions or retrieval handling so tasks affected by the requirement receive its current rule and short rationale together. Keep an old excerpt linked to its replacement, and preserve the distinction in summaries. Put a local reason beside surprising code when that is where future edits begin; use a link for the longer history. Check one actual later input to confirm the record is delivered, not merely saved.

<a id="procedure/schedule-review"></a>

### Arrange a review of ordinary future work

Agree with the user on the expected change, who will examine subsequent relevant tasks, and a check-in date; arrange a reminder or use an existing review job. Look for work affected by the updated requirement and for historical questions or unaffected scopes. If none occur, leave the outcome unresolved and choose another date.

<a id="evaluation"></a>

## Evaluation

Check whether future work follows the current requirement, avoids restoring the superseded behavior, and still explains what applied before. Use [D005's predictions](../diagnoses/failure-to-retire-outdated-memories.md#relations/I007/predictions) when competing memories are the proposed cause. A better explanation in the final answer is not enough if the agent's edits still violate the requirement.

Compare mistakes and rework with relevant opportunities, and include the cost of maintaining and reading the note. If it never reaches the agent, fix delivery. If it arrives intact but is ignored, reconsider the repair. If behavior improves, the note may be useful without proving whether history, clearer scope, or improved delivery made the difference.

<a id="risks-and-confounders"></a>

## Risks and confounders

- A fabricated or oversimplified rationale can make an incorrect rule harder to challenge. Keep unknown reasons unknown and distinguish evidence from the author's interpretation.
- A long history can crowd out the current requirement or repeat the old instruction so prominently that agents follow it again. Keep the current rule explicit and the explanation brief.
- A rationale can fossilize an implementation after its original constraint disappears. Preserve the requirement and conditions for reconsidering it, not a permanent ban on improvement.
- Dates alone can hide differences in authority or scope. A new record may apply only to one customer or environment. Source links must respect the intended audience's access.

<a id="stop-and-rollback"></a>

## Stop and rollback

- If the note causes incorrect changes or obscures current guidance, shorten or correct it and revise the writing or retrieval instructions. Retain the verified current requirement while removing the misleading explanation.
- Inspect consequential work already based on a faulty note; reverting the note does not undo that work. Restore accurate history from its sources where needed.
- Remove temporary observation hooks after the agreed review unless their continued use is justified.
