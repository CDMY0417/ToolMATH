def quadratic_factors(b: int, c: int) -> tuple:
    discriminant = b**2 - 4*c
    r1 = (-b + discriminant**0.5) / 2
    r2 = (-b - discriminant**0.5) / 2
    return r1, r2
