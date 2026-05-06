def matrix_multiply_b(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    a11 = matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0]
    a12 = matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]
    a21 = matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0]
    a22 = matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]
    return [[a11, a12], [a21, a22]]
