---
name: agent-diagnostics
description: Investigate failures in configured AI agents using the Agent Diagnostic Manual (ADM). Use when reviewing agent traces, assessing symptoms and candidate diagnoses, comparing competing explanations, planning interventions, or reading and contributing ADM XML entries.
---

# Agent diagnostics

Use ADM to improve the configured agent system: its models, skills, prompts, tools, memory, and orchestration. Treat completed incidents as evidence, symptoms as observations, diagnoses as provisional explanations, and interventions as lasting changes for future work. Do not infer a mechanism merely from a symptom or an artifact defect.

## Locate the corpus

Use the user's ADM checkout or supplied entry files when provided. When this skill lives in the ADM repository, find the corpus at `../../entries/` relative to this file. Otherwise, download `https://diag.timkellogg.me/catalog.json` once at the start of an assessment. The catalog contains entry metadata, complete structured content, scoped addresses, and relationships. Use a JSON reader to list entries and extract relevant content instead of loading the whole corpus into the model's context. No repository clone or site build is needed for online use.

Keep that catalog snapshot throughout the assessment; record its retrieval time and SHA-256 hash with the report. Fetch a fresh snapshot for a new assessment. For human reading, resolve an entry's `url` against `https://diag.timkellogg.me/` and use the adjacent `.md` or `.xml` variant as needed. Those live pages may have changed since the saved snapshot. If fetching fails, use a clearly dated supplied or cached copy, or ask for one; do not invent entries or describe an old copy as current.

Read XML directly when working with entry files; no build or LLM-specific service is required. Read [the format reference](references/format.md) for parsing, addressing, or authoring rules, including the supported catalog version. In a checkout, run `uv run --script examples/query_manual.py` to enumerate entries, or `uv run --script tools/build.py` to generate HTML, Markdown reading copies, and a JSON catalog. Run these commands from the checkout root. Treat generated copies as views, not editing sources.

Record the corpus revision used for an assessment. Use entry IDs and scoped addresses to cite definitions; keep trace citations separate.

## Investigate the system through incidents

1. Establish the incident's task and success criteria. Record the model, harness, tools, instructions, context policy, environment, and relevant versions. The incident may be over; do not assume its task must be replayed or finished.
2. Read relevant symptom entries. Compare actual calls, returned content, source versions, and model-visible inputs against the observations and benign lookalikes. An explanation is not automatically benign: a faulty instruction can cause a system-level symptom. Accept reasoned qualitative comparisons when the definition allows them; do not demand a benchmark or fixed sample size. Use `what-to-record` to identify useful evidence, not a mandatory intake checklist. Treat agent self-explanations as claims to check.
3. Find diagnoses whose `relations/symptom-ref` references those symptoms. Read the whole candidate entry, including exclusions and differential alternatives. Do not force a catalog match if no entry fits.
4. Assess each criterion as supported, contradicted, or unknown, with trace citations. For `operator="all"`, all criteria must be supported to assign the candidate label. A contradicted required criterion means the definition does not fit; an unknown one leaves insufficient evidence. Symptom references alone do not establish a criterion.
5. Compare plausible alternatives using their discriminators. Describe how the system should work, what fails, and how that would produce the symptoms. Prefer existing evidence that separates explanations; allow interacting causes and keep unavailable input evidence unknown.
6. Report the observed pattern, criterion assessments, exclusions and alternatives, missing evidence, and the next useful action. Separate confidence in this case from the entry's evidence status. Describe concrete consequences; do not invent severity grades.

Keep the report proportionate to the evidence. Cite addresses such as `D001#criteria/delivery-loss` alongside trace event numbers or timestamps so another reviewer can reproduce the assessment.

## Use an intervention

Read the diagnosis's `intervention-ref/when` and `predictions`, then the intervention's purpose, preconditions, ordered procedure, evaluation, confounders, and rollback. An observed problem may justify an intervention without an established catalog diagnosis.

Choose a concrete change to the recurring system behavior. A one-time reminder or a more cautious report does not by itself repair the factory. Keep the change and its evaluation proportional to the problem; do not add instrumentation or repeated trials by default.

Before applying the change, adapt the predictions to this configuration: what should improve, what should remain intact, what could newly appear, and what would weaken the explanation. Agree with the user on a dated check-in, who will review the evidence, and a reminder or job. Use existing records or agreed occasional capture rather than checking every turn. Confirm the changed behavior reaches future agents and observe ordinary work; use replay or ablation only when its expected value justifies its cost.

Evaluate correctness and completion alongside symptom frequency and cost. Distinguish a newly exposed defect from harm introduced by the intervention. Separately decide whether the change helps and whether its predicted pattern supports the diagnosis; improvement alone does not uniquely establish the mechanism.

Execute changes only within the user's authorized scope. Apply the protocol's stop and rollback conditions. Do not interpret a request for diagnosis as authorization to alter a production agent.

## Record evidence and improve entries

Preserve task/configuration details, trace references and access limits, criterion assessments, competing explanations, and any intervention's baseline, prediction, actual outcome, and confounders. Include a healthy comparison and reviewer disagreements when available. Keep sensitive raw traces in an appropriate access-controlled location.

Keep synthetic examples separate from observed cases. Interpret evidence labels as follows:

- `unvalidated`: no inspected empirical support is recorded for the claim.
- `case-supported`: linked, inspectable empirical evidence supports the specific claim.
- `replicated`: linked repetitions support the claim under stated conditions and limits.

Do not promote evidence labels based on plausible examples, successful parsing, or reviewer agreement alone. Distinguish reliability (reviewers agree), validity (the distinction is supported), and utility (it helps decisions).

When asked to contribute, distinguish a provisional scaffold from an evidence-supported entry. Edit canonical XML, preserve stable IDs, and validate the schema and cross-references. Keep private incidents out of public entries unless their publication is authorized. Use the checkout's `docs/` authoring guides, diagnostic process, and observation methods when available; do not introduce a case schema or severity scale without a concrete need.
