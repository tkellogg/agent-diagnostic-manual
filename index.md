# Agent Diagnostic Manual

A small XML corpus of agent symptoms, candidate diagnoses, and interventions, designed for independent tools and human readers.

Start with [the diagnostic process](docs/diagnostic-process.md): learn from past incidents, change the agent system, and use predictions about future behavior to refine the diagnosis. The [diagnostic skill](skills/agent-diagnostics/SKILL.md) and [format reference](skills/agent-diagnostics/references/format.md) explain how to work with the files.

Browse the XML entries for [symptoms](#symptoms), [diagnoses](#diagnoses), and [interventions](#interventions). The website lists all entries automatically.

## Symptoms

- [S001 — Repeated retrieval](symptoms/repeated-retrieval.md)

    An agent retrieves already-delivered information again without a new content, freshness, or verification need.

- [S002 — Doom looping](symptoms/doom-looping.md)

    An agent repeats an unsuccessful action cycle without relevant changes that would reasonably support expecting a different outcome.

- [S003 — Sudden performance degradation](symptoms/sudden-performance-degradation.md)

    An agent shows an abrupt, observable decline relative to its own recent performance on comparable work.

- [S004 — Excessive verification](symptoms/excessive-verification.md)

    An agent continues or expands verification beyond the task’s justified checking needs, delaying the requested outcome.

- [S005 — Correction without behavioral change](symptoms/correction-without-behavioral-change.md)

    An agent acknowledges a specific correction and then repeats the corrected behavior under comparable conditions.

- [S006 — Lost task constraints](symptoms/lost-task-constraints.md)

    A previously established task requirement or decision ceases to govern the agent’s later continuation.

- [S007 — Premature stopping](symptoms/premature-stopping.md)

    An agent ends its turn or run with authorized, actionable work remaining and no identified dependency requiring a stop.

- [S008 — Repeated reauthorization](symptoms/repeated-reauthorization.md)

    An agent requests permission again for an action that remains covered by a clear, applicable authorization.

- [S009 — Unrequested changes](symptoms/unrequested-changes.md)

    An agent modifies artifacts or system state beyond the authorized task scope without an established dependency that requires the change.

- [S010 — Claims completion while work is unfinished](symptoms/completion-artifact-mismatch.md)

    The agent says the requested work is done, but the delivered result still lacks something covered by that claim.

- [S011 — Unsupported verification claims](symptoms/unsupported-verification-claims.md)

    An agent reports verification with a result, scope, freshness, or attribution that the available execution evidence does not support.

- [S012 — Weakening the checks](symptoms/weakening-the-checks.md)

    An agent reduces verification’s ability to detect an unmet requirement while working on the problem that verification is meant to expose.

- [S013 — Agreement-driven reversal](symptoms/agreement-driven-reversal.md)

    An agent reverses a substantive conclusion toward a user’s assertion without establishing evidence or reasoning that supports the reversal.

- [S014 — Inferred values presented as observations](symptoms/inferred-values-as-observations.md)

    An output presents a calculated, estimated, or defaulted value as though it were directly reported by the source.

- [S015 — Opaque jargon (neuralese)](symptoms/opaque-jargon.md)

    The agent’s human-facing writing uses dense, unexplained labels or compressed phrasing that makes the reader reconstruct what it means.


## Diagnoses

- [D001 — Incorrect compaction](diagnoses/context-handoff-loss.md)

    The compaction prompt or algorithm drops information that later work still needs, so the agent repeats work, misses a requirement, or asks for permission again.

- [D002 — Tool discovery reports unusable tools](diagnoses/tool-discovery-delivery-gap.md)

    Tool search says a tool is ready, but the agent lacks the definition or access needed to call it. Searching again gives the same unusable result.

- [D003 — Overbroad verification instructions](diagnoses/verification-policy-overgeneralization.md)

    Instructions make the agent check more than the user’s task needs, often because several files repeat or contradict one another.

- [D004 — Component checks mistaken for complete verification](diagnoses/verification-scope-collapse.md)

    The workflow treats a passing component test as proof that the whole requested behavior works, even though the connections between components were never exercised.


## Interventions

- [I001 — Fix compaction so important information survives](interventions/preserve-task-relevant-evidence.md)

    Change the compaction instructions or implementation to preserve information that later work needs. Where the harness allows it, compare changes on a saved conversation before evaluating ordinary future work.

- [I002 — Consolidate verification instructions with the user](interventions/scope-verification-policy.md)

    Find the instructions that demand extra checking, remove duplicates and contradictions, and agree with the user on one simple account of what verification each kind of work needs.

- [I003 — Repair gaps between tests and real use](interventions/verify-acceptance-path.md)

    Audit where existing tests bypass connections that users rely on, then change the project’s test setup and QA instructions to cover those gaps on relevant future work.

- [I004 — Keep derived values out of source-only fields](interventions/separate-observed-derived-values.md)

    Change the collection and publication path so source observations, authorized calculations, and missing values remain distinguishable in future outputs.

- [I005 — Make discovered tools callable](interventions/complete-tool-discovery-handoff.md)

    Fix tool loading so search reports a tool as ready only after the agent has its definition and the runtime can execute it.


Symptoms describe observable behavior and can overlap in one episode. Each entry includes benign lookalikes, what to record, and examples, with brief recognition hints where helpful. Shared [observation methods](docs/observation-methods.md) describe ways to examine incidents. A symptom does not by itself establish a diagnosis or cause.

These are draft, unvalidated definitions. Synthetic examples are labeled; linked public reports and research observations motivate the definitions but do not validate their thresholds or establish prevalence. Reported cases are distinguished from independently audited traces. Severity remains deferred. Licensing remains to be decided.

## Use the skill

Distribute `skills/agent-diagnostics/` as a skill folder. It contains Markdown instructions and a format reference, with standard skill frontmatter and optional UI metadata. Copy it into a skill directory supported by your agent, then provide an ADM checkout or entry files. The corpus is a separate dependency; it is not duplicated inside the skill. Reading the skill directly also works without a skill-aware harness.

XML structure gives tools stable identities, relationships, and independently readable fields. The usage instructions are ordinary prose and do not need the same schema.

## Review the manual

On any website page, choose **Review this page** to open annotate.js. Highlight text, add a section note, or pin a comment, then post it. Move between entries and guides normally; comments stay attached to their pages.

Choose **Export all comments** above any article to download one `adm-review-YYYY-MM-DD.json` containing posted comments from every ADM page in this browser, including replies and resolved comments. Send that file for review. Exporting leaves your saved comments intact. Unposted drafts are not included. Annotate.js's own panel Download and Import buttons operate on one page; use ADM's button for the complete review.

Comments are private to this browser profile and site address. They do not sync between devices or go to a server. Use the same browser for a review pass and export a backup before clearing site data; private browsing or storage restrictions can prevent persistence.

After exporting a review round, choose **Clear all comments** to start fresh across every ADM page in this browser. Confirm the count in the dialog. **Undo clear** restores the last cleared round, including replies and resolved notes, while keeping new comments; it remains available after navigation or reload, until the next clear. Clearing also discards unposted drafts in open ADM tabs. Exported files and other browsers are unaffected. A single recovery copy stays in local browser storage, so this is a review reset, not a secure erase.

The site bundles [annotate.js](https://github.com/reviewjs/annotate) 1.5.3 and its MIT license locally. ADM's small export adapter reads that pinned version's project store. The JSON groups native page exports under `pages`, retaining entry IDs or guide paths, original URLs, quoted text, anchors, and threads.

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

Read the guides for [authoring symptoms](docs/authoring-symptom.md), [authoring diagnoses](docs/authoring-diagnosis.md), and [authoring interventions](docs/authoring-intervention.md). `docs/` holds public methodology and authoring guidance, independent of the distributable skill. Its Markdown pages are automatically published under “Using ADM” on the website, included in search, and available as adjacent `.html` and `.md` files.

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
