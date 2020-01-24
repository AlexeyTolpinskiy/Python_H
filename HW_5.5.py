#5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

from random import randint


summa = 0
with open("text_5.txt", "w") as t:
    for line in range(100):
        el = randint(1, 100)
        summa += line
        t.write(str(el) + " ")
print(f"Сумма элементов = {summa}")