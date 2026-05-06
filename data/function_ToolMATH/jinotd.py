def scale_matrix_b(scalar: int, matrix: list[list[int]]) -> list[list[int]]:
    return [[scalar * matrix[0][0], scalar * matrix[0][1]],
            [scalar * matrix[1][0], scalar * matrix[1][1]]]
