# Diagnosing and improving an agent system

ADM's diagnostic process aims to improve the software factory: the configured system of models, skills, prompts, tools, memory, and orchestration that produces agent behavior. A completed incident supplies evidence about that system. An intervention changes it so future incidents unfold differently.

A human or a separate maintenance agent can use this process. It does not require the agent doing the work to diagnose itself. This guide describes the method independently of any particular skill, harness, or XML representation.

## The working model

A symptom describes observable behavior. A working diagnosis explains how the system may be producing or maintaining that behavior. Differential diagnosis compares plausible explanations and identifies evidence that would distinguish them. A useful model also suggests other symptoms to look for, including ones the original report did not mention.

The model need not identify one ultimate root cause. Several conditions can interact. A descriptive label can help organize cases without establishing their mechanism; keep the proposed explanation explicit and provisional. If no catalog diagnosis fits, record a working hypothesis rather than forcing a match.

An intervention makes a concrete, lasting change based on that explanation. Its prediction connects the change to future behavior:

> Given this explanation of the system, making this change should produce this particular pattern of future behavior.

That pattern may include symptoms improving, behaviors remaining unchanged, or new problems appearing. Predictions make the explanation answerable to subsequent observations.

## The flow

1. **Review incidents.** Establish what happened from transcripts, artifacts, logs, and the instructions actually in force. Record consequences, relevant configuration versions, and missing evidence. Use symptom definitions and benign lookalikes to separate the reported behavior from acceptable behavior. The original incident may be over; there is no requirement to reproduce or finish it.

2. **Build an explanation and compare alternatives.** Describe how the relevant part of the system should operate, what appears to be malfunctioning, and how that would produce the symptoms. Identify observations each alternative would predict. Treat the agent's explanation of its own behavior as a claim to check.

3. **Choose a system change.** Specify the skill, prompt, context policy, tool interface, or harness behavior to modify. Explain why this addresses the suspected problem, what implementation costs it incurs, and what other behavior it could affect. A maintainer should be able to enact the change without inventing the intervention. A one-time rescue of a session does not by itself improve the factory.

4. **Write predictions before applying it.** State which symptoms should change, under what circumstances, which behaviors should remain intact, and any new symptoms the model predicts. Include results that would favor a competing explanation or weaken the current one. Choose a review point based on future opportunities for the behavior to occur, and specify when to stop or revert.

5. **Observe subsequent work.** Confirm that the intended configuration change reached the relevant agents. Collect outcomes as ordinary work proceeds, including successful episodes and opportunities where the symptom did not occur. Track correctness and consequences alongside symptom frequency. Note changes in task mix, models, tools, and environment that complicate the comparison. Replay and ablation are optional investigations when their expected value justifies their cost.

6. **Revise the model and the change.** Compare the observed pattern with the recorded predictions. Decide whether to retain, refine, extend, or revert the intervention. Separately update confidence in the explanation. An intervention may help for a different reason than expected; a supported explanation may still lead to an intervention whose side effects outweigh its benefits. Use the revised model to choose any next intervention.

## Worked example: redundant authorization requests

This hypothetical example illustrates the flow; it does not establish a diagnosis or remedy.

Completed incidents show workers asking for permission immediately after handoffs, even though the user already authorized the work. The maintenance agent suspects that handoffs preserve the task but omit its authorization. A competing explanation is that a standing instruction requires fresh consent for each action.

The proposed intervention changes the handoff protocol to include the original authorization, its scope, and the conditions requiring renewed consent. It preserves existing consent requirements. The maintainer records these predictions before changing the protocol:

| Future observation | Expected interpretation |
| --- | --- |
| Redundant requests decline after handoffs. | Supports the authorization-loss explanation, subject to other changes in the system and work. |
| Requests for genuinely expanded scope remain. | The intervention preserved the intended authorization boundary. |
| Redundant requests persist despite the receiving agent having the authorization. | Weakens missing authorization as the explanation; inspect the standing instructions and other alternatives. |
| Agents begin acting beyond the original permission. | The handoff may be losing scope restrictions or presenting permission too broadly. Revert or correct the change even if redundant requests declined. |

The maintainer reviews subsequent tasks that actually include handoffs and authorization decisions. A period with no such opportunities supplies little evidence. No replay of the original incidents is needed.

## What to retain

Keep a proportionate record of the incident evidence, competing explanations, exact system change and version, predictions made beforehand, observation period and opportunities, actual outcomes, confounders, and the decision about what to do next. This can be ordinary prose with links to artifacts; the process does not require a new case schema or a formal study.

A prediction coming true supports an explanation most strongly when competing explanations would have predicted something different. General improvement alone is less discriminating. Repeated useful outcomes may justify retaining a change while its mechanism remains uncertain. Case-level confidence and the evidence status of a reusable ADM entry are separate judgments.

## Where the knowledge belongs

Symptoms provide shared descriptions of behavior. Diagnoses organize reusable explanations and their alternatives. Interventions specify changes to the system. The prediction depends on the diagnosis, the intervention, and the configuration where it is applied; it should be stated for that combination rather than treated as an unconditional promise of the intervention.

This guide is the shared methodology. The [diagnostic skill](../skills/agent-diagnostics/SKILL.md) is an agent-facing aid for working with ADM files. The [symptom authoring guide](authoring-symptom.md) and [intervention authoring guide](authoring-intervention.md) describe how to contribute entries; the [format reference](../skills/agent-diagnostics/references/format.md) describes their representation.
