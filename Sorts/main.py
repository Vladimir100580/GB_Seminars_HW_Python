import time
from random import randint
from Sorts.Puzyrek import Puzyr
from Sorts.Pyramid_Sort import SortPyr
from Sorts.Quick_Sort import SortQ
from Sorts.Сount_Sort import counting_sort

mas =[randint(-100, 100) for i in range(20)]
print(f'Исходный массив : {mas}')
print(f'После сортировки: {counting_sort(mas)}')

# print(f'{mas=}')
# Сортировка пузырьком
# n = 100 # количество прогонов
# sum_time = 0
# for p in range(n):
#     mas = [randint(0, 10 ** 7) for i in range(10 ** 4)]
#     start1 = time.time()
#     Puzyr(mas)
#     end1 = time.time()
#     sum_time += end1 - start1
#     print(f'Замер №{p+1}: {end1 - start1}')
# print(f'Пузырек: {sum_time/n}')


# Быстрая сортировка
# n = 20 # количество прогонов
# sum_time = 0
# for p in range(n):
#     mas = [randint(0, 10 ** 7) for i in range(10 ** 6)]    # при изменении 10**4 на 10**5, время увеличивается в 10, и в 5/4 раза, свойства логарифма.
#     start2 = time.time()
#     SortQ(mas, 0, len(mas) - 1)
#     end2 = time.time()
#     sum_time += end2 - start2
#     print(f'Замер №{p+1}: {end2 - start2}')
# print(f'Быстрая сортировка: {sum_time/n}')


# Встроенная сортировка
# n = 100 # количество прогонов
# sum_time = 0
# for p in range(n):
#     mas = [randint(0, 10 ** 7) for i in range(10 ** 5)]
#     start3 = time.time()
#     sorted(mas)
#     end3 = time.time()
#     sum_time += end3 - start3
#     print(f'Замер №{p+1}: {end3 - start3}')
# print(f'Встроенная сортировка: {sum_time/n}')


# Пирамидальная сортировка
# n = 20 # количество прогонов
# sum_time = 0
# for p in range(n):
#     mas = [randint(0, 10 ** 7) for i in range(10 ** 6)]
#     start4 = time.time()
#     SortPyr(mas)
#     end4 = time.time()
#     sum_time += end4 - start4
#     print(f'Замер №{p+1}: {end4 - start4}')
# print(f'Быстрая сортировка: {sum_time/n}')


# Алгоритм: Сортировка подсчетом (Заимствовано у Ильи)
n = 20 # количество прогонов
sum_time = 0
for p in range(n):
    mas = [randint(0, 10 ** 7) for i in range(10 ** 6)]
    start5 = time.time()
    counting_sort(mas)
    end5 = time.time()
    sum_time += end5 - start5
    print(f'Замер №{p+1}: {end5 - start5}')
print(f'Cортировка подсчетом: {sum_time/n}')


