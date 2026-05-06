def matrix_multiply_d(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    a, b = matrix1[0]
    c, d = matrix1[1]
    e, f = matrix2[0]
    g, h = matrix2[1]
    return [[a*e + b*g, a*f + b*h], [c*e + d*g, c*f + d*h]]
