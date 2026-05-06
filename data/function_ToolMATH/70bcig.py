def multiply_matrix_vector(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = [0, 0, 0]
    for i in range(3):
        for j in range(3):
            result[i] += matrix[i][j] * vector[j]
    return result
