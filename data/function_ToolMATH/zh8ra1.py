def scale_matrix(matrix: list[list[float]], scalar: float) -> list[list[float]]:
    return [[scalar * element for element in row] for row in matrix]
