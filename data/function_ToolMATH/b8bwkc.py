def dot_product_h(v1: list[float], v2: list[float]) -> float:
    return sum(a * b for a, b in zip(v1, v2))
