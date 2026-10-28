# Authoring intervention XML files

An intervention describes a concrete, lasting change to the configured agent system. Lead with the skill, prompt, tool, or harness behavior to change, then explain the relevant principles and how to evaluate future work. A useful repair can also test an explanation.

Use this discriminator throughout: after reading the procedure, does the reader know what to change, or do they still have to design an intervention themselves?

## Principle: Fix the system
The goal of this entire diagnostic process isn't to unstick a single agent session, it's to fix the system in which that agent session runs.

When a human is operating an agent, they have a task to be done. This isn't like an RL environment where you can sit there and do ablations until you see all angles of a symptom. No, the environment isn't deterministic at all. Once you perform an intervention, there's no easy control group or baseline to compare it against. It's the real world, things are constantly changing and messy.

This intervention should be phrased in such a way that *future* incidents can be observed, and the impacts of the intervention can be discussed. Typically, we'll make a prediction about how this intervention will be used to support a differential diagnosis.

Write these interventions with this in mind.

See [Diagnosing and improving an agent system](diagnostic-process.md) for the full flow from past incidents through competing explanations, a system change, predictions, and observations of future work. The method applies to human maintainers and independent tools as well as the diagnostic skill.

## Title and summary

Name the action and its target. The summary should say what changes, where, and under what circumstances. "Fix compaction so important information survives" names the mechanism to change; "maintain good memory" leaves the action to the reader.

## Purpose and principles

Explain the intended effect and the working model that makes the action plausible. Include principles that help a reader apply this particular intervention correctly. For compaction, distinguish a full transcript saved for review from the information the working agent retains.

Keep principles in the `purpose` section. They support the procedure; they should not substitute for it or imply that a proposed mechanism is established. A formal diagnosis need not be a prerequisite when the relevant conditions can be observed directly.

## Preconditions

State the circumstances, access, and capabilities required to change the system. Do not require a replayable task or a controlled study merely to apply a plausible repair.

Link relevant symptoms or diagnoses when they help the reader recognize a suitable situation; a confirmed diagnosis need not be required. Do not hide additional applicability requirements later in the evaluation section.

## Procedure

Write ordered, executable steps. Identify the actor or system component, the object changed, and when the change takes effect. Be independent of a particular harness where possible, but specify the behavior an implementation must achieve.

Include how to verify that the change reached its intended target. A saved memory file is not evidence that the model received its contents. If verification is unavailable, say what remains unknown and how that limits the assessment.

Start by inspecting the system that already exists. Repair may mean deleting and consolidating instructions with the user, or fixing how existing tests cover real use. Do not assume every problem needs another rule or test.

Make the repair and its observation practical. Reuse existing logs; if needed evidence would otherwise disappear, specify a small capture hook, where its output goes, and the user’s agreement. Prefer occasional background checks to extra work on every agent turn.

## Harness-specific instructions

Use optional `harness-notes` after `procedure` for the actual settings, files, hooks, and commands a reader can use. Each `harness` has a short stable `id` and a plain-text `title`, followed by prose blocks. Reuse the same ID across entries (`claude-code`, `codex`, `opencode`, or `custom`) so the site's remembered selector works across the manual. Other harness IDs are allowed.

Keep the shared procedure useful on its own. Harness notes explain how to carry it out; they must not hide a precondition, risk, or required step that applies to everyone. Cite official documentation beside product claims, state version boundaries, and verify the relevant route rather than assuming a general instruction file controls compaction. The entry's update date records when its guidance was last revised. Distinguish documented controls from an ADM proposal for using them.

The HTML selector filters only these notes. Markdown, XML, search indexing, printing, and the page without JavaScript retain all variants. Do not duplicate whole interventions for each harness or promise a customization point you have not verified.

## Evaluation

State the predicted observable effect, when to assess it, and what counts as useful progress. Measure correctness and task outcomes alongside the symptom; suppressing visible behavior can make the underlying problem worse.

Agree with the user on how ordinary future work will be observed, who will review it, and a check-in date. Arrange a reminder or scheduled job so follow-up actually happens. A target number of tasks can guide the date; explain what to do if too few relevant tasks occur. Preserve correctness, completion, and required coverage alongside symptom reduction. Replay, ablation, or additional controls are optional investigations when they answer an unresolved question worth their cost.

A frozen-input comparison can be useful when the component can be run separately, as with some compactors. Preserve the original input, change one relevant instruction, and compare a few candidates without replaying the task's external actions. A fixed transcript does not make model output deterministic. Check the chosen change on separate examples and future work; do not turn this optional shortcut into a mandatory ablation study.

Explain positive, negative, and inconclusive results. Distinguish a change that was never active from one that was active but did not help. A successful remedy need not uniquely identify the cause. Put diagnosis-dependent predictions in that diagnosis's `intervention-ref/predictions`; use the intervention's evaluation to explain what to observe and how to interpret its limits. More careful wording alone is not evidence that the system produces better artifacts.

## Risks, rollback, and evidence

Describe concrete ways the change could cause harm or confound interpretation. Specify when to stop, what to remove or restore, and which effects rollback cannot undo.

Use lists for concrete risks and rollback actions. Put sources and important limitations beside the claims they qualify; the root evidence label already identifies an unvalidated proposal. A detailed procedure does not establish that the remedy works.

Write the procedure so the reader knows what to edit, delete, preserve, or inspect. Replace invented abstractions with the actual object, such as “the compaction prompt,” “the loaded tool definition,” or “the CI job.”
