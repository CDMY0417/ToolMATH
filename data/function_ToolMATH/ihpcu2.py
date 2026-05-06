def factor_quartic(a: float, b: float, c: float):
    from math import sqrt
    disc = b**2 - 4*a*c
    if disc < 0:
        return []
    x1 = (-b - sqrt(disc)) / (2*a)
    x2 = (-b + sqrt(disc)) / (2*a)
    return [x1, x2]
