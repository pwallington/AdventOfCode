#!/usr/bin/python

import sys
import numpy as np
import itertools as it
import math

for line in sys.stdin:
	line = line.strip()
	banks = [int(i) for i in line.split()]

	record = list()

	while True:
		ct = max(banks)
		sel_bank = banks.index(ct)
		banks[sel_bank] = 0
		for i in range(ct):
			banks[(i+sel_bank+1) % len(banks)] += 1

		print(banks)
		if (tuple(banks) in record):
			break
		else:
			record.append(tuple(banks))
	print (len(record), record.index(tuple(banks)), len(record) - record.index(tuple(banks)))