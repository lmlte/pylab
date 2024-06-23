"""Лабораторная работа №8.6"""
from requests import get

cities = [
	'Омск',
	'Калининград',
	'Челябинск',
	'Владивосток',
	'Красноярск',
	'Москва',
	'Екатеринбург'
]

def make_url(city):
	return 'https://wttr.in/' + city

def make_parameters():
	return {
    	'0': '',					# №1 - 3
		'T': '',					# №1 - 3
		'M': '',					# №2 - 4
		'lang': 'ru',				# №2
		'Accept-Language': 'ru-RU',	# №3
		'format': 2					# №4
	}

def what_weather(city):
	try:
		response = get(make_url(city), params=make_parameters())
		if response.status_code == 200:
			return response.text
		else:
			return '<ошибка на сервере погоды>'
	except requests.ConnectionError:
		return '<сетевая ошибка>'

print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))