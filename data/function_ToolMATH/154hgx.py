def is_matrix_invertible(a: float, b: float, c: float, d: float) -> bool:
    determinant = a * d - b * c
    return determinant != 0
