def matrix_vector_multiply_a(matrix: list[list[float]], vector: list[float]) -> list[float]:
    result = []
    for row in matrix:
        product_sum = sum(m * v for m, v in zip(row, vector))
        result.append(product_sum)
    return result
