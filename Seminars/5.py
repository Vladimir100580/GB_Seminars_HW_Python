#Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. #
# Количество повторов добавляется к символам с помощью постфикса формата _n.

import random
import  string

string0 = ''.join([random.choice(string.ascii_letters) for _ in range(30)])
print(string0)
dict = {}
for i in string0:
    o = dict.get(i, 0)
    if o == 0:
        dict[i] = 1
        print(i, end=' ')
    else:
        dict[i] += 1
        print(f'{i}_{dict[i]}', end=' ')
print()
print(dict)


