# 7**
# def table_of_products(number, count=1): 
#     if count == 10: 
#         return "Закончилось"
#     print(f"{number} * {count} = {number*count}")
#     table_of_products(number, count+1)
# def breakline():
#     print('-' * 50)

# for i in range(2, 10): 
#     table_of_products(i)
#     breakline()

# 8**
# def is_prime_number(number, count = 2): 
#     if number <= 2: 
#         return number == 2
#     if number % count == 0:
#         return False
#     if count * count > number: 
#         return True
#     return is_prime_number(number, count+1)
# number = int(input("Введите число: "))
# if is_prime_number(number): 
#     print("Число простое!")
# else: 
#     print("Число НЕпростое!")