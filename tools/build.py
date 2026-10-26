#!/usr/bin/env python3
"""Validate canonical XML and build disposable HTML, Markdown, and JSON."""
import argparse
import html
import json
import os
from pathlib import Path
import re
import shutil
try:
    from .xml_entries import load, name, text, ast, N, METADATA, ITEMS
except ImportError:
    from xml_entries import load, name, text, ast, N, METADATA, ITEMS
ROOT=Path(__file__).resolve().parents[1]
TITLES={'criteria':'Candidate criteria','differential':'Differential diagnosis','relations':'Relationships'}

class Renderer:
    def __init__(self,doc,objects,addresses,mode):
        self.doc=doc;self.objects=objects;self.addresses=addresses;self.mode=mode
    def esc(self,s):
        if self.mode=='html':return html.escape(s or '')
        return re.sub(r'([\\`*_{}\[\]<>|])',r'\\\1',s or '')
    def link(self,target,label):
        dest=self.objects[target]['document']['path']
        if self.mode=='md':dest=str(Path(dest).with_suffix('.md'))
        href=os.path.relpath(dest,str(Path(self.doc['path']).parent)).replace(os.sep,'/')
        if '#' in target:href+='#'+target.split('#',1)[1]
        if self.mode=='html':return f'<a href="{html.escape(href,quote=True)}">{label}</a>'
        return f'[{label}]({href})'
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
    def heading(self,label,depth):
        depth=min(depth,6)
        return f'<h{depth}>{self.esc(label)}</h{depth}>\n' if self.mode=='html' else '\n'+'#'*depth+' '+self.esc(label)+'\n\n'
    def block(self,n,depth=2):
        tag=name(n)
        if tag in METADATA:return ''
        if tag=='p':return '<p>'+self.mixed(n)+'</p>\n' if self.mode=='html' else self.mixed(n)+'\n\n'
        if tag in ('ul','ol'):
            if self.mode=='html':return f'<{tag}>'+''.join('<li>'+self.mixed(c)+'</li>' for c in n)+f'</{tag}>\n'
            return '\n'.join((f'{i}. ' if tag=='ol' else '- ')+self.mixed(c) for i,c in enumerate(n,1))+'\n\n'
        if tag=='pre':
            value=''.join(n.itertext())
            if self.mode=='html':return '<pre><code>'+html.escape(value)+'</code></pre>\n'
            fence='`'*max(3,1+max([len(m) for m in re.findall(r'`+',value)]+[0]))
            return fence+'\n'+value.rstrip()+'\n'+fence+'\n\n'
        if tag=='table':
            if self.mode=='html':
                return '<table>'+''.join('<'+name(group)+'>'+''.join('<tr>'+''.join('<'+name(cell)+'>'+self.mixed(cell)+'</'+name(cell)+'>' for cell in row)+'</tr>' for row in group)+'</'+name(group)+'>' for group in n)+'</table>\n'
            rows=list(n.findall('a:thead/a:tr',N))+list(n.findall('a:tbody/a:tr',N))
            lines=['| '+' | '.join(self.mixed(c) for c in row)+' |' for row in rows]
            lines.insert(1,'| '+' | '.join('---' for _ in rows[0])+' |')
            return '\n'.join(lines)+'\n\n'
        if tag=='symptom-ref':
            value=self.link(n.get('ref'),self.esc(n.get('ref')))
            return '<p>Related symptom: '+value+'</p>\n' if self.mode=='html' else 'Related symptom: '+value+'\n\n'
        if tag=='intervention-ref':
            value=self.link(n.get('ref'),self.esc(n.get('ref')))
            condition=self.esc(n.findtext('a:when',namespaces=N))
            return self.anchor(n)+self.anchor(n.find('a:when',N))+(f'<p>{value}</p><p><strong>When:</strong> {condition}</p>\n' if self.mode=='html' else value+'\n\n**When:** '+condition+'\n\n')
        if tag=='sections':return self.anchor(n)+''.join(self.block(c,depth) for c in n)
        title=n.get('title') or TITLES.get(tag) or (n.get('id') or tag).replace('-',' ').capitalize()
        return self.anchor(n)+self.heading(title,depth)+''.join(self.block(c,depth+1) for c in n)
    def body(self):
        return self.heading(self.doc['meta']['title'],1)+''.join(self.block(c) for c in self.doc['node'])

