def dot_product_ag(vector1: tuple, vector2: tuple) -> float:
    return sum(x * y for x, y in zip(vector1, vector2))
