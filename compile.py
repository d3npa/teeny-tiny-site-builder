#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
from glob import glob
from shutil import copytree, rmtree

INPUT = "input"
OUTPUT = "output"
PLACEHOLDER = "{{ BODY }}"

def clean_output():
	if os.path.exists(OUTPUT):
		rmtree(OUTPUT)

def copy_files():
	copytree(INPUT, OUTPUT, symlinks=True)

def compile_drafts():
	with open("template.html", "r", encoding="utf-8") as f:
		template = f.read()
	for draft in glob("%s/**/*.draft" % OUTPUT, recursive=True):
		with open(draft, "r", encoding="utf-8") as f:
			document = template.replace(PLACEHOLDER, f.read())
		with open(draft, "w", encoding="utf-8") as f:
			f.write(document)
		os.rename(draft, draft[:-5] + "html")

if __name__ == "__main__":
	clean_output()
	copy_files()
	compile_drafts()
