# ADM file format

Use this reference when reading, parsing, linking, or editing ADM files. The corpus is XML; this skill and its instructions are Markdown.

## Source and identity

Read UTF-8 XML in namespace `urn:adm:1` with `version="1"`. The namespace is an identifier, not a network resource. The three root kinds and locations are:

| Root | Directory | Document ID |
| --- | --- | --- |
| symptom | entries/symptoms/ | S followed by at least three digits |
| diagnosis | entries/diagnoses/ | D followed by at least three digits |
| intervention | entries/interventions/ | I followed by at least three digits |

Require corpus-wide, case-sensitive document IDs. Documents carry title, summary, editorial status, update date, and evidence status. Titles are plain-text attributes on documents, criteria, and differential alternatives. Summary is a child element. Diagnoses use `unit="configured-agent-system"`: episodes supply evidence about that system. A diagnosis contains a working explanation in `definition`; there is no separate descriptive-diagnosis level.

Use one to three lowercase kebab-case words for list-member IDs, matching `[a-z][a-z0-9]*(-[a-z][a-z0-9]*){0,2}`. Require uniqueness only within the containing list. The same local ID can occur in another list or document. Preserve identity when rearranging items; do not reuse an ID for a different meaning.

Give singleton sections and containers no ID: their tag names identify them. Keep structured lists free of introductory or trailing prose.

## Addresses and relationships

Form an address from a document ID, optionally followed by `#` and a slash-separated structural path. Use singleton tag names and list-member IDs:

| Address | Meaning |
| --- | --- |
| S001 | Whole symptom |
| S001#observations/multi-read | One observation |
| S001#what-to-record | Singleton prose section |
| D001#criteria/delivery-loss | One criterion |
| D001#differential/policy-conflict/discriminator | One alternative's discriminator |
| D001#relations/I001/when | Applicability condition |
| D001#relations/I001/predictions | Predictions for this pairing |
| I001#procedure/locate-boundary | One ordered step |

Use `<ref target="S001#observations/multi-read">label</ref>` for corpus links. Require fully qualified addresses, even inside the same document. Resolve IDs from the corpus rather than guessing filenames.

Use `<symptom-ref ref="S001"/>` for a symptom relationship. An intervention relationship has a plain-text condition and a required prose predictions block:

```xml
<intervention-ref ref="I001">
  <when>Needed state is lost at a context transition.</when>
  <predictions>
    <p>Relevant failures should decline after confirmed delivery; persistence weakens the omission explanation.</p>
  </predictions>
</intervention-ref>
```

Require a whole-document target of the matching kind. The target identifies an intervention reference within the diagnosis's relations list; no separate ID or evidence attribute is needed. Predictions describe the diagnosis–intervention combination and are adapted to the configuration before use. They are prose, not executable tests. Reject duplicate entry-level relationships to the same target. A criterion can also reference symptoms; those references identify relevant symptoms, while the criterion's prose specifies the requirement.

## Entry structure

For symptoms, read observations, how-to-recognize-it, benign-lookalikes, what-to-record, and examples. Observations, lookalikes, and examples are individually addressable items. Examples declare `kind="synthetic"` or `kind="observed"`.

For diagnoses, read relations, definition, criteria, exclusions, differential, investigation, interventions, and evidence-and-uncertainty. Criteria, exclusions, and alternatives have local IDs. Each alternative contains a singleton discriminator. Interpret `criteria operator="all"` as requiring support for every criterion; missing information remains unknown. This combines judgments about prose, not executable predicates.

For interventions, read purpose, preconditions, procedure, evaluation, risks-and-confounders, stop-and-rollback, and evidence-and-uncertainty. Preconditions and steps have local IDs; procedure order follows document order. Interventions describe lasting system changes whose outcomes can also test an explanation.

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

The catalog uses `schema_version: 4` and exposes document metadata and an ordered XML-derived tree, an address index, and explicit relationships. Tree nodes have name, attributes, and ordered content. Content interleaves strings and child nodes; indentation-only structural whitespace is omitted. Address-index records give document, kind, source, and rendered URL. Relationships give their nearest addressable owner, target, and type; intervention relationships also give their address, plain-text `when`, and `predictions` as an XML-derived tree so inline links and formatting remain available to scripts.

Keep a corpus revision with assessment citations. Update schema, this reference, examples, and tests together when changing the draft format. There is no defined compatibility promise, executable diagnosis language, case-record schema, or severity scale yet.
