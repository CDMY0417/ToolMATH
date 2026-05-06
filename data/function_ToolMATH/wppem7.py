def expand_3x3_determinant(matrix: list[list[float]]) -> float:
    a11, a12, a13 = matrix[0]
    a21, a22, a23 = matrix[1]
    a31, a32, a33 = matrix[2]
    minor1 = a22 * a33 - a23 * a32
    minor2 = a21 * a33 - a23 * a31
    minor3 = a21 * a32 - a22 * a31
    return a11 * minor1 - a12 * minor2 + a13 * minor3
