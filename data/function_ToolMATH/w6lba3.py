def multiply_matrices_2x2(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    a11, a12 = matrix_a[0]
    a21, a22 = matrix_a[1]
    b11, b12 = matrix_b[0]
    b21, b22 = matrix_b[1]
    c11 = a11 * b11 + a12 * b21
    c12 = a11 * b12 + a12 * b22
    c21 = a21 * b11 + a22 * b21
    c22 = a21 * b12 + a22 * b22
    return [[c11, c12], [c21, c22]]
