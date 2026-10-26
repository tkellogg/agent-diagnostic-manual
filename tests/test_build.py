"""Tests of the public format, scoped identity, and generated reading views."""
from pathlib import Path
from copy import deepcopy
import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from lxml import etree as ET
from tools.build import build
from tools.xml_entries import load, ast, N
ROOT=Path(__file__).resolve().parents[1]
S='entries/symptoms/repeated-retrieval.xml'
D='entries/diagnoses/unproductive-repeated-retrieval.xml'
I='entries/interventions/preserve-task-relevant-evidence.xml'

class FormatTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        for folder in ('entries','schema','skills','website'):shutil.copytree(ROOT/folder,self.root/folder)
        for file in ('README.md','mkdocs.yml'):shutil.copyfile(ROOT/file,self.root/file)
    def tearDown(self):self.temp.cleanup()
    def change(self,path,old,new):
        p=self.root/path;s=p.read_text();self.assertIn(old,s);p.write_text(s.replace(old,new))
    def test_build_and_scoped_catalog(self):
        docs,objects,refs=build(self.root)
        self.assertEqual(sum(d['meta']['kind']=='symptom' for d in docs),1)
        self.assertEqual(sum(d['meta']['kind']=='diagnosis' for d in docs),1)
        for key in ['S001#observations/multi-read','S001#benign-lookalikes/changed-source','S001#examples/stalled-edit','S001#what-to-record','D001#criteria/recurrence']:
            self.assertIn(key,objects)
        catalog=json.loads((self.root/'dist/catalog.json').read_text())
        self.assertEqual(catalog['objects']['S001#observations/multi-read']['kind'],'observation')
        self.assertTrue(any(r['from']=='D001#criteria/recurrence' and r['to']=='S001' for r in refs))
        self.assertTrue(any(r.get('address')=='D001#relations/I001' for r in refs))
    def test_site_navigation_resolves_without_handwritten_indexes(self):
        from urllib.parse import urlsplit, unquote
        build(self.root)
        out=self.root/'dist'
        home=ET.HTML((out/'index.html').read_text())
        self.assertIn('Agent Diagnostic Manual',(out/'index.html').read_text())
        for page in out.rglob('*.html'):
            node=ET.HTML(page.read_text())
            for href in node.xpath('//a/@href'):
                url=urlsplit(href)
                if url.scheme or href=='#':continue
                urlpath=unquote(url.path)
                target=((out/urlpath.removeprefix('/agent-diagnostic-manual/')).resolve() if urlpath.startswith('/agent-diagnostic-manual/') else (page.parent/urlpath).resolve()) if urlpath else page
                self.assertTrue((target.is_file() or target.is_dir()),href)
                if url.fragment and target.suffix=='.html':
                    dest=ET.HTML(target.read_text())
                    self.assertIn(unquote(url.fragment),dest.xpath('//*[@id]/@id'))
        md=(out/'index.md').read_text()
        self.assertIn('symptoms/repeated-retrieval.md',md)
        self.assertIn('diagnoses/unproductive-repeated-retrieval.md',md)
        self.assertIn('interventions/preserve-task-relevant-evidence.md',md)
    def test_structured_lists_reject_stray_prose(self):
        containers={S:['observations','benign-lookalikes','examples'],
                    D:['criteria','exclusions','differential'],
                    I:['preconditions','procedure']}
        for path,tags in containers.items():
            original=(self.root/path).read_bytes()
            for tag in tags:
                for position in ('before','after'):
                    with self.subTest(path=path,tag=tag,position=position):
                        tree=ET.fromstring(original)
                        node=tree.find('a:'+tag,N)
                        p=ET.Element('{urn:adm:1}p');p.text='Stray prose.'
                        node.insert(0 if position=='before' else len(node),p)
                        (self.root/path).write_bytes(ET.tostring(tree))
                        with self.assertRaises(ValueError):load(self.root)
            (self.root/path).write_bytes(original)
    def test_title_attributes_render_as_plain_text(self):
        title='A & "B" <C> *D*'
        for path in (S,D,I):
            tree=ET.parse(str(self.root/path))
            for node in tree.getroot().iter():
                if 'title' in node.attrib:node.set('title',title)
            tree.write(str(self.root/path),encoding='UTF-8')
        docs,_,_=build(self.root)
        for doc in docs:
            if doc['source'] not in (S,D,I):continue
            self.assertEqual(doc['meta']['title'],title)
            self.assertEqual(doc['node'].findall('.//a:title',N),[])
            count=len(doc['node'].xpath('descendant-or-self::*[@title]'))
            h=(self.root/'dist'/doc['path']).read_text()
            m=(self.root/'dist'/Path(doc['path']).with_suffix('.md')).read_text()
            headings=ET.HTML(h).xpath('//article//*[self::h1 or self::h2 or self::h3 or self::h4 or self::h5 or self::h6]')
            self.assertEqual(sum(''.join(e.itertext()).removesuffix('¶')==title for e in headings),count)
            self.assertEqual(m.count(r'A &amp; "B" &lt;C&gt; \*D\*'),count)
    def test_title_attributes_required(self):
        for path in (S,D,I):
            original=(self.root/path).read_bytes()
            tree=ET.fromstring(original)
            for node in tree.iter():
                if 'title' not in node.attrib:continue
                with self.subTest(path=path,tag=node.tag):
                    title=node.attrib.pop('title')
                    (self.root/path).write_bytes(ET.tostring(tree))
                    with self.assertRaises(ValueError):load(self.root)
                    node.set('title',title)
            (self.root/path).write_bytes(original)
    def test_intervention_reference_has_only_target_and_condition(self):
        _,_,_,refs=load(self.root)
        relation=next(r for r in refs if r['relation']=='intervention-ref')
        self.assertEqual(set(relation),{'from','to','relation','address','when'})
        node=ET.parse(str(self.root/D)).find('a:relations/a:intervention-ref',N)
        self.assertEqual(dict(node.attrib),{'ref':'I001'})
        self.assertTrue(node.findtext('a:when',namespaces=N))
    def test_intervention_reference_rejects_extra_attributes(self):
        original=(self.root/D).read_text()
        for attribute in ['role="both"','evidence="unvalidated"','id="preserve-evidence"']:
            with self.subTest(attribute=attribute):
                (self.root/D).write_text(original.replace('<intervention-ref ref="I001">','<intervention-ref ref="I001" '+attribute+'>'))
                with self.assertRaises(ValueError):load(self.root)
        (self.root/D).write_text(original)
    def test_multiple_intervention_targets_have_distinct_addresses(self):
        original=(self.root/I).read_text()
        (self.root/'entries/interventions/comparison.xml').write_text(original.replace('id="I001"','id="I002"',1))
        self.change(D,'</relations>','<intervention-ref ref="I002"><when>A different condition.</when></intervention-ref></relations>')
        _,objects,_,_=load(self.root)
        self.assertIn('D001#relations/I001',objects)
        self.assertIn('D001#relations/I002',objects)
    def test_same_id_in_different_lists_allowed(self):
        self.change(S,'id="stalled-edit"','id="multi-read"')
        _,objects,_,_=load(self.root)
        self.assertIn('S001#observations/multi-read',objects)
        self.assertIn('S001#examples/multi-read',objects)
    def test_same_id_in_different_documents_allowed(self):
        self.change(D,'id="recurrence"','id="multi-read"')
        _,objects,_,_=load(self.root)
        self.assertIn('D001#criteria/multi-read',objects)
        self.assertIn('S001#observations/multi-read',objects)
    def test_duplicate_in_one_list_rejected(self):
        self.change(S,'id="different-content"','id="changed-source"')
        with self.assertRaisesRegex(ValueError,'duplicate local ID'):load(self.root)
    def test_singleton_id_rejected(self):
        self.change(S,'<what-to-record>','<what-to-record id="record">')
        with self.assertRaises(ValueError):load(self.root)
    def test_short_local_names_required(self):
        for invalid in ['S001-multi-read','too-many-words-here','multi_read']:
            with self.subTest(invalid=invalid):
                original=(self.root/S).read_text();(self.root/S).write_text(original.replace('id="multi-read"',f'id="{invalid}"'))
                with self.assertRaises(ValueError):load(self.root)
                (self.root/S).write_text(original)
    def test_lookalikes_and_examples_are_individual_objects(self):
        node=ET.parse(str(self.root/S)).getroot()
        self.assertEqual(len(node.findall('a:benign-lookalikes/a:lookalike',N)),5)
        self.assertEqual(len(node.findall('a:examples/a:example',N)),2)
        self.assertIsNone(node.find('a:what-to-record',N).get('id'))
        self.assertIsNone(node.find('a:benign-lookalikes/a:ul',N))
    def test_scoped_link_renders_in_both_outputs(self):
        self.change(D,'target="S001"','target="S001#observations/multi-read"')
        build(self.root)
        h=(self.root/'dist/diagnoses/unproductive-repeated-retrieval.html').read_text()
        m=(self.root/'dist/diagnoses/unproductive-repeated-retrieval.md').read_text()
        self.assertIn('../symptoms/repeated-retrieval.html#observations/multi-read',h)
        self.assertIn('../symptoms/repeated-retrieval.md#observations/multi-read',m)
        self.assertIn('id="observations/multi-read"',(self.root/'dist/symptoms/repeated-retrieval.html').read_text())
    def test_unscoped_item_reference_rejected(self):
        self.change(D,'target="S001"','target="multi-read"')
        with self.assertRaisesRegex(ValueError,'unresolved reference'):load(self.root)
    def test_wrong_scope_rejected(self):
        self.change(D,'target="S001"','target="S001#examples/multi-read"')
        with self.assertRaisesRegex(ValueError,'unresolved reference'):load(self.root)
    def test_wrong_typed_target_rejected(self):
        self.change(D,'ref="S001"','ref="I001"')
        with self.assertRaisesRegex(ValueError,'wrong target kind'):load(self.root)
    def test_missing_section_rejected(self):
        self.change(I,'stop-and-rollback','unrecognized-section')
        with self.assertRaises(ValueError):load(self.root)
    def test_duplicate_document_rejected(self):
        shutil.copy(self.root/S,self.root/'entries/symptoms/copy.xml')
        with self.assertRaisesRegex(ValueError,'duplicate document ID'):load(self.root)
    def test_dtd_and_unsafe_links_rejected(self):
        self.change(S,'<symptom ','<!DOCTYPE symptom>\n<symptom ')
        with self.assertRaisesRegex(ValueError,'DTDs'):load(self.root)
    def test_unsupported_version_rejected(self):
        self.change(S,'version="1"','version="2"')
        with self.assertRaises(ValueError):load(self.root)
    def test_mixed_content_preserved(self):
        node=ET.fromstring(b'<p xmlns="urn:adm:1"><strong>one</strong> <em>two</em> tail</p>')
        self.assertEqual(ast(node)['content'][1],' ')
        self.assertEqual(ast(node)['content'][3],' tail')
    def test_build_does_not_write_sources_and_cleans_output(self):
        before={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        build(self.root);(self.root/'dist/stale.html').write_text('stale');build(self.root)
        self.assertFalse((self.root/'dist/stale.html').exists())
        after={str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file() and 'dist' not in p.relative_to(self.root).parts and '.build' not in p.relative_to(self.root).parts}
        self.assertEqual(before,after)
        self.assertFalse((self.root/'content').exists())
    def test_every_catalog_address_has_a_rendered_anchor(self):
        build(self.root)
        catalog=json.loads((self.root/'dist/catalog.json').read_text())
        for address,obj in catalog['objects'].items():
            if '#' not in obj['url']:continue
            page,fragment=obj['url'].split('#',1)
            self.assertIn('id="'+fragment+'"',(self.root/'dist'/page).read_text(),address)
    def test_independent_consumer(self):
        result=subprocess.run([sys.executable,'-I',str(ROOT/'examples/query_manual.py'),'--entries',str(self.root/'entries')],check=True,capture_output=True,text=True)
        rows=json.loads(result.stdout);s=next(x for x in rows if 'symptom' in x)
        self.assertEqual(s['observations'],['S001#observations/multi-read'])
        self.assertEqual(len(s['lookalikes']),5)

if __name__=='__main__':unittest.main()
