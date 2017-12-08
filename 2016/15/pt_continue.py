import sys
size = int(sys.argv[1])

attrs = ['capacity', 'durability', 'flavor', 'texture']
data = {}
ingredients = []

def makeCookieNoCals(ings):
	totals = {attr: sum([ings[i]*data[i][attr] for i in ings]) for attr in attrs}
	score=1
	for i in totals:
		if totals[i] <= 0:
			return 0
		score *= totals[i]
	return score

def makeCookie(ings):
	score=makeCookieNoCals(ings)
	return (score, 0 if score == 0 else sum([ings[i]*data[i]['calories'] for i in ings]))

with open('input.txt','r') as f:
	for line in f.readlines():
		lf = line.rstrip().split(': ')
		ing = lf[0]
		ingredients.append(ing)
		lf2 = lf[1].split(', ')
		data[ing] = {i.split(' ')[0]:int(i.split(' ')[1]) for i in lf2 }

maxscore=0
allcookies = {}

from itertools import combinations_with_replacement as cwr
from collections import Counter
for i in cwr(ingredients, size):
	ings = Counter(i).most_common()
	score = makeCookieNoCals(dict(ings))
	if score > 0 and score > maxscore:
			bestcookie = ings
			maxscore = score

print("Best:", maxscore, bestcookie)