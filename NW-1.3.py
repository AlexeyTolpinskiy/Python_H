#4. Пользователь вводит целое положительное чиcло. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


numbers = input('Введите число: ')

a = 0

for number in numbers:
    while int(number) > a:
        a = int(number)
print(a)
