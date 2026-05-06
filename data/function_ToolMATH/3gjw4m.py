def maximize_quadratic(a: int, b: int, c: int):
    if a >= 0:
        return None, None
    h = -b / (2 * a)
    max_value = a * h**2 + b * h + c
    return h, max_value
