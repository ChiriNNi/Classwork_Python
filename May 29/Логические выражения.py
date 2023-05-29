# print("1 == 1:", 1 == 1)
# print("1 == 2:", 1 == 2)
# print("1 != 1:", 1 != 1)
# print("1 !=:", 1 != 2)
# print("1 > 1:", 1 > 1)
# print("1 > 2:", 1 > 2)

# print(ord("д"))
# print(ord("а"))


# 1 
# n = int(input("Введите число: "))
# if n >= 0: 
#     print(f"Число положительное")
# else:
#     print(f"Число отрицательное")

# 2
# age = int(input("Введите ваш возраст: "))
# if 0 <= age <= 120: 
#     print("Ваши данные корректны!")
# else: 
#     print("Ваши данные некорректны!")

# 3
# number = int(input("Введите число: "))
# if number > 0: 
#     print(f"Модуль числа: {number}")
# else: 
#     print(f"Модуль числа: {-number}")

# 4 
# hour, minute, second = map(int, input("Введите часы в формате (ЧЧ:ММ:СС): ").split())
# if hour > 23 or minute >= 60 or second >= 60: 
#     print("Ваши данные корректны!")
# else: 
#     print("Ваши данные некорректны!")


# 3**
# from decimal import * 
# def sin(x):
#     getcontext().prec += 2
#     i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
#     while s != lasts:
#         lasts = s
#         i += 2
#         fact *= i * (i-1)
#         num *= x * x
#         sign *= -1
#         s += num / fact * sign
#     getcontext().prec -= 2
#     return +s

from math import pi, sin
diameter_input, count_input = input("Введите диаметр окружности: "), input("Введите количество сторон правильного многоульника: ")
try: 
    diameter = float(diameter_input)
    count = int(count_input)
except ValueError: 
    message = "Ваши данные введены неккоректно!"
else:
    radius = diameter / 2
    side_of_polygon = 2 * radius * sin(pi / count)

    template = "Длина стороны правильного многоугольника, вписанного в окружность диаметром %.01f равно %.02f"
    message = template % (diameter, side_of_polygon)
print(message)



