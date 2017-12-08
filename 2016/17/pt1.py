import sys
# from collections import Counter
import itertools
# from functools import reduce

# arg = sys.argv[1]

containers = []

with open('input.txt','r') as f:
	for line in f.readlines():
		containers.append(int(line.rstrip()))
		
print (sum(containers))

count = 0
target = 150

for i in range(1,len(containers)):
	for c in itertools.combinations(containers, i):
		# print (list(c))
		# print (sum(c))
		if (sum(c) == target):
			count += 1

print (count)
