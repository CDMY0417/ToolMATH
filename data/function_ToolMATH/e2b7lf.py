def multiply_matrix_by_scalar(matrix: list[list[float]], scalar: float):
    return [[element * scalar for element in row] for row in matrix]
