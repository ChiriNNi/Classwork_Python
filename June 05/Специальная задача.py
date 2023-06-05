def get_spiral_matrix(rows, cols): 
    matrix = [[0] * cols for i in range(rows)]
    # matrix[0][cols-1] = 1
    # start = matrix[0][cols-1]
    count = 1 
    left, right, top, bottom = 0, cols-1, 0, rows-1

    while count <= rows * cols: 
        # Движение вниз
        for i in range(top, bottom+1): 
            matrix[i][right] = count 
            count += 1
        right -= 1

        # Движение влево
        for j in range(right, left-1, -1): 
            matrix[bottom][j] = count 
            count += 1 
        bottom -= 1

        # Движение вверх
        for i in range(bottom, top-1, -1): 
            matrix[i][left] = count 
            count += 1 
        left += 1

        # Движение вправо
        for j in range(left, right+1): 
            matrix[top][j] = count 
            count += 1 
        top += 1 

    return matrix


rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: ")) 

matrix = get_spiral_matrix(rows, cols)
print("\nМатрица: \n")
# Вывод матрицы №1
print('\n'.join('\t'.join(map(str, row)) for row in matrix))

# Вывод матрицы №2
# for row in matrix:
#     formatted_row = ["{:4d}".format(element) for element in row]
#     row_str = " ".join(formatted_row)
#     print(row_str)
