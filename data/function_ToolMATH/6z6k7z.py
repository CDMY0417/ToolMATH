def product_to_sum_sin_sin(a: float, b: float):
    from math import cos, radians
    return 0.5 * (cos(radians(a - b)) - cos(radians(a + b)))
