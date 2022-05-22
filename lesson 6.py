# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_text = 'Напишите прогабврамму удабваляющую из текста все слова содержащие'
# def my_str(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)
# my_text = my_str(my_text)
# print(my_text)

#*************************************************************************

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# ЭТУ ЗАДАЧУ НЕ СМОГ ПОБЕДИТЬ ((((

# import math
# print('Введите число: ')
# num = int(input())
# print(f'простые множители для заданного числа: ')

# list_mult = []
 
# def is_prime(i):
#     m = min(i, int(math.sqrt(num)))
#     r = map(lambda x: num % x == 0, range(2, int(num)))
#     return r
 
# list_mult = list(filter(is_prime, range(2,int(num))))
# print(list_mult)
        # if num % 2 == 0  or num % 3 == 0:
        #     i = 2
        #     #list_mult = list(map(filter(lambda i: num % i ==0  or num % (i+1) == 0, range(2, int(num)))))
        #     list_mult = filter(lambda i: num % i == 0  or num % (i+1) == 0,range(2,int(num)))
        #     #num = num -1
        #     print(list(list_mult))
        # # else:
        # #     list_mult = list(filter(lambda j: num % j == 1,range(2, int(num))))
        # # for i in range(2, int(num)):
        # else:
        #     print(f"{'число ' + str(num) + ' простое'}")#list_mult = list(filter(lambda j: num % j == 1,range(2, int(num))))



#*******************************************************************************
# 3. Реализовать программу, получающую на вход строку, состоящую из слов, 
#    разделенных пробелами и возвращающую длину каждого слова.
#    Пример: "Солнце небо воздух земля" --> 6 4 6 5

my_str = 'солнце небо воздух земля облака'
my_str = my_str.split()
letter_counts = list(map(lambda x: len(x), my_str))
print(letter_counts)
