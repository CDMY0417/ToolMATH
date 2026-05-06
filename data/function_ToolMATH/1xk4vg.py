def matrix_vector_multiplication(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = [
        matrix[0][0] * vector[0] + matrix[0][1] * vector[1],
        matrix[1][0] * vector[0] + matrix[1][1] * vector[1]
    ]
    return result
