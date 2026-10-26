# ADM file format

Use this reference when reading, parsing, linking, or editing ADM files. The corpus is XML; this skill and its instructions are Markdown.

## Source and identity

Read UTF-8 XML in namespace `urn:adm:1` with `version="1"`. The namespace is an identifier, not a network resource. The three root kinds and locations are:

| Root | Directory | Document ID |
| --- | --- | --- |
| symptom | entries/symptoms/ | S followed by at least three digits |
| diagnosis | entries/diagnoses/ | D followed by at least three digits |
| intervention | entries/interventions/ | I followed by at least three digits |

Require corpus-wide, case-sensitive document IDs. Documents carry title, summary, editorial status, update date, and evidence status. Titles are plain-text attributes on documents, criteria, and differential alternatives. Summary is a child element. Diagnosis unit and level describe the assessed system and whether the category is descriptive or mechanistic.

Use one to three lowercase kebab-case words for list-member IDs, matching `[a-z][a-z0-9]*(-[a-z][a-z0-9]*){0,2}`. Require uniqueness only within the containing list. The same local ID can occur in another list or document. Preserve identity when rearranging items; do not reuse an ID for a different meaning.

Give singleton sections and containers no ID: their tag names identify them. Keep structured lists free of introductory or trailing prose.

## Addresses and relationships

Form an address from a document ID, optionally followed by `#` and a slash-separated structural path. Use singleton tag names and list-member IDs:

| Address | Meaning |
| --- | --- |
| S001 | Whole symptom |
| S001#observations/multi-read | One observation |
| S001#what-to-record | Singleton prose section |
| D001#criteria/recurrence | One criterion |
| D001#differential/context-loss/discriminator | One alternative's discriminator |
| D001#relations/I001/when | Applicability condition |
| I001#procedure/save-baseline | One ordered step |

Use `<ref target="S001#observations/multi-read">label</ref>` for corpus links. Require fully qualified addresses, even inside the same document. Resolve IDs from the corpus rather than guessing filenames.

Use `<symptom-ref ref="S001"/>` and `<intervention-ref ref="I001"><when>Condition</when></intervention-ref>` for typed relationships. Require a whole-document target of the matching kind. An intervention reference needs only its target and condition; its target identifies it within the diagnosis's relations list. Reject duplicate entry-level relationships to the same target. A criterion can also reference symptoms; those references identify relevant symptoms, while the criterion's prose specifies the requirement.

## Entry structure

For symptoms, read observations, how-to-recognize-it, benign-lookalikes, what-to-record, and examples. Observations, lookalikes, and examples are individually addressable items. Examples declare `kind="synthetic"` or `kind="observed"`.

For diagnoses, read relations, definition, criteria, exclusions, differential, investigation, interventions, and evidence-and-uncertainty. Criteria, exclusions, and alternatives have local IDs. Each alternative contains a singleton discriminator. Interpret `criteria operator="all"` as requiring support for every criterion; missing information remains unknown. This combines judgments about prose, not executable predicates.

For interventions, read purpose, preconditions, procedure, evaluation, risks-and-confounders, stop-and-rollback, and evidence-and-uncertainty. Preconditions and steps have local IDs; procedure order follows document order. The same intervention can support an experiment or a remedy.

## Prose and validation

Preserve inline text order and spaces. Prose supports p, ul/ol with li, strong, em, code, ref, and external links using a. Use a only for HTTP(S) or mailto links; use ref for corpus navigation. Escape text when rendering. Generic prose lists do not create independently addressable items.

Validate against `schema/adm-v1.xsd` in the checkout, then check directory/ID agreement, document uniqueness, local list uniqueness, and reference resolution and kinds. Reject unsupported versions and unknown elements or attributes. Disable DTDs, entities, XInclude, network schema fetching, and executable content. Format conformance does not establish empirical validity.

From the checkout root:

```sh
python tools/build.py --check
python -m unittest discover -s tests
python examples/query_manual.py
```

The example uses Python's standard library and imports no ADM code. Independent consumers need neither the reference builder nor an LLM.

## Generated views

Run `python tools/build.py` to produce a linked HTML site, Markdown and XML alongside each HTML entry in `dist/`, and `dist/catalog.json`. MkDocs builds the site, Pagefind indexes it, and the builder derives navigation from entries. The README supplies the homepage. Swap an entry URL’s .html suffix for .md or .xml to read another format. Edit XML and rebuild; do not edit generated copies.

The catalog exposes document metadata and an ordered XML-derived tree, an address index, and explicit relationships. Tree nodes have name, attributes, and ordered content. Content interleaves strings and child nodes; indentation-only structural whitespace is omitted. Address-index records give document, kind, source, and rendered URL. Relationships give their nearest addressable owner, target, and type; intervention relationships also give their address and condition.

Keep a corpus revision with assessment citations. Update schema, this reference, examples, and tests together when changing the draft format. There is no defined compatibility promise, executable diagnosis language, case-record schema, or severity scale yet.
