# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.

from random import randint

n_quantity = int(input('Введите число элементов первого набора: '))
m_quantity = int(input('Введите число элементов второго набора: '))
list_n = [randint(0, 30) for _ in range(n_quantity)]
list_m = [randint(0, 30) for _ in range(m_quantity)]
print(list_n)
print(list_m)
list_n.sort()
list_m.sort()

print(set(list_m) | set(list_n))
