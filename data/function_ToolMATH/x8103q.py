def add_scaled_row_to_row(matrix: list, source_row_index: int, target_row_index: int, scale_factor: int):
    new_matrix = [row[:] for row in matrix]
    scaled_row = [scale_factor * element for element in matrix[source_row_index]]
    new_matrix[target_row_index] = [a + b for a, b in zip(matrix[target_row_index], scaled_row)]
    return new_matrix
