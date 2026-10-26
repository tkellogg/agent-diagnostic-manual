---
id: D001
kind: diagnosis
summary: Repeated retrieval adds little relevant information while interfering with
  task progress or consuming resources without a justified verification purpose.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-26'
unit: configured-agent-episode
level: descriptive
title: Unproductive repeated retrieval
xml_source: diagnoses/unproductive-repeated-retrieval.xml
---

# Unproductive repeated retrieval

Repeated retrieval adds little relevant information while interfering with task progress or consuming resources without a justified verification purpose.

<a id="relations"></a>

## Relationships

Related symptom: [S001](../symptoms/repeated-retrieval.md)

<a id="relations/I001"></a>
<a id="relations/I001/when"></a>
[I001](../interventions/preserve-task-relevant-evidence.md)

**When:** Necessary evidence appears to be lost from the active context; preserving it is feasible without changing source freshness requirements.

<a id="definition"></a>

## Definition

A candidate descriptive diagnosis for an episode in which [repeated retrieval](../symptoms/repeated-retrieval.md) contributes little additional task-relevant information and interferes with progress or spends resources without a justified verification purpose.

The assessed system includes model, harness, tools, memory, instructions, and environment. The diagnosis does not by itself attribute failure to any one component. It also does not claim a human-like compulsion, anxiety, or subjective experience.

<a id="criteria"></a>

## Candidate criteria

<a id="criteria/recurrence"></a>

### Recurrence

The episode contains repeated retrieval of substantially the same information, established by purpose and returned content rather than tool-name counts alone.

Related symptom: [S001](../symptoms/repeated-retrieval.md)

<a id="criteria/low-value"></a>

### Low additional value

The repeated calls add little information relevant to the task, and an independent review cannot identify a justified fresh-verification purpose.

<a id="criteria/functional-consequence"></a>

### Functional consequence

The trace shows work displaced or stalled, a budget consumed without corresponding benefit, or another concrete consequence for the task. State the consequence; no severity grade is assigned.

<a id="criteria/alternative-assessment"></a>

### Alternative assessment

The exclusions below have been examined and do not adequately account for the observed pattern as useful behavior or ordinary recovery from a delivery failure.

<a id="exclusions"></a>

## Exclusions

<a id="exclusions/useful-retrieval"></a>

### Useful retrieval

Do not assign this candidate diagnosis solely because the same file or endpoint was accessed repeatedly. Exclude useful retrieval of changed content, different needed content, justified freshness checks, and ordinary recovery when the tool never delivered a usable result.

<a id="exclusions/failed-delivery"></a>

### Failed delivery

A repeatedly failing tool may itself deserve investigation, but it is not evidence that adequate evidence was retrieved and then reused poorly.

<a id="exclusions/required-checks"></a>

### Required checks

A mandatory verification instruction can explain repetition. If the checks are appropriate to the task, exclude the diagnosis. If a rule forces demonstrably wasteful repetition, the system-level pattern may still fit; record the rule as a suspected cause and avoid blaming model behavior in isolation.

<a id="differential"></a>

## Differential diagnosis

<a id="differential/useful-refresh"></a>

### Useful refresh or different information need

<a id="differential/useful-refresh/discriminator"></a>

#### Discriminator

Compare source versions, requested ranges, decision purpose, and information gained.

<a id="differential/failed-delivery"></a>

### Failed or truncated delivery

<a id="differential/failed-delivery/discriminator"></a>

#### Discriminator

Inspect the exact result supplied to the model; a backend success response alone is insufficient.

<a id="differential/context-loss"></a>

### Loss from active context

<a id="differential/context-loss/discriminator"></a>

#### Discriminator

Inspect pre-call inputs and compaction boundaries; assess whether needed evidence is missing.

<a id="differential/required-checks"></a>

### Instructions demand another check

<a id="differential/required-checks/discriminator"></a>

#### Discriminator

Identify the operative rule and its scope; compare a controlled run with that rule clarified where legitimate.

<a id="differential/available-evidence"></a>

### Repetition despite adequate visible evidence

<a id="differential/available-evidence/discriminator"></a>

#### Discriminator

Verify evidence remains available and no new check is needed; inspect why an available next step was not taken without treating self-report as ground truth.

<a id="investigation"></a>

## Investigation

1. Preserve the task, ordered trace, configuration, and the exact context supplied at relevant decision points where accessible.
2. Annotate each retrieval with information gained and the next task action it enabled or displaced. Record uncertainty in these judgments.
3. Have a second reviewer assess the criteria without seeing the first review. Disagreements identify weak boundaries; agreement alone does not validate the category.
4. Select one hypothesis and a comparison that can distinguish it from an alternative. If context loss is plausible, consider [preserving task-relevant evidence](../interventions/preserve-task-relevant-evidence.md).
5. Evaluate completion and correctness as well as retrieval count and cost. Repeat trials as feasible and state model, task, and harness limits.

<a id="interventions"></a>

## Interventions

[I001 — Preserve task-relevant evidence](../interventions/preserve-task-relevant-evidence.md) is an experimental option when required evidence appears to be disappearing from the active context. It is not a general prescription for every case of D001.

If evidence was never delivered, repair delivery first. If a rule forces redundant checks, investigate the rule. These are differential-directed next steps, not additional intervention entries or proven remedies.

Do not implement “never read twice” as a treatment. It can hide the symptom while increasing factual errors or skipping legitimate checks.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

**Category status: unvalidated.** No real trace has been adjudicated and no intervention outcome is claimed in this repository. The criteria and label are proposals.

Open questions include whether low information gain can be rated consistently, how to distinguish valuable verification from waste, and whether this category predicts useful interventions across different harnesses.

The next evidence should include one inspectable failing episode and a closely matched healthy comparison. A positive result under one configuration would not establish a universal cause or remedy.
