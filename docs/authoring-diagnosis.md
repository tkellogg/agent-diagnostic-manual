# Authoring diagnosis XML files

A diagnosis is a reusable working explanation of how the configured agent system produces or maintains a problem. It should help a maintainer choose a system change and predict what future behavior would support or weaken that explanation. A more severe restatement of a symptom does not supply that model.

## Scope and definition

Treat the configured system as the patient and completed episodes as evidence. In `definition`, explain how the relevant part should work, what goes wrong, and how that produces the observed behavior. Name the boundary or process involved without assuming hidden thoughts or intent.

A bug in generated code establishes an artifact defect. It becomes evidence for an ADM diagnosis when there is a supported connection to how the agent system generates, checks, or uses that code. Defects in an agent's own harness can be part of the pathology, but a catalog entry should describe a reusable failure mechanism rather than give every isolated bug a diagnosis.

Keep plausible models provisional. A draft can name evidence that would be needed without claiming that an observed case already supplies it. If there is only a behavioral pattern, contribute a symptom or leave a working hypothesis in the case notes.

## Criteria and differential

Use criteria to state the observations needed to support the explanation in a particular configuration. Put the mechanism's distinguishing evidence here; do not make a symptom reference stand in for causal evidence. `operator="all"` requires support for every criterion. An inaccessible model input remains unknown, not evidence of omission.

Use exclusions for circumstances that rule this diagnosis out. Use differential alternatives for competing explanations and specify the observation that separates them. Several mechanisms can coexist. A failed delivery can exclude a symptom that requires prior usable delivery without excluding another symptom such as doom looping.

Do not redefine a linked symptom inside a diagnosis. An explanation is not automatically benign: complying with a faulty checking rule can produce a real system-level symptom. Conversely, a slow but justified check is not pathological merely because the user dislikes its cost. Assess policy changes at the maintainer level; recognizing a bad rule does not authorize a worker to bypass it.

## Interventions and predictions

Link a concrete intervention only when its prerequisites make sense for this explanation. Each `intervention-ref` has `when` and a prose `predictions` block. Describe expected improvement, behavior that should remain intact, and an outcome that would weaken the explanation or favor an alternative. Include possible harms or newly visible problems when the model predicts them.

The prediction belongs to this diagnosis–intervention combination. The maintainer adapts it to the actual configuration and chooses a proportionate review point before applying the change. Do not encode a universal sample size or turn predictions into a causal programming language.

Keep `investigation` focused on the evidence needed to distinguish explanations. Prefer existing traces and ordinary future work; repeated replay, independent reviewers, or new instrumentation should answer an actual unresolved question, not become entry boilerplate.

## Evidence and uncertainty

Separate what was observed, what mechanism it supports, whether a proposed repair helped, and how widely the result might apply. A source-backed artifact discrepancy does not automatically validate its proposed cause or remedy. The root evidence label is a coarse summary; use `evidence-and-uncertainty` to state the supported claims and limits precisely.

Keep private cases and excerpts in their authorized location. Public entries can present general hypotheses and clearly synthetic examples without publishing the motivating incident or implying publicly inspectable support that is not supplied.

Use the [diagnostic process](diagnostic-process.md) for the overall flow and the [format reference](../skills/agent-diagnostics/references/format.md) for XML structure and scoped addresses.
