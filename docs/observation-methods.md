# Observation methods

These are ways to find evidence for a symptom or check a prediction. They do not redefine symptoms, and using one is not required to report a problem. Start with existing transcripts, artifacts, and the user’s account; choose the cheapest method that answers the question.

## Scan a transcript for a particular behavior

For correction without behavioral change, give a reviewer the correction, the acknowledgment, and each later relevant action. Ask whether the corrected behavior happens again, with a quote or event number and an option to say “unclear.” Include surrounding turns so an action already in progress or a changed instruction is not mistaken for a new violation.

A small, inexpensive model can do the first pass over many sessions. Try it on a few cases a human has read, including benign cases, before trusting its labels. Keep its model, prompt, evidence references, and disagreements so the classification can be checked. A classifier’s confidence is not proof of a diagnosis.

## Compare before and after

Put a recent good output beside a worse one on similar work. Name the difference in terms the user cares about: missed requirements, tangled code, lost progress, or extra rework. A judgment such as “this is less maintainable code” can be useful when the reviewer points to the relevant changes; no numerical score is required.

Use several nearby examples when they are easy to obtain, including work that stayed good. Check whether the task became harder or the user changed what they wanted before calling the difference a performance drop.

## Check whether verification served the task

Read the request and follow-up messages beside the tests or checks. Ask what decision each disputed check helped the user make, what failure it could catch, and who was supposed to do the remaining review. This can reveal excessive verification even on a first run, without a time budget or stop rule.

A prototype for customer feedback and a production release need different evidence. If the user’s intent is unclear, discuss it instead of silently substituting either “always test everything” or “always move fast.”

## Sample compactions

Use the harness’s saved conversation and compaction summary to compare what was kept with what the next work needed. If those records do not exist, agree with the user on a private capture hook and retention period. A saved full conversation helps investigation; it does not prove the working agent retained its contents.

An occasional async job or maintainer review can inspect samples after normal work. Agree on a check-in date and who will return to the evidence. If no relevant compactions occurred by then, extend the observation period explicitly; do not turn missing opportunities into a successful result.

## Follow a claim to its evidence

For a completion or verification claim, inspect the artifact or check at the claimed version and destination. Record what was actually completed or tested and what the final message says. A test that calls an internal function may not establish that the user’s input reaches it.

This comparison separates unfinished work, an unsupported testing claim, and a reporting mistake. It can suggest a diagnosis, but does not by itself establish the mechanism that caused the discrepancy.

## Check whether evidence still applies

An old observation can be accurate and still fail to support a claim about the present. Pair the agent's claim or action with the time, version, and environment its evidence describes, then identify the relevant change between that observation and the state the task concerns. Use event time rather than log-ingestion time when the two differ. Age alone does not make evidence stale, and a newer commit does not invalidate evidence about an unchanged part.

For an alleged failure after a repair, check when the failure occurred and where the repair took effect. A closed task is not proof of a successful fix: read its resolution and any confirming result. Distinguish a failure before the fix, a new failure after it, and a fix that never reached the affected environment. An explicitly historical review can properly use old failures.

Keep two questions separate: does the evidence support the current claim, and why did the agent use it? The input collector may have supplied only old records; a summary may have dropped their dates or versions; or the agent may have had the newer evidence and ignored it. Inspect the actual input before choosing among those explanations. The repairs differ: deliver the relevant updates, preserve what time and version each record describes, or change how the agent selects evidence. None requires rereading every source on every turn.

In [Codex issue #49083](https://github.com/openai/codex/issues/49083), a reporter describes a PR re-review that used an old local commit after remote reads failed. Two reported defects were already fixed in the newer head. The account includes both commit IDs and command results, and notes that the agent disclosed difficulty checking the remote head. It supports investigating a mismatch between the requested version and the reviewed version; it does not establish how often this happens.

For catalog matching, a claim that a check proves the current version works or fails can fit [S011, Unsupported verification claims](https://diag.timkellogg.me/symptoms/unsupported-verification-claims.html). Acting on an outdated plan or reporting an old business condition as current is broader than a verification claim. [S016, Overconfidence in suspected causes](https://diag.timkellogg.me/symptoms/overconfidence-in-suspected-causes.html) concerns how strongly a cause is asserted; stale evidence can mislead an agent without any causal explanation. These overlaps do not establish one shared diagnosis.

Record the exact claim or action, the evidence's event time and version, the intervening change, what the agent received, and the resulting repeated work or missed problem. If a repair changes evidence selection, predict fewer findings about already-resolved problems while checking that genuine recurrences remain visible. Fewer findings alone could mean the agent stopped looking.

## Review whether a change helped

Before changing the system, record an expected effect, something that should remain intact, and an outcome that would make you reconsider. Agree on a review date or an amount of normal work followed by a dated check-in, and arrange a reminder or job with the user’s agreement.

At review, keep helpful outcomes, failures, and cases where the behavior had no opportunity to occur. Distinguish a change that was never active from one that was active and did not help. Do not infer a population rate from a collection of complaints, or claim a cause is proven merely because one repair helped.
