import sys 
def looknsay(s):
	ret = ""
	l = 1
	n = s[0]
	for i in range(1,len(s)):
		if (s[i] == n):
			l += 1
		else:
			ret += "{}{}".format(l,n)
			l=1
			n=s[i]

	ret += "{}{}".format(l,n)
	return ret

def lookrecurse(s,d):
	if (d<=0):
		return s
	return(looknsay(lookrecurse(s,d-1)))

print(len(lookrecurse("1113222113",int(sys.argv[1]))))

