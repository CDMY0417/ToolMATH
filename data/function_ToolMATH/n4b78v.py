def quadratic_roots_h(a: int, b: int, c: int):
    import math
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return ()
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    return (root1, root2)
