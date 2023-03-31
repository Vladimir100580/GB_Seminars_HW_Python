# Семинар 7

from random import randint

list0 = [randint(0,99) for _ in range(10)]
print(list0)

for i, item in enumerate(list0, 5):
    print(i**3, item)