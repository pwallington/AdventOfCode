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
	lines = parseIn()
	print(lines)
	for line in lines:
		level = 0
		total = 0
		skip = inTrash = trashCount = False
		i = 0

		while i < len(line):
			print (line[i], end=' ')
			# fast skip ! and following char
			if skip:
				print  ('Skip', line[i], 'following ! at', i)
				skip = False
			elif line[i] == '!':
				print ('Skip ! at', i)
				skip = True

			elif inTrash:
				if line[i] == '>':
					print  ('inTrash end at', i)
					inTrash = False
				else:
					trashCount += 1

			elif line[i] == "<":
				print  ('inTrash start at', i)
				inTrash = True

			elif line[i] == '{':
				level += 1
				print  ('group level', level, 'start at', i)

			elif line[i] == '}':
				total += level
				print  ('group level', level, 'end at', i, total)
				level -= 1

			i += 1

print ("Groups total:", total)
print ("Trash  total:", trashCount)