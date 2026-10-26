"""Check boundaries that prevent a plausible-looking but broken manual."""
from pathlib import Path
import shutil
import tempfile
import unittest
from tools.build import build, load

ROOT = Path(__file__).resolve().parents[1]

class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        shutil.copytree(ROOT/'content', self.root/'content')
        shutil.copytree(ROOT/'schema', self.root/'schema')
    def tearDown(self):
        self.temp.cleanup()
    def change(self, path, old, new):
        p = self.root/'content'/path
        p.write_text(p.read_text().replace(old, new))
    def validate(self):
        return load(self.root/'content', self.root/'schema/entry.schema.json')
    def test_real_corpus_builds_and_rewrites_links(self):
        pages, edges = build(self.root)
        self.assertEqual(sum(p['meta']['kind']=='symptom' for p in pages),1)
        self.assertEqual(sum(p['meta']['kind']=='diagnosis' for p in pages),1)
        output=(self.root/'dist/diagnoses/unproductive-repeated-retrieval.html').read_text()
        self.assertIn('../symptoms/repeated-retrieval.html',output)
        self.assertNotIn('href="../symptoms/repeated-retrieval.md',output)
        self.assertEqual(len(edges),2)
    def test_broken_anchor_is_rejected(self):
        self.change('index.md','structure.md','structure.md#missing')
        with self.assertRaisesRegex(ValueError,'missing anchor'):
            self.validate()
    def test_wrong_reference_is_rejected(self):
        self.change('diagnoses/unproductive-repeated-retrieval.md','symptoms: [S001]','symptoms: [S999]')
        with self.assertRaisesRegex(ValueError,'invalid symptom reference'):
            self.validate()
    def test_duplicate_yaml_key_is_rejected(self):
        self.change('index.md','id: manual','id: manual\nid: other')
        with self.assertRaisesRegex(ValueError,'duplicate YAML key'):
            self.validate()
    def test_unknown_metadata_is_rejected(self):
        self.change('index.md','kind: guide','kind: guide\nseverity: 3')
        with self.assertRaises(ValueError):
            self.validate()
    def test_missing_protocol_section_is_rejected(self):
        self.change('interventions/preserve-task-relevant-evidence.md','## Stop and rollback','## Missing')
        with self.assertRaisesRegex(ValueError,'missing section'):
            self.validate()

if __name__ == '__main__':
    unittest.main()
