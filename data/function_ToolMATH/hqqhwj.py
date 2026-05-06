def factor_quadratic_p(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    r1 = (-b + discriminant**0.5) / (2*a)
    r2 = (-b - discriminant**0.5) / (2*a)
    return (r1, r2)
