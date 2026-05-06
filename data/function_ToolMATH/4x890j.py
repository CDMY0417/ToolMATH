def quadratic_solutions_b(a: float, b: float, c: float) -> tuple:
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ()  # No real solutions
    sqrt_discriminant = discriminant**0.5
    x1 = (-b + sqrt_discriminant) / (2*a)
    x2 = (-b - sqrt_discriminant) / (2*a)
    return (x1, x2)
