# 1
# count_input = input("Введите количество смайликов: ")
# try: 
#     count = int(count_input)
# except ValueError: 
#     count = None 

# if count is None or count < 0: 
#     print("Введите целое положительное число!")
# else: 
#     smiley = input("Введите смайлик: ")
#     print("Результат: ")
#     while count != 0: 
#         print(smiley)
#         count -= 1


# 2
# number_input = input("Введите число: ")
# try: 
#     number = int(number_input)
# except ValueError: 
#     print("Введите целое число!")
# else: 
#     print("Результат: ")
#     while number >= 0: 
#         print(number)
#         number -= 1

# 3
# number_input = input("Введите число: ")
# degree_input = input("Введите степень числа: ")
# print("Результат: ")
# try: 
#     number = int(number_input)
#     degree = int(degree_input)
# except ValueError: 
#     print("Вы ввели некорректные значения!")
# else:
#     while degree_input != 0: 
#         number *= number
#         degree_input -= 1

# 4
# number_1_input = input("Введите первое число: ")
# number_2_input = input("Введите второе число: ")

# try: 
#     number_1 = int(number_1_input)
#     number_2 = int(number_2_input)
# except ValueError: 
#     print("Вы ввели некорректные значения!")
# else: 
#     minimum = min(number_1, number_2)
#     i = 1 
#     print("Общие делители: ")
#     while i <= minimum:
#         if number_1 % i == 0 and number_2 % i == 0: 
#             print(i)
#         i += 1 


# 3
# number_input = input("Введите число: ")
# try: 
#     number = int(number_input)
# except ValueError: 
#     print("Введите целое число!")
# else: 
#     print("Числа кратные {number}")
#     for i in range(1, 101): 
#         if i % number == 0: 
#             print(i)

# 3** 
# alphabet = "abcdefgh"
# for i in range(len(alphabet)): 
#     text = ""
#     for j in range(1, 9): 
#         if j % 2 != 0: 
#             text2 += "# "
#         else:
#             text2 += "  "
#     if i % 2 != 0:
#         print(alphabet[i] + " " + text)
#     else:
#         print(alphabet[i] + " " + text[::-1])
# print("  ", end="")
# for i in range(1, 9):
#     print(i, end=" ")


# n = int(input())
# for i in range(1, n + 1):
#     row = [str(j) for j in range(1, i + 1)]
#     row.extend([str(j) for j in range(i - 1, 0, -1)])
#     print(''.join(row))    

