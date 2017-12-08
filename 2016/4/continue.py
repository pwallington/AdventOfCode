import hashlib
import time
start = time.time()
key="bgvyzdsv"

# Hashing at around 300k/sec on one core
# 7 zeroes too 1071 sec, 
num=318903846
zeroes=7

while (True):
	num += 1
	i = "{}{}".format(key, num).encode('utf-8')
	s=hashlib.md5(i).digest().hex()

	if (s[0:zeroes] == '0'*zeroes):
		print (s, zeroes, "zeroes", num, i, "- {:.3f} sec".format(time.time()-start))
		zeroes += 1
		# Repeat this number in case it has more zeroes!
		num -= 1
	elif (not(num % 1e7)):
		print (num)