# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while


f = lambda x: x+2
print(f(4))

# data = [1,2,3,4]
# f_data = [y for x in data if (y := f(x)) is not 4]
# print(f_data)


# Пример нахождения суммы квадратов
list = [2, 4, 6, 7]
s = 0
[s := s + m ** 2 for m in list]
print(s)
print()


s = [0, 1]
[s := s + [s[i-1] + s[i-2]] for i in range(2, 20)]
print(s)


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


