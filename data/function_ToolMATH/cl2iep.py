def scale_matrix_row(matrix: list[list[float]], row_index: int, factor: float) -> list[list[float]]:
    new_matrix = [row[:] for row in matrix]
    new_matrix[row_index] = [factor * element for element in matrix[row_index]]
    return new_matrix
