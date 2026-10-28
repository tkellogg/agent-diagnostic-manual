---
id: I001
kind: intervention
summary: Change the compaction instructions or implementation to preserve information
  that later work needs. Where the harness allows it, compare changes on a saved conversation
  before evaluating ordinary future work.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Fix compaction so important information survives
xml_source: interventions/preserve-task-relevant-evidence.xml
---

# Fix compaction so important information survives

Change the compaction instructions or implementation to preserve information that later work needs. Where the harness allows it, compare changes on a saved conversation before evaluating ordinary future work.

<a id="purpose"></a>

## Purpose

Improve what the compactor keeps so critical information is not forgotten. A completed action may still carry a decision, a failed approach, or a permission limit that future work needs. Choose what to preserve by its likely use, not just by whether the action is finished.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/identified-omission"></a>

### Important information was lost

Important information disappears during compaction, as proposed in [incorrect compaction](../diagnoses/context-handoff-loss.md). [Repeated retrieval](../symptoms/repeated-retrieval.md), [lost constraints](../symptoms/lost-task-constraints.md), or [repeated permission requests](../symptoms/repeated-reauthorization.md) can point you toward an incident to inspect.

<a id="preconditions/editable-transition"></a>

### A supported way to influence compaction

The harness exposes compaction instructions, a hook, or an implementation you control. Identify which path the installed version actually uses. A general instructions file is not automatically a compaction prompt. If the provider hides the retained state, use subsequent behavior to assess the change and record that you cannot inspect the summary directly.

<a id="procedure"></a>

## Procedure

<a id="procedure/locate-boundary"></a>

### Find the control that applies

Use the harness notes below to locate the relevant setting or hook, then save its current version. Compare the affected conversation with the summary or first subsequent mistake. Identify the missing information and why later work needed it.

<a id="procedure/preserve-evidence"></a>

### Save the conversation before compaction

Reuse existing session records. If an upcoming compaction would lose needed evidence, capture it with a supported hook or export. Keep an unchanged copy for comparison and save the resulting summary when it is readable. Agree with the user where these private records go and how long to keep them.

<a id="procedure/create-record"></a>

### Change what compaction preserves

Make a small change tied to the observed omission. For example, if permission survived but its scope did not, ask the compactor to retain each permission together with its limits and expiry conditions. Inspect the existing instructions before adding another rule. Do not remove completed work indiscriminately or hard-code the answer from one incident into the prompt.

<a id="procedure/compare-snapshot"></a>

### Compare on a frozen conversation when practical

If the harness can fork or replay the saved conversation from before compaction, give the original and revised compactor the same input. Start each candidate from that unchanged input, not from the previous candidate's summary. Keep the model, settings, and relevant instruction files fixed apart from the intended change.

Compare whether the needed facts and their qualifications survive, what else is lost, and how much space is used. A small number of focused revisions can be faster than waiting for new incidents. This holds the input steady; it does not make model output deterministic. Stop when further trials are unlikely to change the decision.

<a id="procedure/confirm-delivery"></a>

### Check what survived and deploy the change

Inspect the retained state where possible. If it is opaque, a short continuation with external actions disabled can test whether the agent still follows the relevant constraint; it cannot prove which facts are encoded. A readable summary that looks right is also not enough by itself. Confirm the selected change reaches future sessions.

<a id="procedure/review-work"></a>

### Review occasional samples

Review occasional saved compactions and the work that followed them, using an existing background job where practical. Check a few different kinds of task so a fix for one conversation does not silently damage another. Avoid extra checking on every working turn.

<a id="procedure/agree-followup"></a>

### Agree on a check-in date

Agree with the user on a check-in date, who will review the samples, and a reminder or scheduled job. For example, review in three workdays if normal use should produce several compactions; if too few occur, report that and choose another date.

<a id="harness-notes"></a>

## In your harness

<a id="harness-notes/claude-code"></a>

### Claude Code {data-adm-harness="claude-code"}

