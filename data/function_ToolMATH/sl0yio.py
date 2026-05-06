def factor_quadratic_trinomial(a: int, b: int, c: int):
    discriminant = b**2 - 4 * a * c
    if discriminant < 0:
        return None
    sqrt_discriminant = discriminant**0.5
    root1 = (-b + sqrt_discriminant) / (2 * a)
    root2 = (-b - sqrt_discriminant) / (2 * a)
    return [(a, b + int(root2 * a)), (1, int(root1))] if root1.is_integer() and root2.is_integer() else None
