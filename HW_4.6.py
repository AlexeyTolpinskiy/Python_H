#6. Реализовать два небольших скрипта:
#а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
#б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
#Подсказка: использовать функцию count() и cycle() модуля itertools.




from itertools import count
from itertools import cycle


for el in count(1):
    if el > 20:
        break
    else:
        print(el)


my_list = [10, 9, 8, 7]

n = cycle(my_list)

print(next(cycle(n)))
print(next(cycle(n)))
print(next(cycle(n)))
print(next(cycle(n)))

