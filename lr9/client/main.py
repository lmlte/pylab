"""Лабораторная работа №9"""
# Клиент

import requests

def get_students():
	return requests.get('http://127.0.0.1:80/students').json()

def get_student(id):
	return requests.get('http://127.0.0.1:80/students/' + str(id)).json()

def add_student(student_data):
	return requests.post('http://127.0.0.1:80/students', json = student_data).json()

def update_student(id, student_data):
	return requests.put('http://127.0.0.1:80/students/' + str(id), json = student_data).json()

def delete_student(id):
	return requests.delete('http://127.0.0.1:80/students/' + str(id)).json()


print(get_students())
print(get_student(2))
print(add_student({'id': 4, 'name': 'Новый Студент', 'age': 22, 'major': 'Биология'}))
print(update_student(4, {"name": "Новый Студент", "age": 23, "major": "Химия"}))
print(delete_student(4))
print(get_student(4))