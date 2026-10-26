---
schema_version: 1
id: format
kind: guide
title: XML format contract
summary: Draft ASM XML v1 grammar, cross-document rules, identity, and independent consumption.
status: draft
updated: "2026-10-26"
---
# XML format contract

This draft and `schema/asm-v1.xsd` jointly define ASM XML v1. The XSD specifies per-document grammar; this document specifies corpus-level constraints and meaning. The reference implementation is replaceable. A schema-valid document is not necessarily a valid corpus or a scientifically supported claim.

## Files, namespace, and versions

- XML documents are UTF-8, with namespace `urn:asm:1` and root `version="1"`. The namespace is an identifier, not a network resource to retrieve.
- Root elements are `symptom`, `diagnosis`, or `intervention`. Their directories are respectively `entries/symptoms/`, `entries/diagnoses/`, and `entries/interventions/`.
- The XML source maps to a generated Markdown file at the same relative path under `content/`, replacing `.xml` with `.md`.
- DTDs, entity declarations, XInclude, external schema fetching, and executable content are outside the format. Validators must not resolve external resources. Consumers must reject unsupported namespaces, versions, or core vocabulary rather than guess their meaning.
- Element order follows the XSD. Attribute order and namespace prefix spelling have no semantic significance. Whitespace-only indentation between structural elements has no semantic significance; mixed prose order and spacing do.

## Identity

Entry IDs match `S` / `D` / `I` followed by at least three digits, corresponding to the root kind. Every identified child starts with its entry ID and a hyphen. All IDs are case-sensitive and unique across the corpus, not merely within a file.

IDs persist when titles, ordering, or paths change. Numbers in IDs are identity tokens, not positions: moving `I001-step-3` does not require renaming it. Do not recycle retired IDs. When recording an assessment or result, retain both the object ID and source revision (for example, a Git commit). An ID alone does not freeze its wording.

Required IDs include sections, criteria, exclusions, alternatives, intervention applicability relationships, preconditions, and steps. Structural containers such as `tags` need no identity.

## Metadata and support

Each root requires `id`, `version`, `status`, `evidence`, and `updated`; its first children are `title`, `summary`, and `tags`. `updated` is an XML date. Editorial status is `draft`, `reviewed`, or `retired`. Evidence is `unvalidated`, `case-supported`, or `replicated` under the [evidence policy](cases/index.md).

These labels do not encode severity, confidence in an individual case, or proof of causation. XSD validation cannot establish whether an evidence claim is true.

Diagnosis roots also require `unit="configured-agent-episode"` and `level="descriptive"` or `level="mechanistic"`. Intervention roots include nonempty `targets` listing affected system components.

## Diagnostic structure

The required diagnosis sections are `definition`, `criteria`, `exclusions`, `differential`, `investigation`, `interventions`, and `evidence-and-uncertainty`.

`criteria` contains one or more `criterion` objects, each with an ID, title, and prose. Version 1 supports only `operator="all"`: all criteria must be supported to fit this working definition. Missing information remains unknown; it is not automatically evidence that a criterion is false. There is no executable assessment language.

`exclusions` contains identified `exclusion` descriptions. `differential` contains identified `alternative` objects with titles and `discriminator` prose. Alternatives are explanations to examine, not automatically registered diagnoses. Text before and after the criteria or alternatives remains part of the document and must not be discarded from a complete rendering.

## Intervention structure

Required sections are `purpose`, `preconditions`, `procedure`, `evaluation`, `risks-and-confounders`, `stop-and-rollback`, and `evidence-and-uncertainty`.

Each `precondition` and `step` has a stable ID and rich prose. Step document order specifies procedure order. Preconditions must be assessed before applying the protocol; the format does not implement those assessments. Evaluation and rollback remain explicit prose until actual cases justify more structure.

## Typed references and applicability

A diagnosis's `relations` contains entry-level `symptom-ref` and optional `intervention-ref` elements. A criterion can also contain `symptom-ref`. Every target must resolve in the corpus, and its kind must match the typed reference.

```xml
<intervention-ref xmlns="urn:asm:1"
    id="D001-I001" ref="I001" role="both" evidence="unvalidated">
  <when>Necessary evidence is missing from active context.</when>
</intervention-ref>
```

The fragment illustrates a relationship; it is not a complete entry. `role` is `investigation`, `remediation`, or `both`; `when` is required applicability prose. Applicability belongs to the relationship, so the same protocol can have different conditions and support for different diagnoses.

Entry-level duplicate typed relationships to the same target are rejected by the reference corpus validator. A criterion's additional symptom reference is a distinct relationship from its parent diagnosis's reference.

Inline `<ref target="D001-A">criterion A</ref>` may target any identified object. Its label is presentation text, not identity. The nearest enclosing identified object owns the reference. Reverse links are derived rather than stored as a second authority.

## Rich prose

Supported block elements are `p`, `ul`, and `ol`, with inline `strong`, `em`, `code`, `a`, and `ref`. List items contain inline prose. This deliberately small vocabulary covers the first entries; arbitrary HTML, nested block lists, embedded Markdown, and opaque CDATA payloads are not part of v1.

`a href` is for a guide link, an external HTTP(S) link, or a mail link. Relative guide links resolve from the generated document's location under `content/`; local links must resolve within that tree and their fragments must exist. Absolute local paths, unsafe URL schemes, and escaping the content tree are invalid. Use `ref` for corpus objects so moving their source file does not break references.

Renderers must preserve inline order, text, and link labels. They may style headings and generate navigation. A rendered page is a view, never a second source of truth.

## Validation layers

1. Parse safely and validate the document against the local XSD.
2. Check root kind/directory agreement, entry ID syntax, child ID prefixes, and corpus-wide ID uniqueness.
3. Resolve typed and inline references; reject wrong kinds, missing targets, and duplicate entry-level typed relationships.
4. Validate local guide links and fragments for a complete reader build.
5. For this repository, ensure committed generated Markdown exactly matches the XML-derived output.

Consumers that implement only a subset should report which validation layers they performed. Conformance does not imply scientific validation, diagnostic reliability, or an effective intervention.

## Derived JSON catalog

`dist/catalog.json` has `schema_version: 2` (separate from XML format v1), `xml_namespace`, `entries`, `objects`, and `relationships`.

- `entries` supplies metadata and source/rendered paths. XML entries additionally contain `document`, an ordered tree with `name`, `attributes`, and `content` (text strings interleaved with child nodes). Guides have no XML tree.
- `objects` maps each XML ID to its kind, owning entry, source path, and rendered URL/anchor.
- `relationships` preserves explicit XML references, including criterion-level references and applicability conditions. Inline links have relation `ref`; typed links have `symptom-ref` or `intervention-ref`. The `from` ID is the nearest identified owner; applicability edges also carry their own `id`.

The JSON representation is convenient for consumers, but XML remains canonical. A complete consumer can use XML directly without running this builder.

## Independent consumer example

Run `python examples/query_manual.py` from the checkout. It uses Python's standard-library ElementTree, imports no ASM code, and extracts criteria and applicability conditions directly from XML. It demonstrates reading the format, not complete validation or diagnosis.

The program's `--entries` option accepts a different corpus location. This separation is intentional: other tools should depend on the documented content contract rather than this application's internals.
