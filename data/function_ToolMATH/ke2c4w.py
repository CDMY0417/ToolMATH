def cos_product_to_sum(x: float, y: float) -> float:
    from math import cos, radians
    return 0.5 * (cos(radians(x + y)) + cos(radians(x - y)))
