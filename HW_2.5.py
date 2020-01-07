#5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 4, 3, 2]

x = int(input("Введите число"))
my_list.append(x)

N = len(my_list)

for i in range(1, N):
    k = i
    while k > 0 and my_list[k - 1] > my_list[k]:
        my_list[k], my_list[k - 1] = my_list[k - 1], my_list[k]
        k -= 1

print(my_list.reverse(), end='')
print(my_list)



