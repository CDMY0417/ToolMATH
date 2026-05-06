def dot_product_r(vector1: tuple, vector2: tuple) -> float:
    return sum(a * b for a, b in zip(vector1, vector2))
