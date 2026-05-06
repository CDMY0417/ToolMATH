def sum_to_product_identity(a: float, b: float) -> float:
    from math import sin, radians
    A = radians(a)
    B = radians(b)
    result = 2 * sin((A + B) / 2) * sin((A - B) / 2)
    return result
