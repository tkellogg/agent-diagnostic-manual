# Authoring symptoms XML files

## Observations
Observations define what the behavior is in the canonical case. These blocks should be succinct and phrased as objective observations that can be made by looking at non-experiential evidence (session transcripts, files, audit logs, etc.). 

Make sure to include clear rules. Now, these clear rules are going to be arbitrary to some extent, like "3-5 cycles", chosen as a guiding principle. These rules should be dialed slightly towards optimizing for recall than precision. Try for precision, but when it's ambiguous, reall is fine.

Generally keep an observation to a single paragraph. Ideally 1-2 sentences. Maximize clarity.

## How to recognize it
These are light suggestions for where to look (data sources) and how to surface data that might match one of the `observations`. This block should be more tangibly helpful than the observations block, but should not conflict with it at all.

Read this block, and think to yourself. If such a situation exists in which a reader could read the observations, then this block, and suddenly be confused on if it's a match or not, then you've written this wrong. It shouldn't conflict at all, it should merely be more tangible help.

For this block, focus on where to look — session transcripts, memory files, code, git history, etc. And describe general recipes (not so much detail that it could conflict, but enough to make it tangible) for how to surface the data, how to surface counter examples, how to surface data to show it's not a benign lookalike, etc.

## Benign lookalikes
Describe situations that are acceptable but might look like. This is a chance to explore the boundry conditions and present counter examples. Every benign lookalike should reference the observations to explain why this lookalike doesn't match the criteria.

An explanation is not automatically a benign lookalike: a faulty instruction, failed delivery, or context policy can cause a symptom of the configured system even when the model is behaving reasonably. Exclude justified behavior, not behavior whose cause you can explain. If a case falls outside this symptom's definition, do not imply that the entire system is healthy. Check linked diagnoses for contradictions before changing either boundary.

## What to record
Describe in prose all data that would be helpful to capture per-incident in order to do population-level analysis to spot trends.

## Examples
Make it tangible. Try to use real reported examples from the internet (with links). It's fine to include made-up examples, as long as they're phrased as a real incident. Make sure to include what it looked like (the observation), how it was recognized, and the impacts.

The primary purpose of examples is to quantify the impacts of the symptom. It's done through several real world examples so that the reader can see why it's harmful and suddenly associate behavior that could have been benign and instead categorize it as a real symptom. That is done by understanding the impact.
