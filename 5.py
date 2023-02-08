# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))

fib_list = [0]
if k > 0:
    fib_list.append(1)
    fib_list.insert(0, 1)
    for i in range(1, k):
        fib_list.append(fib_list[-1] + fib_list[-2])
        fib_list.insert(0, fib_list[1] - fib_list[0])

print('для k =', k, 'список чисел Фибонначчи будет выглядеть так:', fib_list)
