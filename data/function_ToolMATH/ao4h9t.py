def sum_to_product_sine(a: float, b: float) -> float:
    from math import sin, cos, radians
    return 2 * sin(radians((a + b) / 2)) * cos(radians((a - b) / 2))
