def apply_transformation_matrix_a(M: list[list[float]], v: list[float]) -> list[float]:
    return [M[0][0] * v[0] + M[0][1] * v[1], M[1][0] * v[0] + M[1][1] * v[1]]
