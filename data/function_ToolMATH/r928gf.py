def matrix_multiply_j(matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result
