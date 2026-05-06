def expand_3x3_determinant_a(matrix: list[list[float]]) -> float:
    a, b, c = matrix[0]
    e, f, d = matrix[1]
    g, h, i = matrix[2]
    return a * (f * i - h * d) - b * (e * i - g * d) + c * (e * h - g * f)
