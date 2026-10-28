"""Reference reader for ADM XML with list-local identities."""
from pathlib import Path
import re
from urllib.parse import urlsplit
from lxml import etree as ET

NS='urn:adm:1'
N={'a':NS}
LOCAL_ID=re.compile(r'[a-z][a-z0-9]*(?:-[a-z][a-z0-9]*){0,2}\Z')
PROSE={'p','ul','ol','li','strong','em','a','ref','code'}
METADATA={'summary'}
ITEMS={'observation','lookalike','example','criterion','exclusion','alternative','precondition','step','intervention-ref','harness'}

def name(node):return ET.QName(node).localname

def text(node):return ''.join(node.itertext()).strip()

def ast(node):
    mixed=name(node) in {'p','li','strong','em','a','ref','code','when','summary'}
    content=[]
    if node.text and (mixed or node.text.strip()):content.append(node.text)
    for child in node:
        content.append(ast(child))
        if child.tail and (mixed or child.tail.strip()):content.append(child.tail)
    return {'name':name(node),'attributes':dict(node.attrib),'content':content}

def load(root):
    schema=ET.XMLSchema(ET.parse(str(root/'schema/adm-v1.xsd')))
    documents=[];objects={};node_addresses={};paths=set()
    for path in sorted((root/'entries').rglob('*.xml')):
        raw=path.read_bytes();raw.decode('utf-8')
        if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw:raise ValueError(f'{path}: DTDs and entities are unsupported')
        try:
            node=ET.fromstring(raw,ET.XMLParser(resolve_entities=False,no_network=True,load_dtd=False,remove_comments=True))
            schema.assertValid(node)
        except (ET.XMLSyntaxError,ET.DocumentInvalid) as e:raise ValueError(f'{path}: {e}') from e
        kind=name(node);did=node.get('id');rel=path.relative_to(root/'entries')
        dirs={'symptom':'symptoms','diagnosis':'diagnoses','intervention':'interventions'}
        prefixes={'symptom':'S','diagnosis':'D','intervention':'I'}
        if kind not in dirs or rel.parts[0]!=dirs[kind]:raise ValueError(f'{path}: wrong directory for {kind}')
        if not re.fullmatch(prefixes[kind]+r'\d{3,}',did):raise ValueError(f'{path}: invalid document ID')
        if did in objects:raise ValueError(f'duplicate document ID: {did}')
        output=rel.with_suffix('.html').as_posix()
        if output in paths:raise ValueError(f'output path collision: {output}')
        paths.add(output)
        meta={'id':did,'kind':kind,'summary':node.findtext('a:summary',namespaces=N),**{k:v for k,v in node.attrib.items() if k!='id'}}
        doc={'node':node,'meta':meta,'path':output,'source':path.relative_to(root).as_posix()};documents.append(doc)
        def register(obj,address):
            if address in objects:raise ValueError(f'duplicate address: {address}')
            objects[address]={'node':obj,'document':doc};node_addresses[obj]=address
        register(node,did)
        def walk(parent,parent_path):
            seen=set()
            for child in parent:
                local=child.get('id')
                if local:
                    if not LOCAL_ID.fullmatch(local):raise ValueError(f'{path}: invalid local ID: {local}')
                    if local in seen:raise ValueError(f'{path}: duplicate local ID in one list: {local}')
                    seen.add(local)
                tag=name(child)
                if tag in PROSE or tag in METADATA or tag=='symptom-ref':continue
                segment=(child.get('ref') if tag=='intervention-ref' else local) or tag
                scoped=(parent_path+'/'+segment) if parent_path else segment
                register(child,did+'#'+scoped);walk(child,scoped)
        walk(node,'')
    refs=[]
    for doc in documents:
        for node in doc['node'].iter():
            tag=name(node)
            if tag=='a':
                url=urlsplit(node.get('href'))
                if url.scheme not in ('https','http','mailto') or (url.scheme in ('http','https') and not url.netloc):raise ValueError('Only external HTTP(S)/mailto links use a; corpus links use ref')
            if tag not in ('ref','symptom-ref','intervention-ref'):continue
            target=node.get('target') if tag=='ref' else node.get('ref')
            if target not in objects:raise ValueError(f'{doc["source"]}: unresolved reference: {target}')
            if tag!='ref':
                target_obj=objects[target]
                if '#' in target or name(target_obj['node'])!=tag.removesuffix('-ref'):raise ValueError(f'wrong target kind: {target}')
            parent=node.getparent()
            while parent not in node_addresses:parent=parent.getparent()
            ref={'from':node_addresses[parent],'to':target,'relation':tag}
            if tag=='intervention-ref':
                ref.update(address=node_addresses[node],when=node.findtext('a:when',namespaces=N),
                           predictions=ast(node.find('a:predictions',N)))
            refs.append(ref)
        relations=doc['node'].find('a:relations',N)
        if relations is not None:
            targets=[c.get('ref') for c in relations]
            if len(targets)!=len(set(targets)):raise ValueError('duplicate entry-level typed relationship')
    return documents,objects,node_addresses,refs
