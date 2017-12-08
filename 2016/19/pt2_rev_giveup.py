import re
from string import ascii_lowercase as lower
from string import ascii_uppercase as upper
import sys

mol = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
m = re.findall('['+upper+']['+lower+']?', mol)
d = {}
e = []
r = {}

res = {}

def decompose(mol):
	if mol in res:
		return res[mol]

	shortest = None
	shortstr = None
	# print ("Decompose:", mol)
	# One step to finish!
	if mol in e:
		return 1

	# for each possible reaction
	for k in sorted(d, reverse=True, key=lambda a: len(a)):
		# for each match of the reaction
		# for m in re.finditer(k,mol):
		# 	newstr = mol[:m.span()[0]]+d[k]+mol[m.span()[1]:]
		pos=0
		while (pos >= 0):
			np = mol.find(k,pos)
			if np == -1:
				# No match
				break
			# Create and decompose the result
			pos = np+len(k)
			newstr = mol[:np]+d[k]+mol[pos:]
			l = decompose(newstr)
			if (l and (shortest is None or l < shortest)):
				shortest = l + 1
				shortstr = newstr
				# print ("New Best of", shortest, "for", mol, "after", d[k], "=>", k)
	# if shortest:
		# print ("Returning Best for", mol, ": ", shortest)
	res[mol] = shortest
	return shortest

def topdecompose(mol):
	# for each possible reaction
	for k in d:
		# for each match of the reaction

		for m in re.finditer(k,mol):
			# Create and decompose the result
			newstr = mol[:m.span()[0]]+d[k]+mol[m.span()[1]:]
			l = decompose(newstr)
			if l:
				return l + 1


with open('input.txt','r') as f:
	for line in f.readlines():
		lf = line.rstrip().split(' ')
		if lf[0] == 'e':
			e.append(lf[2])
		else:
			d[lf[2]] = lf[0]

	print ("d:", d)
	print ("e:", e)

	# print (topdecompose('HOHOHOHOHOHOHOHOHOHOHOHOHOHOHO'))
	# print (decompose('HOHOHOHOHOHOHOHOHOHOHOHOHOHOHO'))
	print (decompose(mol))










