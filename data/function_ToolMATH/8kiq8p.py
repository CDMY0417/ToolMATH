def vector_dot_product_a(vec1: list[float], vec2: list[float]) -> float:
    return sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
