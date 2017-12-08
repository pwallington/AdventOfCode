import operator

r = []
pos = {}
score = {}
racelen=2503

with open('input.txt', 'r') as f:
	for line in f.readlines():
		lf=line.rstrip().split(' ')
		rd = {'name': lf[0], 'speed': int(lf[3]), 'fly': int(lf[6]), 'rest':int(lf[13])}
		rd['dist']=rd['speed']*rd['fly']
		rd['time']=rd['fly']+rd['rest']

		rd['cycles']=int(racelen/rd['time'])
		if (rd['fly'] + rd['cycles']*rd['time'] < racelen):
			rd['racedist'] = (rd['cycles']+1) * rd['dist']
		else:
			rd['racedist'] = rd['cycles']*rd['dist'] + (racelen - rd['cycles']*rd['time']) * rd['speed']

		rd['pos']=[]
		rd['pos'].append(0)
		pos[rd['name']]=[]
		pos[rd['name']].append(0)
		print(rd)
		state='fly'
		t=rd[state]
		for sec in range(1,racelen+1):
			# sec has elapsed
			if (state == 'fly'):
				rd['pos'].append(rd['pos'][-1] + rd['speed'])
			else:
				rd['pos'].append(rd['pos'][-1])
			t -= 1
			if (t == 0):
				# change state, reset time
				state = 'rest' if (state == 'fly') else 'fly'
				t = rd[state]

		r.append(rd)

		score[rd['name']] = 0
		pos[rd['name']] = 0

	r.sort(reverse=True, key=operator.itemgetter('racedist'))
	print(r[0])

for i in range(1,racelen+1):
	md=max(x['pos'][i] for x in r)
	print ("max dist", md, "at time", i)
	rds=[s['name'] for s in r if s['pos'][i] == md]
	rd=sorted(r, reverse=True, key=lambda x:x['pos'][i])[0]
	print ("sec", i, "leaders", list(rds))
	print (["{}:{}".format(n['name'],n['pos'][i]) for n in r])
	for n in rds:
		score[n] += 1

print (score)
print ("Winner:", max(score.items(), key=operator.itemgetter(1)))
print ("total pts:", sum((score[i] for i in score)))



