#!/usr/bin/env -S uv run --script
# Build first: uv run --script tools/build.py
# Package: uv run --script tools/package_release.py --version 0.1.0 --commit <full-sha>
# /// script
# requires-python = ">=3.11"
# dependencies = ["lxml==6.1.1"]
# ///
"""Package a validated site and canonical corpus with version and checksums."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import zipfile
try:
    from .xml_entries import load
except ImportError:
    from xml_entries import load

ROOT=Path(__file__).resolve().parents[1]

def package(root=ROOT,version='0.1.0',commit=None):
    root=Path(root)
    if not re.fullmatch(r'(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)',version):
        raise ValueError('Version must be MAJOR.MINOR.PATCH, without a v prefix')
    if not commit or not re.fullmatch(r'[0-9a-f]{40}',commit):
        raise ValueError('Provide the full source commit SHA')
    docs,_,_,_=load(root)
    site=root/'dist'
    if not (site/'pagefind/pagefind.js').is_file():
        raise ValueError('Build the site and Pagefind index before packaging')
    files={}
    for p in site.rglob('*'):
        if p.is_file():files['html/'+p.relative_to(site).as_posix()]=p.read_bytes()
    for p in site.rglob('*.md'):
        files['markdown/'+p.relative_to(site).as_posix()]=p.read_bytes()
    for folder in ('entries','schema','skills'):
        for p in (root/folder).rglob('*'):
            if p.is_file():
                prefix='xml/' if folder in ('entries','schema') else ''
                files[prefix+p.relative_to(root).as_posix()]=p.read_bytes()
    for p in (root/'schema').rglob('*'):
        if p.is_file():files['markdown/schema/'+p.name]=p.read_bytes()
    for doc in docs:
        path=Path(doc['path'])
        for suffix in ('.html','.md','.xml'):
            if not (site/path.with_suffix(suffix)).is_file():
                raise ValueError('Missing format variant: '+str(path.with_suffix(suffix)))
        if (site/path.with_suffix('.xml')).read_bytes()!=(root/doc['source']).read_bytes():
            raise ValueError('Site XML does not match canonical source')
    manifest={'version':version,'tag':'v'+version,'source_commit':commit,
              'sha256':{name:hashlib.sha256(data).hexdigest() for name,data in sorted(files.items())}}
    files['manifest.json']=(json.dumps(manifest,indent=2)+'\n').encode()
    output=root/'release';output.mkdir(exist_ok=True)
    archive=output/f'adm-{version}.zip'
    with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for name,data in sorted(files.items()):
            info=zipfile.ZipInfo(f'adm-{version}/'+name,date_time=(1980,1,1,0,0,0))
            info.compress_type=zipfile.ZIP_DEFLATED
            info.external_attr=0o100644<<16
            z.writestr(info,data)
    checksum=archive.with_suffix('.zip.sha256')
    checksum.write_text(hashlib.sha256(archive.read_bytes()).hexdigest()+'  '+archive.name+'\n')
    print(archive)
    return archive

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--version',default='0.1.0')
    p.add_argument('--commit',required=True)
    args=p.parse_args()
    try:package(version=args.version,commit=args.commit)
    except ValueError as e:p.exit(1,str(e)+'\n')