**Customize:** Claude Code documents a ` Compact Instructions ` section in ` CLAUDE.md ` for persistent compaction guidance. Use ` /compact ` with a focus instruction for a single comparison. This is the documented route; there is no need to invent a separate compaction ` AGENTS.md `. See [context management](https://code.claude.com/docs/en/how-claude-code-works#when-context-fills-up).

**Capture:** The [PreCompact hook](https://code.claude.com/docs/en/hooks#precompact) receives ` transcript_path `; [PostCompact](https://code.claude.com/docs/en/hooks#postcompact) receives ` compact_summary `. Use these to save the before-and-after evidence. PostCompact cannot rewrite the result; logging a summary and changing compaction are separate operations. Check hook support in the installed version.

**Compare:** Preserve a session from before compaction, then use ` claude --resume SESSION_ID --fork-session ` for each candidate and run ` /compact ` with the candidate focus. The [fork flag](https://code.claude.com/docs/en/cli-reference) gives the continuation a new session ID. Forking an already compacted session does not recreate its original input. Test the final persistent CLAUDE.md change as well as any temporary focus instruction.

<a id="harness-notes/codex"></a>

### Codex CLI {data-adm-harness="codex"}

**Customize:** The [configuration reference](https://learn.chatgpt.com/docs/config-file/config-reference) documents ` compact_prompt ` for an inline override and ` experimental_compact_prompt_file ` for a file-based override. These are compaction-specific settings; ordinary ` AGENTS.md ` guidance should not be treated as a replacement prompt. Check that the installed version and compaction path honor the override before assessing its effect.

**Compare:** Keep an untouched session from before compaction. Use ` codex fork SESSION_ID ` for a separate candidate session, then ` /compact `. The [command reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli) also documents ` /export ` for a readable conversation record. A Markdown export is evidence for review, not a promised exact replay format. Use saved sessions for forks and confirm the effective configuration in each one.

**Limit:** Provider-side compaction can return an opaque state rather than a readable summary. Do not assume a local prompt setting controls every such path. When the state cannot be inspected, compare a constrained continuation and record that limitation. These notes cover the CLI; verify the controls separately for hosted Codex surfaces.

<a id="harness-notes/opencode"></a>

### OpenCode {data-adm-harness="opencode"}

**Customize:** In the [V1 plugin API](https://opencode.ai/docs/plugins/#compaction-hooks), ` experimental.session.compacting ` can append guidance through ` output.context ` or replace the prompt through ` output.prompt `. A replacement ignores the context array, so preserve the useful parts of the default prompt deliberately. [AGENTS.md](https://opencode.ai/docs/rules/) supplies general project instructions; the hook is the explicit compaction control.

**Compare:** V1 documents ` opencode --session SESSION_ID --fork `, ` opencode export SESSION_ID `, and ` /compact `. Fork the same saved session before each candidate compaction and keep the export privately. See the [CLI](https://opencode.ai/docs/cli/) and [TUI](https://opencode.ai/docs/tui/#compact) references.

**Version matters:** The [V2 migration guide](https://dev.opencode.ai/v2/docs/build/plugins/migrate-v1) replaces the V1 hook with ` ctx.session.hook("compaction", ...) `; V1 plugin implementations do not run unchanged in V2. Use the API for the version deployed in your system.

<a id="harness-notes/custom"></a>

### Custom harness {data-adm-harness="custom"}

**Customize and compare:** If you own the summarizer, save its exact input, system instructions, model settings, and output format. Run only that summarization step against the frozen input while changing the targeted instruction. Keep external tools out of the comparison. Then test the chosen change on a separate incident and in ordinary future work.

**Opaque compaction:** OpenAI's [Responses compaction API](https://developers.openai.com/api/docs/guides/compaction) returns a compacted window containing an encrypted item. Keep the returned window intact for subsequent requests; it is not a text summary to edit or inspect. A custom summarizer experiment does not establish how that provider-managed path behaves.

<a id="evaluation"></a>

## Evaluation

- Before applying the change, record which lost facts should now survive and which later mistakes should decline. Use the predictions in [D001](../diagnoses/context-handoff-loss.md#relations/I001/predictions) when that explanation fits.
- Use a frozen-input comparison, when available, to reject poor candidates quickly. Keep an untouched incident for a separate check. A better summary on the example used to tune the prompt is preliminary evidence, not proof of a lasting repair.
- At the agreed check-in, compare retained information and subsequent work. Did requirements and permission limits survive? Did the agent repeat less work? Was enough context space still available?
- If the facts survive but mistakes continue, reconsider the explanation. If evidence was not captured or no relevant compaction occurred, say that the review is inconclusive.

<a id="risks-and-confounders"></a>

## Risks and confounders

- Keeping too much can fill the context; keeping outdated facts can cause bad decisions. A summary can also preserve permission while dropping its limits. Removing completed work can erase why an approach failed.
- Saved conversations can contain private data. Keep collection limited to the agreed location and retention period. A model, harness, or task change can make comparisons harder.
- Forking a conversation does not necessarily isolate its files, credentials, or external services. A continuation test must not repeat the original task's external actions. Prompt revisions can overfit a single transcript.

<a id="stop-and-rollback"></a>

## Stop and rollback

- Restore the previous compaction instructions or implementation if the change causes stale decisions, lost permission limits, or excessive context use.
- Correct affected summaries and repair any resulting work. Reverting the prompt does not undo actions already taken.
- Remove temporary capture or review hooks when the agreed review ends, unless the user chooses to keep them.
