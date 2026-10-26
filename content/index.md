---
schema_version: 1
id: manual
kind: guide
title: Agent Diagnostic Manual
summary: A field guide to recognizing, distinguishing, and investigating failures in configured agents.
status: draft
updated: "2026-10-26"
---
# Agent Diagnostic Manual

**ASM · Working draft · One symptom, one candidate diagnosis.**

Start with what happened. Distinguish plausible explanations. Test an intervention. Keep the evidence and the uncertainty attached to the claim.

## Explore the manual

| Start here | What you will find |
| --- | --- |
| [Symptoms](symptoms/index.md) | Observable features that can occur in healthy or failing runs. |
| [Diagnoses](diagnoses/index.md) | Proposed patterns with criteria, exclusions, and differential reasoning. |
| [Interventions](interventions/index.md) | Conditional, testable protocols with tradeoffs and rollback. |
| [Evidence and cases](cases/index.md) | The evidence policy; no empirical cases have been added yet. |

## Read the first example

An agent keeps looking up the same information. Is it checking something important, recovering from missing context, or spending its budget without advancing the task?

Follow [Repeated retrieval](symptoms/repeated-retrieval.md) to [Unproductive repeated retrieval](diagnoses/unproductive-repeated-retrieval.md), then inspect [Preserve task-relevant evidence](interventions/preserve-task-relevant-evidence.md). The intervention applies only when the evidence-availability hypothesis is plausible.

## How this is organized

Read the [XML format contract](format.md) and [Structure and design decisions](structure.md) for the source format and relationship model, and [Diagnostic foundations](foundations.md) for the distinctions behind it.

This manual describes operational behavior. It does not attribute human psychiatric conditions or subjective experiences to agents. The initial unit of assessment is an **episode of a configured system**: model, instructions, memory, tools, harness, and environment.

Severity scoring is deferred. Entry maturity and evidence strength are separate from severity and from confidence about any individual case.
