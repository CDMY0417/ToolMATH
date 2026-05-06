def compose_matrices(matrix1: list[list[float]], matrix2: list[list[float]]) -> list[list[float]]:
    return [[matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0],
             matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]],
            [matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0],
             matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]]]
