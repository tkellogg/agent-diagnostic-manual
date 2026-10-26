---
schema_version: 1
id: D001
kind: diagnosis
title: Unproductive repeated retrieval
summary: Repeated retrieval adds little relevant information while interfering with task progress or consuming resources without a justified verification purpose.
status: draft
evidence: unvalidated
updated: "2026-10-26"
tags: [retrieval, progress, context]
unit: configured-agent-episode
diagnostic_level: descriptive
symptoms: [S001]
interventions:
  - id: I001
    role: both
    when: Necessary evidence appears to be lost from the active context; preserving it is feasible without changing source freshness requirements.
    evidence: unvalidated
---
# Unproductive repeated retrieval

## Definition

A candidate descriptive diagnosis for an episode in which [repeated retrieval](../symptoms/repeated-retrieval.md) contributes little additional task-relevant information and interferes with progress or spends resources without a justified verification purpose.

The assessed system includes model, harness, tools, memory, instructions, and environment. The diagnosis does not by itself attribute failure to any one component. It also does not claim a human-like compulsion, anxiety, or subjective experience.

## Candidate criteria

For this working definition, **all A–D must be supported**. If the trace cannot establish one, record “insufficient evidence” for the case rather than forcing a label.

- **A — Recurrence:** the episode contains repeated retrieval of substantially the same information, established by purpose and returned content rather than tool-name counts alone.
- **B — Low additional value:** the repeated calls add little information relevant to the task, and an independent review cannot identify a justified fresh-verification purpose.
- **C — Functional consequence:** the trace shows work displaced or stalled, a budget consumed without corresponding benefit, or another concrete consequence for the task. State the consequence; no severity grade is assigned.
- **D — Alternative assessment:** the exclusions below have been examined and do not adequately account for the observed pattern as useful behavior or ordinary recovery from a delivery failure.

No fixed number of calls, duration, or cost threshold is established. These criteria need testing for reviewer agreement and useful discrimination.

## Exclusions

Do not assign this candidate diagnosis solely because the same file or endpoint was accessed repeatedly. Exclude useful retrieval of changed content, different needed content, justified freshness checks, and ordinary recovery when the tool never delivered a usable result.

A repeatedly failing tool may itself deserve investigation, but it is not evidence that adequate evidence was retrieved and then reused poorly.

A mandatory verification instruction can explain repetition. If the checks are appropriate to the task, exclude the diagnosis. If a rule forces demonstrably wasteful repetition, the system-level pattern may still fit; record the rule as a suspected cause and avoid blaming model behavior in isolation.

## Differential diagnosis

These are competing explanations to investigate, not additional ASM diagnoses.

| Explanation | Discriminating observation or comparison |
| --- | --- |
| Useful refresh or different information need | Compare source versions, requested ranges, decision purpose, and information gained. |
| Failed or truncated delivery | Inspect the exact result supplied to the model; a backend success response alone is insufficient. |
| Loss from active context | Inspect pre-call inputs and compaction boundaries; assess whether needed evidence is missing. |
| Instructions demand another check | Identify the operative rule and its scope; compare a controlled run with that rule clarified where legitimate. |
| Repetition despite adequate visible evidence | Verify evidence remains available and no new check is needed; inspect why an available next step was not taken without treating self-report as ground truth. |

Causes can interact: repeated retrieval increases context pressure; compaction removes evidence; the agent retrieves again. Record the sequence instead of insisting on one exclusive explanation.

## Investigation

1. Preserve the task, ordered trace, configuration, and the exact context supplied at relevant decision points where accessible.
2. Annotate each retrieval with information gained and the next task action it enabled or displaced. Record uncertainty in these judgments.
3. Have a second reviewer assess the criteria without seeing the first review. Disagreements identify weak boundaries; agreement alone does not validate the category.
4. Select one hypothesis and a comparison that can distinguish it from an alternative. If context loss is plausible, consider [preserving task-relevant evidence](../interventions/preserve-task-relevant-evidence.md).
5. Evaluate completion and correctness as well as retrieval count and cost. Repeat trials as feasible and state model, task, and harness limits.

## Interventions

[I001 — Preserve task-relevant evidence](../interventions/preserve-task-relevant-evidence.md) is an experimental option when required evidence appears to be disappearing from the active context. It is not a general prescription for every case of D001.

If evidence was never delivered, repair delivery first. If a rule forces redundant checks, investigate the rule. These are differential-directed next steps, not additional intervention entries or proven remedies.

Do not implement “never read twice” as a treatment. It can hide the symptom while increasing factual errors or skipping legitimate checks.

## Evidence and uncertainty

**Category status: unvalidated.** No real trace has been adjudicated and no intervention outcome is claimed in this repository. The criteria and label are proposals.

Open questions include whether low information gain can be rated consistently, how to distinguish valuable verification from waste, and whether this category predicts useful interventions across different harnesses.

The next evidence should include one inspectable failing episode and a closely matched healthy comparison. A positive result under one configuration would not establish a universal cause or remedy. See the [evidence policy](../cases/index.md).
