# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках
# не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. Винни-Пух считает,
# что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# string = input("Ведите стихотворение (на русской раскладке) ")
string = 'пам-парам пум-пум-пам та-ры-ра то-тита'
string = string.upper().replace('  ', ' ').split(' ')   # вдруг случайно будет сделан двойной пробел ...
st_g ='АОУЫЭЕЁИЮЯ'

arr_gl =[]
for s in string:
    arr_gl.append(len(list(filter(lambda x: x in st_g, s))))  # пробегаемся по слову, создаем из него список только гласных букв, находим их количество. Добавляем это число к списку

# print(arr_gl)
if len(set(arr_gl)) == 1:         # состоит ли полученный список только из одинаковых элементов-чисел (т.е. одинаковое ли количество гласных в каждой фразе)
    print('Парам пам-пам')
else:
    print('Пам парам')










