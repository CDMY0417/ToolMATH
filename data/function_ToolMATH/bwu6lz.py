def solve_quadratic_bn(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_disc = discriminant**0.5
    x1 = (-b + sqrt_disc) / (2*a)
    x2 = (-b - sqrt_disc) / (2*a)
    return [x1, x2]
