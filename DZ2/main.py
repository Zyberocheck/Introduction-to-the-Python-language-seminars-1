# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть


# n = int(input('Предположим -0- это орел а -1- герб. Введите количество монеток: '))

# o = g = 0

# for i in range(n):
#     pen = int(input('Введите орел или герб: '))
#     if pen == 0:
#         o+=1
#     else:
#         g+=1
# if o > g:
#     print(f'Монет орлом вверх {o} штук, переверните {g} с гербом')
# elif o == g:
#     print(f'Монеть с орлом и гербом вверх одинаковое количество, придется подкинуть монетку') 
# else:
#     print(f'Монет гербом вверх {g} штук, переврните {o} с орлом')




# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


# x = int(input('Введите первое число: '))
# y = int(input('Введите второе число: '))

# if x>0 and x<= 1000 and y>0 and y<= 1000:
#     count = 0
#     for i in range(x):
#         if count !=1:
#             for j in range(y):
#                 if count !=1:
#                     if i + j == x  and i*j == y:
#                         print(i,j)
#                         count = 1
#                     # elif i + j != x  and i*j != y:
#                     #     print('Введены не корректные числа') --- выводит много раз как сделать чтобы не выводил?
# else:
#     print('Число введено не корректно ')




# Задача 14: Требуется вывести все целые степени двойки 
# (т.е. числа вида 2k), не превосходящие числа N.



# n = int(input('Введите число: '))

# count = 0
# b = 0
# a = 0
# k = 1
# while 2**k<=n:
#     a = 2**k
#     k+=1
#     b+=1
#     count+= 1
#     print(f'2 в степени {b} = {a}')
# print(count)

