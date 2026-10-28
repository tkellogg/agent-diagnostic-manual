#!/usr/bin/env -S uv run --script
# Run: uv run --script examples/query_manual.py [--entries /path/to/entries]
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Read trusted ADM XML using only the standard library.

This reader example is not a full validator. Validate untrusted corpora with
safe parsing and the documented validation layers before consuming them.
"""
import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET
NS={'a':'urn:adm:1'}

def query(entries):
    result=[]
    for path in sorted(entries.rglob('*.xml')):
        raw=path.read_bytes();raw.decode('utf-8')
        if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw:raise ValueError('DTD and entity declarations are unsupported')
        node=ET.fromstring(raw)
        if not node.tag.startswith('{urn:adm:1}') or node.get('version')!='1':raise ValueError('Unsupported namespace or version')
        did=node.get('id')
        if node.tag=='{urn:adm:1}symptom':
            result.append({'symptom':did,
                'observations':[did+'#observations/'+o.get('id') for o in node.findall('a:observations/a:observation',NS)],
                'lookalikes':[did+'#benign-lookalikes/'+o.get('id') for o in node.findall('a:benign-lookalikes/a:lookalike',NS)],
                'examples':[did+'#examples/'+o.get('id') for o in node.findall('a:examples/a:example',NS)]})
        elif node.tag=='{urn:adm:1}diagnosis':
            result.append({'diagnosis':did,'operator':node.find('a:criteria',NS).get('operator'),
                'criteria':[{'address':did+'#criteria/'+c.get('id'),'title':c.get('title')} for c in node.findall('a:criteria/a:criterion',NS)],
                'interventions':[{'address':did+'#relations/'+i.get('ref'),'target':i.get('ref'),
                    'when':i.findtext('a:when',namespaces=NS),
                    'predictions':{field.tag.removeprefix('{urn:adm:1}'):
                        ' '.join(''.join(p.itertext()).strip() for p in field)
                        for field in i.find('a:predictions',NS)}}
                    for i in node.findall('a:relations/a:intervention-ref',NS)]})
        elif node.tag=='{urn:adm:1}intervention':
            result.append({'intervention':did,
                'harnesses':[{'id':h.get('id'),'title':h.get('title'),
                    'address':did+'#harness-notes/'+h.get('id')}
                    for h in node.findall('a:harness-notes/a:harness',NS)]})
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--entries',type=Path,default=Path(__file__).resolve().parents[1]/'entries');args=p.parse_args()
    print(json.dumps(query(args.entries),indent=2))
