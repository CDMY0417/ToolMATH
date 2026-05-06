def solve_quadratic_h(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_disc = discriminant**0.5
    root1 = (-b + sqrt_disc) / (2*a)
    root2 = (-b - sqrt_disc) / (2*a)
    return [root for root in [root1, root2] if root > 0]