def build(root=ROOT,check=False):
    docs,objects,addresses,refs=load(root)
    if not check:
        out=root/'dist'
        if out.exists():shutil.rmtree(out)
        out.mkdir()
        for doc in docs:
            dest=out/doc['path'];dest.parent.mkdir(parents=True,exist_ok=True)
            renderer=Renderer(doc,objects,addresses,'html');m=doc['meta']
            nav=' '.join(renderer.link(i,label) for i,label in [('manual','ASM'),('symptoms','Symptoms'),('diagnoses','Diagnoses'),('interventions','Interventions'),('structure','Structure'),('format','Format')])
            badges=' · '.join(html.escape(m[k]) for k in ('id','kind','status','evidence') if k in m)
            dest.write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+html.escape(m['title'])+' · ASM</title><style>'+CSS+'</style></head><body><header><nav>'+nav+'</nav></header><main><div class="eyebrow">'+badges+'</div>'+renderer.body()+'</main></body></html>',encoding='utf-8')
            md=out/'markdown'/Path(doc['path']).with_suffix('.md');md.parent.mkdir(parents=True,exist_ok=True)
            md.write_text('<!-- Generated from '+doc['source']+'; edit XML and rebuild. -->\n\n'+Renderer(doc,objects,addresses,'md').body().strip()+'\n',encoding='utf-8')
        catalog={'schema_version':3,'xml_namespace':'urn:asm:1',
            'documents':[{**d['meta'],'source':d['source'],'url':d['path'],'document':ast(d['node'])} for d in docs],
            'objects':{key:{'document':o['document']['meta']['id'],'kind':name(o['node']),'source':o['document']['source'],'url':o['document']['path']+('#'+key.split('#',1)[1] if '#' in key else '')} for key,o in objects.items()},'relationships':refs}
        (out/'catalog.json').write_text(json.dumps(catalog,indent=2)+'\n',encoding='utf-8')
    print(f'Validated {len(docs)} XML documents and {len(objects)} scoped addresses'+('' if check else '; built dist/'))
    return docs,objects,refs

CSS='\n:root{color-scheme:light;--ink:#192c3c;--muted:#526474;--line:#d9e0e4;--accent:#0c666c}\n*{box-sizing:border-box}body{margin:0;background:#f9faf7;color:var(--ink);font:17px/1.7 system-ui,-apple-system,sans-serif}\nheader{background:#182d3e;border-bottom:4px solid #65bdb0}nav{max-width:1120px;margin:auto;display:flex;gap:26px;padding:22px 28px;flex-wrap:wrap}nav a{color:#f4f8f7;text-decoration:none;font-size:15px}nav a:first-child{font-weight:800;letter-spacing:.15em;margin-right:auto}\nmain{max-width:1000px;margin:55px auto;padding:0 28px}h1{font-size:clamp(30px,5vw,45px);line-height:1.18;letter-spacing:-.035em;margin:22px 0 30px}h2{font-size:24px;margin:42px 0 14px;line-height:1.3}h3{font-size:20px}p,li{max-width:82ch}a{color:var(--accent);text-underline-offset:3px}a:hover{text-decoration-thickness:2px}a:focus-visible{outline:3px solid #c77b2c;outline-offset:4px}.eyebrow{font-size:12px;text-transform:uppercase;letter-spacing:.1em;color:var(--accent);font-weight:700}.abstract{color:var(--muted);font-size:19px;max-width:72ch}table{border-collapse:collapse;width:100%;font-size:15px;margin:24px 0}th,td{border-bottom:1px solid var(--line);padding:14px;text-align:left;vertical-align:top;overflow-wrap:anywhere}th{background:#eaf0ef;font-size:13px}code{background:#eaf0ef;padding:2px 5px;border-radius:3px;font-size:.87em}pre{background:#182d3e;color:#f4f8f7;border-radius:8px;padding:22px;overflow:auto}pre code{background:none;padding:0}li{margin:9px 0}aside{margin-top:48px;border:1px solid var(--line);border-left:4px solid #65bdb0;padding:8px 24px 20px;background:#fff}aside h2{margin-top:18px}aside ul{padding-left:20px}aside small{color:var(--muted);display:block;font-size:12px}aside p{margin:4px 0 18px;font-size:15px}footer{max-width:1000px;margin:60px auto 30px;padding:24px 28px;border-top:1px solid var(--line);color:var(--muted);font-size:12px}.skip{position:absolute;left:-999px}.skip:focus{left:10px;top:10px;background:white;padding:10px} @media(max-width:600px){nav{gap:14px;padding:18px}main{padding:0 18px;margin:32px auto}th,td{padding:10px 7px;font-size:13px}h2{margin-top:32px}footer{padding:20px 18px}}\n'
if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--check',action='store_true');args=p.parse_args()
    try:build(check=args.check)
    except (ValueError,UnicodeError) as e:p.exit(1,str(e)+'\n')
