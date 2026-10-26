---
name: agent-diagnostics
description: Investigate failures in configured AI agents using the Agent Diagnostic Manual (ADM). Use when reviewing agent traces, assessing symptoms and candidate diagnoses, comparing competing explanations, planning interventions, or reading and contributing ADM XML entries.
---

# Agent diagnostics

Use ADM to organize evidence and decide what to investigate next. Treat a symptom as an observation, a diagnosis as a defined pattern, a mechanism as a causal hypothesis, and an intervention as a change to the system. Do not infer one merely from another.

## Locate the corpus

Use the user's ADM checkout or supplied entry files. When this skill lives in the ADM repository, find the corpus at `../../entries/` relative to this file. When installed separately, locate the checkout in the workspace or use a location supplied by the user. If none is available, ask for the corpus location; do not invent entries or assume access to the private repository.

Read XML directly; no build or LLM-specific service is required. Read [the format reference](references/format.md) for parsing, addressing, or authoring rules. In a checkout, use `examples/query_manual.py` to enumerate entries with standard-library Python, and `tools/build.py` to generate HTML, Markdown reading copies, and a JSON catalog. Run these commands from the checkout root. Treat generated copies as views, not editing sources.

Record the corpus revision used for an assessment. Use entry IDs and scoped addresses to cite definitions; keep trace citations separate.

## Investigate an episode

1. Establish the task and success criteria. Record the model, harness, tools, instructions, context policy, environment, and relevant versions. Assess the configured system and this episode, not the model in isolation.
2. Read relevant symptom entries. Compare actual calls, returned content, source versions, and model-visible inputs against the observations and benign lookalikes. Use each symptom's `what-to-record` section to identify missing evidence. Treat agent self-explanations as claims to check.
3. Find diagnoses whose `relations/symptom-ref` references those symptoms. Read the whole candidate entry, including exclusions and differential alternatives. Do not force a catalog match if no entry fits.
4. Assess each criterion as supported, contradicted, or unknown, with trace citations. For `operator="all"`, all criteria must be supported to assign the candidate label. A contradicted required criterion means the definition does not fit; an unknown one leaves insufficient evidence. Symptom references alone do not establish a criterion.
5. Compare plausible alternatives using their discriminators. Prefer the next observation or experiment that separates explanations. Allow interacting causes. A descriptive diagnosis does not establish a mechanism.
6. Report the observed pattern, criterion assessments, exclusions and alternatives, missing evidence, and the next useful action. Separate confidence in this case from the entry's evidence status. Describe concrete consequences; do not invent severity grades.

Keep the report proportionate to the evidence. Cite addresses such as `D001#criteria/recurrence` alongside trace event numbers or timestamps so another reviewer can reproduce the assessment.

## Use an intervention

Read the diagnosis's `intervention-ref/when` condition, then the referenced intervention's purpose, preconditions, ordered procedure, evaluation, confounders, and rollback instructions.

Distinguish observation, experiment, and remediation. Inspecting a trace can test an explanation without changing the agent. An intervention changes the system and may serve either investigation or remediation, or both.

For an experiment, state the suspected cause, change, predicted result, assessment point, comparison conditions, and what would weaken the hypothesis before running it. Check that the intended manipulation actually occurred. Evaluate task correctness and completion alongside cost and repeated behavior. Report negative results and confounders.

For example, if evidence loss is suspected, compare otherwise similar runs with and without preserved evidence. Predict fewer redundant retrievals after the relevant context transition without losing correctness. If evidence remains visible but repetition persists, weaken the simple evidence-loss hypothesis. If performance improves, report the benefit without claiming that the mechanism is uniquely established.

Execute changes only within the user's authorized scope. Apply the protocol's stop and rollback conditions. Do not interpret a request for diagnosis as authorization to alter a production agent.

## Record evidence and improve entries

Preserve task/configuration details, trace references and access limits, criterion assessments, competing explanations, and any intervention's baseline, prediction, actual outcome, and confounders. Include a healthy comparison and reviewer disagreements when available. Keep sensitive raw traces in an appropriate access-controlled location.

Keep synthetic examples separate from observed cases. Interpret evidence labels as follows:

- `unvalidated`: no inspected empirical support is recorded for the claim.
- `case-supported`: linked, inspectable empirical evidence supports the specific claim.
- `replicated`: linked repetitions support the claim under stated conditions and limits.

Do not promote evidence labels based on plausible examples, successful parsing, or reviewer agreement alone. Distinguish reliability (reviewers agree), validity (the distinction is supported), and utility (it helps decisions).

When asked to contribute, improve existing entries using actual evidence before expanding the taxonomy. Edit canonical XML, preserve stable IDs, and validate the schema and cross-references. Keep shared usage instructions here rather than repeating them inside every entry. Do not introduce a case schema or severity scale without a concrete need.
