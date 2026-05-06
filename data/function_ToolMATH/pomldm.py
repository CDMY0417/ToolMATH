def matrix_multiply_n(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    a, b = matrix1
    c, d = matrix2
    return [[a[0] * c[0] + a[1] * c[1], a[0] * d[0] + a[1] * d[1]],
            [b[0] * c[0] + b[1] * c[1], b[0] * d[0] + b[1] * d[1]]]
