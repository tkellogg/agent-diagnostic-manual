---
schema_version: 1
id: structure
kind: guide
title: Structure and design decisions
summary: The v0.1 source contract, link model, and deliberately limited scope.
status: draft
updated: "2026-10-26"
---
# Structure and design decisions

## Decision: Markdown with YAML frontmatter

Use one Markdown file per symptom, diagnosis, or intervention. YAML frontmatter is parsed with a safe loader and checked against a JSON Schema. Prose remains easy to review in GitHub, a text editor, or the rendered site.

XML could express more deeply structured criteria, but it would add markup to every paragraph before we know which concepts deserve formal structure. We do not currently need that tradeoff. Ordinary scripts can parse the frontmatter and consume the generated JSON catalog. If a future evaluator must execute criteria, introduce a versioned structured criteria format; do not silently extract authoritative logic from prose.

The canonical source is the Markdown file. HTML and JSON are derived outputs, never independently edited.

## Directory layout

| Path | Purpose |
| --- | --- |
| `content/index.md` | Site entry point. |
| `content/symptoms/*.md` | One observable feature per entry, plus an index. |
| `content/diagnoses/*.md` | One candidate diagnostic pattern per entry, plus an index. |
| `content/interventions/*.md` | One reusable investigation or remediation protocol per entry, plus an index. |
| `content/cases/index.md` | Evidence policy; case schema deferred until the first real trace. |
| `content/structure.md`, `content/foundations.md` | Design contract and conceptual background. |
| `schema/entry.schema.json` | Machine-checked metadata contract. |
| `tools/build.py` | Validate, render, and emit catalog/backlinks. |
| `dist/` | Ignored build output; no deployment is configured. |

Index pages have `kind: guide`; they are not extra symptom or diagnosis entries.

## Relationship model

A diagnosis names its relevant symptoms by stable ID. It can link to several interventions. One intervention can be linked from several diagnoses. The builder derives reverse links; authors maintain each relationship in one direction only.

An intervention link records **role**, **when**, and **evidence**. Role is `investigation`, `remediation`, or `both`. A procedure can improve performance while providing only weak evidence for a particular mechanism. Applicability is a statement to review, not an automatically executable predicate.

Today the graph is [D001](diagnoses/unproductive-repeated-retrieval.md) → [S001](symptoms/repeated-retrieval.md), and D001 → [I001](interventions/preserve-task-relevant-evidence.md). The second relationship is conditional on suspected loss of evidence from the active context.

## Content contract

Every page has these frontmatter fields:

| Field | Meaning |
| --- | --- |
| `schema_version` | Integer metadata contract version; currently `1`. |
| `id` | Unique, stable identifier. Entry prefixes: `S`, `D`, `I`; guide IDs are descriptive. |
| `kind` | `guide`, `symptom`, `diagnosis`, or `intervention`. |
| `title`, `summary` | Display title and concise abstract. |
| `status` | Editorial state: `draft`, `reviewed`, or `retired`. Review does not imply empirical validation. |
| `updated` | Quoted ISO date, `YYYY-MM-DD`. |

Entry pages additionally require `evidence` and `tags`. Initial evidence values are `unvalidated`, `case-supported`, and `replicated`. These are reporting labels, not severity or numerical confidence scores. Evidence promotion needs linked, inspectable records; the current corpus is entirely unvalidated. Case-supported means a documented empirical case supports the entry's claim, not that a causal mechanism is proven. Replicated requires documented repetition and stated conditions; it never means universal.

Diagnoses additionally require `unit`, `diagnostic_level` (`descriptive` or `mechanistic`), `symptoms`, and `interventions`. Symptoms are referenced by ID. Intervention relationships look like this:

```yaml
interventions:
  - id: I001
    role: both
    when: Necessary evidence appears to be lost from the active context.
    evidence: unvalidated
```

Interventions require `targets`, a list naming the system components they change. No default intervention is implied by listing one.

The schema rejects unknown fields. Additions require an explicit contract update so misspelled metadata does not quietly disappear. Stable IDs survive title and filename changes. Use native relative Markdown links in prose; fix incoming links when moving a file. Relationship IDs are resolved to current paths at build time.

## Prose contract

Each entry uses fixed second-level headings, validated by the builder. Within those sections, use free text, tables, and lists.

| Kind | Required sections |
| --- | --- |
| Symptom | Observation; How to recognize it; Benign lookalikes; What to record; Examples |
| Diagnosis | Definition; Candidate criteria; Exclusions; Differential diagnosis; Investigation; Interventions; Evidence and uncertainty |
| Intervention | Purpose; Preconditions; Procedure; Evaluation; Risks and confounders; Stop and rollback; Evidence and uncertainty |

Criteria receive local labels such as A–D in prose for review and discussion. They are not executable rules. Relationship metadata is authoritative for catalog links; prose explains the relationship rather than maintaining a second reverse-link list.

## Interventions: proposed structure

Keep interventions first-class and independent of diagnoses. A protocol describes what changes, which prerequisites must hold, how to evaluate it, and when to stop or undo it. The diagnosis owns the conditional applicability link.

For the first example, preserving evidence can be both a diagnostic probe and a possible remedy. These uses share a protocol but make different claims. A successful outcome supports usefulness under the tested conditions; it does not establish the cause by itself.

Do not encode an intervention as “treatment for D001” without conditions. Do not let a symptom directly trigger automatic production changes. This manual records protocols for deliberate evaluation; it is not an autonomous remediation engine.

## Evidence and growth

Keep category validity separate from confidence in a specific case. New entries start as drafts with unvalidated evidence. Use [case records](cases/index.md) when empirical material arrives. Synthetic examples teach distinctions but cannot promote evidence status.

A useful next increment is one real trace plus a healthy comparison for the existing entry. Revise or split a category only when cases justify it. Do not create a second diagnosis simply to fill the directory.

## Deliberately deferred

Severity levels, severity scores, and severity thresholds are absent from the schema. We can describe observed cost and outcome without defining a grading system.

Also deferred: formal case schema, executable criteria, automated diagnosis, intervention ranking, prevalence estimates, comprehensive taxonomy, and public hosting.
