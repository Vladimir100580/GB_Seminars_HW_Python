# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.

nbs = input('Введите номер билета (шестизначное число): ')
nb = int(nbs)

if (nb % 10 + (nb//10) % 10 + (nb//100) % 10) == ((nb//1000) % 10 + (nb//10000) % 10 + nb//100000):
    print(f'Билет {nbs} - счастливый!')
else:
    print(f'Билет {nbs} - не является счастливым!')  # выводим именно строковой тип переменной, т.к. если выводить числовой тип nb, возникнет некорректность последнего вывода с номером билета, начинающегося с нуля(-ей) (например: 034520)
