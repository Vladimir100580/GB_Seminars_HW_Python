# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
my_vars = list(map(int, input("Ведите длину списка, диапазон значений и диапазон выборки (пять чисел через пробел)  ").split()))

my_list1 = [randint(my_vars[1], my_vars[2]) for _ in range(my_vars[0])]
print(my_list1)
my_list2 = [i for i in range(0, len(my_list1)) if my_vars[3] <= my_list1[i] <= my_vars[4]]
print(my_list2)


