def sum_to_product_sin(a: float, b: float):
    import math
    return 2 * math.sin((a + b) / 2) * math.cos((a - b) / 2)
