def factor_quadratic_g(a: int, b: int, c: int):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None  # No real roots
    sqrt_discriminant = discriminant**0.5
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    if root1.is_integer() and root2.is_integer():
        return (int((a*root1, 1)), int((root2, 1)))
    return None
