from math import sqrt
a_input, b_input, c_input = map(str, input("Введите коэффиценты квадратного уравнения A, B, C: ").split())
try:
    a = int(a_input)
    b = int(b_input)
    c = int(c_input)
except ValueError: 
    result = "Ошибка! Вы ввели не числа!"
else:
    d = b**2 - 4*a*c
    x1 = (-b + sqrt(d)) / 2*a
    x2 = (-b - sqrt(d)) / 2*a
    template = "Корни квадратного уравнения %f и %f"
    result = template % (x1, x2)
print(result)