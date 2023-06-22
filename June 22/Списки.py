# user_in = "567, 345, -65"
# mylist = user_in.split(',')
# print('Метод .split:', mylist)
#
# output = ",".join(mylist)
# print('Метод .join:', output)

# 1
# arr_items = input("Введите элементы списка: ")
# arr = arr_items.split(" ")
# print(arr)


'''
2.	Пользователь вводит одномерный массив чисел в интервале от 0 до 20.
Вывести в документ столбчатую диаграмму, соответствующую значениям в массиве, с помощью символов #.
Например, диаграмма для массива [1, 0, 3, 1, 2, 1] :
    #
    #   #
#   # # # #
------------
'''

import random
arr = [random.randint(0, 20) for i in range(5)]
print(arr)
result = []
max_element = max(arr)
while max_element >= 0:
    result_item = ''
    for i in range(len(arr)):
        if arr[i] > 0:
            result_item += '# '
        else:
            result_item += '  '
        arr[i] -= 1
    max_element = max(arr)
    result.append(result_item)
for i in result[::-1]:
    print(i)
print('- ' * len(arr))
