#!/usr/bin/python
from collections import Counter

f = open('input', 'r')
st = f.read()
c=Counter(st)
print (c['(']-c[')'])