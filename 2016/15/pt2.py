
size = 100

attrs = ['capacity', 'durability', 'flavor', 'texture']
data = {}
ingredients = []

def makeCookie(ings):
	totals = {}
	for attr in attrs:
		totals[attr] = 0
		totals[attr] = sum([ings[i]*data[i][attr] for i in ings])

	calories = sum([ings[i]*data[i]['calories'] for i in ings])
	score=1
	for i in totals:
		if totals[i] <= 0:
			return (0,0)
		score *= totals[i]

	# print("Cookie:",calories,totals)
	return (score, calories)

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
	(score, calories) = makeCookie(dict(ings))
	if score > 0 and calories == 500:
		print ("Ingredients:", ings, "Score:", score)
		allcookies[tuple(ings)] = score
		if score > maxscore:
			bestcookie = ings
			maxscore = score

print("Best:", maxscore, bestcookie)