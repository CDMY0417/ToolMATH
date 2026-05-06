def factor_quadratic_s(a: int, b: int, c: int):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return None
    factor1 = (-b + discriminant ** 0.5) / (2 * a)
    factor2 = (-b - discriminant ** 0.5) / (2 * a)
    if factor1.is_integer() and factor2.is_integer():
        return (int(factor1), int(factor2))
    return None
