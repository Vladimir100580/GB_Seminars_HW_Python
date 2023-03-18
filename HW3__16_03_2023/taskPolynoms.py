from random import randint

def PolyToStr(arr):            # Переводим список коэффициентов в строку (считаем, что коэффициенты в списке записаны от бОльшей степени к меньшей)
    st = ''
    deg = len(arr) - 1
    for i in arr:
        if i != 0:
            if i != 1 and i != -1: koef = str(i)
            else:
                if i == 1: koef = ''
                if i == -1: koef = '-'
            if i > 0 and st != '': st += '+'
            if deg == 1:
                st += koef + 'x'
            elif deg == 0:
                st += str(i)
            else: st += koef + 'x' + GetUp(str(deg))
        deg -= 1
    if st == '': st = '0=0'
    else: st += '=0'
    return st

def GetUp(stNom):           #  строку из цифр, преобразуем в строку верхних индексов этих же цифр
    normal = "0123456789"
    up = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = stNom.maketrans(''.join(normal), ''.join(up))
    return stNom.translate(res)

def GetDown(stNom):           #  а теперь, в обратную сторону (для второй части задачи)
    down = "0123456789"
    up = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    res = stNom.maketrans(''.join(up), ''.join(down))
    return stNom.translate(res)

def Splitting1(stNoms):        # дополнительная функция, выуживающая из переданной строки 2 числа, разделенные арифметическим знаком.
    fl1 = 0
    if '=' in stNoms:
        stNoms = stNoms[:stNoms.find('=')]
        fl1 = 1                                 # пришлось ввести флаг, указывающий на место нахождения, в начале, или конце
    fl = 0
    arr2 = stNoms.split('-')
    if len(arr2) == 1:
        fl = 1    # второе число положительное
        arr2 = stNoms.split('+')
        if len(arr2) == 1:
            if fl1 == 0:
                arr2 = ['0', arr2[0]]   # здесь рассматривается первый коэффициент
            if fl1 == 1:
                arr2 = [arr2[0], '0']   # здесь рассматривается случай, когда свободный член равен 0
    if arr2[1] == '': arr2[1] = '1'
    if arr2[0] == '': arr2[0] = '1'
    if fl == 0:
        arr2[1] = '-' + arr2[1]
    return(arr2)

deg1 = int(input('Введите степень первого многочлена: '))
deg2 = int(input('Введите степень второго многочлена: '))
while True:     # учитываем, что коэффициент при указанной старшей степени не должен быть нулем
    coefArr1 = [randint(-5, 5) for _ in range(deg1 + 1)]   # создаем списки коэффициентов многочленов
    coefArr2 = [randint(-5, 5) for _ in range(deg2 + 1)]   # членов должно быть на 1 больше, чем степень (в общем виде)
    if (coefArr1[0]*coefArr2[0] != 0): break
strPoly1 = PolyToStr(coefArr1)
strPoly2 = PolyToStr(coefArr2)
print(f'Первый многочлен: {PolyToStr(coefArr1)}')
print(f'Второй многочлен: {PolyToStr(coefArr2)}')

# ЧАСТЬ 2.
# Далее складываем многочлены, используя только строки strPoly1 и strPoly2 (считаем, что мы не знаем списков коэффициентов, их надо получить)
# Найдем максимальную степень

podStr1 = GetDown(strPoly1).split('x')
podStr2 = GetDown(strPoly2).split('x')

degMax = max(int(Splitting1(podStr1[1])[0]), int(Splitting1(podStr2[1])[0]))    # наибольшая степень
coefArrEnd1 = ['0' for _ in range(degMax + 1)]   # cоздаем пустые списки (для коэффициентов многочлена)
coefArrEnd2 = ['0' for _ in range(degMax + 1)]

for i in range(0, len(podStr1)-1):
    k1 = Splitting1(podStr1[i])            # каждая возвращенная пара возвращает степень текущего члена и коэффициент перед следующим (по убыванию)
    k2 = Splitting1(podStr1[i+1])
    coefArrEnd1[degMax - int(k2[0])] = k1[1]      #  заполняем список коэффициентами
coefArrEnd1[degMax] = Splitting1(podStr1[len(podStr1) - 1])[1]     # свободный член (тот, что при нулевой степени)

for i in range(0, len(podStr2)-1):          # не особо выдержан принцип DRY
    k1 = Splitting1(podStr2[i])
    k2 = Splitting1(podStr2[i+1])
    coefArrEnd2[degMax - int(k2[0])] = k1[1]
coefArrEnd2[degMax] = Splitting1(podStr2[len(podStr2) - 1])[1]

rezultArr = []
for i in range(len(coefArrEnd1)):       # наконец-то складываем
    rezultArr.append(int(coefArrEnd1[i]) + int(coefArrEnd2[i]))    # можно и вычитать (а, вот, с умножением - было бы еще интересней)

print(f'Результат сложения: {PolyToStr(rezultArr)}')