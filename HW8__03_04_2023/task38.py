# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
# 1. Открыть файл
# 2. Сохранить файл
# 3. Просмотреть контакты
# 4. Создать контакт
# 5. Найти контакт
# 6. Изменить контакт
# 7. Удалить контакт
# 8. Выход

def clear_term():
    print("\n" * 10)


def view_contacts():
    with open('tel_directory.txt', 'r', encoding='utf8') as f:
        f0 = list(f)
        list0 = list(enumerate(map(lambda x: x[:len(x) - 1], f0)))
        u = list(zip(*map(lambda x: x.split(' '), map(lambda x: x[:len(x) - 1], f0))))  # создаем вложенные в список кортежи содержащие отдельно: имена, фамилии, телефоны и коментарии ...
        max_len = ([max([len(i) for i in arr]) for arr in u])   # создаем список с максимальной длиной имени, фамилии, тел. и комментария ... Все это для красоты ширины столбцов
        max_len.append(sum(max_len))
        print(max_len)
        for sub in list0:
            list1 = sub[1].split(' ')
            print(f'{int(sub[0]) + 1}.'
                  f' {list1[0]:<{max_len[0] + 2}}'
                  f' {list1[1]:<{max_len[1] + 2}}'
                  f' {list1[2]:<{max_len[2] + 2}}'
                  f' {list1[3]:<{max_len[3] + 2}}')   # каждый столбец будет на 2 символа шире максимальной длины слова в этом столбце
    input("Нажмите ввод для продолжения...")


def create_contact():
    print('Введите Фамилию, Имя, номер телефона, комментарий(при необходимости).')
    data = input("Через пробелы: ").split()     # Конечно, можно было работать просто с одной строкой, но, если решать задачу с заделом на таблицы БД, решил поиграться с разбиением строк
    if len(data) == 3:
        data.append('-')
    if len(data) > 4:                      # Если комментарий содержит несколько слов, - слепляются в одно, с разделителем '_'
        data[3] = '_'.join(data[3:])
        data = data[:4]
    data = ' '.join(data) + '\n'
    with open('tel_directory.txt', 'a', encoding='utf8') as f:
        f.write(data)
    sort_guide_and_save()


def find_contact():
    substr = input('Введите подстроку для поиска: ')
    with open('tel_directory.txt', 'r', encoding='utf8') as f:
        for sub in list(enumerate(map(lambda x: x[:len(x) - 1], f))):
            if substr.upper() in str(sub).upper():    # создаем запрос не чувствительный к регистру букв
                print(f'{int(sub[0]) + 1}. {sub[1]}')
    input("Нажмите ввод для продолжения...")


def change_contact():
    with open('tel_directory.txt', 'r', encoding='utf8') as f:
        arr = list(enumerate(map(lambda x: x[:len(x)-1], f)))
        for sub in arr:
            print(f'{int(sub[0]) + 1}. {sub[1]}')
    nom = int(input("Введите номер контакта для корректировки: "))
    print(f'{nom}. {arr[nom-1][1]}')
    print('Введите заново Фамилию, Имя, номер телефона, комментарий(при необходимости).')
    correctStr = input("Коррекция: ").split()
    if len(correctStr) == 3:
        correctStr.append('-')
    if len(correctStr) > 4:
        correctStr[3] = '_'.join(correctStr[3:])
        correctStr = correctStr[:4]
    correctStr = ' '.join(correctStr) + '\n'
    with open('tel_directory.txt', 'w', encoding='utf8') as f1:
        for l in arr:
            if nom != int(l[0]) + 1:
                f1.write(l[1] + '\n')
            else:
                f1.write(correctStr)
    sort_guide_and_save()


def delete_contact():
    with open('tel_directory.txt', 'r', encoding='utf8') as f:
        arr = list(enumerate(map(lambda x: x[:len(x) - 1], f)))
        for sub in arr:
            print(f'{int(sub[0]) + 1}. {sub[1]}')
    nom = int(input("Введите номер контакта который необходимо удалить: "))
    with open('tel_directory.txt', 'w', encoding='utf8') as f1:
        for l in arr:
            if nom != int(l[0]) + 1:
                f1.write(l[1] + '\n')


def sort_guide_and_save():          # сортировка справочника по фамилии
    with open('tel_directory.txt', 'r', encoding='utf8') as f:
        fl = list(f)
        if '\n' not in fl[-1]:       # избегаем "слепку" последней строчки с какой-либо другой при сортировке.
            fl[-1] += '\n'
        fl.sort()
    with open('tel_directory.txt', 'w', encoding='utf8') as f1:
        for l in fl:
            f1.write(l)


while True:
    clear_term()
    print('''Выберите необходимое действие: 
    1. Просмотреть контакты
    2. Создать контакт
    3. Найти контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Выход''')
    n = int(input('Введите цифру: '))
    clear_term()

    if n == 1:
        view_contacts()
    if n == 2:
        create_contact()
    if n == 3:
        find_contact()
    if n == 4:
        change_contact()
    if n == 5:
        delete_contact()
    if n == 6:
        break


