#!/usr/bin/python

import re
import sys
import numpy as np
import itertools as it
import math

sys.setrecursionlimit(20)

class Node:
	def __repr__(self):
		return (self.__str__())
	def __str__(self):
		if self.childnames:
			return ("{} ({}) -> {}".format(self.name, self.weight, ', '.join(self.childnames)))
		else:
			return ("{} ({})".format(self.name, self.weight))

	def __init__(self, name, weight, childnames=[], parent=None):
		self.weight = int(weight)
		self.name = name
		self.childnames = childnames
		self.parent = parent
		self.childnodes = []


	def subWeight(self):
		self.sw = self.weight
		# print (self.name, "getting child weight from", self.childnames, "\n", self.childnodes)
		for c in self.childnodes:
			self.sw += c.subWeight()
		return self.sw

	def checkBalance(self, targetweight=None):
		if self.subWeight() == targetweight:
			print(self.name, "nothing to see here...")
			return (self.weight)

		balance = {}
		if not self.childnodes:
			if self.weight != targetweight:
				print (self.name, "leaf with wrong weight")
				print (targetweight, "vs", self.weight)
			return (self.weight)
		else:
			for c in self.childnodes:
				w = c.subWeight()
				if w in balance:
					balance[w].append(c)
				else:
					balance[w] = [c]
			if len(balance) == 1:
				(w, n) = balance.popitem()
				print (self.name, ": all my subtrees are balanced, it must be me at fault!")
				print("I weigh", self.weight, "vs target",
					 targetweight - len(n) * w)
			else:
				for i in range(len(balance)):
					k = list(balance)[i]
					if len(balance[k]) > 1:
						## more than one subtree with this weight == balanced subtrees
						pass
					else:
						## odd one out must be unbalanced
						 # assume the puzzle has a single solution,
						 # so any other key will be the correct target weight
						target = list(balance)[i-1]
						for c in balance[k]:
							print ("now going to check", c)
							c.checkBalance(target)


def parseIn(nodes={}):
	for line in sys.stdin:
		line = line.strip()
		shortmatch = re.match(r"^(.+) \((\d+)\)$", line)
		if shortmatch:
			print (shortmatch.group(1), "is a leaf!")
			nodes[shortmatch.group(1)] = Node(shortmatch.group(1), shortmatch.group(2))
		else:
			longmatch = re.match(r"^(.+) \((\d+)\) -> (.+)$", line)
			if longmatch:
				print (longmatch.group(1), "is a branch")
				children = tuple(re.split(r'[-> ,]+', longmatch.group(3)))
				nodes[longmatch.group(1)] = Node(longmatch.group(1), longmatch.group(2), childnames=children)
	return (nodes)

def findParents(nodes={}):
	for p in nodes.values():
		if p.childnames:
			print (p.name, 'has childnames', p.childnames)
			for c in p.childnames:
				if c in nodes:
					print (p.name, 'is parent of', c)
					nodes[c].parent = p
					p.childnodes.append(nodes[c])
				else:
					print (p.name, 'has unknown child', c)

def findRoots(nodes=[]):
	count = 0
	roots = []
	for n in nodes.values():
		if not n.parent:
			print("Found potential root", n)
			roots.append(n)
	if len(roots) > 1:
		print("Warning: More than one parentless node found! Did you call findParents()?")
	return (roots)


if __name__ == '__main__':
	nodes = {}

	parseIn(nodes)
	findParents(nodes)
	for i in nodes:
		print (i, nodes[i].name, nodes[i].childnodes)
	roots = findRoots(nodes)
	for r in roots:
		print(r.name, r.subWeight())
		r.checkBalance()
