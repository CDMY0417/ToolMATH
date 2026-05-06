def dot_product_ae(v1: list[float], v2: list[float]) -> float:
    return sum(x * y for x, y in zip(v1, v2))
