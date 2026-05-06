def matrix_multiply_g(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    a11 = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]
    a12 = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
    a21 = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
    a22 = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]
    return [[a11, a12], [a21, a22]]
