def scalar_multiply_matrix(scalar: int, matrix: list):
    result = [[scalar * element for element in row] for row in matrix]
    return result
