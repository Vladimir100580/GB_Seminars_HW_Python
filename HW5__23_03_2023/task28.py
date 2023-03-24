# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

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
