def matrix_determinant_2x2_b(matrix: list[list[int]]) -> int:
    return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
