def matrix_multiplication(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    a, b, c, d = matrix1[0][0], matrix1[0][1], matrix1[1][0], matrix1[1][1]
    e, f, g, h = matrix2[0][0], matrix2[0][1], matrix2[1][0], matrix2[1][1]
    return [[a * e + b * g, a * f + b * h], [c * e + d * g, c * f + d * h]]
