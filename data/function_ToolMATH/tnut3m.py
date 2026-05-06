def project_vector(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = [sum(matrix[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matrix))]
    return result
