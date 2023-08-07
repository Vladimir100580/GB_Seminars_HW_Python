# 1. Необходимо написать алгоритм поиска всех доступных комбинаций
# (посчитать количество) для количества кубиков K с количеством граней N.
# 2. У вас есть 2 варианта на выбор – количество кубиков может быть строго
# ограничено (4 кубика, например), либо их количество будет
# динамическим. Выбор за вами.
# 3. Если вы реализуете простой вариант, обращает внимание, что данное
# решение имеет сложность O(n4
# ), но если количество кубиков сделать
# переменной, то она трансформируется в O(nk
# ), что будет представлять
# собой экспоненциальную сложность. Для второго решения очевидно, что
# его сложность O(nk
# ) с самого начала.


import random
# n = 6
# k = 3
# dir = set()
# for k1 in range(1, n + 1):
#     for k2 in range(1, n + 1):
#         dir.add((k1, k2))
#
# print(len(dir))
import time

0, 1, 1, 2, 3, 5 ,8, 13, 21

n = 20

def Iter_Fib(n):
    f1 = 0
    f2 = 1
    for i in range(n - 2):
        f3 = f1 + f2
        f1 = f2
        f2 = f3
    if n > 2: return f2
    if n == 1: return 1
    if n == 0: return 0


def Fib_rec(numb1):
    if numb1 == 1: return 0
    if numb1 == 2: return 1
    return Fib_rec(numb1 - 1) + Fib_rec(numb1 - 2)


for i in range(10, 50, 10):
    start = time.time()
    print(f"{i=}")
    Fib_rec(i)
    print(time.time() - start)
    start = time.time()
    Iter_Fib(i)

    print(time.time() - start)


