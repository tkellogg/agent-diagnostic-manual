#!/usr/bin/env python3
"""Validate canonical XML and build disposable HTML, Markdown, and JSON."""
import argparse
import hashlib
import html
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import yaml
from mkdocs.config import load_config
from mkdocs.commands.build import build as mkdocs_build
from markdown.extensions.toc import slugify
try:
    from .xml_entries import load, name, text, ast, N, METADATA, ITEMS
except ImportError:
    from xml_entries import load, name, text, ast, N, METADATA, ITEMS
ROOT=Path(__file__).resolve().parents[1]
TITLES={'definition':'How this could happen',
        'criteria':'What would support this explanation',
        'exclusions':'When this explanation may not fit',
        'differential':'Other explanations to consider',
        'relations':'Symptoms and predicted effects',
        'predictions':'What to expect if this explanation is right',
        'investigation':'Where to look next',
        'harness-notes':'In your harness'}
ENTRY_KINDS=[('symptom','Symptoms'),('diagnosis','Diagnoses'),('intervention','Interventions')]
INDEX_MARKER='<!-- ADM:ENTRY-INDEX -->'
PREDICTION_LABELS={'expected-improvement':'Expected improvement',
                   'still-necessary':'Still necessary',
                   'reason-to-reconsider':'A reason to reconsider',
                   'possible-harm':'Possible harm'}

class Renderer:
    def __init__(self,doc,objects,addresses,mode):
        self.doc=doc;self.objects=objects;self.addresses=addresses;self.mode=mode
    def esc(self,s):
        if self.mode=='html':return html.escape(s or '')
        return re.sub(r'([\\`*_{}\[\]|])',r'\\\1',html.escape(s or '',quote=False))
    def link(self,target,label):
        dest=self.objects[target]['document']['path']
        if self.mode=='md':dest=str(Path(dest).with_suffix('.md'))
        href=os.path.relpath(dest,str(Path(self.doc['path']).parent)).replace(os.sep,'/')
        if '#' in target:href+='#'+target.split('#',1)[1]
        if self.mode=='html':return f'<a href="{html.escape(href,quote=True)}">{label}</a>'
        return f'[{label}]({href})'
    def entry_link(self,target):
        doc=self.objects[target]['document']
        return self.link(target,self.esc(target+' — '+doc['meta']['title']))
    def children(self,n,depth):
        result='';links=[]
        def symptom_list():
            return ('<ul>'+''.join('<li>'+link+'</li>' for link in links)+'</ul>\n'
                    if self.mode=='html' else '\n'.join('- '+link for link in links)+'\n\n')
        for child in n:
            if name(child)=='symptom-ref':
                links.append(self.entry_link(child.get('ref')))
            else:
                if links:result+=symptom_list();links=[]
                result+=self.block(child,depth)
        if links:result+=symptom_list()
        return result
    def mixed(self,n):
        return self.esc(n.text)+''.join(self.inline(c)+self.esc(c.tail) for c in n)
    def inline(self,n):
        tag=name(n)
        if tag=='ref':return self.link(n.get('target'),self.mixed(n) or self.esc(n.get('target')))
        if tag=='a':
            label=self.mixed(n);href=n.get('href')
            return f'<a href="{html.escape(href,quote=True)}">{label}</a>' if self.mode=='html' else f'[{label}]({href})'
        if tag=='code':
            value=text(n)
            if self.mode=='html':return '<code>'+html.escape(value)+'</code>'
            fence='`'*(max([len(m) for m in re.findall(r'`+',value)]+[0])+1)
            return fence+' '+value+' '+fence
        value=self.mixed(n)
        if self.mode=='html':return f'<{tag}>{value}</{tag}>' if tag in ('strong','em') else value
        marker={'strong':'**','em':'*'}.get(tag,'')
        return marker+value+marker
    def anchor(self,n):
        address=self.addresses.get(n,'')
        if '#' not in address:return ''
        return '<a id="'+html.escape(address.split('#',1)[1],quote=True)+'"></a>\n'
    def heading(self,label,depth,anchor_id=None):
        depth=min(depth,6)
        if self.mode=='html':
            attr=' id="'+html.escape(anchor_id,quote=True)+'"' if anchor_id else ''
            return f'<h{depth}{attr}>{self.esc(label)}</h{depth}>\n'
        attr=' {#'+anchor_id+'}' if anchor_id else ''
        return '\n'+'#'*depth+' '+self.esc(label)+attr+'\n\n'
    def block(self,n,depth=2):
        tag=name(n)
        if tag in METADATA:return ''
        if tag=='discriminator':return self.anchor(n)+self.children(n,depth)
        if tag=='harness':
            heading=self.heading(n.get('title'),depth).rstrip()
            if self.mode=='md':heading+=' {data-adm-harness="'+n.get('id')+'"}'
            else:heading=heading.replace('>', ' data-adm-harness="'+n.get('id')+'">',1)
            return self.anchor(n)+heading+'\n\n'+self.children(n,depth+1)
        if tag=='predictions':
            items=[]
            for field in n:
                label=self.esc(PREDICTION_LABELS[name(field)])+':'
                content=self.children(field,depth).strip()
                anchor=self.anchor(field).strip()
                if self.mode=='html':
                    prefix='<strong>'+label+'</strong> '
                    content=('<p>'+prefix+content[3:] if content.startswith('<p>') else '<p>'+prefix+'</p>'+content)
                    items.append('<li>'+anchor+content+'</li>')
                else:
                    separator=' ' if name(field[0])=='p' else '\n\n'
                    content='**'+label+'**'+separator+content
                    items.append('- '+anchor+content.replace('\n','\n    '))
            listing='<ul>'+''.join(items)+'</ul>\n' if self.mode=='html' else '\n\n'.join(items)+'\n\n'
            return self.anchor(n)+self.heading(TITLES[tag],depth)+listing
        if tag=='p':return '<p>'+self.mixed(n)+'</p>\n' if self.mode=='html' else self.mixed(n)+'\n\n'
        if tag in ('ul','ol'):
            if self.mode=='html':return f'<{tag}>'+''.join('<li>'+self.mixed(c)+'</li>' for c in n)+f'</{tag}>\n'
            return '\n'.join((f'{i}. ' if tag=='ol' else '- ')+self.mixed(c) for i,c in enumerate(n,1))+'\n\n'
        if tag=='symptom-ref':
            value=self.entry_link(n.get('ref'))
            return '<p>'+value+'</p>\n' if self.mode=='html' else value+'\n\n'
        if tag=='intervention-ref':
            value=self.entry_link(n.get('ref'))
            condition=self.esc(n.findtext('a:when',namespaces=N))
            return (self.anchor(n)+self.anchor(n.find('a:when',N))+
                    (f'<h{depth}>Intervention: {value}</h{depth}><p><strong>Use this when:</strong> {condition}</p>\n' if self.mode=='html' else '\n'+'#'*depth+' Intervention: '+value+'\n\n**Use this when:** '+condition+'\n\n')+
                    self.block(n.find('a:predictions',N),depth+1))
        title=n.get('title') or TITLES.get(tag) or (n.get('id') or tag).replace('-',' ').capitalize()
        anchor_id=None
        if tag=='criterion':
            # Keep existing heading links and annotation selectors as numbers change.
            anchor_id=slugify(title,'-')
            title=str(n.getparent().index(n)+1)+'. '+title
        badge=''
        if tag=='example':
            label='Synthetic example' if n.get('kind')=='synthetic' else 'Reported example'
            badge='<span class="adm-example-kind">'+label+'</span>\n\n'
        return self.anchor(n)+self.heading(title,depth,anchor_id)+badge+self.children(n,depth+1)
    def body(self):
        return self.heading(self.doc['meta']['title'],1)+self.esc(self.doc['meta']['summary'])+'\n\n'+''.join(self.block(c) for c in self.doc['node'])

