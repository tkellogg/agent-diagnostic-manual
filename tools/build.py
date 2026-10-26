#!/usr/bin/env python3
"""Validate ASM source and render portable HTML plus a metadata catalog."""
from __future__ import annotations
import argparse
import copy
import html
from html.parser import HTMLParser
import json
import os
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit, urlunsplit
import markdown
import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = {
    'symptom': ['Observation', 'How to recognize it', 'Benign lookalikes', 'What to record', 'Examples'],
    'diagnosis': ['Definition', 'Candidate criteria', 'Exclusions', 'Differential diagnosis', 'Investigation', 'Interventions', 'Evidence and uncertainty'],
    'intervention': ['Purpose', 'Preconditions', 'Procedure', 'Evaluation', 'Risks and confounders', 'Stop and rollback', 'Evidence and uncertainty'],
}

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f'duplicate YAML key: {key}')
        result[key] = loader.construct_object(value_node, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a' and 'href' in attrs:
            self.links.append(attrs['href'])

def parse(path: Path, content_root: Path, validator):
    text = path.read_text(encoding='utf-8')
    parts = text.split('---\n', 2)
    if len(parts) != 3 or parts[0]:
        raise ValueError(f'{path}: expected YAML frontmatter')
    meta = yaml.load(parts[1], Loader=UniqueLoader)
    errors = list(validator.iter_errors(meta))
    if errors:
        raise ValueError(f'{path}: ' + '; '.join(e.message for e in errors))
    body = parts[2]
    headings = re.findall(r'^## (.+)$', body, flags=re.M)
    for heading in SECTIONS.get(meta['kind'], []):
        if heading not in headings:
            raise ValueError(f'{path}: missing section {heading}')
    rendered = markdown.markdown(body, extensions=['tables', 'fenced_code', 'toc'])
    links = Links()
    links.feed(rendered)
    return {'meta': meta, 'body': body, 'html': rendered,
            'path': path.relative_to(content_root).as_posix(), 'links': links}

def resolve_local(source, href, content_root):
    url = urlsplit(href)
    if url.scheme or url.netloc:
        if url.scheme not in ('http', 'https', 'mailto'):
            raise ValueError(f'{source}: unsupported link scheme: {href}')
        return None
    if url.path.startswith('/'):
        raise ValueError(f'{source}: use relative links: {href}')
    target = ((content_root / source).parent / unquote(url.path)).resolve() if url.path else (content_root / source).resolve()
    if not target.is_relative_to(content_root.resolve()):
        raise ValueError(f'{source}: link escapes content: {href}')
    return target.relative_to(content_root.resolve()).as_posix(), unquote(url.fragment)

def load(content_root: Path, schema_path: Path):
    validator = Draft202012Validator(json.loads(schema_path.read_text()), format_checker=FormatChecker())
    pages = [parse(p, content_root, validator) for p in sorted(content_root.rglob('*.md'))]
    by_id = {}
    by_path = {p['path']: p for p in pages}
    edges = []
    for page in pages:
        meta = page['meta']
        if meta['id'] in by_id:
            raise ValueError(f'duplicate ID: {meta["id"]}')
        by_id[meta['id']] = page
    for page in pages:
        meta = page['meta']
        relations = [(s, 'symptom', {}) for s in meta.get('symptoms', [])]
        relations += [(i['id'], 'intervention', {k: v for k, v in i.items() if k != 'id'}) for i in meta.get('interventions', [])]
        seen = set()
        for target, kind, details in relations:
            if target in seen:
                raise ValueError(f'{meta["id"]}: duplicate relationship {target}')
            seen.add(target)
            if target not in by_id or by_id[target]['meta']['kind'] != kind:
                raise ValueError(f'{meta["id"]}: invalid {kind} reference {target}')
            edges.append({'from': meta['id'], 'to': target, 'relation': kind, **details})
        for href in page['links'].links:
            local = resolve_local(page['path'], href, content_root)
            if local is None:
                continue
            path, fragment = local
            if path not in by_path:
                raise ValueError(f'{page["path"]}: missing linked page {href}')
            if fragment and fragment not in by_path[path]['links'].ids:
                raise ValueError(f'{page["path"]}: missing anchor {href}')
    return pages, by_id, edges

def relative_html(source, target):
    target = str(Path(target).with_suffix('.html'))
    return os.path.relpath(target, str(Path(source).parent)).replace(os.sep, '/')

def render(page, by_id, edges):
    escape = html.escape
    def rewrite(match):
        href = html.unescape(match.group(1))
        url = urlsplit(href)
        if not url.scheme and not url.netloc and url.path.endswith('.md'):
            href = urlunsplit(('', '', url.path[:-3] + '.html', url.query, url.fragment))
        return 'href="' + escape(href, quote=True) + '"'
    body = re.sub(r'href="([^"]*)"', rewrite, page['html'])
    meta = page['meta']
    def link(target, label=None):
        dest = by_id[target]
        return f'<a href="{escape(relative_html(page["path"], dest["path"]))}">{escape(label or dest["meta"]["title"])}</a>'
    nav = ''.join(link(i, label) for i, label in [('manual','ASM'),('symptoms','Symptoms'),('diagnoses','Diagnoses'),('interventions','Interventions'),('structure','Structure')])
    connections = []
    for edge in edges:
        if edge['from'] == meta['id']:
            label = 'Symptom' if edge['relation'] == 'symptom' else 'Intervention · ' + edge['role']
            condition = f'<p>{escape(edge["when"])} <small>Evidence: {escape(edge["evidence"])}</small></p>' if 'when' in edge else ''
            connections.append(f'<li><small>{escape(label)}</small> {link(edge["to"])}{condition}</li>')
        elif edge['to'] == meta['id']:
            condition = f'<p>{escape(edge["when"])} <small>Role: {escape(edge["role"])} · Evidence: {escape(edge["evidence"])}</small></p>' if 'when' in edge else ''
            connections.append(f'<li><small>Referenced by</small> {link(edge["from"])}{condition}</li>')
    related = '<aside><h2>Connections</h2><ul>' + ''.join(connections) + '</ul></aside>' if connections else ''
    badges = ' · '.join(escape(str(meta[k])) for k in ['id','kind','status','evidence'] if k in meta)
    home = relative_html(page['path'], 'index.md')
    catalog = os.path.relpath('catalog.json', str(Path(page['path']).parent)).replace(os.sep, '/')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{escape(meta['title'])} · ASM</title><meta name="description" content="{escape(meta['summary'], quote=True)}">
<style>{CSS}</style></head><body><a class="skip" href="#main">Skip to content</a>
<header><nav aria-label="Main">{nav}</nav></header><main id="main"><div class="eyebrow">{badges}</div>
<p class="abstract">{escape(meta['summary'])}</p>{body}{related}</main>
<footer><a href="{home}">Agent Diagnostic Manual</a> · Working draft · Updated {escape(meta['updated'])} · <a href="{catalog}">JSON catalog</a></footer></body></html>'''

CSS = '''
:root{color-scheme:light;--ink:#192c3c;--muted:#526474;--line:#d9e0e4;--accent:#0c666c}
*{box-sizing:border-box}body{margin:0;background:#f9faf7;color:var(--ink);font:17px/1.7 system-ui,-apple-system,sans-serif}
header{background:#182d3e;border-bottom:4px solid #65bdb0}nav{max-width:1120px;margin:auto;display:flex;gap:26px;padding:22px 28px;flex-wrap:wrap}nav a{color:#f4f8f7;text-decoration:none;font-size:15px}nav a:first-child{font-weight:800;letter-spacing:.15em;margin-right:auto}
main{max-width:1000px;margin:55px auto;padding:0 28px}h1{font-size:clamp(30px,5vw,45px);line-height:1.18;letter-spacing:-.035em;margin:22px 0 30px}h2{font-size:24px;margin:42px 0 14px;line-height:1.3}h3{font-size:20px}p,li{max-width:82ch}a{color:var(--accent);text-underline-offset:3px}a:hover{text-decoration-thickness:2px}a:focus-visible{outline:3px solid #c77b2c;outline-offset:4px}.eyebrow{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);font-weight:700}.abstract{color:var(--muted);font-size:19px;max-width:72ch}table{border-collapse:collapse;width:100%;font-size:15px;margin:24px 0}th,td{border-bottom:1px solid var(--line);padding:14px;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#eaf0ef;font-size:13px}code{background:#eaf0ef;padding:2px 5px;border-radius:3px;font-size:.87em}pre{background:#182d3e;color:#f4f8f7;border-radius:8px;padding:22px;overflow:auto}pre code{background:none;padding:0}li{margin:9px 0}aside{margin-top:48px;border:1px solid var(--line);border-left:4px solid #65bdb0;padding:8px 24px 20px;background:#fff}aside h2{margin-top:18px}aside ul{padding-left:20px}aside small{color:var(--muted);display:block;font-size:12px}aside p{margin:4px 0 18px;font-size:15px}footer{max-width:1000px;margin:60px auto 30px;padding:24px 28px;border-top:1px solid var(--line);color:var(--muted);font-size:12px}.skip{position:absolute;left:-999px}.skip:focus{left:10px;top:10px;background:white;padding:10px} @media(max-width:600px){nav{gap:14px;padding:18px}main{padding:0 18px;margin:32px auto}th,td{padding:10px 7px;font-size:13px}h2{margin-top:32px}footer{padding:20px 18px}}
'''

def build(root=ROOT, check=False):
    pages, by_id, edges = load(root/'content', root/'schema/entry.schema.json')
    if not check:
        out = root/'dist'
        out.mkdir(exist_ok=True)
        for page in pages:
            dest = out / Path(page['path']).with_suffix('.html')
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(render(page, by_id, edges), encoding='utf-8')
        catalog = {'schema_version': 1, 'entries': [{**copy.deepcopy(p['meta']), 'source': 'content/'+p['path'], 'url': str(Path(p['path']).with_suffix('.html'))} for p in pages], 'relationships': edges}
        (out/'catalog.json').write_text(json.dumps(catalog, indent=2)+'\n', encoding='utf-8')
    print(f'Validated {len(pages)} pages, {len(edges)} typed relationships' + ('' if check else '; built dist/'))
    return pages, edges

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        build(check=args.check)
    except (ValueError, yaml.YAMLError) as error:
        parser.exit(1, str(error)+'\n')
