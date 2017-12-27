#!/usr/bin/python

import collections
import sys
import numpy as np
import itertools as it
import math

count = 0

for line in sys.stdin:
	line = line.strip()
	words = line.split(' ')
	if (len(set(words)) == len(words)):
  		count += 1

print(count)