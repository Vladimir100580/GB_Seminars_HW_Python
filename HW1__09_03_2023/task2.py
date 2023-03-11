# Найдите сумму цифр трехзначного числа.

number = int(input('введите трехзначное число: '))
if 99 < number < 1000:
    print(f'Сумма цифр числа {number} равна {number//100 + (number//10)%10 + number%10}')
else:
    print('ТРЕХЗНАЧНОЕ чиcло!')
