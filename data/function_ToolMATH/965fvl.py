def dot_product_ar(v1: list[float], v2: list[float]) -> float:
    return sum(v1[i] * v2[i] for i in range(len(v1)))
