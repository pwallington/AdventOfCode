from itertools import combinations as cmb

# boss stats
hp = 100
dmg = 8 # we must do less!
dfn = 2

wep = {'Dagger': [8,4,0],
	'Shortsword': [10,5,0],
	'Warhammer': [25,6,0],
	'Longsword': [40,7,0],
	'Greataxe': [74,8,0] }

arm = {'Leather':[13,0,1],
	'Chainmail':[31,0,2],
	'Splintmail':[53,0,3],
	'Bandedmail':[75,0,4],
	'Platemail':[102,0,5],
	'None':[0,0,0]}

ring = {'Dmg1': [25,1,0],
	'Dmg2': [50,2,0],
	'Dmg3': [100,3,0],
	'dfn1': [20,0,1],
	'dfn2': [40,0,2],
	'dfn3': [80,0,3],
	'None': [0,0,0],
	'None2': [0,0,0],
	}

highcost = 0

# must pick one weapon
for w in wep:
	for a in arm:
		for (r1,r2) in cmb(ring, 2):
			stats = [sum(x) for x in zip(wep[w],arm[a],ring[r1],ring[r2])]
			if (stats[0] > highcost and
				max(1,stats[1]-dfn) < max(1,dmg-stats[2])):
				highcost = stats[0]
				print(w, a, r1, r2, stats, highcost)
