# Задача 16: Требуется вычислить, сколько раз встречается
#  некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве. В последующих  
# строках записаны N целых чисел Ai. Последняя строка 
# содержит число X
# *Пример:*

# 5
# 1 2 3 4 5
# 3
# -> 1

import random

a = int(input("Введите количество элементов в массиве: "))
b = int(input("Введите искомое: "))

arrow = [1]*a
count = 0
for i in range(a):
    arrow[i]=random.randint(0,(b+1)*2)
    if arrow[i] == b:
        count+=1
print(arrow)
print('Число встречается : ',count,' раз')



 
# Задача 18: Требуется найти в массиве A[1..N] самый близкий 
# по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X
# *Пример:*

# 5
# 1 2 3 4 5
# 6
# -> 5

# import random


# a = int(input("Введите количество элементов в массиве: "))





