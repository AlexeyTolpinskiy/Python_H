#Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.




my_list = []
while True:
    x = input("Введите что-нибудь: ")
    if x == "":
        print(my_list)
        
    else:
        my_list.append(x)

    with open("text_1.txt", "w") as t:
        t.writelines(my_list)





