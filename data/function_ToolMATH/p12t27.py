def dot_product_ba(vector_a: list[float], vector_b: list[float]) -> float:
    return sum(a * b for a, b in zip(vector_a, vector_b))
