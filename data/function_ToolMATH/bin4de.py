def determinant_2x2_d(matrix: list[list[float]]) -> float:
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c
