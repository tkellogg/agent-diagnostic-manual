---
id: I002
kind: intervention
summary: Find the instructions that demand extra checking, remove duplicates and contradictions,
  and agree with the user on one simple account of what verification each kind of
  work needs.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Consolidate verification instructions with the user
xml_source: interventions/scope-verification-policy.xml
---

# Consolidate verification instructions with the user

Find the instructions that demand extra checking, remove duplicates and contradictions, and agree with the user on one simple account of what verification each kind of work needs.

<a id="purpose"></a>

## Purpose

Reduce [excessive verification](../symptoms/excessive-verification.md) by simplifying the instructions that cause it. A pile of testing rules can make the agent lose sight of whether the user wants a quick demonstration, a maintained feature, or a production release.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/identified-rule"></a>

### Instructions contribute to the problem

Active skills, prompts, project files, or workflows contain broad or conflicting checking instructions. This is a plausible repair for [overbroad verification instructions](../diagnoses/verification-policy-overgeneralization.md); if the instructions are already clear, investigate the agent’s understanding of the task.

<a id="preconditions/authorized-change"></a>

### User or workflow owner involvement

The user or workflow owner can review the proposed simplification and identify checks that must remain. The maintainer can edit the relevant instruction sources.

<a id="procedure"></a>

## Procedure

<a id="procedure/find-instructions"></a>

### Find the active instructions

Search the instructions actually loaded by the agent: system and project guidance, nested instruction files, skills, command templates, and CI rules. List each verification demand with its source; identify duplicates, contradictions, and rules that restart checks after every small edit.

<a id="procedure/agree-needs"></a>

### Agree on what checking is useful

Review that list with the user. Establish what they are trying to learn or ship, what they plan to verify themselves, which failures matter, and what time or cost they consider reasonable. Use familiar task examples to resolve differences.

<a id="procedure/consolidate-rules"></a>

### Remove duplication and contradictions

Delete redundant and obsolete instructions, reconcile contradictions, and keep the remaining guidance in the fewest useful places. Make other files point there instead of copying it. Preserve necessary safety and release checks; do not delete a quota of rules blindly.

<a id="procedure/make-it-simple"></a>

### Write one short rule

Write a short rule for choosing enough verification for the task. For example: check the changed behavior, stop once that question is answered, and run broader checks when the change or release requires them. Show where a prototype and a release differ; avoid replacing the old pile with a larger checklist.

<a id="procedure/review-work"></a>

### Review future tasks

Confirm future sessions load the consolidated guidance. Agree on a check-in after a few normal tasks, then review unwanted checks, time to a usable result, and missed defects with the user.

<a id="evaluation"></a>

## Evaluation

- Predict which duplicate or unnecessary checks should disappear and which important checks should remain. Compare similar tasks before and after consolidation.
- Ask whether the remaining verification fits the user’s intent and planned review. Shorter runs are helpful only if the requested result remains useful and credible.
- If the revised instructions are active but excess checking continues, inspect task misunderstandings or mistaken assumptions about the application.

<a id="risks-and-confounders"></a>

## Risks and confounders

- Simplification can accidentally remove a necessary check or hide a difference between prototype and production work.
- A faster test runner or easier task mix can reduce time independently of the instruction change.

<a id="stop-and-rollback"></a>

## Stop and rollback

- Restore a removed requirement if relevant defects are missed or a required gate is skipped.
- Correct the smallest harmful change instead of automatically restoring every duplicate instruction.
