"""Лабораторная работа №8.5"""
from urllib.parse import quote, unquote

# 1.	У вас есть запрос «как стать бэкенд-разработчиком».
#		Соберите URL страницы, на которой Яндекс покажет результаты поиска по этому запросу.
print('https://yandex.ru/search/?text=' + quote('как стать бэкенд-разработчиком'))


# 2.	Почувствуйте себя веб-сервером Яндекса.
#		Вы получили страшный URL — и чтобы ответить на запрос, вам нужно сперва понять,
# 		о чём же вас спрашивают. Расшифруйте, какой вопрос задал Яндексу пользователь.
url = 'https://yandex.ru/search/?text=%D0%BA%D0%B0%D0%BA%20%D0%B1%D0%B5%D1%81%D0%BF%D0%BB%D0%B0%D1%82%D0%BD%D0%BE%20%D0%B5%D0%B7%D0%B4%D0%B8%D1%82%D1%8C%20%D0%BD%D0%B0%20%D1%82%D0%B0%D0%BA%D1%81%D0%B8'
print(unquote(url[url.find('=') + 1::]))
