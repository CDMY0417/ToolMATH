def matrix_multiply_f(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
