def add_2x2_matrices(matrix1: tuple[tuple[float, float], tuple[float, float]], matrix2: tuple[tuple[float, float], tuple[float, float]]) -> tuple[tuple[float, float], tuple[float, float]]:
    return (
        (matrix1[0][0] + matrix2[0][0], matrix1[0][1] + matrix2[0][1]),
        (matrix1[1][0] + matrix2[1][0], matrix1[1][1] + matrix2[1][1])
    )
