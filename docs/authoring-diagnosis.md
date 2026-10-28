# Authoring diagnosis XML files

A diagnosis is a working explanation of how the configured agent system produces a problem. It earns a place in ADM when it helps choose a repair and predict what that repair will change. Naming an unpleasant behavior again does not provide that explanation.

## Start with the model

In `definition`, explain how the relevant part should work, what goes wrong, and how that produces the symptoms. Use familiar objects and actions: “the compaction summary drops permission” is clearer than “authority fails to survive the transition.” A reader should understand the proposed failure before being asked to inspect evidence for it.

The system includes the model, prompts, skills, tools, harness, and working repository. A harness fault can therefore be relevant. A bug in generated code is not automatically an agent diagnosis: explain how the recurring generation, testing, or completion process produces or misses it. Do not give every isolated bug a catalog entry.

Use a title specific enough to identify the proposed failure. “Tool discovery underperformance” could mean poor search results, slow search, unavailable tools, or bad tool choice; an entry about missing tool definitions should say so.

## Put predictions near the explanation

In `relations`, link the symptoms the model could explain and the interventions that plausibly address it. Each `intervention-ref` contains `when` and `predictions`. The predictions belong to the diagnosis **and** the intervention, applied to a particular configuration; a symptom link alone does not predict improvement.

`predictions` requires these four singleton sections, in order. Each contains prose blocks and needs no ID:

| XML field | Question it answers |
| --- | --- |
| `expected-improvement` | What should improve if this explanation and repair are right? |
| `still-necessary` | What useful behavior or constraint must survive the change? |
| `reason-to-reconsider` | What result would weaken this explanation or favor another one? |
| `possible-harm` | What new problem might the change cause? |

The renderer supplies the labels; do not repeat them in the prose. Name a plausible harm rather than inventing one to fill the field. If none is identified, say so and explain the limit of that judgment. Keep predictions concrete. “After compaction, the agent should stop asking again for saved permission” is more useful than “continuity should improve.” Predict ordinary future behavior; do not make an ablation study the price of admission.

## Evidence for this explanation

`criteria` states what would support the proposed cause in a particular case. It is separate from `definition`: the model explains; the criteria help decide whether it fits. For compaction loss, a useful chain is “the information mattered, compaction dropped it, and the omission explains the later mistake.” A repeated-read symptom alone does not establish that chain.

`operator="all"` means every listed criterion must have support before assigning the diagnosis. Missing evidence leaves a working hypothesis, not a reason to force the label or dismiss the complaint. A reviewer’s reasoned judgment can count as evidence; a numerical benchmark is not required.

Keep criteria few and specific to the explanation. Arrange them so the reader can follow the proposed cause through to its consequence. The generated headings are numbered in document order; the numbers guide reading, not a scoring system or a requirement to investigate in that order. Keep numbers out of XML titles and IDs. Do not copy the symptom definition or prescribe a large investigation in every criterion.

## Boundaries and other explanations

Use `exclusions` to describe situations where the explanation may not fit, including normal behavior that resembles the failure. Explain the boundary in ordinary language: compaction should forget obsolete information. Avoid treating every uncertainty as a firm exclusion.

Use `differential` for alternative causes that would lead to a different repair. Each `alternative` has a `discriminator`: what should the maintainer look at to tell them apart? For example, “the summary dropped permission” suggests fixing compaction; “the summary kept it but another rule demands fresh consent” suggests reviewing that rule. Omit alternatives that merely repeat a caveat without changing the next action.

Several causes can coexist. A faulty instruction can explain a symptom without making it benign, and a normal action by the model can reveal a problem in the configured system. Check linked symptoms for contradictory boundaries.

## Investigation, sources, and writing

Keep `investigation` to the next useful evidence to inspect. Shared recipes belong in [observation methods](observation-methods.md), not repeated paragraphs on every entry.

The root `status` and `evidence` attributes identify provisional entries. Put a specific source or limitation next to the claim it qualifies; do not add an “evidence and uncertainty” section that repeats the draft badge. Reports of a behavior do not establish its cause or the effectiveness of a remedy. Keep private cases private.

Use ordinary verbs, name the thing being changed, and avoid invented labels for familiar actions. Read the draft as someone who has not followed its author’s reasoning. If the reader must translate the prose before assessing the model, revise it.

See the [diagnostic process](diagnostic-process.md) and [format reference](../skills/agent-diagnostics/references/format.md) for the shared flow and XML details. These conventions remain a working draft; a useful example should shape the structure, not be stretched to fill it.
