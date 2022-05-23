# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_text = 'Напишите прогабврамму удабваляющую из текста все слова содержащие'
# def my_str(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)
# my_text = my_str(my_text)
# print(my_text)

#*************************************************************************

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# import math
# print('Введите число: ')
# num = int(input())
# print(f'простые множители для заданного числа: ')
# mult_list = []

# def count(i):
#     global num
#     global mult_list
#     a = []
#     while (num % i == 0):
#         num //= i
#         mult_list.append(i)

# list(map(count, [i for i in range(2, int(num**0.5)+1)]))
# if (num != 1):
#     mult_list.append(num)
# print(mult_list)

#*******************************************************************************
# 3. Реализовать программу, получающую на вход строку, состоящую из слов, 
#    разделенных пробелами и возвращающую длину каждого слова.
#    Пример: "Солнце небо воздух земля" --> 6 4 6 5

my_str = 'солнце небо воздух земля облака'
my_str = my_str.split()
letter_counts = list(map(lambda x: len(x), my_str))
print(letter_counts)
