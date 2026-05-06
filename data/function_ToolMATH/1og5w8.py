def dot_product_a(vector1: tuple[float, ...], vector2: tuple[float, ...]) -> float:
    return sum(x * y for x, y in zip(vector1, vector2))
