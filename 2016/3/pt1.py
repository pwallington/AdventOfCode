#!/usr/bin/python

num = 3
pos = []
for i in range(0, num):
	pos.append([0,0])

grid = {}

# Initial deliveries
# Could loop thru starting pos instead...
grid[(0,0)] = num

print (pos)

# Worker ID
j = 0
with open('input.txt', 'r') as f:
	for i in f.read():
		# Move worker j
		if   (i == '>'):
			pos[j][0]+=1
		elif (i == '<'):
			pos[j][0]-=1
		elif (i == '^'):
			pos[j][1]+=1
		elif (i == 'v'):
			pos[j][1]-=1
		print (i, j, pos)

		# Deliver at j's pos (.get() needed for default)
		grid[tuple(pos[j])] = grid.get(tuple(pos[j]),0) + 1

		# Go to next worker
		j += 1
		j %= num

	print (len(grid))