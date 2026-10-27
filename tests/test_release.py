"""Release packaging guarantees, independent of GitHub."""
import hashlib
import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile
from tools.build import build
from tools.package_release import package
ROOT=Path(__file__).resolve().parents[1]

class ReleaseTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        for folder in ('entries','schema','skills','website','docs'):
            shutil.copytree(ROOT/folder,self.root/folder)
        for file in ('README.md','mkdocs.yml'):
            shutil.copyfile(ROOT/file,self.root/file)
        shutil.copytree(ROOT/'node_modules/@reviewjs/annotate',self.root/'node_modules/@reviewjs/annotate')
        build(self.root)
    def tearDown(self):self.temp.cleanup()
    def search_fixture(self):
        path=self.root/'dist/pagefind/pagefind.js'
        path.parent.mkdir()
        path.write_text('// search bundle fixture for packaging tests')
    def test_package_requires_search(self):
        with self.assertRaisesRegex(ValueError,'Pagefind'):
            package(self.root,'0.1.0','a'*40)
    def test_archive_formats_manifest_and_repeatability(self):
        self.search_fixture()
        path=package(self.root,'0.1.0','a'*40)
        original=path.read_bytes()
        with zipfile.ZipFile(path) as archive:
            prefix='adm-0.1.0/'
            manifest=json.loads(archive.read(prefix+'manifest.json'))
            self.assertEqual(manifest['source_commit'],'a'*40)
            self.assertEqual(manifest['tag'],'v0.1.0')
            for name,digest in manifest['sha256'].items():
                self.assertEqual(hashlib.sha256(archive.read(prefix+name)).hexdigest(),digest)
            stem='symptoms/repeated-retrieval'
            for suffix in ('.html','.md','.xml'):
                self.assertIn(prefix+'html/'+stem+suffix,archive.namelist())
            self.assertIn(prefix+'markdown/'+stem+'.md',archive.namelist())
            self.assertEqual(archive.read(prefix+'xml/entries/'+stem+'.xml'),(self.root/'entries'/Path(stem+'.xml')).read_bytes())
            self.assertIn(prefix+'skills/agent-diagnostics/SKILL.md',archive.namelist())
            self.assertIn(prefix+'html/assets/vendor/annotate-1.5.3.js',archive.namelist())
            self.assertIn(prefix+'html/assets/vendor/annotate-LICENSE.txt',archive.namelist())
            for source in (self.root/'docs').rglob('*.md'):
                relative=source.relative_to(self.root)
                self.assertIn(prefix+'html/'+relative.with_suffix('.html').as_posix(),archive.namelist())
                self.assertEqual(archive.read(prefix+'markdown/'+relative.as_posix()),source.read_bytes())
        self.assertEqual(package(self.root,'0.1.0','a'*40).read_bytes(),original)
        checksum=path.with_suffix('.zip.sha256').read_text().split()[0]
        self.assertEqual(hashlib.sha256(original).hexdigest(),checksum)
    def test_rejects_bad_version_and_stale_xml(self):
        self.search_fixture()
        for version in ('v0.1.0','../bad','0.1','01.1.0','0.1.0;echo bad'):
            with self.subTest(version=version),self.assertRaises(ValueError):
                package(self.root,version,'a'*40)
        (self.root/'dist/symptoms/repeated-retrieval.xml').write_text('stale')
        with self.assertRaisesRegex(ValueError,'does not match'):
            package(self.root,'0.1.0','a'*40)
