#!/usr/bin/python

f = open('input', 'r')
st = f.read()

pos = 0
floor = 0

for i in st:
	pos+=1
	if (i=='('):
		floor+=1
	elif (i==')'):
		floor-=1

	if (floor < 0):
		print (pos)
		exit(0)


exit(1)



