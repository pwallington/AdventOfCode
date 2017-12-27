#!/usr/bin/python

from math import sqrt
import sys

for line in sys.stdin:
  line = line.strip()
  cell = int(line)
  
  # Find largest odd square below cell #
  start = int((sqrt(cell)-1)/2)

  pos_x = start
  pos_y = -start
    
  square = (2*start+1)**2
  offset = cell - square
  sidelen = 2*(start+1)
# UP
  if offset > 0:
    pos_x += 1
    pos_y += min(offset-1, sidelen-1)
    print ("out 1, UP",min(offset-1, sidelen) )

# LEFT
  if offset > sidelen:
    pos_x -= min(offset-sidelen, sidelen)
    print ("LEFT", min(offset-sidelen, sidelen))

# DOWN
  if offset > 2*sidelen:
    pos_y -= min(offset-2*sidelen, sidelen)
    print ("DOWN", min(offset-2*sidelen, sidelen))

# RIGHT
  if offset > 3*sidelen:
    pos_x += offset-3*sidelen
    print ("RIGHT", offset-3*sidelen)

  print(start, square, offset, sidelen, ":", pos_x, pos_y, ":", abs(pos_x) + abs(pos_y))

