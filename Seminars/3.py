# 1. Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
#
# Каждое число – среднесуточная температура в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50


from random import randint

days = int(input("Введите количество дней: "))
lengh = 0
tToday = 0
maxOt = 0

for i in range(days):
    tToday = randint(-10, 10)
    if tToday > 0:
        lengh += 1
        if maxOt < lengh:
            maxOt = lengh
    else:
        # print("(" + str(lengh) + ")", end="  ")  # Здесь указывается длина оттепели (если не оттепель - выдает (0))
        lengh = 0
    print(tToday, end="  ")

print(sep="")
print(maxOt)


# s = 1
# while number > 1:
#     s *= number
#     number -= 1
# print("N!=", s)


