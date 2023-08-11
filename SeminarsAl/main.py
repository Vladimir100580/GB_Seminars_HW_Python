import time
from dices import *

print(f"Всего {dice} кубиков с {n} сторонами.")
ss = 0
nn = 0
for t in range(10):
    start = time.time()
    throw(dice, s)
    ss += time.time() - start
    nn += 1
    print(ss/nn)
# print(f"Количество комбинаций {sorted(combos)}.")  # Распечатать комбинации
print(f"Количество уникальных комбинаций {len(combos)}.")
print(f"Время выполнения {time.time() - start} сек.")