#3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    empty = []
    max_1 = max(my_list)
    empty.append(max_1)
    my_list.remove(max_1)
    max_2 = max(my_list)
    empty.append(max_2)
    print(sum(empty))

my_func(-19, 0, 37)