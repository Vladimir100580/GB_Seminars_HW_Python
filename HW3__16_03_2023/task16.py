# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

quant = int(input('Введите количество элементов в массиве: '))
arr = [randint(1, 10) for _ in range(quant)]
print(arr)
number = int(input('Введите чиcло X: '))
dict = {}         # можно было и банальной пробежкой. Но открылась жажда поэкспериментировать со словарем.
for i in arr:
    dict[i] = dict.get(i, 0) + 1
# print(dict)
k = dict.get(number, 0)
tx = 'раз'       # возвращение "орфографической красоты"
if (k % 10 == 2 or k % 10 == 3 or k % 10 == 4) and (k // 10) % 10 != 1: tx = 'раза'
print(f'Число {number} встречается {k} {tx}. ')


