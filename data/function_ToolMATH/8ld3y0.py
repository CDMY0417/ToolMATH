def factor_quadratic_ai(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    sqrt_discriminant = int(discriminant**0.5)
    x1 = (-b + sqrt_discriminant) // (2*a)
    x2 = (-b - sqrt_discriminant) // (2*a)
    return (x1, x2)
