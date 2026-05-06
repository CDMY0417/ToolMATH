def factor_quadratic_polynomial(b: int, c: int):
    discriminant = b**2 - 4*c
    if discriminant < 0:
        return []
    sqrt_disc = discriminant**0.5
    root1 = (-b + sqrt_disc) / 2
    root2 = (-b - sqrt_disc) / 2
    return [root1, root2]
