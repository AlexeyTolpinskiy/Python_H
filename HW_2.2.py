#2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().
my_list = list(input("Введите что-нибудь: "))

if len(my_list) % 2 == 0:
    i = 0
    while i < len(my_list):
        t = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = t
        i += 2
    print(my_list)
else:
    i = 0
    while i < len(my_list) - 1:
        t = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = t
        i += 2
    print(my_list)
