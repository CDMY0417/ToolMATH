def factor_quadratic_aa(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    sqrt_d = int(discriminant**0.5)
    if sqrt_d * sqrt_d != discriminant:
        return None
    p = (-b + sqrt_d) // (2*a)
    q = (-b - sqrt_d) // (2*a)
    return (p, q)
