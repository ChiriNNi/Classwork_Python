# user_input = input("Введите число: ")
# try:
#     user_number = int(user_input)
# except ValueError: 
#     result = "Ошибка! Вы ввели не число!"
# else: 
#     result = user_number ** 2
# print("Квадрат числа:", result)


user_number = input("Введите число: ")
try: 
    number = int(user_number)
except ValueError: 
    message = "Ошибка! Вы ввели не число!"
else: 
    message = "Ваше число в:"
    message += "\n - двоичном виде: %s" % bin(number)
    message += "\n - восьмиричном виде: %s" % oct(number)
    message += "\n - шеснадцатиричном виде: %s" % hex(number)
print(message)