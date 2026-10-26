# Agent Diagnostic Manual (ASM)

A small XML corpus of agent symptoms, candidate diagnoses, and interventions, designed for independent tools and human readers.

Start with the [structure](guides/structure.xml) and [format contract](guides/format.xml).

The first worked example:

- [S001 — Repeated retrieval](entries/symptoms/repeated-retrieval.xml)
- [D001 — Unproductive repeated retrieval](entries/diagnoses/unproductive-repeated-retrieval.xml)
- [I001 — Preserve task-relevant evidence](entries/interventions/preserve-task-relevant-evidence.xml)

These are draft, unvalidated entries. Examples are synthetic. Severity remains deferred. The repository is private; publication and licensing are separate decisions.

## Build and read

Python 3.11+:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python tools/build.py
python -m http.server 8000 --directory dist --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. The build also writes Markdown reading copies under `dist/markdown/` and a structured `dist/catalog.json`. All output is disposable and ignored by Git. Edit XML and rebuild.

## Authoring

`entries/` contains canonical symptoms, diagnoses, and interventions. `guides/` contains canonical explanatory documents and navigation. [XSD](schema/asm-v1.xsd) validates document structure; the [format contract](guides/format.xml) defines cross-document rules. The builder is a reference implementation.

Singleton sections use tag names; list members use short, locally unique IDs:

```xml
<observations>
  <observation id="multi-read">
    <p>The agent retrieves substantially the same information repeatedly.</p>
  </observation>
</observations>
```

Reference that item as `S001#observations/multi-read`. Reference a singleton as `S001#what-to-record`. Local IDs may repeat in different lists or documents.

## Validate and consume

```sh
python tools/build.py --check
python -m unittest discover -s tests
python examples/query_manual.py
```

The independent example uses only Python's standard library and imports no ASM code. Consumers do not need an LLM, the reference builder, or a hosted service.
