def is_zero_matrix(matrix: list[list[float]]) -> bool:
    return all(all(element == 0 for element in row) for row in matrix)
