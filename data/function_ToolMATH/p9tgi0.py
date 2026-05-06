def determinant_2x2_f(matrix: list[list[float]]) -> float:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    return a * d - b * c
