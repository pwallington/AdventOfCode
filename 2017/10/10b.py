#!/usr/bin/python
import sys
import numpy as np
import itertools as it
import math
from functools import reduce
from operator import xor

def parseIn(i=[]):
	for line in sys.stdin:
		line = line.strip()
		i.append(line)
	return (i)

def condense(r_in):
	if len(r_in) != 256:
		print("ERR: Wrong input length to condense!", len(r_in))
		return None
	return [reduce(xor, r_in[16*i:16*(i+1)]) for i in range(16)]


def flip(ring, l, p):
	# print("FLIP: len:", l, "pos:", p)
	if (p+l) <= len(ring):
		# print (ring[p:p+l]," = ", list(reversed(ring[p:p+l])))
		ring[p:p+l] = reversed(ring[p:p+l])
	else:
		temp = list(reversed(ring[p:] + ring[:(p+l)-ringLen]))
		# print("temp:", temp)
		# print (ring[p:], " = ", temp[:ringLen-p])
		ring[p:] = temp[:ringLen-p]
		# print (ring[:(p+l)-ringLen]," = ", temp[ringLen-p:])
		ring[:(p+l)-ringLen] = temp[ringLen-p:]
	return(ring)
	
if __name__ == '__main__':
	ringLen = 256
	rounds = 64
	final = [17, 31, 73, 47, 23]

	if len(sys.argv) > 1:
		ringLen = int(sys.argv[1])
	if len(sys.argv) > 2:
		rounds = int(sys.argv[2])

	lines = parseIn()
	# print(lines)
	for line in lines:
		ring = list(range(ringLen))
		p = skipSize = 0
		lengths = list(map(ord, list(line))) + final
		for i in range(rounds):
			for l in lengths:
				l=int(l)
				ring = flip(ring, l, p)
				p += l + skipSize
				p %= len(ring)
				skipSize += 1
		dense = condense(ring)

		for i in dense:
			print("{:02x}".format(i), end='')
		print()
