# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

quantity = int(input('Введите общее число монеток (большее 1): '))
reshk = -1
while not(0 < reshk < quantity):
    reshk = int(input(f'Введите количество тех монеток, что лежат решкой вверх 1 - {quantity-1}: '))
if 2 * reshk < quantity:
    print(reshk)
else:
    print(quantity-reshk)


