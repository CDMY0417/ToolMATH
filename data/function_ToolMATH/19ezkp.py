def matrix_multiply_a(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    return [[matrix_a[0][0] * matrix_b[0][0] + matrix_a[0][1] * matrix_b[1][0], matrix_a[0][0] * matrix_b[0][1] + matrix_a[0][1] * matrix_b[1][1]],
            [matrix_a[1][0] * matrix_b[0][0] + matrix_a[1][1] * matrix_b[1][0], matrix_a[1][0] * matrix_b[0][1] + matrix_a[1][1] * matrix_b[1][1]]]
