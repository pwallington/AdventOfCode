area=0
ribbon=0
with open('input.txt', 'r') as f:
	for line in f:
		d = sorted([int(x) for x in line.rstrip().split('x')])
		print("box: {0:d} x {1:d} x {2:d}\n".format(*d))
		area += (3*d[0]*d[1] + 2*d[1]*d[2] + 2*d[0]*d[2])
		ribbon += 2*(d[0]+d[1]) + d[0]*d[1]*d[2]


print(area, "sq ft paper")
print(ribbon, "ft ribbon")
