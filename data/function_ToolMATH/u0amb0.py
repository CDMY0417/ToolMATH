def dot_product_ah(vector1: list[float], vector2: list[float]) -> float:
    return sum(a * b for a, b in zip(vector1, vector2))
