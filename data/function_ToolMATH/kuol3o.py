def reflect_vector(matrix: list[list[float]], vector: list[float]) -> list[float]:
    a, b = matrix[0]
    c, d = matrix[1]
    x, y = vector
    return [a*x + b*y, c*x + d*y]
