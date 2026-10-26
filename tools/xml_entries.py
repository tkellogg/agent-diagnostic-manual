"""Reference reader and Markdown renderer for the published ASM XML contract."""
from pathlib import Path
import os
import re
from lxml import etree as ET

NS = 'urn:asm:1'
N = {'a': NS}
HEADINGS = {'criteria': 'Candidate criteria', 'differential': 'Differential diagnosis'}
META = {'title','summary','tags','relations','targets'}

def name(node):
    return ET.QName(node).localname

def text(node):
    return ''.join(node.itertext()).strip()

def ast(node):
    """Preserve mixed content order; discard indentation-only whitespace."""
    content = []
    mixed = name(node) in {'p','li','strong','em','a','ref','code','when','title','summary','tag','target'}
    if node.text and (mixed or node.text.strip()):
        content.append(node.text)
    for child in node:
        content.append(ast(child))
        if child.tail and (mixed or child.tail.strip()):
            content.append(child.tail)
    return {'name': name(node), 'attributes': dict(node.attrib), 'content': content}

def load_entries(root):
    schema = ET.XMLSchema(ET.parse(str(root/'schema/asm-v1.xsd')))
    entries, objects = [], {}
    for path in sorted((root/'entries').rglob('*.xml')):
        raw = path.read_bytes()
        raw.decode('utf-8')
        if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw:
            raise ValueError(f'{path}: DTDs and entities are not supported')
        parser = ET.XMLParser(resolve_entities=False, no_network=True, load_dtd=False, remove_comments=True)
        try:
            node = ET.fromstring(raw, parser)
            schema.assertValid(node)
        except (ET.XMLSyntaxError, ET.DocumentInvalid) as e:
            raise ValueError(f'{path}: {e}') from e
        kind = name(node)
        if kind not in ('symptom','diagnosis','intervention'):
            raise ValueError(f'{path}: unsupported entry root {kind}')
        entry_id = node.get('id')
        prefix = {'symptom':'S','diagnosis':'D','intervention':'I'}[kind]
        if not re.fullmatch(prefix+r'\d{3,}', entry_id):
            raise ValueError(f'{path}: invalid entry ID {entry_id}')
        rel = path.relative_to(root/'entries')
        if rel.parts[0] != {'symptom':'symptoms','diagnosis':'diagnoses','intervention':'interventions'}[kind]:
            raise ValueError(f'{path}: wrong directory for {kind}')
        meta = {'schema_version': 1, 'id': entry_id, 'kind':kind,
                'title': node.findtext('a:title',namespaces=N),
                'summary': node.findtext('a:summary',namespaces=N),
                'status':node.get('status'),'evidence':node.get('evidence'),
                'updated':node.get('updated'),
                'tags':[text(t) for t in node.findall('a:tags/a:tag',N)]}
        if kind == 'diagnosis':
            meta.update(unit=node.get('unit'),diagnostic_level=node.get('level'),
                symptoms=[r.get('ref') for r in node.findall('a:relations/a:symptom-ref',N)],
                interventions=[{'id':r.get('ref'),'role':r.get('role'),'when':r.findtext('a:when',namespaces=N),'evidence':r.get('evidence')} for r in node.findall('a:relations/a:intervention-ref',N)])
        if kind == 'intervention':
            meta['targets']=[text(t) for t in node.findall('a:targets/a:target',N)]
        record={'node':node,'meta':meta,'path':rel.with_suffix('.md').as_posix(),'source':'entries/'+rel.as_posix()}
        entries.append(record)
        for obj in node.iter():
            oid=obj.get('id')
            if oid:
                if oid in objects:
                    raise ValueError(f'duplicate ID: {oid}')
                if obj is not node and not oid.startswith(entry_id+'-'):
                    raise ValueError(f'{path}: child ID must start with {entry_id}-')
                objects[oid]={'node':obj,'entry':record}
    refs=[]
    for entry in entries:
        for obj in entry['node'].iter():
            tag=name(obj)
            if tag not in ('ref','symptom-ref','intervention-ref'):
                continue
            target=obj.get('target') if tag=='ref' else obj.get('ref')
            if target not in objects:
                raise ValueError(f'{entry["source"]}: unresolved reference {target}')
            if tag!='ref' and name(objects[target]['node']) != tag.removesuffix('-ref'):
                raise ValueError(f'{entry["source"]}: wrong target kind for {target}')
            owner=obj.getparent()
            while owner is not None and not owner.get('id'):
                owner=owner.getparent()
            edge={'from':owner.get('id'),'to':target,'relation':tag}
            if tag=='intervention-ref':
                edge.update(id=obj.get('id'), role=obj.get('role'), evidence=obj.get('evidence'), when=obj.findtext('a:when',namespaces=N))
            refs.append(edge)
    return entries,objects,refs

