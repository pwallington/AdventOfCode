#!/usr/bin/python

import sys

sum = 0

for line in sys.stdin:
  min = 1000
  max = 0
  for n in map(int, line.strip().split()):
    if n > max:
      max = n
    if n < min:
      min = n
  sum += max-min

print (sum)

