def solve_quadratic_e(a: int, b: int, c: int) -> tuple[float, float] | None:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    sqrt_discriminant = discriminant**0.5
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    return root1, root2
