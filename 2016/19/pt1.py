import re
from string import ascii_lowercase as lower
from string import ascii_uppercase as upper
import sys


mol = "CRnCaSiRnBSiRnFArTiBPTiTiBFArPBCaSiThSiRnTiBPBPMgArCaSiRnTiMgArCaSiThCaSiRnFArRnSiRnFArTiTiBFArCaCaSiRnSiThCaCaSiRnMgArFYSiRnFYCaFArSiThCaSiThPBPTiMgArCaPRnSiAlArPBCaCaSiRnFYSiThCaRnFArArCaCaSiRnPBSiRnFArMgYCaCaCaCaSiThCaCaSiAlArCaCaSiRnPBSiAlArBCaCaCaCaSiThCaPBSiThPBPBCaSiRnFYFArSiThCaSiRnFArBCaCaSiRnFYFArSiThCaPBSiThCaSiRnPMgArRnFArPTiBCaPRnFArCaCaCaCaSiRnCaCaSiRnFYFArFArBCaSiThFArThSiThSiRnTiRnPMgArFArCaSiThCaPBCaSiRnBFArCaCaPRnCaCaPMgArSiRnFYFArCaSiThRnPBPMgAr"
m = re.findall('['+upper+']['+lower+']?', mol)
d = {}
r = {}
with open('input.txt','r') as f:
	for line in f.readlines():
		lf = line.rstrip().split(' ')
		if lf[0] in d:
			d[lf[0]].append(lf[2])
		else:
			d[lf[0]] = [lf[2],]

for s in range(0,len(m)):
	if m[s] in d:
		for l in d[m[s]]:
			r[''.join((m[0:s]+[l]+m[s+1:]))] = 1

print(len(r))



