def dot_product_o(vector_a: tuple, vector_b: tuple) -> float:
    return sum(a * b for a, b in zip(vector_a, vector_b))
