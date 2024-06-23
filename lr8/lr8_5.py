"""Лабораторная работа №8"""

# 5.	Реализуйте систему лутбоксов для игры, у вас должнобыть несколько списков с предметами:
#		обычные, редкие, эпические, легендарные. У каждого из типов есть свой шанс на дроп, для
#		обычных 0.7, для редких 0.2, для эпических (0.1), для легендарных (0.05). Также существует
#		система гаранта за 20 открытых лутбоксов, выпадает легендарный предмент. При запуске программы
#		должно происходить 20 автоматических открытий лутбокса, в результате программа должна написать
#		сколько выпало, обычных, редких, эпических и легендарных. Если эпических выпало больше 3 то вы
#		должны написать (Удача!), если легендарных больше 1, вы должны написать (Большая удача!), в
#		конце вы должны написать список полученных предметов, вы должны отобразить разным цветов разное
#		качество полученных предметов (белый - обычный, синий - редкий, фиолетовый - эпический,
#		оранжевый - легендарный).

from random import random, choice, randint

nouns = ['flight', 'solution', 'extent', 'setting', 'selection', 'protection', 'mood', 'message', 'impression', 'winner', 'media', 'preparation', 'independence', 'communication', 'worker', 'engine', 'bath', 'presence', 'video', 'reputation', 'conclusion', 'knowledge', 'bedroom', 'gene', 'promotion', 'depth', 'leadership', 'thing', 'girl', 'painting', 'unit', 'perspective', 'coffee', 'possibility', 'history', 'income', 'chest', 'dad', 'wealth', 'shopping', 'chapter', 'estate', 'union', 'committee', 'percentage', 'bird', 'beer', 'stranger', 'orange', 'sector', 'hearing', 'winner', 'housing', 'driver', 'independence', 'information', 'country', 'perspective', 'engine', 'departure', 'direction', 'news', 'historian', 'girl', 'situation', 'trainer', 'midnight', 'guest', 'entry', 'software', 'republic', 'perception', 'drawing', 'technology', 'ambition', 'bedroom', 'resolution', 'emphasis', 'chemistry', 'shopping']
verbs = ['private', 'joyous', 'accidental', 'ritzy', 'gullible', 'cuddly', 'roasted', 'far', 'square', 'modern', 'eminent', 'second', 'lacking', 'deadpan', 'exotic', 'cheerful', 'moaning', 'closed', 'weary', 'spiffy', 'damaging', 'trite', 'axiomatic', 'spiky', 'same', 'reminiscent', 'separate', 'somber', 'materialistic', 'itchy', 'necessary', 'busy', 'alert', 'careless', 'abstracted', 'earthy', 'cooing', 'military', 'recondite', 'null', 'jazzy', 'breezy', 'mindless', 'guiltless', 'obese', 'obscure', 'fantastic', 'dear', 'wonderful', 'damaged', 'vigorous', 'grieving', 'foregoing', 'present', 'dusty', 'valuable', 'obese', 'healthy', 'lively', 'additional', 'selfish', 'maniacal', 'dizzy', 'stormy', 'mammoth', 'loud', 'gray', 'sad', 'parallel', 'every', 'rustic', 'groovy', 'irritating', 'wary', 'old', 'acceptable', 'internal', 'abandoned', 'guilty', 'spiritual']

chances = [0.05, 0.1, 0.2, 0.7]
colors = ['\033[97m', '\033[94m', '\033[95m', '\033[33m']
drops = []
items = [[]] * 4
for i in range(4):
	for j in range(20):
		items[i].append(choice(verbs) + ' ' + choice(nouns))



runs = 20
for i in range(runs):
	roll = random()
	
	drop = None
	if roll <= 0.05:
		drop = 3
	elif roll <= 0.1:
		drop = 2
	elif roll <= 0.2:
		drop = 1
	elif roll <= 0.7:
		drop = 0
	else:
		continue

	drops.append([drop, randint(0, len(items[drop]) - 1)])

print('Выпавшие предметы:')
for drop in drops:
	type, id = drop[0], drop[1]
	print(colors[type] + items[type][id] + '\033[0m')

if len(drops[3]) > 1:
	print('Большая удача!')
elif len(drops[2]) > 3:
	print('Удача!')