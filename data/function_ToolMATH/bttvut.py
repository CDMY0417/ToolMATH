def product_to_sum_sin_cos(a: float, b: float):
    from math import sin, radians
    return 0.5 * (sin(radians(a + b)) + sin(radians(a - b)))
