#!/usr/bin/env -S uv run --script
# Run after `npm ci`: uv run --script tools/test.py [-v]
# Select test files: uv run --script tools/test.py -p test_release.py
# /// script
# requires-python = ">=3.11"
# dependencies = ["lxml==6.1.1", "mkdocs==1.6.1"]
# ///
"""Discover and run the repository's tests with their inline dependencies."""
from pathlib import Path
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))

if __name__=='__main__':
    unittest.main(module=None,argv=[sys.argv[0],'discover','-s',str(ROOT/'tests'),*sys.argv[1:]])
