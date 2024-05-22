"""Лабораторная работа №8.3"""

def show_meteo(temperature, weather):
	print(f'Сейчас {weather}, на градуснике {str(temperature)}.')

show_meteo(24, 'облачно')


for	messages_count in range(0, 21):
	if messages_count == 0:
		print('У вас нет новых сообщений')
	elif messages_count == 1:
		print('У вас 1 новое сообщение')
	elif messages_count <= 4:
		print(f'У вас {str(messages_count)} новых сообщения')
	else:
		print(f'У вас {str(messages_count)} новых сообщений')


def print_time(hour, minute, second):
	print(f'{hour}:{minute}:{second}')

print_time('19', '28', '06')


def calc_stat(listened):
	return f"Вы прослушали {len(listened)} песен общей продолжительностью {sum(listened)} минут."

print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))


DATABASE = {
	'Серёга': 'Омск',
	'Соня': 'Москва',
	'Миша': 'Москва',
	'Дима': 'Челябинск',
	'Алина': 'Красноярск',
	'Егор': 'Пермь',
	'Коля': 'Красноярск'
}

def format_friends_count(friends_count):
	if friends_count == 1:
		return '1 друг'
	elif 2 <= friends_count <= 4:
		return f'{friends_count} друга'
	else:
		return f'{friends_count} друзей'

def process_friend(name, query):
	if not name in DATABASE.keys():
		return f'У тебя нет друга по имени {name}'
	
	query = query.lower()
	if query == 'ты где?':
		return f'{name} в городе {DATABASE[name]}'
	else:
		return '<неизвестный запрос>'

def process_anfisa(query):
	query = query.lower()
	if query == 'сколько у меня друзей?':
		return f'У тебя {format_friends_count(len(DATABASE))}.'
	elif query == 'кто все мои друзья?':
		return f'Твои друзья: {', '.join(DATABASE)}'
	elif query == 'где все мои друзья?':
		return f'Твои друзья в городах: {', '.join(set(DATABASE.values()))}'
	else:
		return '<неизвестный запрос>'

def process_query(query):
	print(query)
	arr = query.split(', ')
	name = arr[0]
	query = ' '.join(arr[1:])

	if name == 'Анфиса':
		return process_anfisa(query)
	else:
		return process_friend(name, query)


print('Привет, я Анфиса!')
print(process_query('Анфиса, сколько у меня друзей?'))
print(process_query('Анфиса, кто все мои друзья?'))
print(process_query('Анфиса, где все мои друзья?'))
print(process_query('Анфиса, кто виноват?'))
print(process_query('Соня, ты где?'))
print(process_query('Коля, что делать?'))
print(process_query('Антон, ты где?'))