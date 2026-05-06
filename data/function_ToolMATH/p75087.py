def subtract_scalar_from_identity_matrix(matrix: list[list[float]], scalar: float) -> list[list[float]]:
    identity = [[1 if i == j else 0 for j in range(len(matrix))] for i in range(len(matrix))]
    return [[matrix[i][j] - scalar * identity[i][j] for j in range(len(matrix[i]))] for i in range(len(matrix))]
