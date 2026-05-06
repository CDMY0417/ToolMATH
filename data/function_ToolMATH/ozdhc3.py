def factor_quadratic_ag(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    sqrt_disc = discriminant**0.5
    r1 = (-b + sqrt_disc) / (2*a)
    r2 = (-b - sqrt_disc) / (2*a)
    return (r1, r2)
