import sys, itertools
happy = {}
names = []

with open('input.txt','r') as f:
	for line in f.readlines():
		line=line.rstrip()
		if not line:
			continue
		lf = line.split(' ')
		(n1,n2) = (lf[0],lf[10])
		if n1 not in names:
			print("Adding ",n1)
			names.append(n1)
			happy[n1] = {}
		if n2 not in names:
			print("Adding ",n2)
			names.append(n2)
			happy[n2] = {}

		if (lf[2] == 'lose'):
			delta = -int(lf[3])
		elif (lf[2] == 'gain'):
			delta = int(lf[3])
		else:
			print("line error!", lf[2])
			sys.exit(1)

		happy[n1][n2] = delta

	print (happy)

	result = []
	for seats in itertools.permutations(names):
		print ("Seats:",seats)
		neighbors = [(i,j) for i,j in zip(seats,seats[1:])]
		# print ("Neighbors:",neighbors)
		# for i in neighbors:
		# 	print(i,happy[i[0]][i[1]],happy[i[1]][i[0]])

		tothaps=sum(happy[i][j]+happy[j][i] for (i,j) in neighbors)
		# print (neighbors, tothaps)
		result.append((tothaps, seats))

	result.sort()
	print(result[-1])

