def multiply_matrices(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    return [[sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix1[0]))) for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
