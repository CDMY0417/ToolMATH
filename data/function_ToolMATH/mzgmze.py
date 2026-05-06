def quadratic_roots_g(a: int, b: int, c: int):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return []
    sqrt_disc = math.sqrt(discriminant)
    root1 = (-b + sqrt_disc) / (2*a)
    root2 = (-b - sqrt_disc) / (2*a)
    return [root1, root2] if root1 != root2 else [root1]
