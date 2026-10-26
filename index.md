# Agent Diagnostic Manual (ADM)

A small XML corpus of agent symptoms, candidate diagnoses, and interventions, designed for independent tools and human readers.

Start with [how to use the files](skills/agent-diagnostics/SKILL.md) and the [format reference](skills/agent-diagnostics/references/format.md).

The first worked example:

- [S001 — Repeated retrieval](symptoms/repeated-retrieval.md)
- [D001 — Unproductive repeated retrieval](diagnoses/unproductive-repeated-retrieval.md)
- [I001 — Preserve task-relevant evidence](interventions/preserve-task-relevant-evidence.md)

## Symptoms

The symptom directory includes the original repeated-retrieval entry and twelve additional working definitions:

- [S002 — Doom looping](symptoms/doom-looping.md)
- [S003 — Sudden performance degradation](symptoms/sudden-performance-degradation.md)
- [S004 — Excessive verification](symptoms/excessive-verification.md)
- [S005 — Correction without behavioral change](symptoms/correction-without-behavioral-change.md)
- [S006 — Lost task constraints](symptoms/lost-task-constraints.md)
- [S007 — Premature stopping](symptoms/premature-stopping.md)
- [S008 — Repeated reauthorization](symptoms/repeated-reauthorization.md)
- [S009 — Unrequested changes](symptoms/unrequested-changes.md)
- [S010 — Completion–artifact mismatch](symptoms/completion-artifact-mismatch.md)
- [S011 — Unsupported verification claims](symptoms/unsupported-verification-claims.md)
- [S012 — Weakening the checks](symptoms/weakening-the-checks.md)
- [S013 — Agreement-driven reversal](symptoms/agreement-driven-reversal.md)

Symptoms describe observable behavior and can overlap in one episode. Each entry includes recognition guidance, benign lookalikes, what to record, and examples. A symptom does not by itself establish a diagnosis or cause.

These are draft, unvalidated definitions. Synthetic examples are labeled; linked public reports and research observations motivate the definitions but do not validate their thresholds or establish prevalence. Reported cases are distinguished from independently audited traces. Severity remains deferred. Licensing remains to be decided.

## Use the skill

Distribute `skills/agent-diagnostics/` as a skill folder. It contains Markdown instructions and a format reference, with standard skill frontmatter and optional UI metadata. Copy it into a skill directory supported by your agent, then provide an ADM checkout or entry files. The corpus is a separate dependency; it is not duplicated inside the skill. Reading the skill directly also works without a skill-aware harness.

XML structure gives tools stable identities, relationships, and independently readable fields. The usage instructions are ordinary prose and do not need the same schema.

## Build and read

Python 3.11+ and Node.js 22+:

```sh
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
npm ci
python tools/build.py
python -m http.server 8000 --directory dist --bind 127.0.0.1
```

Open `http://127.0.0.1:8000`. MkDocs builds the site and Pagefind adds local, static search. Each entry has adjacent `.html`, `.md`, and `.xml` files, with format links on the HTML page. For example, replace `symptoms/repeated-retrieval.html` with `symptoms/repeated-retrieval.md` or `symptoms/repeated-retrieval.xml`. The build also writes `dist/catalog.json`. All output is disposable and ignored by Git. Edit XML and rebuild.

## Authoring

`entries/` contains canonical symptoms, diagnoses, and interventions. [XSD](schema/adm-v1.xsd) validates document structure; the [format reference](skills/agent-diagnostics/references/format.md) defines cross-document rules. The builder is a reference implementation.

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

The independent example uses only Python's standard library and imports no ADM code. Consumers do not need an LLM, the reference builder, or a hosted service.

## Releases

Run **Actions → Release ADM → Run workflow**, select `main`, and enter a version without the `v` prefix. Start with `0.1.0`. The workflow captures HEAD of main at checkout, validates XML and references, runs tests, builds all formats and search, and publishes tag `v0.1.0` and release assets. An existing tag is rejected rather than moved.

The ZIP contains `html/` (the complete searchable site with adjacent source variants), `markdown/`, `xml/entries/`, `xml/schema/`, the distributable `skills/` folder, and `manifest.json` with the source commit and per-file SHA-256 hashes. A separate checksum covers the ZIP. Serve `html/` over HTTP to use search.

To build the same package locally after building the site:

```sh
python tools/package_release.py --version 0.1.0 --commit "$(git rev-parse HEAD)"
```

## GitHub Pages

Every push to main validates and builds the site, stores a complete generated copy on `gh-pages`, and deploys it through GitHub Actions. No repository variables are required. Generated branch commits do not trigger the main-branch workflows.

In **Settings → Pages**, select **GitHub Actions** as the source and save **diag.timkellogg.me** as the custom domain. At the DNS provider, set `diag` to a CNAME targeting `tkellogg.github.io.` (without a repository path). Enable **Enforce HTTPS** once GitHub has issued the certificate. DNS and certificate provisioning may take time; saving the custom domain in the repository is required in addition to DNS.

The Pages workflow builds with MkDocs and Pagefind; no separate Jekyll workflow is needed. With Actions-based publishing, GitHub uses the custom domain saved in repository settings, not a CNAME file in the artifact.

`mkdocs.yml` sets `https://diag.timkellogg.me/` as the canonical site URL and disables directory-style URLs. All normal page assets and format links are relative. The README is the homepage source. To skip search during quick local iterations, use `python tools/build.py --no-search`.

The CI, release, and Pages workflows all validate against `schema/adm-v1.xsd` and check document IDs, local IDs, and typed references before building.
