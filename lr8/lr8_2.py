"""Лабораторная работа №8"""

# 2.	Встраивание функций: Напишите функцию reverse_number, которая принимает число в
#		качестве параметра и возвращает перевернутое число. Напишите функцию
#		is_palindrome, которая проверяет, является ли число палиндромом. Напишите функцию
#		process_numbers, которая принимает список чисел в качестве параметра,
#		переворачивает каждое число и выводит новый список с перевернутыми числами. Если
#		какое-то число является палиндромом, ваш код должен об этом сообщить.
def float_check(num):
	num = float(num)
	num2 = int(num)
	return num == num2 and num2 or num

def reverse_number(num):
	return float_check(str(float_check(num))[::-1])

def is_palindrome(num):
	return str(float_check(num)) == str(reverse_number(num))

def process_numbers(list):
	list2 = []

	palindrome = False
	for num in list:
		if is_palindrome(num):
			palindrome = True
		
		list2.append(reverse_number(num))
	
	return list2, palindrome


print(reverse_number(41))
print(reverse_number(42.1))
print(is_palindrome(43))
print(is_palindrome(44))
print(is_palindrome(45.3))
print(process_numbers([53.3, 50.2, 55, 55.4]))