#!/usr/bin/python
import sys
import numpy as np
import itertools as it
import math

def parseIn(i=[]):
	for line in sys.stdin:
		line = line.strip()
		i.append(line)
	return (i)

if __name__ == '__main__':
	ringLen = 256
	if len(sys.argv) != 1:
		ringLen = int(sys.argv[1])

	lines = parseIn()
	print(lines)
	for line in lines:

		ring = list(range(ringLen))
		p = skipSize = 0
		lengths = line.split(',')
		for l in lengths:
			l=int(l)
			print("len:", l, "pos:", p, "skip:",skipSize)
			if (p+l) <= len(ring):
				print (ring[p:p+l]," = ", list(reversed(ring[p:p+l])))
				ring[p:p+l] = reversed(ring[p:p+l])
			else:
				temp = list(reversed(ring[p:] + ring[:(p+l)-ringLen]))
				print("temp:", temp)
				print (ring[p:], " = ", temp[:ringLen-p])
				ring[p:] = temp[:ringLen-p]
				print (ring[:(p+l)-ringLen]," = ", temp[ringLen-p:])
				ring[:(p+l)-ringLen] = temp[ringLen-p:]
			p += l + skipSize
			p %= len(ring)
			skipSize += 1

			print	(ring, "\n")
		print(ring[0] * ring[1])

#		0		1		2		3		4		5
# 3, 4
#								1		2		3		4
