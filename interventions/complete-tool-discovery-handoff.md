---
id: I005
kind: intervention
summary: Fix tool loading so search reports a tool as ready only after the agent has
  its definition and the runtime can execute it.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Make discovered tools callable
xml_source: interventions/complete-tool-discovery-handoff.xml
---

# Make discovered tools callable

Fix tool loading so search reports a tool as ready only after the agent has its definition and the runtime can execute it.

<a id="purpose"></a>

## Purpose

Repair the harness fault described by [tool discovery reports unusable tools](../diagnoses/tool-discovery-delivery-gap.md). A tool name alone is not enough: the agent needs its arguments, and the runtime needs to know how to execute the call.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/delivery-gap"></a>

### Tool search promises access it has not provided

Search claims a tool is ready, but its definition or runtime registration is missing. An ordinary failed service call is a different problem.

<a id="preconditions/adapter-access"></a>

### Access to tool loading

The maintainer can change tool loading and inspect the tool definitions supplied to the model.

<a id="procedure"></a>

## Procedure

<a id="procedure/trace-handoff"></a>

### Find the missing tool setup

Follow one tool from search to registration and the next model request. Find which definition or registration is missing.

<a id="procedure/complete-delivery"></a>

### Finish loading before reporting success

Change tool loading to finish registration and supply the definition before returning “ready.” For slow loading, return an explicit pending status and a working way to wait.

<a id="procedure/expose-blocks"></a>

### Report unavailable tools clearly

When loading fails, return an unavailable result with the reason and any useful recovery step. Do not keep returning success when repeating the same search cannot help.

<a id="procedure/confirm-use"></a>

### Check calls and future use

Check a harmless call to an available tool and a failed load. Then review ordinary use at an agreed follow-up, including whether the agent still repeats discovery.

<a id="evaluation"></a>

## Evaluation

- Expect repeated discovery to decline and required tool work to continue. Unavailable tools should produce clear blockers or useful alternatives.
- If the tool is callable but the agent keeps searching, reconsider D002. If calls reach the service and fail, investigate those errors.

<a id="risks-and-confounders"></a>

## Risks and confounders

- Loading unnecessary tool definitions can fill the context. Incorrect registrations can call the wrong tool.
- Preserve existing permissions; making tools callable must not expose capabilities the user has not authorized.

<a id="stop-and-rollback"></a>

## Stop and rollback

- Revert a loader change that exposes unauthorized tools or breaks working calls.
- Continue to report unavailable tools honestly while repairing the loader.
