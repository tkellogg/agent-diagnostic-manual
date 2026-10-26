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

## Purpose: a format other tools can use

ASM is intended to support an ecosystem of independently built tools. The corpus and its documented format should be useful without an LLM, a hosted service, or this repository's Python code. The included builder is a reference implementation.

This is a design commitment, not a claim that an ecosystem or a validated diagnostic science already exists. The repository remains private while the format and first entries develop. Publication and licensing are future decisions.

## Decision: canonical XML, generated Markdown

One XML document per symptom, diagnosis, or intervention lives under `entries/`. Its metadata, criteria, relationships, and prose share one canonical document. The namespace is `urn:asm:1`; the schema is XSD 1.0.

The builder produces readable Markdown in `content/` and a static site plus JSON catalog in `dist/`. Generated Markdown is committed so GitHub is a usable reader. Each generated page links to its XML source. CI rejects stale generated pages.

General guides and index pages remain authored Markdown: they explain the project rather than define diagnostic objects. Their frontmatter describes navigation and presentation only.

## Directory layout

| Path | Authority and purpose |
| --- | --- |
| `entries/symptoms/*.xml` | Canonical symptom documents. |
| `entries/diagnoses/*.xml` | Canonical diagnostic documents. |
| `entries/interventions/*.xml` | Canonical intervention documents. |
| `schema/asm-v1.xsd` | Normative XML grammar and vocabulary. |
| `content/format.md` | Normative cross-document rules and semantics the XSD cannot enforce. |
| `content/symptoms/*.md`, `content/diagnoses/*.md`, `content/interventions/*.md` | Generated reader pages, except authored `index.md` files. |
| `content/*.md`, `content/cases/index.md` | Authored guides and navigation. |
| `schema/guide.schema.json` | Guide frontmatter validation only. |
| `tools/` | Reference reader, validator, and builders. |
| `examples/query_manual.py` | Independent consumer using only Python's standard library. |
| `tests/` | Executable conformance and rendering examples. |
| `dist/` | Disposable static HTML and JSON output; never canonical. |

## Relationship model

A diagnosis refers to symptoms by ID. An individual criterion can also reference a symptom. Intervention applicability is its own identified relationship: `D001-I001` records the target, role, evidence, and condition for applying I001 to D001.

A protocol can serve several diagnoses, and a diagnosis can link to several protocols. Reverse links are derived. Prose references use `<ref target="D001-A">` and can address an individual criterion without knowing its filename.

Today there is one [symptom](symptoms/repeated-retrieval.md), one [diagnosis](diagnoses/unproductive-repeated-retrieval.md), and one [intervention](interventions/preserve-task-relevant-evidence.md). Criteria, exclusions, differential alternatives, preconditions, and procedure steps have their own IDs. This does not add new diagnoses.

## Content contract

The [XML format contract](format.md) specifies identity, typed references, document order, version handling, and mixed prose. The XSD validates individual documents. A conforming corpus validator also checks uniqueness and reference integrity across documents.

A consumer can choose its implementation: standard XML parsing, XPath, a different language, another renderer, or the generated JSON. No consumer must import `tools/`.

Structured criteria remain statements that require assessment. For example, `operator="all"` means all the listed criteria must be supported; it does not provide an algorithm for judging them. Applicability conditions are likewise explicit prose, not executable predicates.

## Interventions: proposed structure

Keep interventions independent and reusable. An intervention defines its purpose, preconditions, identified steps, evaluation, risks, rollback, and uncertainty. The diagnosis owns the applicability relationship.

A relationship's role is `investigation`, `remediation`, or `both`. Role does not imply effectiveness. Its evidence label describes support for that particular use; the intervention's own evidence label describes the protocol more broadly.

For I001, preserving evidence can be a diagnostic probe and a potential remedy. A successful task outcome does not establish the mechanism. Applications may build tools around these records, but the format does not authorize automatic production changes.

## Compatibility and independent implementations

Stable IDs are the public handles. Do not recycle them or change them when moving files. Distinguish format version, source revision, editorial status, and empirical support. Consumers should retain a Git revision when recording an assessment so a reference identifies the wording assessed.

This first XML contract is a draft. Changes to it must update the schema, format document, fixtures, and tests together. Before outside consumers depend on a release, define the release's compatibility policy. A future incompatible format needs a new namespace/version and an explicit migration; do not teach consumers to guess silently.

No mandatory extension framework is introduced yet. Version 1 rejects unknown elements and attributes. Keep experimental consumer data outside canonical documents until an extension contract is designed. This avoids silently losing fields an independent tool thought were meaningful.

## Evidence and growth

Category validity and confidence in a case remain separate. Current entries are drafts with unvalidated evidence. Synthetic examples do not count as observations or successful interventions. The next empirical increment is still a real trace and a healthy comparison; see [cases](cases/index.md).

## Deliberately deferred

Severity levels and thresholds remain absent. Other deferred topics include a formal case schema, executable assessment rules, intervention ranking, prevalence, a comprehensive taxonomy, public hosting, and a release license. XML creates addressable content; it does not resolve these research or governance questions.
