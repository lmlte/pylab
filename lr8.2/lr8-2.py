"""Лабораторная работа №8.2"""

def penult_word(message):
	return message.split(' ')[-3]

print(penult_word('Работает? Не трогай'))
print(penult_word('Если твой код работает, значит это хороший код'))
print(penult_word('Лень - главное достоинство программиста'))


def check_query(query):
	elements = query.split(', ')
	# name = elements[0]
	return elements[1]

queries = [
	'Анфиса, сколько у меня друзей?',
	'Андрей, ну где ты был?',
	'Андрей, ну обними меня скорей!',
	'Анфиса, кто все мои друзья?'
]
for q in queries:
	print(q, '-', check_query(q))


DATABASE = {
	'Серёга': 'Омск',
	'Соня': 'Москва',
	'Миша': 'Москва',
	'Дима': 'Челябинск',
	'Алина': 'Красноярск',
	'Егор': 'Пермь',
	'Коля': 'Красноярск'
}

def process_anfisa(query):
	if query == 'Сколько у меня друзей?':
		return 'У тебя ' + str(len(DATABASE)) + ' друзей.'
	elif query == 'Кто все мои друзья?':
		return 'Твои друзья: ' + ' '.join(DATABASE.keys())
	elif query == 'Где все мои друзья?':
		return 'Твои друзья в городах: ' + ' '.join(set(DATABASE.values()))
	else:
		return '<неизвестный запрос>'

print('Привет, я Анфиса!')
print(process_anfisa('Сколько у меня друзей?'))
print(process_anfisa('Кто все мои друзья?'))
print(process_anfisa('Где все мои друзья?'))