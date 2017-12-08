import itertools

edges = {}
nodes = []

with open('input.txt', 'r') as f:
	for i in f.readlines():
		fl = i.rstrip().split(' ')
		fn = fl[0]
		tn = fl[2]
		dist = int(fl[4])

		if (fn in edges):
			edges[fn][tn] = dist
		else:
			edges[fn] = {tn: dist}

		if (tn in edges):
			edges[tn][fn] = dist
		else:
			edges[tn] = {fn: dist}

		if not (fn in nodes): nodes.append(fn)
		if not (tn in nodes): nodes.append(tn)

pls = []

for j in itertools.permutations(nodes):
	pl = 0
	for n in range(0,len(j)-1):
		pl += edges[j[n]][j[n+1]]
	pls.append((pl, j))

print ("Shortest:", sorted(pls)[0])
print ("Longest:", sorted(pls, reverse=True)[0])



