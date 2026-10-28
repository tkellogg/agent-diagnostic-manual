"""Tests of the public format, scoped identity, and generated reading views."""
from pathlib import Path
from copy import deepcopy
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from lxml import etree as ET
from tools.build import build, Renderer
from tools.xml_entries import load, ast, N
ROOT=Path(__file__).resolve().parents[1]
S='entries/symptoms/repeated-retrieval.xml'
D='entries/diagnoses/context-handoff-loss.xml'
I='entries/interventions/preserve-task-relevant-evidence.xml'

class FormatTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.root=Path(self.temp.name)
        for folder in ('entries','schema','skills','website','docs'):shutil.copytree(ROOT/folder,self.root/folder)
        for file in ('README.md','mkdocs.yml'):shutil.copyfile(ROOT/file,self.root/file)
        shutil.copytree(ROOT/'node_modules/@reviewjs/annotate',self.root/'node_modules/@reviewjs/annotate')
    def tearDown(self):self.temp.cleanup()
    def change(self,path,old,new):
        p=self.root/path;s=p.read_text();self.assertIn(old,s);p.write_text(s.replace(old,new))
    def test_build_and_scoped_catalog(self):
        docs,objects,refs=build(self.root)
        expected_ids={ET.parse(str(path)).getroot().get('id') for path in (self.root/'entries').rglob('*.xml')}
        self.assertEqual({d['meta']['id'] for d in docs},expected_ids)
        for key in ['S001#observations/multi-read','S001#benign-lookalikes/changed-source','S001#examples/stalled-edit','S001#what-to-record','D001#criteria/linked-disruption']:
            self.assertIn(key,objects)
        catalog=json.loads((self.root/'dist/catalog.json').read_text())
        self.assertEqual(catalog['objects']['S001#observations/multi-read']['kind'],'observation')
        self.assertTrue(any(r['from']=='D001#criteria/linked-disruption' and r['to']=='S001' for r in refs))
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
                target=((out/urlpath.lstrip('/')).resolve() if urlpath.startswith('/') else (page.parent/urlpath).resolve()) if urlpath else page
                self.assertTrue((target.is_file() or target.is_dir()),href)
                if url.fragment and target.suffix=='.html':
                    dest=ET.HTML(target.read_text())
                    self.assertIn(unquote(url.fragment),dest.xpath('//*[@id]/@id'))
        md=(out/'index.md').read_text()
        self.assertIn('symptoms/repeated-retrieval.md',md)
        self.assertIn('diagnoses/context-handoff-loss.md',md)
        self.assertIn('interventions/preserve-task-relevant-evidence.md',md)
    def test_homepage_lists_new_entries_from_the_corpus(self):
        tree=ET.parse(str(self.root/S))
        tree.getroot().set('id','S900')
        tree.getroot().set('title','A new symptom')
        tree.find('a:summary',N).text='A new summary for the index.'
        tree.write(str(self.root/'entries/symptoms/new-symptom.xml'),encoding='UTF-8',xml_declaration=True)
        docs,_,_=build(self.root)
        home=ET.HTML((self.root/'dist/index.html').read_text())
        article=home.xpath('//article')[0]
        links={a.get('href'):''.join(a.itertext()) for a in article.xpath('.//a[@href]')}
        for doc in docs:
            self.assertIn(doc['path'],links)
            self.assertIn(doc['meta']['title'],links[doc['path']])
        self.assertEqual(links['symptoms/new-symptom.html'],'S900 — A new symptom')
        self.assertIn('A new summary for the index.',' '.join(article.itertext()))
        self.assertIn('[S900 — A new symptom](symptoms/new-symptom.md)',(self.root/'dist/index.md').read_text())
    def test_public_docs_are_discovered_and_exposed_as_markdown(self):
        source=self.root/'docs/methods/new-guide.md'
        source.parent.mkdir()
        source.write_text('# A new public guide\n\nGuidance for human maintainers and tools.\n')
        build(self.root)
        out=self.root/'dist'
        home=ET.HTML((out/'index.html').read_text())
        nav_links={a.get('href'):''.join(a.itertext()) for a in home.xpath('//div[contains(@class,"navbar")]//a[@href]')}
        self.assertEqual(nav_links['docs/methods/new-guide.html'],'A new public guide')
        for path in (self.root/'docs').rglob('*.md'):
            relative=path.relative_to(self.root)
            self.assertEqual((out/relative).read_bytes(),path.read_bytes())
            page=ET.HTML((out/relative.with_suffix('.html')).read_text())
            self.assertTrue(page.xpath('//article[@data-pagefind-body]'))
            self.assertEqual(page.xpath('//meta[@data-pagefind-meta="kind[content]"]/@content'),['Guide'])
            self.assertEqual(page.xpath('//a[@aria-label="Download Markdown"]/@href'),[path.name])
    def test_homepage_and_navigation_sort_entries_by_numeric_id(self):
        for entry_id,filename in [('S999','a-new.xml'),('S1000','z-new.xml')]:
            tree=ET.parse(str(self.root/S))
            tree.getroot().set('id',entry_id)
            tree.write(str(self.root/'entries/symptoms'/filename),encoding='UTF-8',xml_declaration=True)
        docs,_,_=build(self.root)
        expected=[d['meta']['id'] for d in docs if d['meta']['kind']=='symptom']
        home=ET.HTML((self.root/'dist/index.html').read_text())
        for xpath in ('//article//a[@href]', '//div[contains(@class,"navbar")]//a[@href]'):
            labels=[''.join(a.itertext()).split(' — ')[0] for a in home.xpath(xpath)]
            ids=[label for label in labels if label in expected]
            self.assertEqual(ids,expected)
        self.assertEqual(expected[-2:],['S999','S1000'])
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
            def unnumber(value):return re.sub(r'^\d+\. ', '',value)
            self.assertEqual(sum(unnumber(''.join(e.itertext()).removesuffix('¶'))==title for e in headings),count)
            self.assertEqual(sum(unnumber(re.sub(r' \{#[^}]*\}$','',line.lstrip('# ').strip())) == r'A &amp; "B" &lt;C&gt; \*D\*' for line in m.splitlines() if line.startswith('#')),count)
    def test_title_attributes_required(self):
        for path in (S,D,I):
            original=(self.root/path).read_bytes()
            tree=ET.fromstring(original)
            for node in tree.iter():
                if ET.QName(node).localname not in ('symptom','diagnosis','intervention','criterion','alternative'):continue
                if 'title' not in node.attrib:continue
                with self.subTest(path=path,tag=node.tag):
                    title=node.attrib.pop('title')
                    (self.root/path).write_bytes(ET.tostring(tree))
                    with self.assertRaises(ValueError):load(self.root)
                    node.set('title',title)
            (self.root/path).write_bytes(original)
    def test_optional_recognition_hint_and_item_titles(self):
        tree=ET.parse(str(self.root/S))
        root=tree.getroot()
        root.remove(root.find('a:how-to-recognize-it',N))
        item=root.find('a:observations/a:observation',N)
        item.set('title','The same information is read again')
        tree.write(str(self.root/S),encoding='UTF-8')
        _,objects,_,_=load(self.root)
        self.assertIn('S001#observations/multi-read',objects)
        self.assertNotIn('S001#how-to-recognize-it',objects)
        item.attrib.pop('title')
        tree.write(str(self.root/S),encoding='UTF-8')
        load(self.root)
    def test_relationships_and_examples_are_readable_in_generated_views(self):
        build(self.root)
        page=ET.HTML((self.root/'dist/diagnoses/context-handoff-loss.html').read_text())
        article=page.xpath('//article')[0]
        symptom_links=article.xpath('.//ul/li/a[@href="../symptoms/repeated-retrieval.html"]')
        self.assertTrue(any('S001 — Repeated retrieval'==''.join(a.itertext()) for a in symptom_links))
        intervention=article.xpath('.//h3/a[@href="../interventions/preserve-task-relevant-evidence.html"]')
        self.assertTrue(any('I001 — Fix compaction' in ''.join(a.itertext()) for a in intervention))
        predictions=article.xpath('.//h4[starts-with(@id,"what-to-expect")]/following-sibling::ul[1]/li')
        self.assertEqual(len(predictions),4)
        self.assertTrue(all(li.xpath('./p/strong') for li in predictions))
        self.assertFalse(any(li.xpath('.//pre') for li in predictions))
        symptom=ET.HTML((self.root/'dist/symptoms/opaque-jargon.html').read_text())
        badges=symptom.xpath('//span[@class="adm-example-kind"]/text()')
        self.assertIn('Synthetic example',badges)
        self.assertIn('Reported example',badges)
        md=(self.root/'dist/diagnoses/context-handoff-loss.md').read_text()
        self.assertIn('**Expected improvement:**',md)
        self.assertNotIn('Related symptom:',md)
        for doc in (self.root/'entries/diagnoses').glob('*.xml'):
            source=ET.parse(str(doc))
            h=ET.HTML((self.root/'dist/diagnoses'/doc.with_suffix('.html').name).read_text())
            for number,criterion in enumerate(source.findall('a:criteria/a:criterion',N),1):
                heading=h.xpath('//*[@id="criteria/'+criterion.get('id')+'"]/following::h3[1]')[0]
                self.assertTrue(''.join(heading.itertext()).startswith(f'{number}. '+criterion.get('title')))
        self.assertTrue(article.xpath('.//h3[@id="the-information-mattered"]'))
    def test_criteria_renumber_without_changing_identity(self):
        tree=ET.parse(str(self.root/D))
        criteria=tree.find('a:criteria',N)
        criteria.insert(0,criteria[-1])
        tree.write(str(self.root/D),encoding='UTF-8')
        docs,objects,addresses,_=load(self.root)
        doc=next(d for d in docs if d['meta']['id']=='D001')
        h=ET.HTML(Renderer(doc,objects,addresses,'html').body())
        self.assertEqual(h.xpath('//h3[@id="the-omission-explains-the-mistake"]/text()'),['1. The omission explains the mistake'])
        self.assertTrue(h.xpath('//*[@id="criteria/linked-disruption"]'))
    def test_intervention_reference_has_condition_and_predictions(self):
        _,_,_,refs=load(self.root)
        relation=next(r for r in refs if r['relation']=='intervention-ref')
        self.assertEqual(set(relation),{'from','to','relation','address','when','predictions'})
        node=ET.parse(str(self.root/D)).find('a:relations/a:intervention-ref',N)
        self.assertEqual(dict(node.attrib),{'ref':'I001'})
        self.assertTrue(node.findtext('a:when',namespaces=N))
        self.assertEqual(relation['predictions'],ast(node.find('a:predictions',N)))
    def test_predictions_required_and_addressed_without_id(self):
        original=(self.root/D).read_bytes()
        for mutation in ('missing','empty','id'):
            with self.subTest(mutation=mutation):
                node=ET.fromstring(original)
                predictions=node.find('a:relations/a:intervention-ref/a:predictions',N)
                if mutation=='missing':predictions.getparent().remove(predictions)
                elif mutation=='empty':predictions.clear()
                else:predictions.set('id','outcome')
                (self.root/D).write_bytes(ET.tostring(node))
                with self.assertRaises(ValueError):load(self.root)
        (self.root/D).write_bytes(original)
        _,objects,_,_=load(self.root)
        self.assertIn('D001#relations/I001/predictions',objects)
    def test_prediction_fields_are_required_singletons(self):
        original=(self.root/D).read_bytes()
        fields=('expected-improvement','still-necessary','reason-to-reconsider','possible-harm')
        for field in fields:
            for mutation in ('missing','empty','duplicate','id','unknown'):
                with self.subTest(field=field,mutation=mutation):
                    node=ET.fromstring(original)
                    predictions=node.find('a:relations/a:intervention-ref/a:predictions',N)
                    child=predictions.find('a:'+field,N)
                    if mutation=='missing':predictions.remove(child)
                    elif mutation=='empty':child.clear()
                    elif mutation=='duplicate':predictions.insert(predictions.index(child),deepcopy(child))
                    elif mutation=='id':child.set('id','outcome')
                    else:child.tag='{urn:adm:1}unknown'
                    (self.root/D).write_bytes(ET.tostring(node))
                    with self.assertRaises(ValueError):load(self.root)
        node=ET.fromstring(original)
        predictions=node.find('a:relations/a:intervention-ref/a:predictions',N)
        predictions.clear()
        predictions.append(ET.fromstring(b'<p xmlns="urn:adm:1">Unstructured predictions.</p>'))
        (self.root/D).write_bytes(ET.tostring(node))
        with self.assertRaises(ValueError):load(self.root)
        (self.root/D).write_bytes(original)
        _,objects,_,_=load(self.root)
        for field in fields:self.assertIn('D001#relations/I001/predictions/'+field,objects)
    def test_predictions_preserve_prose_links_in_every_view(self):
        tree=ET.parse(str(self.root/D))
        predictions=tree.find('a:relations/a:intervention-ref/a:predictions',N)
        improvement=predictions.find('a:expected-improvement',N)
        improvement.clear()
        improvement.append(ET.fromstring(b'<p xmlns="urn:adm:1"><strong>Less</strong> <ref target="S001">retrieval</ref>, with correct results.</p>'))
        improvement.append(ET.fromstring(b'<ul xmlns="urn:adm:1"><li>Preserve <em>inline</em> formatting.</li></ul>'))
        tree.write(str(self.root/D),encoding='UTF-8')
        build(self.root)
        catalog=json.loads((self.root/'dist/catalog.json').read_text())
        self.assertEqual(catalog['schema_version'],6)
        relation=next(r for r in catalog['relationships'] if r.get('address')=='D001#relations/I001')
        self.assertEqual(relation['predictions'],ast(predictions))
        h=ET.HTML((self.root/'dist/diagnoses/context-handoff-loss.html').read_text())
        self.assertTrue(h.xpath('//*[@id="relations/I001/predictions"]'))
        self.assertTrue(h.xpath('//li/p[strong="Less"]/a[@href="../symptoms/repeated-retrieval.html"]'))
        self.assertTrue(h.xpath('//li/ul/li/em[text()="inline"]'))
        for field in predictions:
            self.assertTrue(h.xpath('//*[@id="relations/I001/predictions/'+ET.QName(field).localname+'"]'))
        md=(self.root/'dist/diagnoses/context-handoff-loss.md').read_text()
        self.assertIn('**Less** [retrieval](../symptoms/repeated-retrieval.md), with correct results.',md)
        result=subprocess.run([sys.executable,'-I',str(ROOT/'examples/query_manual.py'),'--entries',str(self.root/'entries')],check=True,capture_output=True,text=True)
        diagnosis=next(r for r in json.loads(result.stdout) if r.get('diagnosis')=='D001')
        self.assertEqual(diagnosis['interventions'][0]['predictions']['expected-improvement'],'Less retrieval, with correct results. Preserve inline formatting.')
    def test_diagnosis_assesses_configured_system(self):
        original=(self.root/D).read_bytes()
        for unit in ('configured-agent-episode','model',None):
            with self.subTest(unit=unit):
                node=ET.fromstring(original)
                if unit is None:node.attrib.pop('unit')
                else:node.set('unit',unit)
                (self.root/D).write_bytes(ET.tostring(node))
                with self.assertRaises(ValueError):load(self.root)
        (self.root/D).write_bytes(original)
    def test_intervention_reference_rejects_extra_attributes(self):
        original=(self.root/D).read_text()
        for attribute in ['role="both"','evidence="unvalidated"','id="preserve-evidence"']:
            with self.subTest(attribute=attribute):
                (self.root/D).write_text(original.replace('<intervention-ref ref="I001">','<intervention-ref ref="I001" '+attribute+'>'))
                with self.assertRaises(ValueError):load(self.root)
        (self.root/D).write_text(original)
    def test_multiple_intervention_targets_have_distinct_addresses(self):
        original=(self.root/I).read_text()
        (self.root/'entries/interventions/comparison.xml').write_text(original.replace('id="I001"','id="I999"',1))
        tree=ET.parse(str(self.root/D))
        relations=tree.find('a:relations',N)
        other=deepcopy(relations.find('a:intervention-ref',N));other.set('ref','I999')
        relations.append(other)
        tree.write(str(self.root/D),encoding='UTF-8')
        _,objects,_,_=load(self.root)
        self.assertIn('D001#relations/I001',objects)
        self.assertIn('D001#relations/I999',objects)
    def test_same_id_in_different_lists_allowed(self):
        self.change(S,'id="stalled-edit"','id="multi-read"')
        _,objects,_,_=load(self.root)
        self.assertIn('S001#observations/multi-read',objects)
        self.assertIn('S001#examples/multi-read',objects)
    def test_same_id_in_different_documents_allowed(self):
        self.change(D,'id="linked-disruption"','id="multi-read"')
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
        self.assertTrue({'stalled-edit','verified-edit'} <= {e.get('id') for e in node.findall('a:examples/a:example',N)})
        self.assertIsNone(node.find('a:what-to-record',N).get('id'))
        self.assertIsNone(node.find('a:benign-lookalikes/a:ul',N))
    def test_scoped_link_renders_in_both_outputs(self):
        self.change(D,'target="S001"','target="S001#observations/multi-read"')
        build(self.root)
        h=(self.root/'dist/diagnoses/context-handoff-loss.html').read_text()
        m=(self.root/'dist/diagnoses/context-handoff-loss.md').read_text()
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
        rows=json.loads(result.stdout);s=next(x for x in rows if x.get('symptom')=='S001')
        self.assertEqual(s['observations'],['S001#observations/multi-read'])
        self.assertEqual(len(s['lookalikes']),5)
    def test_review_export_adapter(self):
        subprocess.run(['node','--test',str(ROOT/'tests/review-export.test.cjs')],check=True,capture_output=True,text=True)
    def test_review_tools_are_local_and_use_stable_page_keys(self):
        docs,_,_=build(self.root)
        out=self.root/'dist'
        for doc in docs:
            page=ET.HTML((out/doc['path']).read_text())
            script=page.xpath('//script[@data-project="agent-diagnostic-manual"]')[0]
            self.assertEqual(script.get('data-page'),doc['meta']['id'])
            self.assertIn('annotate-1.5.3.js',script.get('src'))
            self.assertFalse(script.get('src').startswith('https:'))
            self.assertIsNone(script.get('data-api'))
            self.assertIsNone(script.get('data-post-url'))
            self.assertTrue(page.xpath('//button[@id="adm-review-export"]'))
            self.assertTrue(page.xpath('//button[@id="adm-review-clear"]'))
            self.assertTrue(page.xpath('//button[@id="adm-review-undo"][@hidden]'))
        home=ET.HTML((out/'index.html').read_text())
        self.assertEqual(home.xpath('//script[@data-project]/@data-page'),['index.md'])
        guide=ET.HTML((out/'docs/authoring-diagnosis.html').read_text())
        self.assertEqual(guide.xpath('//script[@data-project]/@data-page'),['docs/authoring-diagnosis.md'])
        self.assertEqual((out/'assets/vendor/annotate-1.5.3.js').read_bytes(),(ROOT/'node_modules/@reviewjs/annotate/annotate.js').read_bytes())
        self.assertTrue((out/'assets/vendor/annotate-LICENSE.txt').is_file())

if __name__=='__main__':unittest.main()
