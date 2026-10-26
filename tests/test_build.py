"""Conformance examples: a usable format independently of a particular UI."""
from pathlib import Path
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from lxml import etree as ET
from tools.build import build, load
from tools.xml_entries import load_entries, markdown_entry, ast

ROOT = Path(__file__).resolve().parents[1]
D='entries/diagnoses/unproductive-repeated-retrieval.xml'
I='entries/interventions/preserve-task-relevant-evidence.xml'
S='entries/symptoms/repeated-retrieval.xml'

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        for folder in ('content','entries','schema'):
            shutil.copytree(ROOT/folder,self.root/folder)
    def tearDown(self):
        self.temp.cleanup()
    def change(self,path,old,new):
        p=self.root/path
        value=p.read_text()
        self.assertIn(old,value)
        p.write_text(value.replace(old,new))
    def validate(self):
        return load(self.root/'content',self.root/'schema/guide.schema.json')
    def test_real_corpus_builds_with_structured_catalog(self):
        pages,edges=build(self.root)
        self.assertEqual(sum(p['meta']['kind']=='symptom' for p in pages),1)
        self.assertEqual(sum(p['meta']['kind']=='diagnosis' for p in pages),1)
        html=(self.root/'dist/diagnoses/unproductive-repeated-retrieval.html').read_text()
        self.assertIn('../symptoms/repeated-retrieval.html',html)
        self.assertIn('id="D001-A"',html)
        catalog=json.loads((self.root/'dist/catalog.json').read_text())
        self.assertEqual(catalog['objects']['D001-A']['kind'],'criterion')
        self.assertTrue(any(e['from']=='D001-A' and e['to']=='S001' for e in catalog['relationships']))
        self.assertTrue(any(e.get('id')=='D001-I001' and e.get('when') for e in catalog['relationships']))
        self.assertEqual(next(e for e in catalog['entries'] if e['id']=='D001')['document']['name'],'diagnosis')
    def test_broken_anchor_rejected(self):
        self.change('content/index.md','structure.md','structure.md#missing')
        with self.assertRaisesRegex(ValueError,'missing anchor'):self.validate()
    def test_unresolved_typed_reference_rejected(self):
        self.change(D,'ref="S001"','ref="S999"')
        with self.assertRaisesRegex(ValueError,'unresolved reference'):self.validate()
    def test_wrong_reference_kind_rejected(self):
        self.change(D,'ref="S001"','ref="I001"')
        with self.assertRaisesRegex(ValueError,'wrong target kind'):self.validate()
    def test_duplicate_global_id_rejected(self):
        self.change(S,'id="S001-observation"','id="D001-A"')
        with self.assertRaisesRegex(ValueError,'duplicate ID'):self.validate()
    def test_missing_protocol_section_rejected_by_xsd(self):
        self.change(I,'stop-and-rollback','unrecognized-section')
        with self.assertRaises(ValueError):self.validate()
    def test_unknown_metadata_rejected_by_xsd(self):
        self.change(D,'version="1"','version="1" severity="3"')
        with self.assertRaises(ValueError):self.validate()
    def test_unsupported_version_rejected(self):
        self.change(D,'version="1"','version="2"')
        with self.assertRaises(ValueError):self.validate()
    def test_duplicate_yaml_key_rejected(self):
        self.change('content/index.md','id: manual','id: manual\nid: other')
        with self.assertRaisesRegex(ValueError,'duplicate YAML key'):self.validate()
    def test_dtd_rejected_without_resolution(self):
        p=self.root/D;s=p.read_text();s=s.replace('<diagnosis ', '<!DOCTYPE diagnosis [<!ENTITY secret SYSTEM "file:///does-not-exist">]>\n<diagnosis ',1);p.write_text(s)
        with self.assertRaisesRegex(ValueError,'DTDs and entities'):self.validate()
    def test_generated_drift_detected(self):
        build(self.root)
        self.change('content/diagnoses/unproductive-repeated-retrieval.md','Recurrence','Changed only in Markdown')
        with self.assertRaisesRegex(ValueError,'stale generated Markdown'):build(self.root,check_generated=True)
    def test_generated_markdown_deterministic(self):
        build(self.root)
        first=(self.root/'content/diagnoses/unproductive-repeated-retrieval.md').read_text()
        build(self.root)
        self.assertEqual(first,(self.root/'content/diagnoses/unproductive-repeated-retrieval.md').read_text())
        build(self.root,check_generated=True)
    def test_reference_to_individual_criterion(self):
        self.change(S,'target="D001"','target="D001-A"')
        entries,objects,_=load_entries(self.root)
        source=next(e for e in entries if e['meta']['id']=='S001')
        self.assertIn('unproductive-repeated-retrieval.md#D001-A',markdown_entry(source,objects))
        self.validate()
    def test_mixed_content_spaces_preserved_in_json(self):
        node=ET.fromstring(b'<p xmlns="urn:asm:1"><strong>one</strong> <em>two</em> tail</p>')
        data=ast(node)
        self.assertEqual(data['content'][1],' ')
        self.assertEqual(data['content'][3],' tail')
    def test_unsafe_link_rejected(self):
        self.change(D,'href="../cases/index.md"','href="javascript:alert(1)"')
        with self.assertRaisesRegex(ValueError,'unsupported link scheme'):self.validate()
    def test_independent_stdlib_consumer(self):
        result=subprocess.run([sys.executable,'-I',str(ROOT/'examples/query_manual.py'),'--entries',str(self.root/'entries')],check=True,capture_output=True,text=True)
        data=json.loads(result.stdout)[0]
        self.assertEqual([c['id'] for c in data['criteria']],['D001-A','D001-B','D001-C','D001-D'])
        self.assertEqual(data['interventions'][0]['relationship'],'D001-I001')
        self.assertEqual(data['operator'],'all')

if __name__=='__main__':unittest.main()
