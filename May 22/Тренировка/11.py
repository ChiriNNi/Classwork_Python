from math import sqrt
x1_input, y1_input = map(str, input("Введите координаты первой точки: ").split())
x2_input, y2_input = map(str, input("Введите координаты второй точки: ").split())
try:
    x1 = int(x1_input)
    y1 = int(y1_input)
    x2 = int(x2_input)
    y2 = int(y2_input)
except ValueError: 
    result = "Ошибка! Вы ввели неверные координаты!"
else:
    length = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    template = "Расстояние между двумя точками %f"
    result = template % (length)
print(result)