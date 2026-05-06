def negate_matrix(matrix: list[list[float]]) -> list[list[float]]:
    result = [[-element for element in row] for row in matrix]
    return result
