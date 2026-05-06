def solve_quadratic_x(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # No real roots
    sqrt_disc = discriminant**0.5
    root1 = (-b + sqrt_disc) / (2*a)
    root2 = (-b - sqrt_disc) / (2*a)
    return [root1, root2]
