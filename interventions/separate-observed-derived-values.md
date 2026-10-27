---
id: I004
kind: intervention
summary: Change the collection and publication path so source observations, authorized
  calculations, and missing values remain distinguishable in future outputs.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Keep derived values out of source-only fields
xml_source: interventions/separate-observed-derived-values.xml
---

# Keep derived values out of source-only fields

Change the collection and publication path so source observations, authorized calculations, and missing values remain distinguishable in future outputs.

<a id="purpose"></a>

## Purpose

Prevent [inferred values presented as observations](../symptoms/inferred-values-as-observations.md) by preserving a field's meaning through collection and serialization. An accurate calculation can still violate a source-only contract.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/field-contract"></a>

### Field contract

The task or output format distinguishes source-reported fields from calculations, and that distinction is being lost or bypassed.

<a id="preconditions/editable-publisher"></a>

### Editable publisher

The maintainer can change the collector instructions, serializer, or publication template and its consumers without silently changing the agreed output contract.

<a id="procedure"></a>

## Procedure

<a id="procedure/separate-values"></a>

### Separate values

Update the reusable collector and serializer to keep an observed value tied to its source location. Permit calculations only in explicitly authorized derived fields, with their formula and inputs; preserve the contract's missing-value representation.

<a id="procedure/block-substitution"></a>

### Block substitution

Remove formula fallbacks and guessed defaults from source-only assignments. When the source lacks a value, publish the agreed missing marker rather than a computed substitute. If the current format cannot express the distinction, leave that field missing and report the limitation.

<a id="procedure/check-boundary"></a>

### Check boundary

Check the final publication path with one observed value, a genuine zero, a missing value, and an authorized calculation. Confirm that serialization and display retain each meaning; use the existing data model where it can express these distinctions.

<a id="procedure/review-publications"></a>

### Review publications

Review subsequent comparable outputs against available source evidence, including outputs that look complete and those with missing fields.

<a id="evaluation"></a>

## Evaluation

Predict fewer unsupported non-missing values in source-only fields, with genuine observations and permitted calculations preserved. Compare published values with accessible sources and inspect whether downstream consumers retain the distinction.

More missing values may reflect honest uncertainty, lost access, or a broken collector. Check useful data coverage and publication success alongside provenance accuracy. Correct source records with misleading rendered labels point to the publication layer; this change will not repair unrelated date filters or arithmetic errors.

<a id="risks-and-confounders"></a>

## Risks and confounders

Overstrict handling can discard valid observations, convert real zeros to missing values, or break consumers expecting a complete row. Source changes and inaccessible source pages limit retrospective assessment.

<a id="stop-and-rollback"></a>

## Stop and rollback

Repair or revert the faulty collector or serializer if valid data is lost or publication breaks. Preserve the observed-versus-derived distinction in a compatible output or an explicit limitation; do not reinstate silent fabrication as the fallback.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This proposed intervention has no established outcome here. It can be appropriate from an observed contract violation without a catalog diagnosis; the underlying cause may lie in instructions, extraction, serialization, or presentation.
