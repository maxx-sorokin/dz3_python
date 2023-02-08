# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

decimal_number = int(input('Введите десятичное число: '))

number = decimal_number
binary_number = ''
while number > 0:
    binary_number = str(number % 2) + binary_number
    number //= 2

print(decimal_number, '->', binary_number)
