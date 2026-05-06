def matrix_multiply_2x2_a(m1: list[list[float]], m2: list[list[float]]) -> list[list[float]]:
    a = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    b = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    c = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    d = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return [[a, b], [c, d]]
