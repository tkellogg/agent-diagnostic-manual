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

The builder validates frontmatter, unique IDs, typed references, required entry sections, and local links; then renders pages, backlinks, and `dist/catalog.json`. CI performs the same checks and builds without deploying.

## Authoring

Edit `content/**/*.md`. YAML frontmatter stores stable identity and relationships; Markdown carries explanations, criteria, and protocols. Read the [content contract](content/structure.md#content-contract) before adding an entry. Generated HTML and JSON are disposable; source Markdown is canonical.

There is exactly one symptom and one diagnosis in this first iteration. Expand from reviewed cases rather than brainstorming a large taxonomy.
