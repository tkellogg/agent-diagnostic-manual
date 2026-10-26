# Agent Diagnostic Manual (ASM)

A slowly growing, linked manual of agent symptoms, candidate diagnoses, and interventions. **ASM** is the project's chosen short name.

**Start reading:** [Manual home](content/index.md) · [Structure and design decisions](content/structure.md)

The first worked example:

1. [S001 — Repeated retrieval](content/symptoms/repeated-retrieval.md): the observation, including benign lookalikes.
2. [D001 — Unproductive repeated retrieval](content/diagnoses/unproductive-repeated-retrieval.md): a candidate descriptive diagnosis, with criteria and a differential.
3. [I001 — Preserve task-relevant evidence](content/interventions/preserve-task-relevant-evidence.md): an experimental protocol, linked conditionally rather than presented as a cure.

These entries are **drafts and unvalidated**. Examples are synthetic; no empirical case or treatment result is claimed. Severity is deliberately deferred.

## Read as a site

Python 3.11+:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python tools/build.py
python -m http.server 8000 --directory dist --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. The output is also ordinary static HTML with relative links. No hosting or deployment is configured. Keep publication a separate decision from repository visibility.

## Validate without building

```sh
python tools/build.py --check
python -m unittest discover -s tests
```

The builder validates XML against XSD, corpus IDs and references, guide metadata, and local links; then renders Markdown, HTML, backlinks, and `dist/catalog.json`. CI performs the same checks and builds without deploying.

## Authoring and independent tools

Edit `entries/**/*.xml` for symptoms, diagnoses, and interventions. Run `python tools/build.py` and commit both the XML source and generated Markdown reader pages. General guides and index pages in `content/` remain authored Markdown.

The [XML format contract](content/format.md) and [XSD](schema/asm-v1.xsd) define the draft format. The builder is a reference implementation. Criteria, exclusions, alternatives, preconditions, procedure steps, and applicability relationships have stable IDs. Consumers need neither an LLM nor this implementation.

```sh
python examples/query_manual.py
python tools/build.py --check-generated
```

The example consumer uses only Python's standard library. The generated JSON catalog retains the structured document tree and object-level references. CI checks XML validity, cross-document links, and generated-file freshness before building.

There is still exactly one symptom and one diagnosis. Severity remains deferred. The repository stays private; publication and licensing are separate future decisions.
