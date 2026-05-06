def factor_quadratic_equation(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_disc = discriminant**0.5
    if int(sqrt_disc) != sqrt_disc:
        return []
    x1 = (-b + sqrt_disc) / (2*a)
    x2 = (-b - sqrt_disc) / (2*a)
    return [x1, x2]
