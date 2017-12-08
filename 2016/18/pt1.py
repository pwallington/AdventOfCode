import sys
from collections import Counter
import itertools
from functools import reduce

arg = int(sys.argv[1])


def gol(grid):
	out = [[] for i in grid]
	for i in range(0,len(grid)):
		out[i] = [0 for k in range(0,len(grid[i]))]
		for j in range(0,len(grid[i])):
			# print ("i:",i,"j:",j,(max(0,j-1), 1+min(len(grid[i]),j+1)),(max(0,i-1), 1+min(len(grid[0]),i+1)))
			g = [[grid[r][c] for c in range(max(0,j-1), min(len(grid[i]),j+2))]
					   for r in range(max(0,i-1), min(len(grid[0]),i+2))]
			# print (g)
			n = sum(sum(a) for a in g) - grid[i][j]
			# print("n:", n)
			if n == 3:
				out[i][j] = 1
			elif n == 2 and grid[i][j] == 1:
				out[i][j] = 1
			else:
				out[i][j] = 0
	return out

with open('input.txt','r') as f:
	start = [[0 if i == '.' else 1 for i in line.rstrip()] for line in f.readlines()]
	grid = start
	print(grid)
	for i in range(0,arg):
		print("Iteration", i, sum(sum(i for i in l) for l in grid))
		grid2 = gol(grid)
		grid = grid2

	print("Finished:", sum(sum(i for i in l) for l in grid))
