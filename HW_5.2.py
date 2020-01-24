#Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open("text_2.txt", "r") as tx:
    stroki = 0
    bukvi = 0
    for stroka in tx:
        stroki += stroka.count("\n")
        bukvi = len(stroka)
        print(f"Всего символов в строке - {bukvi}")
    print(f"Всего строк - {stroki + 1}")

