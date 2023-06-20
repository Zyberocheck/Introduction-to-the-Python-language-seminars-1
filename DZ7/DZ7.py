# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.  
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, 
# если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да  
  
# **Вывод:** Парам пам-пам

# 'аоуыэеёиюя'


ritm = 'пара-ра-рам рам-пам-папам па-ра-па-да'


def search_vowel(a):
    str= a.lower().split()
    print(str)
    slog = []
    for word in str:
        sum = 0
        for i in word:
            if i in 'аоуыэеёиюя':
                sum+=1
        slog.append(sum)
        print(slog)
    return slog

number_of_syllables = search_vowel(ritm)

def search_true_false(funfunction,word_songs):
    for item in word_songs:
        if not funfunction(item):
            return False
    return True

if search_true_false(lambda x: x % 2 == 0 , number_of_syllables):
     print('Парам пам-пам')
else:
    print('Пам парам')







# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, 
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы 
# (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, 
# у которой ровно два аргумента, как, например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**

# 1 2 3 4 5 6
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36




# num_r = int(input('Введите количество строк: '))
# num_c = int(input('Введите количество столбцов: '))

# def print_operation_table(operation,num_rows,num_columns):
#     for i in range(1,num_rows+1):
#         print()
#         for j in range(1,num_columns+1):
#             if i !=0 and j != 0:
#                 print(operation(i,j),end='  ')


# print_operation_table(lambda x,y: x*y,num_r,num_c)









