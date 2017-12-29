#!/usr/bin/python
import sys
import numpy as np
import itertools as it
import operator as op
import math
from functools import reduce

def parseIn(i=[]):
	for line in sys.stdin:
		line = line.strip()
		i.append(line)
	return (i)

if __name__ == '__main__':
	lines = parseIn()
	print(lines)
	for line in lines:
		max_dist = pos_ns = pos_ew = 0
		moves = line.split(',')
		for move in moves:
			if move == "n":
				pos_ns += 1
			elif move == "s":
				pos_ns -= 1
			elif move == "ne":
				pos_ns += 0.5
				pos_ew += 1
			elif move == "se":
				pos_ns -= 0.5
				pos_ew += 1
			elif move == "nw":
				pos_ns += 0.5
				pos_ew -= 1
			elif move == "sw":
				pos_ns -= 0.5
				pos_ew -= 1

			maxdist = min(maxdist, abs(pos_ew) + max(0, abs(pos_ns) - abs(pos_ew/2)))
		print(pos_ns, pos_ew, dist)
