# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырехзначных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль



import random
from random import randint
import string

arr = [randint(1000,9999) for _ in range(10)]
print(arr)
num = input('Введите цифру: ')
arr1 = [int((str(i).replace(num, ''))) for i in arr]
print(arr1)
arr2 = []
for i in arr1:
    while True:
        i = sum([int(k) for k in str(i)])
        if i < 10:
            arr2.append(i)     # [i := i + int(m) for m in ist]
            break
print(arr2)
arr3 = []
for i in arr2:
    if i not in arr3:
        arr3.append(i)
print(arr3)

print("\nморж\n")
list = [2, 4, 6, 7]
s = 0
[s := s + m ** 2 for m in list]
print("Сумма квадратов" + str(s))

s = [0, 1]
[s := s + [s[i-2] + s[i-1]] for i in range(2, 20)]
print(s)
