#!/usr/bin/python

import sys
import numpy as np
import itertools as it
import math

jumplist = []
pc = 0
steps = 0

for line in sys.stdin:
  line = line.strip()
  jumplist.append(int(line))

exit = len(jumplist)
jumplist.append(999)

while (pc != exit):
	steps += 1
	jump = jumplist[pc]
	if (jump < 3):
		jumplist[pc] += 1
	else:
		jumplist[pc] -= 1
	pc += jump

print (steps)