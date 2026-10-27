---
id: I005
kind: intervention
summary: Change the deferred-tool adapter so successful discovery delivers a callable
  interface to the receiving turn, and failed activation returns an explicit unavailable
  result.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Complete the discovery-to-invocation handoff
xml_source: interventions/complete-tool-discovery-handoff.xml
---

# Complete the discovery-to-invocation handoff

Change the deferred-tool adapter so successful discovery delivers a callable interface to the receiving turn, and failed activation returns an explicit unavailable result.

<a id="purpose"></a>

## Purpose

Repair the interface between tool discovery and use. A capability name is not enough when invocation requires additional schema or runtime registration. Discovery should either complete that handoff or tell the agent what remains blocked.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/delivery-gap"></a>

### Delivery gap

The adapter promises callable access after discovery, but inspection shows a gap in registration, schema delivery, or the supported invocation route.

<a id="preconditions/adapter-access"></a>

### Adapter access

The maintainer can change and inspect the adapter and receiving tool configuration while preserving existing permissions.

<a id="procedure"></a>

## Procedure

<a id="procedure/trace-handoff"></a>

### Trace handoff

Locate where discovery resolves the capability, where runtime registration occurs, and how the receiving turn gets its invocation contract.

<a id="procedure/complete-delivery"></a>

### Complete delivery

Change that shared path to register and deliver the interface before reporting callable availability. If activation is asynchronous, return its pending state and supported continuation instead of an apparently completed discovery.

<a id="procedure/expose-blocks"></a>

### Expose blocks

Return an explicit unavailable result when activation fails, with the actionable reason and supported recovery if one exists. Repeated discovery should not return the same success-looking reference while the capability remains inaccessible.

<a id="procedure/confirm-use"></a>

### Confirm use

Inspect a representative receiving input and safe invocation, then observe ordinary subsequent tool-use opportunities. Check an unavailable capability as well so errors remain visible and permission boundaries hold.

<a id="evaluation"></a>

## Evaluation

Record predictions for available and unavailable tools separately. On applicable future turns, compare successful discovery-to-use transitions, repeated searches for the same capability, explicit blocks, and completed required tool work.

Confirmed delivery with continued rediscovery weakens the delivery-gap explanation. Correct invocations that fail at an external service indicate another obstruction. Fewer searches caused by silently skipping required work are not success.

<a id="risks-and-confounders"></a>

## Risks and confounders

Loading unnecessary schemas can consume context; stale registrations can call the wrong interface. Adapter changes must preserve authorization and tool selection. Model or provider changes can independently affect discovery behavior.

<a id="stop-and-rollback"></a>

## Stop and rollback

Revert the adapter change if it exposes unauthorized tools, delivers incompatible schemas, or breaks working routes. Report unavailable capabilities explicitly while repairing the handoff; do not mask activation failures as successful access.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This is an unvalidated proposed adapter repair. No particular harness is asserted to have this defect, and a completed handoff does not guarantee correct tool choice or successful task completion.
