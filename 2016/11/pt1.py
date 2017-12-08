import sys, re
from functools import reduce

def rule1(s):
	""" must contain 3 consecutive characters """
	if (len(s) < 3):
		return False

	groups = [(i,j,k) for i,j,k in zip(s,s[1:],s[2:])]
	for g in groups:
		if (ord(g[1])-ord(g[0]) == 1
			and 
			ord(g[2])-ord(g[1]) == 1):
			return True
	return False

def rule2(s):
	""" Passwords must not contain 'i', 'o' or 'l' """
	if (re.search('[ilo]', s)):
		return False
	return True

def rule3(s):
	""" must contain 2 different pairs """
	if (len(s) < 4):
		return False

	pairs = {(i,j):1 for i,j in zip(s,s[1:]) if (i==j)}
	if (len(pairs) > 1):
		return True
	return False

rules = [rule1,rule2,rule3]


def checkRules(s):
	for rule in rules:
		if not rule(s):
			# print ("{} - Rule '{}' failed!".format(s, rule.__name__))
			return False
	return True

def sinc(s):
	l=list(s)[::-1]
	pos = 0
	while (pos < len(l) and l[pos] == "z"):
		l[pos] = "a"
		pos += 1
	if (pos >= len(l)):
		l.append("a")
	else:
 		l[pos] = chr(ord(l[pos])+1)
	return "".join(l[::-1])

start = 'cqjxjnds'
reqd = 2
found = 0
while (found<reqd):
# for i in range(0,100):
	if checkRules(start):
		print ("{} is valid".format(start))
		found += 1
	start = sinc(start)

# for s in sys.stdin:
# 	print (checkRules(s))