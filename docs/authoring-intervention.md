# Authoring intervention XML files

An intervention describes a concrete change someone can make to an agent or its environment. Lead with that change, then explain the relevant principles and how to evaluate it. The same action may help a task recover, test an explanation, or do both.

Use this discriminator throughout: after reading the procedure, does the reader know what to change, or do they still have to design an intervention themselves?

## Title and summary

Name the action and its target. The summary should say what changes, where, and under what circumstances. "Restore missing evidence to active context" identifies an action; "maintain good memory" leaves the action to the reader.

## Purpose and principles

Explain the intended effect and the working model that makes the action plausible. Include principles that help a reader apply this particular intervention correctly. For evidence restoration, the distinction between information stored somewhere and information actually supplied to the model matters.

Keep principles in the `purpose` section. They support the procedure; they should not substitute for it or imply that a proposed mechanism is established. A formal diagnosis need not be a prerequisite when the relevant conditions can be observed directly.

## Preconditions

State the circumstances, access, and capabilities required to carry out the action. Distinguish these from requirements for a stronger experiment. A replayable task may be necessary for a matched comparison without being necessary for a one-off repair.

Do not hide additional applicability requirements later in the evaluation section.

## Procedure

Write ordered, executable steps. Identify the actor or system component, the object changed, and when the change takes effect. Be independent of a particular harness where possible, but specify the behavior an implementation must achieve.

Include how to verify that the change reached its intended target. A saved memory file is not evidence that the model received its contents. If verification is unavailable, say what remains unknown and how that limits the assessment.

Keep experimental comparisons and repeated trials in `evaluation`, so someone applying the intervention once does not have to conduct a study first. Keep preparation proportional to the action. Specify when a temporary change should be removed or reconsidered.

## Evaluation

State the predicted observable effect, when to assess it, and what counts as useful progress. Measure correctness and task outcomes alongside the symptom; suppressing visible behavior can make the underlying problem worse.

Include an evaluation protocol specific to the intervention: what to compare, what needs to stay comparable, and which additional controls or repetitions would answer an unresolved question. Distinguish evaluation of one episode from evidence for a general policy.

Explain positive, negative, and inconclusive results. Separate failure to deliver the intervention from failure after confirmed delivery. A successful remedy need not uniquely identify the cause. Keep general experimental guidance here; each entry should supply the details needed for its own prediction and comparison.

## Risks, rollback, and evidence

Describe concrete ways the change could cause harm or confound interpretation. Specify when to stop, what to remove or restore, and which effects rollback cannot undo.

Keep `evidence-and-uncertainty` about inspected support for this intervention and its limits. Plausible principles and detailed protocols do not establish effectiveness. Clearly label invented examples and do not use them to promote evidence status.
