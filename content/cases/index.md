---
schema_version: 1
id: cases
kind: guide
title: Evidence and cases
summary: No empirical cases yet; keep observations, hypotheses, and outcomes distinguishable.
status: draft
updated: "2026-10-26"
---
# Evidence and cases

**No empirical cases are included yet.** Examples elsewhere in the manual are explicitly synthetic. They do not count as validation or measured intervention outcomes.

## First case record

When an actual trace is available, preserve:

- Task and success criteria; model and harness versions; relevant tools, instructions, memory policy, and environment.
- Trace reference and access constraints; calls, results, source versions, and relevant model-visible inputs.
- Observed symptoms, candidate criteria assessment, missing evidence, and alternative explanations.
- Confidence in this case assessment, recorded separately from confidence in the category itself.
- Any intervention, prerequisites, baseline/comparison conditions, outcomes, confounders, and rollback.
- A healthy comparison where possible; reviewer disagreements and negative results.

Keep sensitive raw traces in an appropriate access-controlled location. A record can link to them and describe their access limitations. Review before including any source material in the repository.

## Evidence labels

`unvalidated` means there is no inspected empirical support recorded here. `case-supported` requires linked, inspectable empirical evidence for the specific claim. `replicated` requires linked repetitions with stated conditions and limits. Neither label implies a unique mechanism or universal effectiveness.

The current metadata schema cannot verify empirical truth. Evidence labels require human review and traceable records. The case file schema will be designed around the first actual case rather than guessed now.

## Next contribution

Use one failing episode and one similar healthy episode to assess the existing [diagnosis](../diagnoses/unproductive-repeated-retrieval.md). Improve that entry before expanding the taxonomy. Severity remains deferred.
