import sys
# from collections import Counter
import itertools
# from functools import reduce

# arg = sys.argv[1]
with open('input.txt','r') as f:
	containers = [int(line.rstrip()) for line in f.readlines()]
	print (containers)

	count = 0
	target = 150

	for i in range(1,len(containers)):
		count += len([1 for c in itertools.combinations(containers, i) if sum(c) == target])
		if (count != 0):
			print (i)
			break
	print (count)