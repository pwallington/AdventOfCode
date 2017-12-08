d = {}
r = {}

res = {}

def generate(start, target):
	# print ("Generate", target, "from", start)
	if start in res:
		return res[start]

	if start == target: 
		return 0	

	# Shortcut because patterns are always expansions
	if len(start) > len(target):
		# print ("overshoot")
		return None

	shortest = None
	shortstr = None

	# for each possible reaction, longest first?
	for k in sorted(d, reverse=True, key=lambda a: len(a)):
		# print(k, "=>", d[k])
		# for each match of the reaction
		pos=0
		while (pos >= 0):
			np = start.find(k,pos)
			if np == -1:
				# No match
				break
			# print ("match", k, "@", np, pos)
			# Create and decompose the result
			pos = np+len(k)
			for r in d[k]:
				newstr = start[:np]+r+start[pos:]
				# print(k, "=>", r, "gives:", newstr)
				l = generate(newstr, target)
				if (l is not None and (shortest is None or l < shortest)):
					shortest = l + 1
					shortstr = newstr
					print ("New Best of", shortest, "for", start, "after", d[k], "=>", k)
	if shortest:
		print ("Returning Best for", start, ": ", shortest)
	res[start] = shortest
	return shortest


with open('input.txt','r') as f:
	for line in f.readlines():
		lf = line.rstrip().split(' ')
		if lf[0] in d:
			d[lf[0]].append(lf[2])
		else:
			d[lf[0]] = [lf[2],]
	print ("d:", d)
	mol = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
	# print (generate('e', 'HOHOHO'))
	# print (generate('e', 'HOHOHOHOHOHOHOHOHOHOHOHOHOHOHO'))
	print (generate('e', mol))










