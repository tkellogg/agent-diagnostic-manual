---
id: I002
kind: intervention
summary: Replace an overbroad checking instruction with a rule that specifies its
  trigger, required coverage, completion condition, and reasons to reopen verification.
version: '1'
status: draft
evidence: unvalidated
updated: '2026-10-27'
title: Give verification a scope and stopping condition
xml_source: interventions/scope-verification-policy.xml
---

# Give verification a scope and stopping condition

Replace an overbroad checking instruction with a rule that specifies its trigger, required coverage, completion condition, and reasons to reopen verification.

<a id="purpose"></a>

## Purpose

Reduce redundant checking by fixing the policy that generates it. Verification should answer a task-relevant question; more passing runs do not necessarily add evidence. Retain checks justified by the work's risks and acceptance conditions.

<a id="preconditions"></a>

## Preconditions

<a id="preconditions/identified-rule"></a>

### Identified rule

A specific instruction or workflow causes extra checks, and the maintainer can identify the class of work for which its scope is excessive.

<a id="preconditions/authorized-change"></a>

### Authorized change

The maintainer has authority to revise that policy and can identify the requirements that must remain enforced. Otherwise seek the policy owner's change rather than bypassing it during execution.

<a id="procedure"></a>

## Procedure

<a id="procedure/name-purpose"></a>

### Name purpose

Identify the decision or failure risk the rule is intended to address and the checks needed to address it.

<a id="procedure/rewrite-rule"></a>

### Rewrite rule

Edit the source instruction or workflow to state when it applies, which relevant checks satisfy it, and when checking stops. State the changes or new failures that warrant reopening it. Remove conflicting blanket instructions in the same policy.

<a id="procedure/preserve-gates"></a>

### Preserve gates

Retain mandatory coverage and justified repeated sampling. For example, a targeted check may finish a small local edit while release approval still requires the project's release gate; neither is automatically a substitute for the other.

<a id="procedure/apply-and-review"></a>

### Apply and review

Deliver the revised policy to future agents and confirm it is active at an affected decision. Review subsequent eligible work for both reduced overrun and preserved defect detection.

<a id="evaluation"></a>

## Evaluation

Before the change, predict which trigger points should lose redundant work and which checks should remain. At a proportionate review point, compare time spent after requirements were satisfied, checks repeated without new justification, missed defects, and usable task completion in comparable work.

Less checking alone is insufficient. If defects rise, coverage may have been removed. If the revised rule reaches the agent but excess checking persists, inspect other instructions and decision behavior. Work with no relevant check opportunity supplies little evidence.

<a id="risks-and-confounders"></a>

## Risks and confounders

A narrow rule can miss interacting changes or encourage premature completion. A different task mix or faster test infrastructure can also reduce checking time without validating the policy explanation.

<a id="stop-and-rollback"></a>

## Stop and rollback

Restore needed coverage if the change skips required gates or misses relevant defects. Revert the rule or narrow its exception; preserve evidence of defects and repair affected artifacts separately.

<a id="evidence-and-uncertainty"></a>

## Evidence and uncertainty

This intervention is unvalidated. Its usefulness depends on correctly identifying an overbroad rule; it is not a general recommendation to test less.
