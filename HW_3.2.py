#2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, birthday, city, email, number):
    print(name, surname, birthday, city, email, number)

my_func(name = 'Robert', surname = 'Trogmorton', birthday = '13.10.1956', city = 'Okland', email = 'robt@mail.ru', number = '=79878654321')