# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Здесь различные примеры из лекций!!!!!!!!!!!!!!!!!

from random import randint
import time
from pufu import sum1

print(sum1(5, 7))





t0 = time.time()
for n in range(10000):
    arr = [randint(0, 10000) for i in range(1000)]
    arr.sort()
print(time.time() - t0)


# Сравнение скорости быстрой сортировки и сортировки слиянием
def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)

t1= time.time()
for n in range(10000):
    arr = [randint(0, 10000) for i in range(1000)]
    o = (quicksort(arr))
print(time.time() - t1)

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

t2= time.time()
for n in range(10000):
    arr = [randint(0, 10000) for i in range(1000)]
    merge_sort(arr)
print(time.time() - t2)




# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
# list_1 = []
# for i in range(3, 10):
#     list_1.append(fib(i - 2))
# print(list_1)



f = lambda x: x+2
print(f(4))

lis = [2, 3, 5, 10, 7]

print(5 % 5)
print(lis[(5 % 5)])

# data = [1,2,3,4]
# f_data = [y for x in data if (y := f(x)) is not 4]
# print(f_data)


# Пример нахождения суммы квадратов
# list = [2, 4, 6, 7]
# s = 0
# [s := s + m ** 2 for m in list]
# print(s)
# print()

# Числа Фибоначчи
# s = [0, 1]
# [s := s + [s[i-1] + s[i-2]] for i in range(2, 20)]
# print(s)


# e = 'YРВАФ'
# print("A" in e)
#
# print(min('27', '3'))
#
# print(tuple("Привет"))
#
# asj1 = {{1, 2}: "Петр"}
#
# print(asj1[1])
#
# print('5667'.split("X"))

# number = int(input("Введите число"))
# s = 1
# while number > 1:
#     s *= number
#     number -= 1
# print("N!=", s)


