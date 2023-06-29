from functools import reduce
number = input("Введите целое положительное число: ") 

try: 
    number = int(number)
except ValueError: 
    number = None 

if number is None: 
    print("Вы ввели некорректное значение!")
else: 
    if number > 0: 
        result = reduce(lambda x, y: x * y, range(1, number + 1))
        print(f"Факториал числа {number}:", result)
    else:
        print("Введите положительное число!")