# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# спользовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.



my_list = ["1", "2", "3", "4", "5", "6"]
my_int = 9
my_float = 3.14
my_dict = {"summer": "June", "spring": "March"}
my_tuple = ("a", "b", "c")
my_set = {"Alex", "Sam,", "John", "Michael"}

main = [my_list, my_int, my_float, my_dict, my_tuple, my_set]
for i in main:
    print(type(i))