def build(root=ROOT,check=False,search=False):
    root=Path(root).resolve()
    docs,objects,addresses,refs=load(root)
    docs.sort(key=lambda d:(d['meta']['id'][0],int(d['meta']['id'][1:]),d['meta']['id']))
    if check:
        print(f'Validated {len(docs)} XML documents and {len(objects)} scoped addresses')
        return docs,objects,refs
    staging=root/'.build/docs'
    if staging.exists():shutil.rmtree(staging)
    staging.mkdir(parents=True)
    out=root/'dist'
    nav=[{'Home':'index.md'}]
    for kind,label in ENTRY_KINDS:
        nav.append({label:[{d['meta']['id']+' — '+d['meta']['title']:str(Path(d['path']).with_suffix('.md'))}
                           for d in docs if d['meta']['kind']==kind]})
    guide_nav=[]
    for source in sorted((root/'docs').rglob('*.md')):
        relative=source.relative_to(root)
        target=staging/relative
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(source,target)
        title=re.search(r'^#\s+(.+?)\s*#*\s*$',source.read_text(encoding='utf-8'),re.MULTILINE)
        guide_nav.append({title.group(1) if title else source.stem.replace('-',' ').capitalize():relative.as_posix()})
    nav.append({'Using ADM':guide_nav+[
        {'Diagnostic skill':'skills/agent-diagnostics/SKILL.md'},
        {'File format':'skills/agent-diagnostics/references/format.md'}]})
    for doc in docs:
        path=Path(doc['path'])
        md=staging/path.with_suffix('.md')
        md.parent.mkdir(parents=True,exist_ok=True)
        metadata={**doc['meta'],'xml_source':path.with_suffix('.xml').as_posix()}
        md.write_text('---\n'+yaml.safe_dump(metadata,sort_keys=False)+'---\n\n'+
                      Renderer(doc,objects,addresses,'md').body().strip()+'\n',encoding='utf-8')
        shutil.copyfile(root/doc['source'],staging/path.with_suffix('.xml'))
    # README provides the homepage prose; the corpus supplies its entry index.
    readme=(root/'README.md').read_text()
    if readme.count(INDEX_MARKER)!=1:
        raise ValueError('README must contain exactly one ADM entry index marker')
    sections=[]
    for kind,label in ENTRY_KINDS:
        entries=[doc for doc in docs if doc['meta']['kind']==kind]
        lines=['## '+label, '']
        if not entries:lines.append('No entries yet.')
        for doc in entries:
            render=Renderer(doc,objects,addresses,'md')
            label_text=render.esc(doc['meta']['id']+' — '+doc['meta']['title'])
            path=Path(doc['path']).with_suffix('.md').as_posix()
            lines.append('- ['+label_text+']('+path+')\n\n    '+render.esc(doc['meta']['summary'])+'\n')
        sections.append('\n'.join(lines))
    readme=readme.replace(INDEX_MARKER,'\n\n'.join(sections))
    # Directory links in the repository README lead to generated section anchors.
    for kind,label in ENTRY_KINDS:
        readme=readme.replace('](entries/'+label.lower()+'/)','](#'+label.lower()+')')
    for doc in docs:
        readme=readme.replace(']('+doc['source']+')',']('+str(Path(doc['path']).with_suffix('.md'))+')')
    (staging/'index.md').write_text(readme,encoding='utf-8')
    shutil.copytree(root/'skills',staging/'skills')
    shutil.copytree(root/'schema',staging/'schema')
    shutil.copytree(root/'website/assets',staging/'assets')
    # Ship a pinned, self-hosted annotation layer, including its MIT license.
    annotate=root/'node_modules/@reviewjs/annotate'
    if not (annotate/'package.json').exists():
        raise ValueError('Run npm ci before building the site (annotate.js is required)')
    if json.loads((annotate/'package.json').read_text())['version']!='1.5.3':
        raise ValueError('The review export adapter requires annotate.js 1.5.3; run npm ci')
    vendor=staging/'assets/vendor'
    vendor.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(annotate/'annotate.js',vendor/'annotate-1.5.3.js')
    shutil.copyfile(annotate/'LICENSE',vendor/'annotate-LICENSE.txt')
    catalog={'schema_version':7,'xml_namespace':'urn:adm:1',
        'documents':[{**d['meta'],'source':d['source'],'url':d['path'],'document':ast(d['node'])} for d in docs],
        'objects':{key:{'document':o['document']['meta']['id'],'kind':name(o['node']),'source':o['document']['source'],'url':o['document']['path']+('#'+key.split('#',1)[1] if '#' in key else '')} for key,o in objects.items()},'relationships':refs}
    (staging/'catalog.json').write_text(json.dumps(catalog,indent=2)+'\n',encoding='utf-8')
    # A content version prevents an old cached stylesheet accompanying new HTML.
    asset_version=hashlib.sha256((root/'website/assets/adm.css').read_bytes()+
                                 (root/'website/assets/adm.js').read_bytes()+
                                 (root/'website/assets/adm-harness.js').read_bytes()+
                                 (root/'website/assets/adm-review.js').read_bytes()).hexdigest()[:12]
    # Loading repository hooks must not create cache files among the sources.
    previous_bytecode=sys.dont_write_bytecode
    try:
        sys.dont_write_bytecode=True
        config=load_config(config_file=str(root/'mkdocs.yml'),nav=nav,strict=True,
                           extra_css=['assets/adm.css?v='+asset_version],
                           extra={'asset_version':asset_version})
        mkdocs_build(config)
    finally:
        sys.dont_write_bytecode=previous_bytecode
    # MkDocs consumes Markdown; expose exact source variants alongside HTML.
    for md in staging.rglob('*.md'):
        target=out/md.relative_to(staging)
        target.parent.mkdir(parents=True,exist_ok=True)
        shutil.copyfile(md,target)
    (out/'.nojekyll').touch()
    if search:
        subprocess.run(['npm','run','search'],cwd=root,check=True)
    print(f'Validated {len(docs)} XML documents and {len(objects)} scoped addresses; built dist/')
    return docs,objects,refs

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--check',action='store_true')
    p.add_argument('--no-search',action='store_true',help='Skip Pagefind for fast local iterations')
    args=p.parse_args()
    try:build(check=args.check,search=not args.no_search)
    except (ValueError,UnicodeError,subprocess.CalledProcessError) as e:p.exit(1,str(e)+'\n')
