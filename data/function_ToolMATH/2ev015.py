def cross_product(vector_a: list[float], vector_b: list[float]) -> list[float]:
    cx = vector_a[1] * vector_b[2] - vector_a[2] * vector_b[1]
    cy = vector_a[2] * vector_b[0] - vector_a[0] * vector_b[2]
    cz = vector_a[0] * vector_b[1] - vector_a[1] * vector_b[0]
    return [cx, cy, cz]
