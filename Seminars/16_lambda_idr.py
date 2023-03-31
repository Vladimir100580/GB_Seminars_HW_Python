# Лекция 4 (Экспериментируем с лямбда-функцией и т.д.)

from random import randint

def calc1(x):
    return x + 10

print(calc1(5))

def calc2(x):
    return x * 10

def math(op, x):
    print(op(x))

math(calc2, 7)

def sum(x, y):
    return x + y
# sum = lambda x, y: x + y

# def mylt(x, y):
#     return x * y
mylt = lambda x, y: x * y

def calc(op, a, b):
    print(op(a, b))

print(mylt(6, 7))

calc(lambda x, y: x + y, 4, 5)

# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа)
quantity = 20 # int(input('Введите количество элементов: '))
my_list1 = [randint(1, 100) for _ in range(quantity)]
print(my_list1)
my_list2 = [[i, i**2] for i in my_list1 if i%2 == 0]
print(my_list2)

def select(f, col):                          #!!!!!!!!!!! это и есть функция map
    return [f(x) for x in col]

def where(f, col):                    # это и есть функция filter
    return [x for x in col if f(x)]   # лямбда функция lambda x: x % 2 == 0 выступает как f

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
res = where(lambda x: x % 2 == 0, res)     # посылаем условие лямбда в саму функцию f
print(res) # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))

print(res)

# Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает итератор с новыми объектами.
# list_1 = [x for x in range (1,20)]
# list_1 = list(map(lambda x: x + 10, list_1 ))

# Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и
# возвращает итератор с теми объектами, для которых функция вернула True.
# data = [x for x in range(10)]
# res = list(filter(lambda x: x % 2 == 0, data)))
# print(res) # [0, 2, 4, 6, 8]

# Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами
# из элементов входных данных (т.е. создает кортежи)   МОЖЕТ СОЕДИНИТЬ В ПАРЫ 2 (и более списков)
# (пробегает по минимальному входящему набору)
print(list(zip([12, 23, 'Q'], ['R', 45, 5, 9], ['W', 4, 11])))

# Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор с
# кортежами из индекса и элементов входных данных.


