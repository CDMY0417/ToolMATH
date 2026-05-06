def factor_quadratic_j(a: int, b: int, c: int):
    delta = b**2 - 4*a*c
    sqrt_delta = int(delta**0.5)
    if sqrt_delta * sqrt_delta != delta:
        return None  # not factorable over rationals
    r1 = (-b + sqrt_delta) / (2*a)
    r2 = (-b - sqrt_delta) / (2*a)
    p, q = a, int(-r1 * a)
    r, s = 1, int(-r2)
    return (p, q), (r, s)
