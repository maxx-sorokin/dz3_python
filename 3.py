# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = [1.1, 1.2, 3.1, 5, 10.01]

mini = 10**10
maxi = 0
for i in range(len(my_list)):
    a = round(my_list[i]%1, 10)
    if (a > maxi) and (a > 0):
        maxi = a
    elif a < mini and (a > 0):
        mini = a
print(my_list, '=>', maxi - mini)