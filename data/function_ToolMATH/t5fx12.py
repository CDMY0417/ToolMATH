def solve_quadratic_equation_as(a: float, b: float, c: float) -> tuple:
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        return ()  # No real roots
    sqrt_discriminant = discriminant ** 0.5
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return (root1, root2)
