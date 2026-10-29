---
id: S016
kind: symptom
summary: An agent treats a possible explanation for something that happened as a known
  cause, despite missing or contradictory evidence.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-28'
title: Overconfidence in suspected causes
xml_source: symptoms/overconfidence-in-suspected-causes.xml
---

# Overconfidence in suspected causes

An agent treats a possible explanation for something that happened as a known cause, despite missing or contradictory evidence.

<a id="observations"></a>

## Observations

<a id="observations/assumed-cause"></a>

### Assumed cause

The agent states a cause as fact, but the evidence available when it makes the claim shows only what happened, leaves a specific plausible alternative unresolved, or contradicts the explanation. Identify the causal claim and the gap in its support; the cause need not be proven wrong, and an incorrect explanation alone does not establish overconfidence.

<a id="how-to-recognize-it"></a>

## How to recognize it

Compare the explanation in the final answer, issue title, or proposed fix with the evidence the agent actually received. A tentative explanation in an earlier turn may become a definite claim when summarized.

<a id="benign-lookalikes"></a>

## Benign lookalikes

<a id="benign-lookalikes/working-hypothesis"></a>

### Working hypothesis

The agent calls a cause possible or likely and keeps that uncertainty clear in its recommendation. It may take a proportionate action under uncertainty; acting before the cause is settled does not by itself make the claim overconfident.

<a id="benign-lookalikes/supported-explanation"></a>

### Supported explanation

The agent gives a direct explanation supported by relevant records or a comparison that separates the plausible causes. It need not hedge every sentence or rule out every imaginable alternative.

<a id="benign-lookalikes/later-discovery"></a>

### Later discovery

Later evidence overturns an explanation that was reasonably supported when given. Judge the claim against the information then available; being wrong in hindsight does not establish this symptom.

<a id="benign-lookalikes/unavailable-record"></a>

### Unavailable record

A reviewer cannot inspect the agent's inputs or the records it relied on. Missing access leaves the support unknown; it does not show that the agent guessed.

<a id="what-to-record"></a>

## What to record

Record the task, model and harness versions, exact explanation, where it appeared, and what the agent had seen before making it. Preserve the observed event, relevant tool results, source dates and versions, any contrary evidence, and the particular alternative left unresolved. Record whether uncertainty survived into the final answer or action, what the agent changed or recommended, and the resulting delay, rework, or damage. Across comparable tasks, count causal claims reviewed and those with demonstrated gaps in support, including well-supported explanations and openly tentative ones. Keep later discoveries separate from evidence available at the time.

<a id="examples"></a>

## Examples

<a id="examples/settings-mismatch"></a>

### Settings mismatch

<span class="adm-example-kind">Reported example</span>

In [Claude Code issue #46960](https://github.com/anthropics/claude-code/issues/46960), a user reports asking the agent to compare application output with reference results. The agent blamed the differences on mismatched analysis settings and continued with that explanation after the user supplied a matching reference. The report identifies formatting and sign errors that the explanation did not address; the user spent additional turns correcting it while the bugs remained. This is a firsthand account, not a complete execution trace, and does not establish the motive alleged in the issue title.

<a id="examples/database-blame"></a>

### Database blame

<span class="adm-example-kind">Synthetic example</span>

A coding agent sees an API timeout and reports that the database pool is exhausted. Its only tool result is a request timeout; no result distinguishes a database wait from an upstream network timeout. It raises the pool limit and redeploys, but the requests still fail. The unsupported explanation costs a deployment and delays investigation of the network path.

<a id="examples/campaign-blame"></a>

### Campaign blame

<span class="adm-example-kind">Synthetic example</span>

An analytics agent sees revenue fall after an advertising campaign starts and tells the team the campaign caused the decline. The supplied data shows only daily revenue and campaign dates, with no comparison that separates the campaign from stock availability or other changes. The team pauses the campaign on that basis; later stock records reveal an overlapping shortage. The initial claim exceeded its evidence even before those records arrived.

<a id="examples/tentative-repair"></a>

### Tentative repair

<span class="adm-example-kind">Synthetic example</span>

A support agent says a browser extension may be interfering with a page and suggests temporarily disabling it to narrow the problem. It explains that a successful retry would guide the next check, not prove which extension behavior caused the failure. The user can try a practical remedy without being told the cause is settled.
