def determinant_of_2x2(matrix: list[list[float]]) -> float:
    [[a, b], [c, d]] = matrix
    return a * d - b * c
