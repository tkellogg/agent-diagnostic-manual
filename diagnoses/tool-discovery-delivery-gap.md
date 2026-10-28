---
id: D002
kind: diagnosis
summary: Tool search says a tool is ready, but the agent lacks the definition or access
  needed to call it. Searching again gives the same unusable result.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
unit: configured-agent-system
title: Tool discovery reports unusable tools
xml_source: diagnoses/tool-discovery-delivery-gap.xml
---

# Tool discovery reports unusable tools

Tool search says a tool is ready, but the agent lacks the definition or access needed to call it. Searching again gives the same unusable result.

<a id="definition"></a>

## How this could happen

Some harnesses load tools only when an agent searches for them. A successful search should supply the tool’s arguments and a working way to call it. If the harness reports success before doing that, the agent can keep finding a tool it cannot use.

This is a possible harness fault. It belongs here because ADM examines the configured agent system, including its tools. Repeated searches alone do not show that the harness is faulty: the tool may be available and the agent may simply fail to call it.

<a id="relations"></a>

## Symptoms and predicted effects

- [S002 — Doom looping](../symptoms/doom-looping.md)

<a id="relations/I005"></a>
<a id="relations/I005/when"></a>

### Intervention: [I005 — Make discovered tools callable](../interventions/complete-tool-discovery-handoff.md)

**Use this when:** Tool search claims a tool is ready, but its definition or registration is missing.

<a id="relations/I005/predictions"></a>

#### What to expect if this explanation is right

- <a id="relations/I005/predictions/expected-improvement"></a>**Expected improvement:** Once search returns a callable tool, the agent should use it instead of searching for it again. If the tool is unavailable, an honest error should let the agent choose another route or report the blocker.

- <a id="relations/I005/predictions/still-necessary"></a>**Still necessary:** The agent should still respect tool permissions and report failed calls accurately. A callable tool may still fail because of bad arguments, expired credentials, or a service outage.

- <a id="relations/I005/predictions/reason-to-reconsider"></a>**A reason to reconsider:** If the tool is callable and the agent keeps searching, investigate its tool choice or instructions. Fewer searches count as improvement only if required work still gets done.

- <a id="relations/I005/predictions/possible-harm"></a>**Possible harm:** Making more tools callable without preserving their permission checks could enable actions the user did not authorize. Keep those checks in place when repairing delivery.

<a id="criteria"></a>

## What would support this explanation

<a id="criteria/promised-capability"></a>

### 1. Search promises a ready tool {#search-promises-a-ready-tool}

The harness documents or reports that a successful search makes this tool ready to call.

<a id="criteria/missing-interface"></a>

### 2. The tool cannot be called {#the-tool-cannot-be-called}

The tool’s arguments are missing from the model’s input, or the runtime has not registered the tool. Distinguish this from a tool call that reaches the service and returns an error.

<a id="criteria/stalled-use"></a>

### 3. The agent keeps searching for it {#the-agent-keeps-searching-for-it}

The agent needs the tool and repeats the same unsuccessful search cycle, matching [doom looping](../symptoms/doom-looping.md). Searching again does not fix the missing definition or registration.

- [S002 — Doom looping](../symptoms/doom-looping.md)

<a id="exclusions"></a>

## When this explanation may not fit

<a id="exclusions/reference-contract"></a>

### A listing is not a ready tool

A catalog may list an uninstalled tool and clearly say how to install it. Finding that listing is useful; it has not claimed that the tool is ready to call.

<a id="exclusions/expected-delay"></a>

### Loading is still in progress

A tool may take time to activate. A clear “still loading” result and a working way to wait are reasonable, provided the stated wait has not expired.

<a id="differential"></a>

## Other explanations to consider

<a id="differential/callable-but-unused"></a>

### The tool is ready, but the agent does not call it

<a id="differential/callable-but-unused/discriminator"></a>
Inspect the tool definitions supplied for that turn. If the tool and its arguments are available, look at tool-selection instructions instead of repairing registration.

<a id="differential/runtime-rejection"></a>

### The call reaches the tool and fails

<a id="differential/runtime-rejection/discriminator"></a>
An authentication, permission, argument, or service error shows that a call was attempted. Repair that failure; repeated discovery usually cannot help.

<a id="differential/later-loss"></a>

### The tool disappears after compaction

<a id="differential/later-loss/discriminator"></a>
Check whether the agent used the tool before compaction. If so, inspect whether the harness restores the tool definitions afterward; the initial search may have worked.

<a id="investigation"></a>

## Where to look next

Follow one tool from its search result to the next model request and attempted call. This distinguishes a missing tool definition from an available tool that the agent ignores; the two need different repairs.
