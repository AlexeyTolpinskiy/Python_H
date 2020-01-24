#6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.

my_dict = {}
types = []
with open("text_6.txt") as text:
    for line in text:
        line_split = line.split()
        line_name = line_split[0]
        all_hours = line_split[1:]
        my_dict[line_name] = 0
        for i in all_hours:
            try:
                my_dict[line_name] += int(types[:types.find('(')])
            except ValueError:
                pass
print(my_dict)