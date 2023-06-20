# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    # Определение размеров исходной матрицы
    rows = len(matrix)
    cols = len(matrix[0])

    # Создание новой матрицы для транспонированных элементов
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    # Транспонирование элементов
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix
