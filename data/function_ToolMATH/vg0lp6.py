def add_matrices(matrix_a: list[list[float]], matrix_b: list[list[float]]) -> list[list[float]]:
    num_rows = len(matrix_a)
    num_cols = len(matrix_a[0])
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(num_cols)] for i in range(num_rows)]