def escape(value):
    return re.sub(r'([\\`*_{}\[\]<>|])',r'\\\1',value)

def markdown_entry(entry,objects):
    def link(target,label=''):
        item=objects[target]; dest=item['entry']
        href=os.path.relpath(dest['path'],str(Path(entry['path']).parent)).replace(os.sep,'/')
        if target!=dest['meta']['id']:
            href+='#'+target
        return f'[{label or escape(target)}]({href})'
    def mixed(node):
        result=escape(node.text or '')
        for child in node:
            result+=inline(child)+escape(child.tail or '')
        return result
    def inline(node):
        tag=name(node)
        if tag=='strong':return '**'+mixed(node)+'**'
        if tag=='em':return '*'+mixed(node)+'*'
        if tag=='code':
            value=text(node); fence='`'*(max([len(m) for m in re.findall(r'`+',value)]+[0])+1)
            return fence+' '+value+' '+fence
        if tag=='ref':return link(node.get('target'),mixed(node))
        if tag=='a':return '['+mixed(node)+']('+node.get('href')+')'
        return mixed(node)
    def anchor(node):
        return f'<a id="{node.get("id")}"></a>\n\n' if node.get('id') else ''
    def blocks(node):
        result=''
        for child in node:
            tag=name(child)
            if tag=='p':result+=mixed(child)+'\n\n'
            elif tag in ('ul','ol'):
                result+='\n'.join((f'{i}. ' if tag=='ol' else '- ')+mixed(li) for i,li in enumerate(child,1))+'\n\n'
            elif tag in ('criterion','alternative'):
                result+=anchor(child)+'### '+escape(child.get('id'))+' — '+escape(child.findtext('a:title',namespaces=N))+'\n\n'+blocks(child)
            elif tag in ('exclusion','step','precondition'):
                result+=anchor(child)+'### '+escape(child.get('id'))+'\n\n'+blocks(child)
            elif tag=='discriminator':result+='**Discriminating evidence:**\n\n'+blocks(child)
            elif tag=='symptom-ref':result+='Related symptom: '+link(child.get('ref'))+'\n\n'
        return result
    body='# '+entry['meta']['title']+'\n\n'
    for section in entry['node']:
        tag=name(section)
        if tag in META:continue
        title=HEADINGS.get(tag,tag.replace('-',' ').capitalize())
        body+=anchor(section)+'## '+title+'\n\n'+blocks(section)
    relations=entry['node'].find('a:relations',N)
    if relations is not None:
        body+='## Structured relationships\n\n'
        for rel in relations:
            body+=anchor(rel)
            body+='- '+link(rel.get('ref'))
            if name(rel)=='intervention-ref':
                body+=' · '+rel.get('role')+' · '+rel.get('evidence')+'\n\n  **When:** '+escape(rel.findtext('a:when',namespaces=N))
            body+='\n\n'
    return body

def document(entry,objects):
    source=os.path.relpath(entry['source'],str(Path('content')/Path(entry['path']).parent)).replace(os.sep,'/')
    m=entry['meta']
    return ('<!-- Generated by tools/build.py; edit the linked XML source. -->\n\n'
            + f'> Generated from [XML source]({source}). {m["id"]} · {m["status"]} · {m["evidence"]}.\n\n'
            + markdown_entry(entry,objects)).rstrip()+"\n"
