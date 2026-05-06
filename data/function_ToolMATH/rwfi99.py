def sum_to_product_formula(a: int, b: int, x: float):
    import math
    return 2 * math.sin((a + b) / 2 * x) * math.cos((a - b) / 2 * x)
