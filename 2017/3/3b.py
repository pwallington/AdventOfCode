#!/usr/bin/python

import sys
import numpy as np
from math import sqrt

grid = np.zeros((500,500))

for line in sys.stdin:
  line = line.strip()
  target = int(line)
  break
 

def around(x, y, g):
  sum = 0
  for i in (-1, 0, 1):
    for j in (-1, 0, 1):
      sum += g[x+i][y+j]
  sum -= g[x][y]
  print (x, y, sum)
  return sum

cell = 1
grid[0][0] = 1

while (cell < 100):
  cell += 1
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

  grid[pos_x][pos_y] = around(pos_x, pos_y, grid)
  print (grid[pos_x][pos_y])
  if (grid[pos_x][pos_y] > target):
   break

  
