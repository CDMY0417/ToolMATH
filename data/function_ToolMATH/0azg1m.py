def solve_quadratic(a: float, b: float, c: float):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []  # No real roots
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    return [root1, root2]
