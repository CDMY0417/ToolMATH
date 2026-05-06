def matrix_add_a(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
