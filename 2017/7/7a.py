#!/usr/bin/python

import re
import sys
import numpy as np
import itertools as it
import math

leafs = {}
branches = {}

for line in sys.stdin:
	line = line.strip()
	shortmatch = re.match(r"^(.+) \((\d+)\)$", line)
	if shortmatch:
		print (shortmatch.group(1), "is a leaf!")
		leafs[shortmatch.group(1)] = {'w': shortmatch.group(2) }
	else:
		longmatch = re.match(r"^(.+) \((\d+)\) -> (.+)$", line)
		if longmatch:
			print (longmatch.group(1), "is a branch")
			children = re.split(r'[-> ,]+', longmatch.group(3))
			branches[longmatch.group(1)] = {'w': longmatch.group(2), 'c': children}

for p in branches:
	print (p, 'has children', branches[p]['c'])
	for c in branches[p]['c']:
		if c in branches:
			print (p, 'is parent of', c)
			branches[c]['p'] = p
		elif c in leafs:
			print (p, 'is parent of leaf', c)
			leafs[c]['p'] = p
		else:
			print (p, 'has unknown child', c)

print('\n', branches, '\n')

for n in branches:
	if 'p' not in branches[n]:
		print("no parent found for", n)

