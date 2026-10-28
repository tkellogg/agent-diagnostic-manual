# Authoring symptoms XML files

## Observations
Observations define what the behavior is in the canonical case. These blocks should be succinct and phrased as objective observations that can be made by looking at non-experiential evidence (session transcripts, files, audit logs, etc.). 

Make sure to include clear rules. Now, these clear rules are going to be arbitrary to some extent, like "3-5 cycles", chosen as a guiding principle. These rules should be dialed slightly towards optimizing for recall than precision. Try for precision, but when it's ambiguous, recall is fine.

Generally keep an observation to a single paragraph. Ideally 1-2 sentences. Maximize clarity.

Observable does not mean numerically measured. A reviewer can identify poorer code, misunderstood intent, or an explanation that is hard to follow by pointing to concrete evidence. Do not require a benchmark, fixed sample size, or explicit time budget unless the behavior actually needs that boundary.

## How to recognize it

This optional section gives a specific, useful hint about where to find evidence. Keep it to one or two sentences. Omit it when it merely restates the observations or repeats generic advice to read transcripts and logs.

It must not change the definition or add a new requirement for recognizing the symptom. Reusable techniques such as transcript classifiers, before-and-after comparisons, and occasional background reviews belong in [observation methods](observation-methods.md).

## Benign lookalikes
Describe situations that are acceptable but might look like. This is a chance to explore the boundary conditions and present counter examples. Make the lookalike the negative half of the definition: reinforce what the behavior is by showing what it is not. A conceptual reference is enough; an explicit XML link to the observation is optional.

An explanation is not automatically a benign lookalike: a faulty instruction, failed delivery, or context policy can cause a symptom of the configured system even when the model is behaving reasonably. Exclude justified behavior, not behavior whose cause you can explain. If a case falls outside this symptom's definition, do not imply that the entire system is healthy. Check linked diagnoses for contradictions before changing either boundary.

## What to record
Describe in prose all data that would be helpful to capture per-incident in order to do population-level analysis to spot trends.

## Examples
Make it tangible. Try to use real reported examples from the internet (with links). It's fine to include made-up examples, as long as they're phrased as a real incident. Make sure to include what it looked like (the observation), how it was recognized, and the impacts.

The primary purpose of examples is to quantify the impacts of the symptom. It's done through several real world examples so that the reader can see why it's harmful and suddenly associate behavior that could have been benign and instead categorize it as a real symptom. That is done by understanding the impact.

Use `kind="synthetic"` or `kind="observed"` on each example; the builder displays a badge, so do not repeat “Synthetic incident” in its prose. Prefer linked firsthand reports when available, preserve important qualifications and follow-ups, and keep invented examples concrete and easy to follow.

Write for a reader who has not followed the author’s reasoning. Use familiar words, name actors and actions, and explain necessary terms. Dense labels and compressed noun phrases can themselves obscure the behavior being defined; see [S015](https://diag.timkellogg.me/symptoms/opaque-jargon.html).
