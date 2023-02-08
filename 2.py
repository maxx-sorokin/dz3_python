# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

list_numbers = [2, 3, 4, 5, 6]

prod = []
for i in range(round(len(list_numbers)/2 + 0.1)):
    prod.append(list_numbers[i] * list_numbers[-i - 1])

print(list_numbers, '=>', prod)
