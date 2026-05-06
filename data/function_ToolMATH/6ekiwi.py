def dot_product_ay(vec1: list[float], vec2: list[float]) -> float:
    return sum(x * y for x, y in zip(vec1, vec2))
