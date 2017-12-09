#!/usr/bin/python

import sys

sum = 0

for line in sys.stdin:
  a = list(map(int, line.strip().split()))
  for n in a:
    for d in a:
      r = n/d
      if (r > 1) and (int(r) == r): 
        print("Found", n, "/", d, "=", r)
        sum += r
        break

print (sum)

