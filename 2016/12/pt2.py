import json


def sumtraverse(j):
	if isinstance(j,int):
		return j
	elif isinstance(j,list):
		return sum([sumtraverse(i) for i in j])
	elif isinstance(j,dict):
		if ('red' in list(j)+list(j.values())):
			return 0
		else:
			return sum(sumtraverse(j[i]) for i in j)
	else:
		return 0

with open('input.txt','r') as f:
	l=f.readline().rstrip()
	j=json.loads(l)
	print(sumtraverse(j))
