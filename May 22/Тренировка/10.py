number_input = input("Введите трехзначное число: ")
try:
    number = int(number_input)
except ValueError: 
    result = "Ошибка! Вы ввели не число!"
else:
    n = number % 10 
    result = str(n) + number_input[-2::-1]
print(result)

