#!/usr/bin/env python3
"""Read trusted ASM XML with the standard library; no ASM or LLM dependency.

This is a reader example, not a complete corpus validator. Validate untrusted
corpora with the documented safe parsing and validation layers first.
"""
import argparse
import json
from pathlib import Path
import xml.etree.ElementTree as ET

NS = {'a':'urn:asm:1'}

def query(entries):
    result = []
    for path in sorted(entries.rglob('*.xml')):
        raw = path.read_bytes()
        raw.decode('utf-8')
        if b'<!DOCTYPE' in raw or b'<!ENTITY' in raw:
            raise ValueError('DTD and entity declarations are unsupported')
        node = ET.fromstring(raw)
        if not node.tag.startswith('{urn:asm:1}') or node.get('version') != '1':
            raise ValueError('Unsupported namespace or version')
        if node.tag != '{urn:asm:1}diagnosis':
            continue
        result.append({
            'diagnosis':node.get('id'),
            'operator':node.find('a:criteria',NS).get('operator'),
            'criteria':[{'id':c.get('id'),'title':c.findtext('a:title',namespaces=NS)} for c in node.findall('a:criteria/a:criterion',NS)],
            'interventions':[{'relationship':i.get('id'),'target':i.get('ref'),'role':i.get('role'),'evidence':i.get('evidence'),'when':i.findtext('a:when',namespaces=NS)} for i in node.findall('a:relations/a:intervention-ref',NS)]})
    return result

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--entries', type=Path, default=Path(__file__).resolve().parents[1]/'entries')
    args=parser.parse_args()
    print(json.dumps(query(args.entries),indent=2))
