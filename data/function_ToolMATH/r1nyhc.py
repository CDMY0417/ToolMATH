def cosine_difference_formula(x: float, y: float):
    from math import sin, radians
    return 2 * sin(radians((x + y) / 2)) * sin(radians((y - x) / 2))
