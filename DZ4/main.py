


# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

# import random


# a = abs(int(input("Введите количество элементов в массиве a: ")))
# b = abs(int(input("Введите количество элементов в массиве b: ")))
# d = abs(int(input('Введите максимальное число в массиве: ')))

# arrowa = [1]*a
# arrowb = [1]*b

# for i in range(a):
#     arrowa[i]=random.randint(0,d)
# print(f'Первый НЕупорядоченный массив: {arrowa}')
# print()
# for i in range(b):
#     arrowb[i]=random.randint(0,d)
# print(f'Второй НЕупорядоченный массив: {arrowb}')
# print()
# arrowa.sort()
# arrowb.sort()
# print(f'Первый упорядоченный массив: {arrowa}')
# print()
# print(f'Второй упорядоченный массив: {arrowb}')
# print()
# arrowa= set(arrowa)
# arrowb= set(arrowb)

# print(f'Первое упорядоченное множество: {arrowa}')
# print()
# print(f'Второе упорядоченное множество: {arrowb}')
# print()

# interarrowab = arrowa.intersection(arrowb)

# print(f'В обоих массивах в порядке возрастания встречаются числа: {interarrowab}')






# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
# число ягод — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, 
# которое может собрать за один заход собирающий модуль, 
# находясь перед некоторым кустом заданной во входном файле грядки.

# 4 -> 1 2 3 4
# 9

# import random

# kollcyst = abs(int(input("Введите количество кустов на грядке не мене 3 кустов: ")))
# print()
# if kollcyst < 3:
#     print('Вы ввели меньшее количество кустов!')
# else:
#     kyst = [1]*kollcyst
#     ygodi = random.randint(1,100)
#     for i in range(kollcyst):
#         kyst[i]=random.randint(0,ygodi)
#     print(kyst)

#     max = kyst[0] + kyst[len(kyst) - 1] + kyst[1]
#     print(f'Это max = {max}')

#     if kollcyst == 3:
#         print(f'Вы ввели 3 куста. Комуто достанется {max} ягод')

#     last = kyst[len(kyst) - 1] + kyst[0] + kyst[len(kyst) - 2]
#     print(f'Это last = {last}')
#     print()

#     sum = 0
#     count = 0
#     i = 1
#     for i in range(1,kollcyst-1):
#         sumy = (kyst[i]+kyst[i+1]+kyst[i-1])
#         print(f'Это sum = {sumy}')
#         if sumy > sum:
#             sum = sumy
#             county = i
#             count = county
#         print()
#     print(f'Это конечный sum = {sum}')
    
#     print(f'Это конечный count = {count}')

#     if sum > max and sum > last:
#         print()
#         print(f'Максимальное количество ягод на - {count}, {count + 1}, {count + 2} кустах, а количество ягод составляет {sum} ягод.')    
        
#     if last > max and last > sum:
#         count = kollcyst
#         print()
#         print(f'2 Максимальное количество ягод на - {count - 1}, {count}, {count - (len(kyst) - 1)} кустах, а количество ягод составляет {last} ягод')

#     if max > sum and max > last:
#         count = count - (len(kyst) - 1)
#         print()
#         print(f'3 Максимальное количество ягод на - {count - (len(kyst) - 2)}, {count}, {count - (len(kyst) - 1)} кустах, а количество ягод составляет {max} ягод')

#     if max == sum == last:
#         print(f'На первом и соседних, на последнем и соседних, а также на {county} кусте и соседних от него одинаковое количество ягод а именно - {max}')


        








