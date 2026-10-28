---
id: S014
kind: symptom
summary: An output presents a calculated, estimated, or defaulted value as though
  it were directly reported by the source.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Inferred values presented as observations
xml_source: symptoms/inferred-values-as-observations.xml
---

# Inferred values presented as observations

An output presents a calculated, estimated, or defaulted value as though it were directly reported by the source.

<a id="observations"></a>

## Observations

<a id="observations/unsupported-value"></a>

### Unsupported value

At least one output value is presented as source-reported, through its label or the applicable field contract, but the trace or transformation shows it was calculated, estimated, or defaulted without a matching source observation. The output does not disclose that substitution.

<a id="how-to-recognize-it"></a>

## How to recognize it

Trace a published source-only value back through the source, extraction result, and any calculation or default. If the source cannot be inspected and there is no evidence of substitution, leave the case uncertain.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/labeled-derivation"></a>

### Labeled derivation

An authorized calculated field is labeled as derived and identifies its formula or basis. It lacks the undisclosed substitution in [unsupported value](inferred-values-as-observations.md#observations/unsupported-value).

<a id="benign-lookalikes/representation-change"></a>

### Representation change

Converting a displayed quantity into the agreed units or numeric representation preserves its meaning and precision. It does not supply an unobserved quantity as required by [unsupported value](inferred-values-as-observations.md#observations/unsupported-value).

<a id="benign-lookalikes/explicit-missing"></a>

### Explicit missing

The output uses the agreed missing marker, distinct from a source-reported zero. No substituted observation is claimed under [unsupported value](inferred-values-as-observations.md#observations/unsupported-value).

<a id="what-to-record"></a>

## What to record

Record the field contract, source location and capture time, observed source content, transformation or default, publication format, and final label. Preserve the configuration and artifact versions, source-access limits, and any authorization to calculate. Count affected fields against comparable field decisions, including correct zeros, missing values, and disclosed calculations. Record downstream decisions, correction effort, and useful coverage rather than inferring harm from a discrepancy alone.

<a id="examples"></a>

## Examples

<a id="examples/computed-total"></a>

### Computed total

<span class="adm-example-kind">Synthetic example</span>

A collector must copy a supplier's quoted total, leaving it missing when absent. For one quote it multiplies quantity by unit price and fills the source-only total. The transformation exposes the substitution; a reviewer spends six minutes correcting the export because the unobserved total might exclude fees.

<a id="examples/missing-as-zero"></a>

### Missing as zero

<span class="adm-example-kind">Synthetic example</span>

A survey extractor converts three unanswered counts into zeros with a default-value expression. Comparing the form with the export reveals three unobserved values presented as responses, and the analyst must regenerate the summary before using it.

<a id="examples/authorized-estimate"></a>

### Authorized estimate

<span class="adm-example-kind">Synthetic example</span>

The user requests an estimated total from observed quantity and unit price. The output labels one calculated estimate and leaves the supplier's quoted-total field missing. The derivation and its source inputs are explicit, so no source observation is substituted.
