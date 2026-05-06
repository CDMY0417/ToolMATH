def matrix_addition(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))] for i in range(len(matrix_a))]
