# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.


a = int(input('Введите первое слагаемое: '))
b = int(input('Введите второе слагаемое: '))


def Sum1(a, b):
    if b == 0:
        return a
    return 1 + Sum1(a, b - 1)  # Решив задачу 26, эта решилась на раз-два.


print(f'{a}+{b}={Sum1(a, b)}')
