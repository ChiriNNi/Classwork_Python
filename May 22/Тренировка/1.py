salary, credit, communal = int(input("Зарплату за месяц (тг): ")), int(input("Сумма месячного платежа по кредиту (тг): ")), int(input("Задолженность за коммунальные услуги (тг): "))
balance = salary - (credit + communal)
print("Баланс (тг):", balance)