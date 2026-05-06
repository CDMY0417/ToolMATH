def sum_to_product_cosine(a: float, b: float):
    from math import cos, radians
    return 2 * cos(radians((a + b) / 2)) * cos(radians((a - b) / 2))
