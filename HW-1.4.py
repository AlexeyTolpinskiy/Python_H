#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.


proceed = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
profit = proceed - costs

if profit <= costs:
    print("Ваши издержки слишком высоки")
elif profit > costs:
    print("Ваша выручка выше ваших издержки")
    prifitab = profit / costs
    employ = float(input('Введите колличество сотрудников в компании: '))
    profit_emp = (profit) / (employ)
    print(f"Прибыль на одного работника составляет - {profit_emp:.3f}")





