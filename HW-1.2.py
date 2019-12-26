#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


number_1 = input('Введите число: ')

number_2 = int(number_1 + number_1)
number_3 = int(number_1 + number_1 + number_1)
number_4 = int(number_1) + number_2 + number_3

print(number_4)