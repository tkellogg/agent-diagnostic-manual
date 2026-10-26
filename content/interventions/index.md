---
schema_version: 1
id: interventions
kind: guide
title: Interventions
summary: Conditional protocols for investigation and remediation, with evaluation and rollback.
status: draft
updated: "2026-10-26"
---
# Interventions

Interventions are independent entries. A diagnosis links to a protocol with an applicability condition, a role, and an evidence label. One protocol may eventually be relevant to several diagnoses.

- [I001 — Preserve task-relevant evidence](preserve-task-relevant-evidence.md): an unvalidated protocol for testing a suspected loss of evidence from active context.

An intervention can be both an investigation and a potential remedy. Success on the task does not by itself prove a mechanism. Read the [structure proposal](../structure.md#interventions-proposed-structure) before adding protocols.
