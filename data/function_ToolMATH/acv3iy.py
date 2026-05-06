def product_to_sum(a: float, b: float) -> float:
    from math import cos, radians
    return 0.5 * (cos(radians(a - b)) - cos(radians(a + b)))
