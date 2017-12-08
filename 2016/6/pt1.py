#!/usr/bin/python
import sys

grid = {}

for line in sys.stdin.readlines():
	fields = line.rstrip().split(' ')

	# Strip 'turn' off to give consistent field nubmering
	if (fields[0] == "turn"):
		fields = fields[1:]

	if (fields[2] != "through"):
		exit [1]

	pos1 = tuple(int(i) for i in fields[1].split(','))
	pos2 = tuple(int(i) for i in fields[3].split(','))

	print (fields, pos1, pos2)

	for i in range(pos1[0], pos2[0]+1):
		for j in range(pos1[1], pos2[1]+1):
			if   (fields[0] == "on"):
				grid[(i,j)] = True
			elif (fields[0] == "off"):
				grid[(i,j)] = False
			elif (fields[0] == "toggle"):
				grid[(i,j)] = grid.get((i,j),False) ^ True
			else:
				exit(1)

print (sum(grid.values()))