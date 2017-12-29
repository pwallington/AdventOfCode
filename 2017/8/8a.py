#!/usr/bin/python

import sys
import numpy as np
import itertools as it
import math

registers = {}
comparators = { '>': (lambda x, y: x>y),
				'<': (lambda x, y: x<y),
				'<=': (lambda x, y: x<=y),
				'>=': (lambda x, y: x>=y),
				'==': (lambda x, y: x==y),
				'!=': (lambda x, y: x!=y),
			}

def parseIn(i=[]):
	for line in sys.stdin:
		line = line.strip()
		i.append(line)
	return (i)

def parseLine(line):
	fields = line.split(" ")
	if len(fields) != 7:
		print ("invalid line format:", line)
		raise ValueError

	if fields[1] not in ("inc", "dec"):
		print ("unknown instruction", fields[2], "at line", line)
		raise ValueError

	if fields[5] not in comparators:
		print ("unknown comparator", fields[5], "at line", line)
		raise ValueError

	inc_val = int(fields[2])
	if fields[1] == "dec":
		inc_val *= -1
	if comparators[fields[5]](registers.get(fields[4], 0), int(fields[6])):
		print ("adding", inc_val, "to register", fields[0])
		registers[fields[0]] = registers.get(fields[0], 0) + inc_val
	else:
		print ("test", fields[4:6], "failed,", fields[4], "=", registers.get(fields[4]))




if __name__ == '__main__':
	lines = parseIn()
	for i in lines:
		print (i)
		parseLine(i)
		print (registers)

	print ("Max register = ", max(registers.values()))