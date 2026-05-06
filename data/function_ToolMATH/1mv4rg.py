def factor_quadratic_am(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    sqrt_discriminant = int(discriminant**0.5)
    root1 = (-b + sqrt_discriminant) // (2 * a)
    root2 = (-b - sqrt_discriminant) // (2 * a)
    return (root1, root2)
