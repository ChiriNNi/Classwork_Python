balance, price = int(input("Введите сумму денег в кошельке (тг): ")), int(input("Введите сумму одной шоколадки (тг): "))
count = balance // price
print(f"Вы сумеете купить {count} шоколадок и у вас останется {balance - (count * price)} тенге")