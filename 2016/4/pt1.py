import hashlib
key="bgvyzdsv"
num=0

while (num < 1e9):
	num += 1
	i = "{}{}".format(key, num).encode('utf-8')
	s=hashlib.md5(i).digest()
	if (len(s) < 3): 
		continue
	if (s[0] > 0):
		continue
	if (s[1] > 0):
		continue
	if (s[2] > 0):
		continue
	print (num, i, ":".join("{:02x}".format(c) for c in s))
	exit(0)

exit(1)

