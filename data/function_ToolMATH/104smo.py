def factor_quadratic_a(a: int, b: int, c: int):
    d = b**2 - 4*a*c
    if d < 0:
        return None
    m = (-b + d**0.5) / (2*a)
    n = (-b - d**0.5) / (2*a)
    return m, n
