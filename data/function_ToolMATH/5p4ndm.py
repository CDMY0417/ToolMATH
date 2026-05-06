def matrix_multiply_c(mat1: list[list[float]], mat2: list[list[float]]) -> list[list[float]]:
    return [[sum(mat1[i][k] * mat2[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
