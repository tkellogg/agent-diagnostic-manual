---
id: D002
kind: diagnosis
summary: The discovery interface identifies a tool as available without supplying
  the callable interface needed by the next agent turn, leaving the system searching
  for a capability it cannot use.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
unit: configured-agent-system
title: Tool discovery delivery gap
xml_source: diagnoses/tool-discovery-delivery-gap.xml
---

# Tool discovery delivery gap

The discovery interface identifies a tool as available without supplying the callable interface needed by the next agent turn, leaving the system searching for a capability it cannot use.

<a id="relations"></a>

## Relationships

Related symptom: [S002](../symptoms/doom-looping.md)

<a id="relations/I005"></a>
<a id="relations/I005/when"></a>
[I005](../interventions/complete-tool-discovery-handoff.md)

**When:** Discovery is expected to make a tool callable, but registration or delivery to the receiving turn is missing or inconsistent.

<a id="relations/I005/predictions"></a>

#### Predictions

After the adapter delivers a usable tool or an explicit unavailable result, repeated discovery for that same capability should decline. Available tools should be invoked when the task calls for them; unavailable tools should lead to a supported alternative or a specific blocker.

Invocation errors from invalid credentials, bad arguments, or external services may persist. Repeated search despite a confirmed callable interface weakens this diagnosis. Fewer searches accompanied by missing required tool work is not improvement.

<a id="definition"></a>

## Definition

In a deferred-tool system, discovery must connect a capability name to an invocation contract available to the receiving model and runtime. A partial handoff can advertise success while omitting the schema, registration, or supported invocation route. Rediscovery then returns the same reference without repairing the gap.

The problem is the discovery-to-invocation boundary. Repeated search is a clue, not proof that this boundary failed.

<a id="criteria"></a>

## Candidate criteria

<a id="criteria/promised-capability"></a>

### Discovery promises usable access

The adapter's contract says a successful discovery response makes the identified capability callable for the relevant turn.

<a id="criteria/missing-interface"></a>

### The invocation interface is missing

Inspection of registration and effective model input establishes that the required callable interface or supported route was not delivered despite a successful discovery response.

<a id="criteria/stalled-use"></a>

### The gap obstructs tool use

The agent needs that capability and enters repeated unsuccessful discovery cycles matching [doom looping](../symptoms/doom-looping.md), while those cycles leave the invocation gap unchanged.

Related symptom: [S002](../symptoms/doom-looping.md)

<a id="exclusions"></a>

## Exclusions

<a id="exclusions/reference-contract"></a>

### Reference contract

The service promises only a directory reference and supplies a working, documented next step to activate it.

<a id="exclusions/expected-delay"></a>

### Expected delay

Activation is asynchronous, still within its stated completion window, and the agent is following the supported wait or retry path.

<a id="differential"></a>

## Differential diagnosis

<a id="differential/callable-but-unused"></a>

### A callable tool is present but unused

<a id="differential/callable-but-unused/discriminator"></a>

#### Discriminator

Inspect the effective tool set for the actual decision turn. A transcript showing only a tool name cannot distinguish this explanation from a delivery gap.

<a id="differential/runtime-rejection"></a>

### Invocation reaches a runtime block

<a id="differential/runtime-rejection/discriminator"></a>

#### Discriminator

Look for an actual invocation and its authentication, permission, argument, or service error. Fixing discovery will not necessarily remove that block.

<a id="differential/context-loss"></a>

### A later transition removes a delivered interface

<a id="differential/context-loss/discriminator"></a>

#### Discriminator

Establish whether the interface was initially usable and then lost at a transition; that timing distinguishes initial delivery failure from [context handoff loss](context-handoff-loss.md).

<a id="investigation"></a>

## Investigation

Compare one failed discovery-to-use sequence with a successful sequence under the same adapter. Inspect the discovery result, registration state, receiving tool definitions, and invocation route. If those inputs are unavailable, retain this as an unconfirmed differential instead of diagnosing from repeated searches.

<a id="interventions"></a>

## Interventions

[Complete the discovery-to-invocation handoff](../interventions/complete-tool-discovery-handoff.md) repairs the interface used on future turns. A blanket search limit may hide the loop while leaving needed capabilities inaccessible.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This is an unvalidated scaffold. No public case in this entry establishes missing registration or model-visible delivery, and no intervention benefit is claimed. It makes no claim about a particular tool provider or harness.
