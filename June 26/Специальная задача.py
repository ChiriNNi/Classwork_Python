import random

def get_matrix(n): 
    matrix = [[random.randint(100, 200) for _ in range(n)] for _ in range(n)]

    for i in range(n): 
        matrix[i][i] = 0 
    
    return matrix

def calculate_distance(input_data, matrix):
    nums = list(map(int, input_data.split(",")))

    distance = []
    for i in range(len(nums) - 1): 
        distance.append(matrix[nums[i] - 1][nums[i+1] - 1])
    
    return distance

n = int(input("Введите количество домов: "))
matrix = get_matrix(n)

input_data = input("Введите номера домов через запятую, в порядке их обхода: ") 
distance = calculate_distance(input_data, matrix)


print("\nТаблица домов: \n")
print('\n'.join('\t'.join(map(str, row)) for row in matrix))


print("\nПуть:", distance)
print("Длина пути:", sum(distance))


