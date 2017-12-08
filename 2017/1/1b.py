#!/usr/bin/python

import sys

for line in sys.stdin:
 total = 0
 line = line.strip()
 for i in range(len(line)):
  p = int(i-len(line)/2)
  if line[p] == line[i]:
    print("Match pos", i, "adding", line[i])
    total += int(line[i])
 print (total)



