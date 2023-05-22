from math import sqrt
a, b = map(int, input("Введите длины катетов прямоугольного треугольника: ").split())
print("Длина гипотенузы:", sqrt(a**2 + b**2))