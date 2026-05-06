def solve_quadratic_equation_an(a: float, b: float, c: float):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_discriminant = discriminant**0.5
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    return [root1, root2] if root1 != root2 else [root1]
