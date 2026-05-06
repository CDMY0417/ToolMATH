def is_invertible(matrix: list[list[float]]) -> bool:
    a, b, c, d = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    determinant = a * d - b * c
    return determinant != 0
