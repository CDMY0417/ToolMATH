def matrix_vector_multiplication_a(M: list[list[float]], v: list[float]) -> list[float]:
    result = [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]
    return result
