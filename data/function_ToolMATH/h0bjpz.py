def matrix_multiply_h(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    return [[sum(a * b for a, b in zip(matrix1_row, matrix2_col)) for matrix2_col in zip(*matrix2)] for matrix1_row in matrix1]
